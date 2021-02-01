# Sigfox FSK (Device to Device)

To communicate between two Sigfox capable devices, it may be used in FSK mode. Two devices are required to be set to the same frequency, both using FSK.

> `Sigfox.FSK` mode is not supported on LoPy 4 and FiPy.

**Device 1**:

```python
from network import Sigfox
import socket
sigfox = Sigfox(mode=Sigfox.FSK, frequency=868000000)

s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
s.setblocking(True)

while True:
  s.send('Device-1')
  time.sleep(1)
  print(s.recv(64))
```

**Device 2**:

```python
from network import Sigfox
import socket
sigfox = Sigfox(mode=Sigfox.FSK, frequency=868000000)

s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
s.setblocking(True)

while True:
  s.send('Device-2')
  time.sleep(1)
  print(s.recv(64))
```

