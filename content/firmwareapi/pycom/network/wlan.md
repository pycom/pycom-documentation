---
title: "WLAN"
aliases:
    - firmwareapi/pycom/network/wlan.html
    - firmwareapi/pycom/network/wlan.md
    - chapter/firmwareapi/pycom/network/wlan
---
This class provides a driver for the WiFi network processor in the module. Example usage:

```python
import network
import time
# setup as a station
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect('your-ssid', auth=(network.WLAN.WPA2, 'your-key'))
while not wlan.isconnected():
    time.sleep_ms(50)
print(wlan.ifconfig())

# now use socket as usual
```

## Quick Usage Example

```python
import machine
from network import WLAN

# configure the WLAN subsystem in station mode (the default is AP)
wlan = WLAN(mode=WLAN.STA)
# go for fixed IP settings (IP, Subnet, Gateway, DNS)
wlan.ifconfig(config=('192.168.0.107', '255.255.255.0', '192.168.0.1', '192.168.0.1'))
wlan.scan()     # scan for available networks
wlan.connect(ssid='mynetwork', auth=(WLAN.WPA2, 'my_network_key'))
while not wlan.isconnected():
    pass
print(wlan.ifconfig())
```

## Constructors

### class network.WLAN([id=0], ...)

Create a WLAN object, and optionally configure it. See init for params of configuration.

> The WLAN constructor is special in the sense that if no arguments are given, it will return the already existing WLAN instance without re-configuring it. This is because WLAN is a system feature of the WiPy. If the already existing instance is not initialised it will do the same as the other constructors an will initialise it with default values.

## Methods

#### wlan.init(mode, [ssid=None, auth=None, channel=1, antenna=WLAN.INT_ANT, power_save=False, hidden=False, bandwidth=WLAN.HT40, max_tx_pwr, country=NA, protocol=(1,1,1)])

Set or get the WiFi network processor configuration.

Arguments are:

* `mode`: can be either:
  * `WLAN.STA`: Station mode, connect to a WiFinetwork
  * `WLAN.AP`: Access Point mode, create a WiFi network. You _must_ specify the `ssid`
  * `WLAN.STA_AP`: Both Station and Access Point mode are active. 
* `ssid`: a string with the SSID name.
* `auth`: a tuple with `(sec, key)`. Security can be one of the following. The key is a string with the network password.
  * `None`: 
  * `WLAN.WEP`: Using this in `WLAN.AP`, the key must be a string of hexadecimal values.
  * `WLAN.WPA`
  * `WLAN.WPA2`
  * `WLAN.WPA2_ENT`: this will use the following format: `(sec, username, password)`
* `channel`: a number in the range 1-11. Only needed when mode is `WLAN.AP`.
* `antenna`: select between the internal and the external antenna. With our development boards it defaults to using the on-board antenna. Value can be either:
  * `WLAN.INT_ANT`
  * `WLAN.EXT_ANT`
* `power_save` enables or disables power save functions in `WLAN.STA` mode.
* `hidden`: create a hidden SSID when set to `True`. only valid in `WLAN.AP` mode.
* `bandwidth` is the Bandwidth to use, either:
  * `WLAN.HT20`: 20MHz
  * `WLAN.HT40`: 40MHz
* `max_tx_pwr` is the maximum WiFi TX power allowed. see `WLAN.max_tx_power()` for more details
* `country` tuple representing the country configuration parameters. see `WLAN.country()` for more details
* `protocol` tuple representing the protocol. see `WLAN.wifi_protocol()` for more details


### wlan.deinit()

Disables the WiFi radio.

### wlan.connect(ssid, [auth=None, bssid=None, timeout=None, ca_certs=None, keyfile=None, certfile=None, identity=None, hostname=None])

Connect to a WiFi Access Point using the given SSID, and other parameters

* `ssid`: a string with the SSID name.
* `auth`: a tuple with `(sec, key)`. Security can be one of the following. The key is a string with the network password.
  * `None`: 
  * `WLAN.WEP`: Using this in `WLAN.AP`, the key must be a string of hexadecimal values.
  * `WLAN.WPA`
  * `WLAN.WPA2`
  * `WLAN.WPA2_ENT`: this will use the following format: `(sec, username, password)`
* `bssid` is the MAC address of the AP to connect to. This is useful when there are several APs with the same SSID.
* `timeout` is the maximum time in milliseconds to wait for the connection to succeed.
* `ca_certs` is the path to the CA certificate. This argument is not mandatory.
* `keyfile` is the path to the client key. Only used if `username` and `password` are not part of the `auth` tuple.
* `certfile` is the path to the client certificate. Only used if `username` and `password` are not part of the `auth` tuple.
* `identity` is only used in case of `WLAN.WPA2_ENT` security. Needed by the server.
* `hostname` is the name of the host connecting to the AP. Max length of name string is 32 Bytes

