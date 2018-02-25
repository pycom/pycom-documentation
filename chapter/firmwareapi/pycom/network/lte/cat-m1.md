# LTE class for Cat M1 

The LTE Cat M1 service gives full IP access through the cellular modem.

Once the lte.connect() function has completed all the IP socket functions - including SSL - will be routed through this connection. This mean any code using WLAN can be adapted to Cat M1 by simply adding the connection setup step first and disconnect after.

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


**IMPORTANT:** Once the LTE radio is initialized, it must be de-nitialized before going to deepsleep in order to ensure
minimum power consumption. This is required due to the LTE radio being powered independently and allowing use cases which require the system to be taken out from deepsleep by an event from the LTE network (data or SMS received for instance).

When using the expansion board and the FiPy together, the RTS/CTS jumpers **MUST** be removed as those pins are being used byt the LTE radio. Keeping those jumpers in place will lead to erratic operation and higher current consumption specially while in deepsleep.


### Constructors

#####<class><i>class</i> network.LTE(id=0, ...)</class>

Create and configure a LTE object. See init for params of configuration.

```python
from network import LTE
lte = LTE()
```

### Methods

#####<function>LTE.init()</function>

This method is used to set up the LTE subsystem. After a **deinit()** this method can take several seconds to return waiting for the LTE modem to start-up.

#####<function>lte.deinit()</function>

Disables LTE modem completely. This reduces the power consumption to the minimum. Call this before
entering deepsleep.

#####<function>lte.attach()</function>

Enable radio functionality and attach to the LTE Cat M1 network authorized by the inserted SIM card.

#####<function>lte.isattached()</function>

Returns ``True`` if the cellular mode is attached to the network. ``False`` otherwise.

#####<function>lte.dettach()</function>

Dettach the modem from the LTE Cat M1 and disable the radio functionality.

#####<function>lte.connect(*, cid=1)</function>

Start a data session and obtain and IP address. Optionally specify a CID (Connection ID) for the data session.
The arguments are:

    - ``cid`` is a Connection ID. This is carrier specific, for Verizon use cid=3. For others like Telstra it should be cid=1.

#####<function>lte.isconnected()</function>

Returns ``True`` if there is an active LTE data session and IP address has been obtained. ``False`` otherwise.

#####<function>lte.disconnect()</function>

End the data session with the network.

#####<function>lte.send_at_cmd(cmd)</function>

Send an AT command directly to the modem. Returns the raw response from the modem as a string object. **IMPORTANT:** If a data session is active (i.e.: the modem is *connected*), sending the AT commands requires to pause and then resume the data session. This is all done automatically, but makes the whole request take around 2.5 seconds.

Example:

```
lte.send_at_cmd('AT+CEREG?')    # check for network registration
```

Optionally the response can be parsed for pretty printing:

```
def send_at_cmd_pretty(cmd):
    response = lte.send_at_cmd(cmd).split('\r\n')
    for line in response:
        print(line)

send_at_cmd_pretty('AT!="showphy"')     # get the PHY status
send_at_cmd_pretty('AT!="fsm"')         # get the System FSM
```

#####<function>lte.reset()</function>

Perform a hardware reset on the cellular modem. This function can take up to 5 seconds tu return as it waits for the modem to shutdown and reboot.
