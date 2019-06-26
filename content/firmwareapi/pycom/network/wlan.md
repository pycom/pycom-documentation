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

### class network.WLAN(id=0, ...)

Create a WLAN object, and optionally configure it. See [`init`](../wlan#wlan-init-mode-ssid-none-auth-none-channel-1-antenna-none-power_save-false-hidden-false) for params of configuration.

{{% hint style="info" %}}
The WLAN constructor is special in the sense that if no arguments besides the `id` are given, it will return the already existing WLAN instance without re-configuring it. This is because WLAN is a system feature of the WiPy. If the already existing instance is not initialised it will do the same as the other constructors an will initialise it with default values.
{{< /hint >}}

## Methods

#### wlan.init(mode, \* , ssid=None, auth=None, channel=1, antenna=None, power\_save=False, hidden=False, bandwidth=HT40, max\_tx\_pwr=20, country=CN)

Set or get the WiFi network processor configuration.

Arguments are:

* `mode` can be either `WLAN.STA`, `WLAN.AP`, or `WLAN.STA_AP`.
* `ssid` is a string with the SSID name. Only needed when mode is `WLAN.AP`.
* `auth` is a tuple with (sec, key). Security can be `None`, `WLAN.WEP`, `WLAN.WPA`, or `WLAN.WPA2`. The key is a string with the network password.
  * If `sec` is `WLAN.WEP` the key must be a string representing hexadecimal values (e.g. `ABC1DE45BF`). Only needed when mode is `WLAN.AP`.
* `channel` a number in the range 1-11. Only needed when mode is `WLAN.AP`.
* `antenna` selects between the internal and the external antenna. Can be either `WLAN.INT_ANT`, `WLAN.EXT_ANT`. With our development boards it defaults to using the internal antenna, but in the case of an OEM module, the antenna pin (`P12`) is not used, so it's free to be

  used for other things.

* `power_save` enables or disables power save functions in `STA` mode.
* `hidden` only valid in `WLAN.AP` mode to create an access point with a hidden SSID when set to `True`.
* `bandwidth` is the Bandwidth to use, either 20MHz or 40 MHz , use `HT20` or `HT40`
* `max_tx_pwr` is the maximum WiFi Tx power allowed. see `WLAN.max_tx_power()` for more details
* `country` tuple representing the country configuration parameters. see `WLAN.country()` for more details

For example, you can do:

```python
# create and configure as an access point
wlan.init(mode=WLAN.AP, ssid='wipy-wlan', auth=(WLAN.WPA2,'www.wipy.io'), channel=7, antenna=WLAN.INT_ANT)
```

or

```python
# configure as an station
wlan.init(mode=WLAN.STA)
```

### wlan.deinit()

Disables the WiFi radio.

### wlan.connect(ssid, \* , auth=None, bssid=None, timeout=None, ca\_certs=None, keyfile=None, certfile=None, identity=None, hostname=None)

Connect to a wifi access point using the given SSID, and other security parameters.

* `auth` is a tuple with `(sec, key)`. Security can be `None`, `WLAN.WEP`, `WLAN.WPA`, `WLAN.WPA2` or `WLAN.WPA2_ENT`. The key is a string with the network password.
  * If `sec` is `WLAN.WEP` the key must be a string representing hexadecimal values (e.g. `ABC1DE45BF`).
  * If `sec` is `WLAN.WPA2_ENT` then the `auth` tuple can have either 3 elements: `(sec, username, password)`, or just 1: `(sec,)`. When passing the 3 element tuple, the`keyfile` and `certifle` arguments must not be given.
* `bssid` is the MAC address of the AP to connect to. Useful when there are several APs with the same SSID.
* `timeout` is the maximum time in milliseconds to wait for the connection to succeed.
* `ca_certs` is the path to the CA certificate. This argument is not mandatory.
* `keyfile` is the path to the client key. Only used if `username` and `password` are not part of the `auth` tuple.
* `certfile` is the path to the client certificate. Only used if `username` and `password` are not part of the `auth` tuple.
* `identity` is only used in case of `WLAN.WPA2_ENT` security. Needed by the server.
* `hostname` is the name of the host connecting to the AP. Max length of name string is 32 Bytes

{{% hint style="info" %}}
The ESP32 only handles certificates with `pkcs8` format (but not the "Traditional SSLeay RSAPrivateKey" format). The private key should be RSA coded with 2048 bits at maximum.
{{< /hint >}}

#### wlan.scan(\[ssid=NULL, bssid=NULL, channel=0, show\_hidden=False, type=WLAN.SCAN\_ACTIVE, scantime=120ms\])

Performs a network scan and returns a list of named tuples with (ssid, bssid, sec, channel, rssi). When no config args passed scan will be performed with default configurations.

Note: For Fast scan mode ssid/bssid and channel should be

* `ssid` : If the SSID is not NULL, it is only the AP with the same SSID that can be scanned.
* `bssid` : If the BSSID is not NULL, it is only the AP with the same BSSID that can be scanned. The bssid is given as 6 Hexadecimal bytes literals (i.e b'\xff\xff\xff\xff\xff\xff')
* `channel` : If “channel” is 0, there will be an all-channel scan; otherwise, there will be a specific-channel scan.
* `show_hidden` : If “show\_hidden” is 0, the scan ignores the AP with a hidden SSID; otherwise, the scan considers the hidden AP a normal one.
* `type` : If “type” is `WLAN.SCAN_ACTIVE`, the scan is “active”; otherwise, it is a “passive” one.
  * Active Scan is performed by sending a probe request. The default scan is an active scan
  * Passive Scan sends no probe request. Just switch to the specific channel and wait for a beacon.
* `scantime` :

  This field is used to control how long the scan dwells on each channel. For passive scans, scantime=\[int\] designates the dwell time for each channel.

  For active scans, dwell times for each channel are listed below. scantime is given as a tuple for min and max times (min,max)

min=0, max=0: scan dwells on each channel for 120 ms.

min&gt;0, max=0: scan dwells on each channel for 120 ms.

min=0, max&gt;0: scan dwells on each channel for max ms.

min&gt;0, max&gt;0: The minimum time the scan dwells on each channel is min ms. If no AP is found during this time frame, the scan switches to the next channel. Otherwise, the scan dwells on the channel for max ms.If you want to improve the performance of the the scan, you can try to modify these two parameters.

### wlan.disconnect()

Disconnect from the WiFi access point.

### wlan.isconnected()

In case of STA mode, returns `True` if connected to a WiFi access point and has a valid IP address. In AP mode returns `True` when a station is connected, `False` otherwise.

### wlan.ifconfig(id=0, config=\['dhcp' or configtuple\])

When `id` is 0, the configuration will be get/set on the Station interface. When `id` is 1 the configuration will be done for the AP interface.

With no parameters given returns a 4-tuple of `(ip, subnet_mask, gateway, DNS_server)`.

If `dhcp` is passed as a parameter then the DHCP client is enabled and the IP params are negotiated with the AP.

If the 4-tuple config is given then a static IP is configured. For instance:

```python
wlan.ifconfig(config=('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
```

### wlan.mode(\[mode\])

Get or set the WLAN mode.

### wlan.ssid(\[ssid\])

Get or set the SSID (Set SSID of AP).

In case if mode = `WLAN.STA` this method can get the ssid of AP the board is connected to.

In case of mode = `WLAN.AP` this method can get the ssid of the board's own AP.

In case of mode = `WLAN.STA_AP` this method can get the ssid of board's own AP plus the AP the STA is connected to in form of a tuple:

_\_

### wlan.auth(\[auth\])

Get or set the authentication type when in AP mode.

### wlan.channel(\[channel, sec\_chn\])

_In AP mode:_

Get or set the wifi channel

_In STA mode:_

`channel`: is the primary channel to listen to.

`sec_chn` : Only in case of Bandwidth = HT40 this should specify the position of the secondary channel weather above or below primary channel. `WLAN.SEC_CHN_POS_ABOVE` or `WLAN.SEC_CHN_POS_BELOW`

_Note: Setting Channel in STA mode is only Allowed in Promiscuous mode_

### wlan.antenna(\[antenna\])

Get or set the antenna type (external or internal).

### wlan.mac(\[mac, mode\])

when no arguments are passed a 6-byte long `bytes` tuple object with the WiFI MAC address of both Wifi Station mode and Acces Point mode

`mac`: a 6 bytes bytearray mac address

`mode`: The Interface to set the given MAC address to `WLAN.STA` or `WLAN.AP`

Ex: To set the mac address of Wifi Station mode:

```python
wlan.mac(bytearray([0xAE, 0x77, 0x88, 0x99, 0x22, 0x44]), WLAN.STA)
```

_Note: STA and AP cannot have the Same Mac Address_

### wlan.bandwidth()

Set the bandwidth of the wifi, either 20 MHz or 40 MHz can be configured, use constants `HT20` or `HT40`

### wlan.hostname()

Set the Host name of the device connecting to the AP in case of Wifi `mode=WLAN.STA`, in case of `mode=WLAN.AP` this is the name of the host hosting the AP. Max length of name string is 32 Bytes

### wlan.ap\_sta\_list()

Gets an info list of all stations connected to the board's AP.

Info returned is a list of tuples containning (\[mac address of connected STA\], \[average rssi value\], \[Wlan protocol enabled by STA\]).

Protocol types are either : `WLAN.PHY_11_B`, `WLAN.PHY_11_G`, `WLAN.PHY_11_N` or `WLAN.PHY_LOW_RATE`

### wlan.max\_tx\_power(\[power\])

Gets or Sets the maximum allowable transmission power for wifi.

Packets of different rates are transmitted in different powers according to the configuration in phy init data. This API only sets maximum WiFi transmiting power. If this API is called, the transmiting power of every packet will be less than or equal to the value set by this API. Default is Level 0.

Values passed in power are mapped to transmit power levels as follows:

* \[78, 127\]: level0
* \[76, 77\]: level1
* \[74, 75\]: level2
* \[68, 73\]: level3
* \[60, 67\]: level4
* \[52, 59\]: level5
* \[44, 51\]: level5 - 2dBm
* \[34, 43\]: level5 - 4.5dBm
* \[28, 33\]: level5 - 6dBm
* \[20, 27\]: level5 - 8dBm
* \[8, 19\]: level5 - 11dBm
* \[-128, 7\]: level5 - 14dBm

### wlan.country(\[country, schan, nchan, max\_tx\_pwr, policy\])

Gets or set s Country configuration parameters for wifi.

* `country` That is the country name code , it is max 2 characters string representing the country eg: "CN" for china nad "NL" for Netherlands
* `scahn` is the start channel number, in scan process scanning will be performed starting from this channels till the total number of channels. it should be less than or equal 14.
* `nchan` is the total number of channels in the specified country. maximum is 14
* `max_tx_pwr` Maximum transmission power allowed. see `WLAN.max_tx_power()` for more details.
* `policy` Is the method when setting country configuration for `WLAN.COUNTRY_POL_AUTO` in STA mode the wifi will aquire the same country config of the connected AP, for `WLAN.COUNTRY_POL_MAN` the configured country parameters will take effect regardless of Connected AP.

### wlan.joined\_ap\_info()

Returns a tuple with (bssid, ssid, primary channel, rssi, Authorization method, wifi standard used) of the connected AP in case of STA mode.

### wlan.wifi\_protocol(\[(bool PHY11\_\_B, bool PHY11\_G, bool PHY11\_N)\])

Sets or gets Wifi Protocol supported.

### wlan.send\_raw(Buffer, interface=STA, use\_sys\_seq=True)

Send raw data through the Wifi Interface.

`Buffer`: Buffer of bytes object Containning Data to be transmitted. Data should not be greater than 1500 nor smaller than 24.

`interface`: The Interface to use for transmitting Data AP or STA in case the mode used is APSTA. other wise the interface currently active will be used.

`use_sys_seq`: `True` to use the systems next sequance number for sending the data, `False` for keeping the sequance number in the given raw data buffer unchanged.

### wlan.callback(trigger, handler=Null, arg=Null)

Register a user callback function `handler` to be called once any of the `trigger` events occures optionally with a passed `arg`. by default the wlan obj is passed as arg to the handler. To unregister the callback you can call the `wlan.callback` function with empty `handler` and `arg` parameters.

For trigger events see `Constants` section.

### wlan.promiscuous(\[bool\])

* To enable Promiscuous mode `WLAN.promiscuous(True)` should be called, and `WLAN.promiscuous(False)` for disabling
* To get current mode setting call function with empty args

Note:

* Promiscuous mode should be enabled for Wifi packets types Events to be triggered
* for changing wifi channel via `wlan.channel()` promiscuous mode should be enabled.

### wlan.events()

This function will return an integer object as mask for triggered events.

### wlan.wifi\_packet()

This function will return a tuble with Wifi packet info captured in promiscuous mode.

### wlan.ctrl\_pkt\_filter(\[int\])

This function is used to set the filter mask for Wifi control packets in promiscuous mode. for Filter masks, see `Constants` section.

To get the current Filter mask, call the function with empty args.

## Constants

* WLAN mode: `WLAN.STA`, `WLAN.AP`, `WLAN.STA_AP`
* WLAN network security: `WLAN.WEP`, `WLAN.WPA`, `WLAN.WPA2`, `WLAN.WPA2_ENT`
* Antenna type: `WLAN.INT_ANT`, `WLAN.EXT_ANT`
* WLAN Bandwidth: `WLAN.HT20`, `WLAN.HT40`
* WLAN protocol: `WLAN.PHY_11_B`, `WLAN.PHY_11_G`, `WLAN.PHY_11_N`, `WLAN.PHY_LOW_RATE`
* Scan Type: `WLAN.SCAN_ACTIVE` `WLAN.SCAN_PASSIVE`
* WLAN country config policy: `WLAN.COUNTRY_POL_AUTO`, `WLAN.COUNTRY_POL_MAN`
* Secondary Channel position: `WLAN.SEC_CHN_POS_ABOVE`, `WLAN.SEC_CHN_POS_BELOW`
* Wlan callback triggers:

  `WLAN.EVENT_PKT_MGMT`: Managment packet recieved in promiscuous mode.

  `WLAN.EVENT_PKT_CTRL`: Control Packet recieved in promiscuous mode

  `WLAN.EVENT_PKT_DATA`: Data packet recieved in promiscuous mode

  `WLAN.EVENT_PKT_DATA_MPDU`: MPDU data packet recieved in promiscuous mode

  `WLAN.EVENT_PKT_DATA_AMPDU`: AMPDU data packet recieved in promiscuous mode

  `WLAN.EVENT_PKT_MISC`: misc paket recieved in promiscuous mode.

  `WLAN.EVENT_PKT_ANY`: Any packet recieved in promiscuous mode.

* Control packet filters in promiscuous mode:

  `WLAN.FILTER_CTRL_PKT_ALL`: Filter all Control packets

  `WLAN.FILTER_CTRL_PKT_WRAPPER`: Filter control wrapper packets

  `WLAN.FILTER_CTRL_PKT_BAR`: Filter Control BAR packets

  `WLAN.FILTER_CTRL_PKT_BA`: Filter Control BA packets

  `WLAN.FILTER_CTRL_PKT_PSPOLL`: Filter Control PSPOLL Packets

  `WLAN.FILTER_CTRL_PKT_CTS`: Filter Control CTS packets

  `WLAN.FILTER_CTRL_PKT_ACK`: Filter Control ACK packets

  `WLAN.FILTER_CTRL_PKT_CFEND`: Filter Control CFEND Packets

  `WLAN.FILTER_CTRL_PKT_CFENDACK`: Filter Control CFENDACK Packets