> The ESP32 only handles certificates with `pkcs8` format (but not the "Traditional SSLeay RSAPrivateKey" format). The private key should be RSA coded with 2048 bits at maximum.


### wlan.scan([ssid=None, bssid=None, channel=0, show_hidden=False, type=WLAN.SCAN_ACTIVE, scantime=120ms])

Performs a network scan and returns a list of named tuples with (ssid, bssid, sec, channel, rssi). When no config args passed scan will be performed with default configurations.

Note: For Fast scan mode ssid/bssid and channel should be

* `ssid`: Scan only for the given ssid
* `bssid`: Scan only for the givenbssid. The bssid is given as 6 Hexadecimal bytes literals (i.e `b'\xff\xff\xff\xff\xff\xff'`)
* `channel`: If set to 0, there will be an all-channel scan; otherwise, there will be a specific-channel scan.
* `show_hidden`: Scan for hidden ssid's as well.
* `type`: The type of scan performed. Values can be 
  * `WLAN.SCAN_ACTIVE`: the scan is will be performed by sending a probe request. 
  * `WLAN.SCAN_PASSIVE`: switches to a specifi channel and waits for beacon
* `scantime` : This field is used to control how long the scan dwells on each channel. For active scans, dwell times for each channel are listed below. For passive scans, this designates the dwell time for each channel. scantime is given as a tuple for min and max times `(min,max)`
  * min=0, max=0: scan dwells on each channel for 120 ms.
  * min>0, max=0: scan dwells on each channel for 120 ms.
  * min=0, max>0: scan dwells on each channel for max ms.
  * min>0, max>0: The minimum time the scan dwells on each channel is min ms. If no AP is found during this time frame, the scan switches to the next channel. Otherwise, the scan dwells on the channel for max ms.If you want to improve the performance of the the scan, you can try to modify these two parameters.

### wlan.disconnect()

Disconnect from the WiFi access point.

### wlan.isconnected()

In case of STA mode, returns `True` if connected to a WiFi access point and has a valid IP address. In AP mode returns `True` when a station is connected, `False` otherwise.

### wlan.ifconfig(id=0, config=['dhcp' or configtuple])

When `id` is 0, the configuration will be get/set on the Station interface. When `id` is 1 the configuration will be done for the AP interface.

Get or set the interface configuration. 

Optionally specify the configuration parameter:

* `config='dhcp'`: If 'dhcp' is passed as a parameter, then the DHCP client is enabled and the IP parameters are negotiated with the DHCP server.
* `config=(ip, nm, gw, dns)`: If the 4-tuple config is given then a static IP is configured. 

For example: `eth.ifconfig(config=('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))`.

### wlan.mode([mode])

Get or set the WLAN mode.

### wlan.ssid([ssid])

Get or set the SSID (Set SSID of AP).

In case if mode = `WLAN.STA` this method can get the ssid of AP the board is connected to.

In case of mode = `WLAN.AP` this method can get the ssid of the board's own AP.

In case of mode = `WLAN.STA_AP` this method can get the ssid of board's own AP plus the AP the STA is connected to in form of a tuple:


### wlan.auth([auth])

Get or set the authentication type when in AP mode.

### wlan.channel([channel, secondary_channel=WLAN.SEC_CHN_NONE])

* In AP mode, this will get or set the WiFi channel. The secondary channel has no effect.
* In STA mode, this will get the channel. Setting the channel is only allowed in Promiscuous mode. A secondary channel can be given as well if the bandwidth is set to `WLAN.HT40`, choosing from the following:
  * `WLAN.SEC_CHN_POS_ABOVE`: Choose a secondary channel above the currently selected channel
  * `WLAN.SEC_CHN_POS_BELOW`: Choose a secondary channel below the currently selected channel
  * `WLAN.SEC_CHN_NONE`
Possible channels are in the range of 1-14, depending on your country settings.

### wlan.antenna([antenna])

Get or set the antenna type (external or internal). Value can be:


### wlan.mac([mac, mode])

when no arguments are passed a 6-byte long `bytes` tuple object with the WiFI MAC address of both Wifi Station mode and Acces Point mode

`mac`: a 6 bytes bytearray mac address

`mode`: The Interface to set the given MAC address to `WLAN.STA` or `WLAN.AP`

Ex: To set the mac address of Wifi Station mode:

```python
wlan.mac(bytearray([0xAE, 0x77, 0x88, 0x99, 0x22, 0x44]), WLAN.STA)
```

_Note: STA and AP cannot have the Same Mac Address_

### wlan.bandwidth()

