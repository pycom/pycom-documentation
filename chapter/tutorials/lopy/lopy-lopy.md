# LoPy to LoPy

This example show how to connect two LoPys \(nodes\) via raw LoRa.

### Node A

```py
from network import LoRa
import socket
import time

print("Node A")
print("initializing program")
lora = LoRa(mode=LoRa.LORA, frequency=863000000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

while True:
    if s.recv(64) == b'Ping':
        s.send('Pong')
    time.sleep(5)
```

### Node B

```py
from network import LoRa
import socket
import time

print("Node B")
print("initializing program")
lora = LoRa(mode=LoRa.LORA, frequency=863000000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
while True:
    s.send('Ping')
    time.sleep(5)
```



