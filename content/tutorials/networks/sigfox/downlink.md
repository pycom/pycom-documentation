# Sigfox Downlink

A Sigfox capable Pycom devices can both send and receive data from the Sigfox network. To receive data, a message must first be sent up to Sigfox, requesting a downlink message. This can be done by passing a `True` argument into the `setsockopt()` method.

```python
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, True)
```

An example of the downlink procedure can be seen below:

```python
from network import Sigfox
import socket
# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as DOWNLINK specified by 'True'
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, True)

# send some bytes and request DOWNLINK
s.send(bytes([1, 2, 3]))

# await DOWNLINK message
r = s.recv(32)
print(ubinascii.hexlify(r))
```