Set the bandwidth of the wifi, either 20 MHz or 40 MHz can be configured, use the following:
* `WLAN.HT20`: 20MHz
* `WLAN.HT40`: 40MHz

### wlan.hostname()

Set the Host name of the device connecting to the AP in case of Wifi `mode=WLAN.STA`, in case of `mode=WLAN.AP` this is the name of the host hosting the AP. Max length of name string is 32 Bytes

### wlan.ap_sta_list()

Gets an info list of all stations connected to the board's AP.

Info returned is a list of tuples containning ([mac address of connected STA], [average rssi value], [Wlan protocol enabled by STA]).

Protocol types are either : `WLAN.PHY_11_B`, `WLAN.PHY_11_G`, `WLAN.PHY_11_N` or `WLAN.PHY_LOW_RATE`

### wlan.ap_tcpip_sta_list()

This API returns with a list of the devices connected to the Pycom board when it is in AP mode.
Each element of the returned list is a tuple, containing the MAC address and IP address of the device.

### wlan.max_tx_power([power])

Gets or Sets the maximum allowable transmission power for wifi. This is also related to the country setting.

Packets of different rates are transmitted in different powers according to the configuration in phy init data. This API only sets maximum WiFi transmiting power. If this API is called, the transmiting power of every packet will be less than or equal to the value set by this API.

Values passed in power are mapped to transmit power levels as power = [8, 78] = [2, 20] dBm, in 0.25dBm increments.

### wlan.country([country, schan, nchan, max_tx_pwr, policy])

Gets or sets Country configuration parameters for wifi.

* `country` That is the country name code , it is max 2 characters string representing the country eg: "CN" for china nad "NL" for Netherlands
* `scahn` is the start channel number, in scan process scanning will be performed starting from this channels till the total number of channels. it should be less than or equal 14.
* `nchan` is the total number of channels in the specified country. maximum is 14
* `max_tx_pwr` Maximum transmission power allowed. see `WLAN.max_tx_power()` for more details.
* `policy` Is the method when setting country configuration. Possible options are
  * `WLAN.COUNTRY_POL_AUTO` in STA mode the wifi will aquire the same country config of the connected AP
  * `WLAN.COUNTRY_POL_MAN` the configured country parameters will take effect regardless of connected AP.

### wlan.joined_ap_info()

Returns a tuple with `(bssid, ssid, primary channel, rssi, Authorization method, wifi standard used)` of the connected AP in case of STA mode.

### wlan.wifi_protocol([(bool PHY11_B, bool PHY11_G, bool PHY11_N)])


Sets or gets Wifi Protocol supported.	Sets or gets Wifi Protocol supported in (`PHY_11_B`,`PHY_11_G`,`PHY_11_N`) format. Currently 802.11b or 802.11bg or 802.11bgn mode is available.

### wlan.send_raw(Buffer, interface=STA, use_sys_seq=True)

Send raw data through the Wifi Interface.

`Buffer`: Buffer of bytes object Containning Data to be transmitted. Data should not be greater than 1500 nor smaller than 24.

`interface`: The Interface to use for transmitting Data AP or STA in case the mode used is APSTA. other wise the interface currently active will be used.

`use_sys_seq`: `True` to use the systems next sequance number for sending the data, `False` for keeping the sequance number in the given raw data buffer unchanged.

### wlan.callback(trigger, [handler=Null, arg=Null])

Register a user callback function `handler` to be called once any of the `trigger` events occures optionally with a passed `arg`. by default the wlan obj is passed as arg to the handler. To unregister the callback you can call the `wlan.callback` function with empty `handler` and `arg` parameters. Possible triggers:

* `WLAN.EVENT_PKT_MGMT`: Managment packet recieved in promiscuous mode.
* `WLAN.EVENT_PKT_CTRL`: Control Packet recieved in promiscuous mode
* `WLAN.EVENT_PKT_DATA`: Data packet recieved in promiscuous mode
* `WLAN.EVENT_PKT_DATA_MPDU`: MPDU data packet recieved in promiscuous mode
* `WLAN.EVENT_PKT_DATA_AMPDU`: AMPDU data packet recieved in promiscuous mode
* `WLAN.EVENT_PKT_MISC`: misc paket recieved in promiscuous mode.
* `WLAN.EVENT_PKT_ANY`: Any packet recieved in promiscuous mode. 
* `WLAN.SMART_CONF_DONE`: Smart Config of wifi ssid/pwd Finished
* `WLAN.SMART_CONF_TIEMOUT`: Smart Config of wifi ssid/pwd timed-out

### wlan.promiscuous([bool])

Gets or sets WiFi Promiscuous mode. 

Note:

* Promiscuous mode should be enabled for Wifi packets types Events to be triggered
* for changing wifi channel via `wlan.channel()` promiscuous mode should be enabled.

