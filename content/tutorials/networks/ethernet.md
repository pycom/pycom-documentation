---
title: "Ethernet Examples"
aliases:
    - tutorials/networks/ethernet.html
    - tutorials/networks/ethernet.md
    - chapter/tutorials/networks/ethernet
---

Using the PyEthernet adapter on the Pygate board, we are able to connect to the local area network. The Ethernet functionality works separately from the PoE (Power over Ethernet) feature and works without a PoE power injector attached. 
>Note: Make sure you have flashed the Pygate firmware to your -py board!

```python
from network import ETH
import time
import socket

eth = ETH()

eth.init("hostname")
print("connecting...")
while not eth.isconnected():
    time.sleep(1)
    print(".", end='')

print(eth.ifconfig())
print(socket.getaddrinfo("pycom.io", 80))
```
>Note: If you get the error `Expected Device ID 0x8870, got 0x0`, your PoE module is not plugged in (correctly)

