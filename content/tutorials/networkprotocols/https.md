---
title: "HTTPS"
aliases:
    - tutorials/all/https.html
    - tutorials/all/https.md
    - chapter/tutorials/all/https
---
Using HTTPS adds Transport Layer Security (TLS) to your network traffic. The advantage is an encrypted connection between your device and the server.

## Basic example
```python
from network import WLAN #note that you can also use LTE
import socket
import ssl
import time

wlan = WLAN()
wlan.init(mode=WLAN.STA, ssid='your ssid', auth=(WLAN.WPA2, 'your password'))
print("connecting", end='')
while not wlan.isconnected():
    time.sleep(0.25)
    print(".", end='')

print("connected")
print(wlan.ifconfig())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss = ssl.wrap_socket(s) #adds TLS
ss.connect(socket.getaddrinfo(host, 443)[0][-1])
httpreq = 'GET / HTTP/1.1 \r\nHOST: '+ host + '\r\nConnection: close \r\n\r\n'
ss.send(httpreq)
time.sleep(1)
rec = ss.recv(10000)
print(rec)
```
Basic connection using `ssl.wrap_socket()`.

```python
import socket
import ssl

s = socket.socket()
ss = ssl.wrap_socket(s)
ss.connect(socket.getaddrinfo('www.google.com', 443)[0][-1])
ss.se
```

Below is an example using certificates with the blynk cloud.

Certificate was downloaded from the blynk examples [folder](https://github.com/wipy/wipy/tree/master/examples/blynk) and placed in `/flash/cert/` on the device.

```python
import socket
import ssl

s = socket.socket()
ss = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='/flash/cert/ca.pem')
ss.connect(socket.getaddrinfo('cloud.blynk.cc', 8441)[0][-1])
```

For more info, check the [`ssl`](/firmwareapi/micropython/ussl) module in the API reference.
