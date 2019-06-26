---
title: "Sigfox Examples"
aliases:
    - tutorials/sigfox.html
    - tutorials/sigfox.md
    - chapter/tutorials/sigfox
---

Before you start, make sure that your device was registered with [Sigfox](/gettingstarted/registration/sigfox).

The following tutorials demonstrate how to register and get started with the SiPy. The board can be configured for operation in various countries based upon specified RCZ zones (see the `Sigfox` class for more info). The SiPy, LoPy 4, and FiPy supports both uplink and downlink `Sigfox` messages as well as device to device communication via its FSK Mode `Sigfox`.

```python

from network import Sigfox
import socket
​
# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)
​
# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
​
# make the socket blocking
s.setblocking(True)
​
# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)
​
# send some bytes
s.send(bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
```

{{% hint style="danger" %}}
Please ensure that there is an antenna connected to your device before sending/receiving Sigfox messages as in proper use (e.g. without an antenna), may damage the device.
{{< /hint >}}

## Disengage Sequence Number

If your are experiencing issues with Sigfox connectivity, this could be due to the sequence number being out of sync. To prevent replay on the network, the Sigfox protocol uses sequence numbers. If there is a large difference between the sequence number sent by the device and the one expected by the backend, your message is dropped by the network.

You can use the `Disengage sequence number` button on the device information or on the device type information page of the Sigfox backend to reset the number expected by the backend. If the sequence number of your next message is different from the last trashed sequence number, the message will be accepted.

Issues with the sequence number can occur when a lot of messages are sent when outside of Sigfox coverage for instance.

Firstly you will need to log into the [Sigfox Backend](https://backend.sigfox.com), navigate to device, and click on the Sigfox ID of the affected SiPy.

![](/gitbook/assets/seq_dis_1-1.png)

You should now see the Information page with an entry `Device Type:` followed by a link. Please follow the link

![screenshot of sigfox ID](/gitbook/assets/seq_dis_2%20%281%29.png)

Finally, on this page click on `Disengage sequence number` button in the upper right corner.

![screenshot of sigfox ID](/gitbook/assets/seq_dis_3.png)
