---
title: "MDNS"
---
On this page, we will explore the Multicast DNS feature. MDNS is very useful for connecting to a device of which you do not know the IP address, and works similar to the Domain Name System, on a local network without the need for a DNS server. You can use the `hostname.local` url to connect. To be able to use MDNS on your computer, you might need some additional software.
* Windows:
* MacOS: built in!
* Linux: 

## Use MDNS for a Telnet connection
```python
from network import MDNS
MDNS.init()
MDNS.set_name(hostname ="pycom", instance_name="pycom")
MDNS.add_service("_http",MDNS.PROTO_TCP, 80)
MDNS.add_service("_telnetd", MDNS.PROTO_TCP, 23)
```

When this is running on your development board, you can go to your terminal and try `ping pycom.local`. The second service activate the telnet link, so you can also try `telnet pycom.local` and connect to the REPL through this method!