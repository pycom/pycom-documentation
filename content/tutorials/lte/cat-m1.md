---
title: "CAT-M1"
aliases:
    - tutorials/lte/cat-m1.html
    - tutorials/lte/cat-m1.md
    - chapter/tutorials/lte/cat-m1
---

{{% hint style="info" %}}
Please ensure you have the latest Sequans modem firmware for the best network compatibility. Instructions for this can be found [here](../firmware).
{{< /hint >}}

The LTE Cat M1 service gives full IP access through the cellular modem.

Once the `lte.connect()` function has completed all the IP socket functions - including SSL - will be routed through this connection. This mean any code using WLAN can be adapted to Cat M1 by simply adding the connection setup step first and disconnect after.

For example to connect over LTE Cat M1 to Google's web server over secure SSL:

```python

import socket
import ssl
import time
from network import LTE

lte = LTE()         # instantiate the LTE object
lte.attach()        # attach the cellular modem to a base station
while not lte.isattached():
    time.sleep(0.25)
lte.connect()       # start a data session and obtain an IP address
while not lte.isconnected():
    time.sleep(0.25)

s = socket.socket()
s = ssl.wrap_socket(s)
s.connect(socket.getaddrinfo('www.google.com', 443)[0][-1])
s.send(b"GET / HTTP/1.0\r\n\r\n")
print(s.recv(4096))
s.close()

lte.disconnect()
lte.dettach()
```

This also applies to our MQTT and AWS examples.

**IMPORTANT:** Once the LTE radio is initialised, it must be de-initialised before going to deepsleep in order to ensure minimum power consumption. This is required due to the LTE radio being powered independently and allowing use cases which require the system to be taken out from deepsleep by an event from the LTE network (data or SMS received for instance).

When using the expansion board and the FiPy together, the RTS/CTS jumpers **MUST** be removed as those pins are being used by the LTE radio. Keeping those jumpers in place will lead to erratic operation and higher current consumption specially while in deepsleep.