Example using promoscious mode:

```python
from network import WLAN
import ubinascii

def pack_cb(pack):
    mac = bytearray(6)
    pk = wlan.wifi_packet()
    control = pk.data[0]
    subtype = (0xF0 & control) >> 4
    type = 0x0C & control
    #print("Control:{}, subtype:{}, type:{}".format(control, subtype, type))
    if subtype == 4:
        for i in range (0,6):
            mac[i] = pk.data[10 + i]
        print ("Wifi Node with MAC: {}".format(ubinascii.hexlify(mac)))

wlan = WLAN(mode=WLAN.STA, antenna=WLAN.EXT_ANT)
wlan.callback(trigger=WLAN.EVENT_PKT_MGMT, handler=pack_cb)
wlan.promiscuous(True)
```

### wlan.events()

This function will return an integer object as mask for triggered events.

### wlan.wifi_packet()

This function will return a tuble with Wifi packet info captured in promiscuous mode.

### wlan.ctrl_pkt_filter([int])

This function is used to set the filter mask for Wifi control packets in promiscuous mode. Possible filters:

* `WLAN.FILTER_CTRL_PKT_ALL`: Filter all Control packets
* `WLAN.FILTER_CTRL_PKT_WRAPPER`: Filter control wrapper packets
* `WLAN.FILTER_CTRL_PKT_BAR`: Filter Control BAR packets
* `WLAN.FILTER_CTRL_PKT_BA`: Filter Control BA packets
* `WLAN.FILTER_CTRL_PKT_PSPOLL`: Filter Control PSPOLL Packets
* `WLAN.FILTER_CTRL_PKT_CTS`: Filter Control CTS packets
* `WLAN.FILTER_CTRL_PKT_ACK`: Filter Control ACK packets
* `WLAN.FILTER_CTRL_PKT_CFEND`: Filter Control CFEND Packets
* `WLAN.FILTER_CTRL_PKT_CFENDACK`: Filter Control CFENDACK Packets


To get the current Filter mask, call the function with empty args.

### wlan.smartConfig()

Start SmartConfig operation, the smartConfig is a provisioning technique that enables setting Wifi credentials for station mode wirelessly via mobile app.

#### Steps:
- call `wlan.smartConfig()` (if smartConfig is not enabled on boot or you want to restart smartConfig)
- Use mobile App (ESP touch or Pycom App) to set ssid and password for the AP 
- You can register a callback to be triggered when smart Config is Finished successfuly or times out.

### wlan.Connected_ap_pwd()

Get the password of AP the Device is connected to.


## Constants

* WLAN mode: `WLAN.STA`, `WLAN.AP`, `WLAN.STA_AP`
* WLAN network security: `WLAN.WEP`, `WLAN.WPA`, `WLAN.WPA2`, `WLAN.WPA2_ENT`
* Antenna type: `WLAN.INT_ANT`, `WLAN.EXT_ANT`
* WLAN Bandwidth: `WLAN.HT20`, `WLAN.HT40`
* WLAN protocol: `WLAN.PHY_11_B`, `WLAN.PHY_11_G`, `WLAN.PHY_11_N`, `WLAN.PHY_LOW_RATE`
* Scan Type: `WLAN.SCAN_ACTIVE` `WLAN.SCAN_PASSIVE`
* WLAN country config policy: `WLAN.COUNTRY_POL_AUTO`, `WLAN.COUNTRY_POL_MAN`
* Secondary Channel position: `WLAN.SEC_CHN_POS_ABOVE`, `WLAN.SEC_CHN_POS_BELOW`, `WLAN.SEC_CHN_NONE`
* Wlan callback triggers: `WLAN.EVENT_PKT_MGMT`, `WLAN.EVENT_PKT_CTRL`, `WLAN.EVENT_PKT_DATA`, `WLAN.EVENT_PKT_DATA_MPDU`, `WLAN.EVENT_PKT_DATA_AMPDU`, `WLAN.EVENT_PKT_MISC`, `WLAN.EVENT_PKT_ANY`, `SMART_CONF_DONE`, `SMART_CONF_TIEMOUT`
* Control packet filters in promiscuous mode: `WLAN.FILTER_CTRL_PKT_ALL`, `WLAN.FILTER_CTRL_PKT_WRAPPER`, `WLAN.FILTER_CTRL_PKT_BAR`, `WLAN.FILTER_CTRL_PKT_BA`, `WLAN.FILTER_CTRL_PKT_PSPOLL`, `WLAN.FILTER_CTRL_PKT_CTS`, `WLAN.FILTER_CTRL_PKT_ACK`, `WLAN.FILTER_CTRL_PKT_CFEND`, `WLAN.FILTER_CTRL_PKT_CFENDACK`
