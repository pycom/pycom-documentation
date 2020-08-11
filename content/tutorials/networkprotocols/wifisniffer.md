---
title: "WiFi Sniffer"
aliases:

---
A WiFi sniffer can be very useful when testing the presence of a mobile phone or other device. The following example will return the MAC addresses of devices in range.

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