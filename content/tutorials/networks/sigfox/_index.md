---
title: "Sigfox Examples"
aliases:
    - tutorials/sigfox.html
    - tutorials/sigfox.md
    - chapter/tutorials/sigfox
---

> Before you start, make sure that your device was registered with [Sigfox](/gettingstarted/registration/sigfox).

When using the SigFox network, **Always** connect the appropriate LoRa antenna to your device. See the figures below for the correct antenna placement

|  Lopy4 | Fipy  |   
|---|---|
| ![](/gitbook/assets/lora_sigfox_pigtail_lopy4.png) | ![](/gitbook/assets/lora_sigfox_pigtail_fipy.png)  |   


## Connecting to SigFox
The following tutorials demonstrate how to register and get started with the SiPy. The board can be configured for operation in various countries based upon specified RCZ zones (see the `Sigfox` class for more info). The SiPy, LoPy 4, and FiPy supports both uplink and downlink `Sigfox` messages as well as device to device communication via its FSK Mode `Sigfox`.

```python
from network import Sigfox
import socket

# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

# send some bytes
s.send(bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
```



