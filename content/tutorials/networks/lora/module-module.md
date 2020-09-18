---
title: "LoPy to LoPy"
aliases:
    - tutorials/lora/module-module.html
    - tutorials/lora/module-module.md
    - chapter/tutorials/lora/module-module
---

This example shows how to connect two Pycode LoRa capable modules (nodes) via raw LoRa.

## Node A

```python
from network import LoRa
import socket
import time

# Please pick the region that matches where you are using the device

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
i = 0
while True:
    if s.recv(64) == b'Ping':
        s.send('Pong')
        print('Pong {}'.format(i))
        i = i+1
    time.sleep(5)
```

## Node B

```python
from network import LoRa
import socket
import time

# Please pick the region that matches where you are using the device

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
i = 0
while True:
    s.send('Ping')
    print('Ping {}'.format(i))
    i= i+1
    time.sleep(5)
```

