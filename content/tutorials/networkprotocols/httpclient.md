---
Title: 'HTTP Client'
---
In this example, we discuss how to access information served on the internet. Once you have connected to either WiFi or LTE, it is possible to access any webpage. Now there is no such thing as a webbrowser like Chrome or Firefox in your device, and the REPL is not that great at rendering webpages either, so we are mainly looking at the source of the page here. Though for sending and receiving sensor measurements, this can be very useful. The example below connects to `pycom.io` using the HTTP protocol. Note that we use the `ssl` library to wrap the socket with for use with HTTPS, as it is required by most webservices nowadays. The example will print out the received data from the webserver, which in this case, is the index page's source.


```python
#setup internet connection
from network import WLAN
import time
import socket
import ssl
wlan = WLAN()
wlan.connect(ssid='', auth=(WLAN.WPA2, ''))
print('connecting..',end='')
while not wlan.isconnected():
    time.sleep(1)
    print('.',end='')

print('connected')
# setup socket for connection
s = socket.socket()
s = ssl.wrap_socket(s)
host = 'pycom.io'
addr = socket.getaddrinfo(host,443)[0][-1]
s.connect(addr)
print('socket connected')
# it is possible to attach additional HTTP headers in the line below, but note to always close with \r\n\r\n
httpreq = 'GET / HTTP/1.1 \r\nHOST: '+ host + '\r\nConnection: close \r\n\r\n'
print('http request: \n', httpreq)
s.send(httpreq)
time.sleep(1)
rec_bytes = s.recv(10000)
print(rec_bytes)
print('end')

```