---
title: "LoRaWAN Nano-gateway"
aliases:
    - tutorials/lora/lorawan-nano-gateway.html
    - tutorials/lora/lorawan-nano-gateway.md
    - chapter/tutorials/lora/lorawan-nano-gateway
---

This example allows a development module to act as a single channel gateway, and connect to a LoRaWAN network such as The Things Network (TTN) or Loriot.
The files can be found in our [GitHub Repository](https://github.com/pycom/pycom-libraries/tree/master/examples/lorawan-nano-gateway).

## Nano-gateway setup

The functionality of the Nano-Gateway is split into 3 files, `main.py`, `config.py` and `nanogateway.py`. These are used to configure and specify how the gateway will connect to a preferred network and how it can act as packet forwarder.

### Gateway ID

Most LoRaWAN network servers expect a Gateway ID in the form of a unique 64-bit hexadecimal number (called a EUI-64). The recommended practice is to produce this ID from your board by expanding the WiFi MAC address (a 48-bit number, called MAC-48). You can obtain that by running this code prior to configuration:

```python

from network import WLAN
import ubinascii
wl = WLAN()
ubinascii.hexlify(wl.mac())[:6] + 'FFFE' + ubinascii.hexlify(wl.mac())[6:]
```

The result will by something like `b'240ac4FFFE008d88'` where `240ac4FFFE008d88` is your Gateway ID to be used in your network provider configuration.

### main.py

This file runs at boot and calls the library and `config.py` files to initialise the nano-gateway. Once configuration is set, the nano-gateway is then started.

```python
""" LoPy LoRaWAN Nano Gateway example usage """
# Acknowledgement:
# Thanks to robert-hh for providing us with an updated, more stable example for the nanogateway 

# disable heartbeat
from pycom import heartbeat
heartbeat(False)
print ("Heartbeat off")


import utime
from machine import RTC
rtc = RTC()
rtc.ntp_sync("pool.ntp.org")
utime.sleep_ms(750)
t = rtc.now()
with open("bootlog.txt", "a") as f:
   f.write(repr(utime.time()) + " " + repr(t) + "\n")

def reload(mod):
    import sys
    mod_name = mod.__name__
    del sys.modules[mod_name]
    return __import__(mod_name)

from machine import reset

""" LoPy LoRaWAN Nano Gateway example usage """

import config
from nanogateway import NanoGateway

if True: #__name__ == '__main__':
    nanogw = NanoGateway(
        id=config.GATEWAY_ID,
        frequency=config.LORA_FREQUENCY,
        datarate=config.LORA_GW_DR,
        ssid=config.WIFI_SSID,
        password=config.WIFI_PASS,
        server=config.SERVER,
        port=config.PORT,
        ntp_server=config.NTP,
        ntp_period=config.NTP_PERIOD_S
        )

    nanogw.start()
    #nanogw._log('You may now press ENTER to enter the REPL')
    #input()

```

### config.py

This file contains settings for the server and network it is connecting to. Depending on the nano-gateway region and provider (TTN, Loriot, etc.) these will vary. The provided example will work with The Things Network (TTN) in the European, 868Mhz, region.

The Gateway ID is generated in the script using the process described above.

**Please change the WIFI_SSID and WIFI_PASS variables to match your desired WiFi network**

```python
""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import ubinascii

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
# GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]
GATEWAY_ID = WIFI_MAC[:6] + "FFFF" + WIFI_MAC[6:12]
SERVER = 'router.eu.thethings.network'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

WIFI_SSID = ''
WIFI_PASS = ''

# for IN865
# LORA_FREQUENCY = 865062500
# LORA_GW_DR = "SF7BW125" # DR_5
# LORA_NODE_DR = 5

# for EU868
LORA_FREQUENCY = 868500000
LORA_GW_DR = "SF7BW125" # DR_5
LORA_NODE_DR = 5

# for US915
# LORA_FREQUENCY = 903900000
# LORA_GW_DR = "SF7BW125" # DR_3
# LORA_NODE_DR = 3
```

### nanogateway.py

The nano-gateway library controls all of the packet generation and forwarding for the LoRa data. This does not require any user configuration and the latest version of this code should be downloaded from the Pycom [GitHub Repository](https://github.com/pycom/pycom-libraries/tree/master/examples/lorawan-nano-gateway).

```python
""" LoPy LoRaWAN Nano Gateway. Can be used for both EU868 and US915. """

import errno
import machine
import ubinascii
import ujson
import uos
import usocket
import utime
import _thread
import gc
from micropython import const
from network import LoRa
from network import WLAN
from machine import Timer
from machine import WDT

PROTOCOL_VERSION = const(2)

PUSH_DATA = const(0)
PUSH_ACK = const(1)
PULL_DATA = const(2)
PULL_ACK = const(4)
PULL_RESP = const(3)

TX_ERR_NONE = 'NONE'
TX_ERR_TOO_LATE = 'TOO_LATE'
TX_ERR_TOO_EARLY = 'TOO_EARLY'
TX_ERR_COLLISION_PACKET = 'COLLISION_PACKET'
TX_ERR_COLLISION_BEACON = 'COLLISION_BEACON'
TX_ERR_TX_FREQ = 'TX_FREQ'
TX_ERR_TX_POWER = 'TX_POWER'
TX_ERR_GPS_UNLOCKED = 'GPS_UNLOCKED'

UDP_THREAD_CYCLE_MS = const(10)
WDT_TIMEOUT = const(120)


STAT_PK = {
    'stat': {
        'time': '',
        'lati': 0,
        'long': 0,
        'alti': 0,
        'rxnb': 0,
        'rxok': 0,
        'rxfw': 0,
        'ackr': 100.0,
        'dwnb': 0,
        'txnb': 0
    }
}

RX_PK = {
    'rxpk': [{
        'time': '',
        'tmst': 0,
        'chan': 0,
        'rfch': 0,
        'freq': 0,
        'stat': 1,
        'modu': 'LORA',
        'datr': '',
        'codr': '4/5',
        'rssi': 0,
        'lsnr': 0,
        'size': 0,
        'data': ''
    }]
}

TX_ACK_PK = {
    'txpk_ack': {
        'error': ''
    }
}


class NanoGateway:
    """
    Nano gateway class, set up by default for use with TTN, but can be configured
    for any other network supporting the Semtech Packet Forwarder.
    Only required configuration is wifi_ssid and wifi_password which are used for
    connecting to the Internet.
    """

    def __init__(self, id, frequency, datarate, ssid, password, server, port, ntp_server='pool.ntp.org', ntp_period=3600):
        self.id = id
        self.server = server
        self.port = port

        self.frequency = frequency
        self.datarate = datarate

        self.ssid = ssid
        self.password = password

        self.ntp_server = ntp_server
        self.ntp_period = ntp_period

        self.server_ip = None

        self.rxnb = 0
        self.rxok = 0
        self.rxfw = 0
        self.dwnb = 0
        self.txnb = 0

        self.sf = self._dr_to_sf(self.datarate)
        self.bw = self._dr_to_bw(self.datarate)

        self.stat_alarm = None
        self.pull_alarm = None
        self.uplink_alarm = None

        self.wlan = None
        self.sock = None
        self.udp_stop = False
        self.udp_lock = _thread.allocate_lock()

        self.lora = None
        self.lora_sock = None

        self.rtc = machine.RTC()

        self.watchdog = WDT(timeout=10000)

    def start(self):
        """
        Starts the LoRaWAN nano gateway.
        """

        self._log('Starting LoRaWAN nano gateway with id: {}', self.id)

        # setup WiFi as a station and connect
        self.wlan = WLAN(mode=WLAN.STA)
        self._connect_to_wifi()
        self.watchdog.feed()
        # get a time sync
        self._log('Syncing time with {} ...', self.ntp_server)
        self.rtc.ntp_sync(self.ntp_server, update_period=self.ntp_period)
        while not self.rtc.synced():
            utime.sleep_ms(50)
            self.watchdog.feed()
        self._log("RTC NTP sync complete")
        self.watchdog.feed()
        # get the server IP and create an UDP socket
        self.server_ip = usocket.getaddrinfo(self.server, self.port)[0][-1]
        self._log('Opening UDP socket to {} ({}) port {}...', self.server, self.server_ip[0], self.server_ip[1])
        self.sock = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM, usocket.IPPROTO_UDP)
        self.sock.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
        self.sock.setblocking(False)

        # push the first time immediatelly
        self._push_data(self._make_stat_packet())

        # create the alarms
        self.stat_alarm = Timer.Alarm(handler=lambda t: self._push_data(self._make_stat_packet()), s=60, periodic=True)
        self.pull_alarm = Timer.Alarm(handler=lambda u: self._pull_data(), s=25, periodic=True)

        # start the watchdog
        self.watchdog.feed()
        utime.sleep(1)
        self._log("Watchdog started")

        # start the UDP receive thread
        self.udp_stop = False
        _thread.start_new_thread(self._udp_thread, ())
        self.watchdog.feed()
        # initialize the LoRa radio in LORA mode
        self._log('Setting up the LoRa radio at {} Mhz using {}', self._freq_to_float(self.frequency), self.datarate)
        self.lora = LoRa(
            mode=LoRa.LORA,
            region=LoRa.EU868,
            frequency=self.frequency,
            bandwidth=self.bw,
            sf=self.sf,
            preamble=8,
            coding_rate=LoRa.CODING_4_5,
            tx_iq=True
        )

        # create a raw LoRa socket
        self.lora_sock = usocket.socket(usocket.AF_LORA, usocket.SOCK_RAW)
        self.lora_sock.setblocking(False)
        self.lora_tx_done = False
        self.watchdog.feed()
        self.lora.callback(trigger=(LoRa.RX_PACKET_EVENT | LoRa.TX_PACKET_EVENT), handler=self._lora_cb)
        self.watchdog.feed()
        if uos.uname()[0] == "LoPy":
            self.window_compensation = -1000
        else:
            self.window_compensation = -6000
        self.watchdog.feed()
        self._log('LoRaWAN nano gateway online')

    def stop(self):
        """
        Stops the LoRaWAN nano gateway.
        """

        self._log('Stopping...')

        # send the LoRa radio to sleep
        self.lora.callback(trigger=None, handler=None)
        self.lora.power_mode(LoRa.SLEEP)

        # stop the NTP sync
        self.rtc.ntp_sync(None)

        # cancel all the alarms
        self.stat_alarm.cancel()
        self.pull_alarm.cancel()

        # signal the UDP thread to stop
        self.udp_stop = True
        while self.udp_stop:
            utime.sleep_ms(50)

        # disable WLAN
        self.wlan.disconnect()
        self.wlan.deinit()

    def _connect_to_wifi(self):
        self.wlan.connect(self.ssid, auth=(None, self.password))
        while not self.wlan.isconnected():
            utime.sleep_ms(50)
            self.watchdog.feed()
        self._log('WiFi connected to: {}', self.ssid)

    def _dr_to_sf(self, dr):
        sf = dr[2:4]
        if sf[1] not in '0123456789':
            sf = sf[:1]
        return int(sf)

    def _dr_to_bw(self, dr):
        bw = dr[-5:]
        if bw == 'BW125':
            return LoRa.BW_125KHZ
        elif bw == 'BW250':
            return LoRa.BW_250KHZ
        else:
            return LoRa.BW_500KHZ

    def _sf_bw_to_dr(self, sf, bw):
        dr = 'SF' + str(sf)
        if bw == LoRa.BW_125KHZ:
            return dr + 'BW125'
        elif bw == LoRa.BW_250KHZ:
            return dr + 'BW250'
        else:
            return dr + 'BW500'

    def _lora_cb(self, lora):
        """
        LoRa radio events callback handler.
        """

        events = lora.events()
        if events & LoRa.RX_PACKET_EVENT:
            self.rxnb += 1
            self.rxok += 1
            rx_data = self.lora_sock.recv(256)
            stats = lora.stats()
            packet = self._make_node_packet(rx_data, self.rtc.now(), stats.rx_timestamp, stats.sfrx, self.bw, stats.rssi, stats.snr)
            self._push_data(packet)
            self._log('Received packet: {}', packet)
            self.rxfw += 1
        if events & LoRa.TX_PACKET_EVENT:
            self.txnb += 1
            lora.init(
                mode=LoRa.LORA,
                region=LoRa.EU868,
                frequency=self.frequency,
                bandwidth=self.bw,
                sf=self.sf,
                preamble=8,
                coding_rate=LoRa.CODING_4_5,
                tx_iq=True
                )

    def _freq_to_float(self, frequency):
        """
        MicroPython has some inprecision when doing large float division.
        To counter this, this method first does integer division until we
        reach the decimal breaking point. This doesn't completely elimate
        the issue in all cases, but it does help for a number of commonly
        used frequencies.
        """

        divider = 6
        while divider > 0 and frequency % 10 == 0:
            frequency = frequency // 10
            divider -= 1
        if divider > 0:
            frequency = frequency / (10 ** divider)
        return frequency

    def _make_stat_packet(self):
        now = self.rtc.now()
        STAT_PK["stat"]["time"] = "%d-%02d-%02d %02d:%02d:%02d GMT" % (now[0], now[1], now[2], now[3], now[4], now[5])
        STAT_PK["stat"]["rxnb"] = self.rxnb
        STAT_PK["stat"]["rxok"] = self.rxok
        STAT_PK["stat"]["rxfw"] = self.rxfw
        STAT_PK["stat"]["dwnb"] = self.dwnb
        STAT_PK["stat"]["txnb"] = self.txnb
        return ujson.dumps(STAT_PK)

    def _make_node_packet(self, rx_data, rx_time, tmst, sf, bw, rssi, snr):
        RX_PK["rxpk"][0]["time"] = "%d-%02d-%02dT%02d:%02d:%02d.%dZ" % (rx_time[0], rx_time[1], rx_time[2], rx_time[3], rx_time[4], rx_time[5], rx_time[6])
        RX_PK["rxpk"][0]["tmst"] = tmst
        RX_PK["rxpk"][0]["freq"] = self._freq_to_float(self.frequency)
        RX_PK["rxpk"][0]["datr"] = self._sf_bw_to_dr(sf, bw)
        RX_PK["rxpk"][0]["rssi"] = rssi
        RX_PK["rxpk"][0]["lsnr"] = snr
        RX_PK["rxpk"][0]["data"] = ubinascii.b2a_base64(rx_data)[:-1]
        RX_PK["rxpk"][0]["size"] = len(rx_data)
        return ujson.dumps(RX_PK)

    def _push_data(self, data):
        token = uos.urandom(2)
        packet = bytes([PROTOCOL_VERSION]) + token + bytes([PUSH_DATA]) + ubinascii.unhexlify(self.id) + data
        with self.udp_lock:
            try:
                self.sock.sendto(packet, self.server_ip)
            except Exception as ex:
                self._log('Failed to push uplink packet to server: {}', ex)

    def _pull_data(self):
        token = uos.urandom(2)
        packet = bytes([PROTOCOL_VERSION]) + token + bytes([PULL_DATA]) + ubinascii.unhexlify(self.id)
        with self.udp_lock:
            try:
                self.sock.sendto(packet, self.server_ip)
            except Exception as ex:
                self._log('Failed to pull downlink packets from server: {}', ex)

    def _ack_pull_rsp(self, token, error):
        TX_ACK_PK["txpk_ack"]["error"] = error
        resp = ujson.dumps(TX_ACK_PK)
        packet = bytes([PROTOCOL_VERSION]) + token + bytes([PULL_ACK]) + ubinascii.unhexlify(self.id) + resp
        with self.udp_lock:
            try:
                self.sock.sendto(packet, self.server_ip)
            except Exception as ex:
                self._log('PULL RSP ACK exception: {}', ex)

    def _send_down_link(self, data, tmst, datarate, frequency):
        """
        Transmits a downlink message over LoRa.
        """

        self.lora.init(
            mode=LoRa.LORA,
            region=LoRa.EU868,
            frequency=frequency,
            bandwidth=self._dr_to_bw(datarate),
            sf=self._dr_to_sf(datarate),
            preamble=8,
            coding_rate=LoRa.CODING_4_5,
            tx_iq=True
            )
        while utime.ticks_diff(utime.ticks_cpu(), tmst) > 0:
            pass
        self.lora_sock.settimeout(1)
        self.lora_sock.send(data)
        self.lora_sock.setblocking(False)
        self._log(
            'Sent downlink packet scheduled on {:.3f}, at {:,d} Hz using {}: {}',
            tmst / 1000000,
            frequency,
            datarate,
            data
        )

    def _udp_thread(self):
        """
        UDP thread, reads data from the server and handles it.
        """

        while not self.udp_stop:
            gc.collect()
            try:
                data, src = self.sock.recvfrom(1024)
                _token = data[1:3]
                _type = data[3]
                if _type == PUSH_ACK:
                    self._log("Push ack")
                elif _type == PULL_ACK:
                    self._log("Pull ack")
                elif _type == PULL_RESP:
                    self.dwnb += 1
                    ack_error = TX_ERR_NONE
                    tx_pk = ujson.loads(data[4:])
                    payload = ubinascii.a2b_base64(tx_pk["txpk"]["data"])
                    # depending on the board, pull the downlink message 1 or 6 ms upfronnt
                    tmst = utime.ticks_add(tx_pk["txpk"]["tmst"], self.window_compensation)
                    t_us = utime.ticks_diff(utime.ticks_cpu(), utime.ticks_add(tmst, -15000))
                    if 1000 < t_us < 10000000:
                        self.uplink_alarm = Timer.Alarm(
                            handler=lambda x: self._send_down_link(
                                payload,
                                tmst, tx_pk["txpk"]["datr"],
                                int(tx_pk["txpk"]["freq"] * 1000 + 0.0005) * 1000
                            ),
                            us=t_us
                        )
                    else:
                        ack_error = TX_ERR_TOO_LATE
                        self._log('Downlink timestamp error!, t_us: {}', t_us)
                    self._ack_pull_rsp(_token, ack_error)
                    self._log("Pull rsp")
            except usocket.timeout:
                pass
            except OSError as ex:
                if ex.args[0] != errno.EAGAIN:
                    self._log('UDP recv OSError Exception: {}', ex)
            except Exception as ex:
                self._log('UDP recv Exception: {}', ex)

            self.watchdog.feed()
            # self._log("Feeding the dog")

            # wait before trying to receive again
            utime.sleep_ms(UDP_THREAD_CYCLE_MS)

        # we are to close the socket
        self.sock.close()
        self.udp_stop = False
        self._log('UDP thread stopped')

    def _log(self, message, *args):
        """
        Outputs a log message to stdout.
        """

        print('[{:>10.3f}] {}'.format(
            utime.ticks_ms() / 1000,
            str(message).format(*args)
            ))

```

## Registering with TTN

To set up the gateway with The Things Network (TTN), navigate to their website and create/register an account. Enter a username and an email address to verify with their platform.

![](/gitbook/assets/ttn-1.png)

Once an account has been registered, the nano-gateway can then be registered. To do this, navigate to the TTN Console web page.

### Registering the Gateway

Inside the TTN Console, there are two options, `applications` and `gateways`. Select `gateways` and then click on `register gateway`. This will allow for the set up and registration of a new nano-gateway.

![](/gitbook/assets/ttn-2.png)

On the Register Gateway page, you will need to set the following settings:

![](/gitbook/assets/ttn-gatewayreg-11-2017-2.jpg) These are unique to each gateway, location and country specific frequency. Please verify that correct settings are selected otherwise the gateway will not connect to TTN.

**You need to tick the "I'm using the legacy packet forwarder" to enable the right settings.** This is because the Nano-Gateway uses the 'de facto' standard Semtech UDP protocol.

| Option | Value |
| :--- | :--- |
| Protocol | Packet Forwarder |
| Gateway EUI | User Defined (must match `config.py`) |
| Description | User Defined |
| Frequency Plan | Select Country (e.g. EU - 868 MHz) |
| Location | User Defined |
| Antenna Placement | Indoor or Outdoor |

The Gateway EUI should match your Gateway ID from the `config.py` file. We suggest you follow the procedure described near the top of this document to create your own unique Gateway ID.

Once these settings have been applied, click `Register Gateway`. A Gateway Overview page will appear, with the configuration settings showing. Next click on the `Gateway Settings` and configure the Router address to match that of the gateway (default: `router.eu.thethings.network`).

![](/gitbook/assets/ttn-4.png)

The `Gateway` should now be configured. Next, one or more nodes can now be configured to use the nano-gateway and TTN applications may be built.

### Nano-gateway node

As the gateway only supports a single channel, we need to setup our nodes to only send packets over that channel. The node can either use OTAA or ABP, but we'll have to setup the correct channel. Use the following example to setup the correct channels for EU868. This can be modified for use in 915MHz regions as well:

```python

# remove all the default channels for EU868
for i in range(3, 16):
    lora.remove_channel(i)

# set the 3 default channels to the same frequency (must be before sending the join request)
lora.add_channel(0, frequency=868100000, dr_min=0, dr_max=5)
lora.add_channel(1, frequency=868100000, dr_min=0, dr_max=5)
lora.add_channel(2, frequency=868100000, dr_min=0, dr_max=5)

# remove all the default channels for US915 / AU915
for i in range(3, 64):
    lora.remove_channel(i)

# set the 3 default channels to the same frequency (must be before sending the join request)
lora.add_channel(0, frequency=903900000, dr_min=0, dr_max=3)
lora.add_channel(1, frequency=903900000, dr_min=0, dr_max=3)
lora.add_channel(2, frequency=903900000, dr_min=0, dr_max=3)
```


## TTN Setup

Now that the gateway & nodes have been setup, a TTN Application can be built; i.e. what happens to the LoRa data once it is received by TTN. There are a number of different setups/systems that can be used, however the following example demonstrates the HTTP request integration.

### Registering an Application (Gateway)

Selecting the `Applications` tab at the top of the TTN console, will bring up a screen for registering applications. Click register and a new page, similar to the one below, will open.

![](/gitbook/assets/ttn-5.png)

Enter a unique `Application ID` as well as a Description & Handler Registration.

Now the LoPy nodes must be registered to send data up to the new Application.

### Registering Nodes

To connect nodes to the nano-gateway, devices need to be added to the application. To do this, navigate to the `Devices` tab on the `Application` home page and click the `Register Device` button.

![](/gitbook/assets/ttn-6.png)

In the `Register Device` panel, complete the forms for the `Device ID` and the `Device EUI`. The `Device ID` is user specified and is unique to the device in this application. The `Device EUI` is also user specified but must consist of exactly 8 bytes, given in hexadecimal.

Once the device has been added, change the `Activation Method` between `OTAA` and `ABP` depending on user preference. This option can be found under the Settings tab.

### Adding Application Integrations

Now that the data is arriving on the TTN Backend, TTN can be managed as to where data should be delivered to. To do this, use the `Integrations` tab within the new Application's settings.

![](/gitbook/assets/ttn-7.png)

Upon clicking `add integration`, a screen with 4 different options will appear. These have various functionality and more information about them can be found on the TTN website/documentation.

For this example, use the `HTTP Integration` to forward the LoRaWAN Packets to a remote server/address.

![](/gitbook/assets/ttn-8.png)

Click `HTTP Integration` to connect up an endpoint that can receive the data.

For testing, a website called [RequestBin](https://requestbin.com/), may be used to receive the data that TTN forwards (via POST Request). To set this up, navigate to [RequestBin](https://requestbin.com/) and click the `Create a RequestBin`.

![](/gitbook/assets/ttn-9.png)

Copy the URL that is generated and past this into the `URL` form under the `Application Settings`.

![](/gitbook/assets/ttn-10.png)

This is the address that TTN will forward data onto. As soon as a LoPy starts sending messages, TTN will forward these onto `RequestBin` and they will appear at the unique `RequestBin URL`.
