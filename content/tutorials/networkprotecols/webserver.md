---
title: "HTTP Webserver Example"
aliases:
    - tutorials/networks/webserver.html
    - tutorials/networks/webserver.md
    - chapter/tutorials/networks/webserver
---

Using the WiFi connection, we can create a simple webserver on the module

```python
from network import WLAN
import socket

wlan = WLAN()
wlan.init(mode=WLAN.STA, ssid="", auth=(WLAN.WPA2, "")) #you can use both STA or AP mode for the webserver

sock = socket.socket(usocket.AF_INET, usocket.SOCK_STREAM) #use the socket on the WLAN (INET) adapter, and use stream (TCP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #set the options to use IP addresses, and check the default option to reuse. 
sock.bind(("192.168.4.1"), 80) #use the socket on this ip address, using this port. Change the IP address if you are using STA mode.

sock.listen(5) #allow for 5 simultaneous connections


while True:
    # Accept the connection of the clients
    (clientsocket, address) = serversocket.accept()
    # Reply with the webpage





