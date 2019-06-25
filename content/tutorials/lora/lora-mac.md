---
title: "LoRa-MAC (Raw LoRa)"
aliases:
    - tutorials/lora/lora-mac.html
    - tutorials/lora/lora-mac.md
    - chapter/tutorials/lora/lora-mac
---

Basic LoRa connection example, sending and receiving data. In LoRa-MAC mode the LoRaWAN layer is bypassed and the radio is used directly. The data sent is not formatted or encrypted in any way, and no addressing information is added to the frame.

For the example below, you will need two LoPys. A `while` loop with a random delay time is used to minimise the chances of the 2 LoPy's transmitting at the same time. Run the code below on the 2 LoPy modules and you will see the word 'Hello' being received on both sides.

```python

from network import LoRa
import socket
import machine
import time

# initialise LoRa in LORA mode
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
# more params can also be given, like frequency, tx power and spreading factor
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)

# create a raw LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

while True:
    # send some data
    s.setblocking(True)
    s.send('Hello')

    # get any data received...
    s.setblocking(False)
    data = s.recv(64)
    print(data)

    # wait a random amount of time
    time.sleep(machine.rng() & 0x0F)
```

