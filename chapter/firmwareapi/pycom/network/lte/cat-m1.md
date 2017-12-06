# LTE class for Cat M1 

The LTE Cat M1 service gives full IP access to through the cellular modem. 

Once the lte.connect() function has completed all the IP socket functions - including SSL - will be routed through this connection. This mean any code using WLAN can be adapted to Cat M1 by simply adding the connection setup step first and disconnect after.

For example to connect over LTE Cat M1 to Google's web server over secure SSL:

```python
import socket
import ssl
from network import LTE

lte = LTE()
lte.connect()

s = socket.socket()
ss = ssl.wrap_socket(s)
ss.connect(socket.getaddrinfo('www.google.com', 443)[0][-1])

lte.disconnect()
```

This also applies to our MQTT and AWS examples.


### Constructors

<class><i>class</i> network.LTE(id=0, ...)</class>

Create and configure a LTE object. See init for params of configuration.

```python
from network import LTE
lte = LTE()
```

### Methods

<function>LTE.init(cid=3)</function>

This method is used to set up the LTE subsystem and to specify a CID (Connection ID) for the connection
The arguments are:

- ``cid`` is a Connection ID. This is carrier specific, for Verizon use cid=3. For others like Telstra it should be cid=1. 

<function>wlan.deinit()</function>

Disables LTE until it's been initialized again

<function>lte.connect()</function>

Connect to the LTE Cat M1 network authorized by the inserted SIM card and CID

<function>lte.disconnect()</function>

Disconnect from the LTE network and return to modem to sleep 

<function>lte.isconnected()</function>

Returns *true* if there is an active LTE Cat M1 connection 
