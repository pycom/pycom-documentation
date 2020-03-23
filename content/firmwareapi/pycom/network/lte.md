---
title: "LTE"
aliases:
    - firmwareapi/pycom/network/lte.html
    - firmwareapi/pycom/network/lte.md
    - chapter/firmwareapi/pycom/network/lte
---

The LTE class provides access to the LTE-M/NB-IoT modem on the GPy and FiPy. LTE-M/NB-IoT are new categories of cellular protocols developed by the [3GPP](http://www.3gpp.org) and optimised for long battery life power and longer range. These are new protocols currently in the process of being deployed by mobile networks across the world.

The GPy and FiPy support both new LTE-M protocols:

* **Cat-M1**: also known as **LTE-M** defines a 1.4 MHz radio channel size and about 375 kbps of throughput. It is optimised for coverage and long battery life, outperforming 2G/GPRS, while being similar to previous LTE standards.
* **Cat-NB1** also known as **NB-IoT**, defines a 200 kHz radio channel size and around 60 kbps of uplink speed. It's optimised for ultra low throughput and specifically designed for IoT devices with a very long battery life. NB-IoT shares some features with LTE such as operating in licensed spectrum, but it's a very different protocol. It should be noted that NB-IoT has many restrictions as does not offer full IP connectivity and does not support mobility. When moving between cells, you will need to reconnect.

{{% hint style="info" %}}
**Please note:** The GPy and FiPy only support the two protocols above and are not compatible with older LTE standards.
{{% /hint %}}

{{% hint style="info" %}}
The Sequans modem used on Pycom's cellular enabled modules can only work in one of these modes at a time. In order to switch between the two protocols you need to flash a different firmware to the Sequans modem. Instructions for this can be found [here](/tutorials/lte/firmware).
{{% /hint %}}

{{% hint style="info" %}}

**FiPy/Gpy Band Support**

- Fipy/GPy v1.0 ==> supports 6 bands only (3, 4, 12, 13, 20, 28)

- Fipy/GPy v1.2  with Sequans modem Firmware (41xxx) ==> Supports Full range of 17 bands (1, 2, 3, 4, 5, 8, 12, 13, 14, 17, 18, 19, 20, 25, 26, 28, 66)

- Fipy/GPy v1.2  with Sequans older modem Firmwares  (39xxx)==> Supports 8 Bands (3, 4, 5, 8, 12, 13, 20, 28)

- Fipy/GPy v1.2  with Sequans old modem Firmwares  < (39xxx)==> Supports 6 Bands (3, 4, 12, 13, 20, 28)

{{% /hint %}}

## AT Commands

The AT commands for the Sequans Monarch modem on the GPy/FiPy are available in a PDF file.
<a href="/gitbook/assets/Monarch-LR5110-ATCmdRefMan-rev6_noConfidential.pdf" target="_blank"> AT Commands for Sequans </a>

## Constructors

#### class network.LTE(id=0, ...)

Create and configure a LTE object. See init for params of configuration.

```python

from network import LTE
lte = LTE()
```

## Methods

#### lte.init(\*, carrier=None)

This method is used to set up the LTE subsystem. After a `deinit()` this method can take several seconds to return waiting for the LTE modem to start-up. Optionally specify a carrier name. The available options are: `verizon, at&t, standard`. `standard` is generic for any carrier, and it's also the option used when no arguments are given.

**Power Saving Mode**

The _Power Saving Mode_ allows a user to configure how often a device will connect and how long it will stay connected. Upon `attach()` this configuration is then requested from the network. Ultimately it is up to the network to decide the PSM configuration. After a successful PSM configuration,

- the LTE modem will go into a low power state during deep sleep, but
- it will stay attached to the network, thus no time is spent for `attach()` after waking up.

The configuration is done with these four parameters:

- `psm_period_value` : Configure at which period the device will connect to the network. Values from 0 to 31 are allowed.
- `psm_period_unit` : Specify the _unit_ to be used for `psm_period_value`.
- `psm_active_value` : Configure how long the device will be connected. Values from 0 to 31 are allowed.
- `psm_active_unit` : Specify the _unit_ for `psm_active_value`.

The LTE specification prescribes certain _units_ for configuring PSM. See the constants below.

For the following example, assume you want to wake up once per hour, connect and do some processing, then go to deepsleep for 55 minutes:

```python

from network import LTE
import time
import socket
import machine
import pycom

def attach():
    start = time.time()
    if lte.isattached():
        print("already attached")
    else:
        print("attach")
        lte.attach(band=20, apn="spe.inetd.vodafone.nbiot")
        while not lte.isattached():
            time.sleep(1)
    print("attached after", time.time() - start, "seconds")
    print(lte.psm())

def connect():
    print("connect")
    start = time.time()
    lte.connect()
    while not lte.isconnected():
        time.sleep(0.5)
    print("connected after", time.time() - start, "seconds")

def http_get(url = 'http://detectportal.firefox.com/'):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    s.close()

# period 1h, active 10s
lte = LTE(psm_period_value=1, psm_period_unit=LTE.PSM_PERIOD_1H,
          psm_active_value=5, psm_active_unit=LTE.PSM_ACTIVE_2S )
print(lte.psm())
attach()
connect()
http_get()
print("deinit")
lte.deinit(detach=False, reset=False)
print("deepsleep")
machine.deepsleep(55 * 60 * 1000) # 55m
```

#### lte.deinit(detach=True, reset = False)

Disables LTE modem completely. This reduces the power consumption to the minimum. Call this before entering deepsleep.

- `detach` : detach from network.

- `reset` : reset LTE modem.

#### lte.attach(\*, band=None, apn=None, cid=None, type=LTE.IP, legacyattach=True)

Enable radio functionality and attach to the LTE network authorised by the inserted SIM card. Optionally specify:

- `band` : to scan for networks. If no band (or `None`) is specified, all 8 bands will be scanned. The possible values for the band are: `3, 4, 5, 8, 12, 13, 20 and 28`.

- `apn` : Specify the APN (Access point Name).

- `cid` : connection ID, see `LTE.connect()`. when the ID is set here it will be remembered when doint connect so no need to specify again

- `type` : PDP context type either `LTE.IP` or `LTE.IPV4V6`. These are options to specify PDP type ‘Packet Data protocol' either IP [Internet Protocol] or IPV4V6 ver4,6 , that depends actually on what does the Network support.

- `legacyattach` : When kept = True the API `LTE.isattached()` will return True when attached to the Network AND Network registration status is home or roaming, when flag is False, API `LTE.isattached()` will return True when attached to the Network only.

---
*NOTE* :
When carrier is specified in `LTE()` or `LTE.init()` (eg. `lte = LTE(carrier=verizon)`) No need to specify band, apn or type these parameters are already programmed in to the LTE modem for each carrier.

---

#### lte.isattached()

Returns `True` if the cellular mode is attached to the network. `False` otherwise.

#### lte.detach(reset=False)

Detach the modem from the LTE Cat M1 and disable the radio functionality.

- `reset` : set to True to reset the LTE modem.

#### lte.connect(\*, cid=1)

Start a data session and obtain and IP address. Optionally specify a CID (Connection ID) for the data session. The arguments are:

* `cid` is a Connection ID. This is carrier specific, for Verizon use `cid=3`. For others like Telstra it should be `cid=1`.

For instance, to attach and connect to Verizon:

```python

import time
from network import LTE

lte = LTE(carrier="verizon")
lte.attach(band=13)

while not lte.isattached():
    time.sleep(0.5)
    print('Attaching...')

lte.connect(cid=3)
while not lte.isconnected():
    time.sleep(0.5)
    print('Connecting...')

# Now use sockets as usual...
```

#### lte.isconnected()

Returns `True` if there is an active LTE data session and IP address has been obtained. `False` otherwise.

#### lte.disconnect()

End the data session with the network.

#### lte.send\_at\_cmd(cmd, delay=10000)

Send an AT command directly to the modem. Returns the raw response from the modem as a string object. **IMPORTANT:** If a data session is active (i.e. the modem is _connected_), sending the AT commands requires to pause and then resume the data session. This is all done automatically, but makes the whole request take around 2.5 seconds.

Example:

```python

lte.send_at_cmd('AT+CEREG?')    # check for network registration manually (sames as lte.isattached())
```

Optionally the response can be parsed for pretty printing:

```python

def send_at_cmd_pretty(cmd):
    response = lte.send_at_cmd(cmd).split('\r\n')
    for line in response:
        print(line)

send_at_cmd_pretty('AT!="showphy"')     # get the PHY status
send_at_cmd_pretty('AT!="fsm"')         # get the System FSM
```

- `delay` : specify the number of milliseconds the esp32 chip will wait between sending an AT command to the modem. and reading the response.

#### lte.imei()

Returns a string object with the IMEI number of the LTE modem.

#### lte.iccid()

Returns a string object with the ICCID number of the SIM card.

#### lte.reset()

Perform a hardware reset on the cellular modem. This function can take up to 5 seconds to return as it waits for the modem to shutdown and reboot.

#### lte.pppsuspend()

Suspend PPP session with LTE modem. this function can be used when needing to send AT commands which is not supported in PPP mode.

#### lte.pppresume()

Resumes PPP session with LTE modem.

#### lte.factory\_reset()

Reset modem configuration to Factory settings.

#### lte.modem\_upgrade\_mode()

 Puts the modem in to modem upgrade mode and bridging LTE modem UART port to FiPy/GPy UART0 to enable upgrading Firmware over USB port.

 ---
 *NOTE* :
 In this mode all All tasks on the board are halted and a reset is required to regain functionality.
 ---

#### lte.reconnect\_uart()

Reconnect esp32 UART 2 to LTE modem UART port.

#### lte.ue\_coverage()

Check Network Coverage for UE device (i.e LTE modem).

`True`: There is Network Coverage.

`False`: No Netwok Coverage.


## Constants

- `LTE.IP` : Internet Protocol IP

- `LTE.IPV4V6` : Internet protocol ver. 4/6

- `PSM_PERIOD_2S`, `PSM_PERIOD_30S`, `PSM_PERIOD_1M`, `PSM_PERIOD_10M`, `PSM_PERIOD_1H`, `PSM_PERIOD_10H`, `PSM_PERIOD_320H`: Specify the unit for the PSM period to be 2 seconds, 30 seconds, 1 minute, 10 minutes, 1 hour, 10 hours, or 320 hours, respectively.
- `PSM_PERIOD_DISABLED`: Specifying the unit for PSM period of `PSM_PERIOD_DISABLED` means turning PSM off. This is the default.
- `PSM_ACTIVE_2S`, `PSM_ACTIVE_1M`, `PSM_ACTIVE_6M`: Specify the unit for the PSM active duration to be 2 seconds, 1 minute, or 6 minutes, respectively.
- `PSM_ACTIVE_DISABLED`: Specifying the active duration unit of `PSM_ACTIVE_DISABLED` means turning PSM off. This is the default.
