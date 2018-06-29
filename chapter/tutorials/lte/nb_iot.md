# LTE class for Narrow Band IoT

{% hint style='tip' %}
As shipped, Pycom modules only support CAT-M1, in order to use NB-IoT you need
to flash a different firmware to the Sequans modem. Instructions for this can be
found [here](firmware.md).
{% endhint %}

## Current NB-IoT limitations

At the moment the NB-IoT firmware supplied by Sequans only support Ericsson
base stations configured for In-Band mode. Standalone and guard-band modes will
be supported in a later release. Support for Huawei base stations is also
limited and only lab testing with Huawei eNodeB is recommended at the moment.
Full support for Huawei is planned for early Q2 2018.

# NB-IoT usage:

Example with Vodafone:

```python
from network import LTE

lte = LTE()
lte.send_at_cmd('AT+CFUN=0')
lte.send_at_cmd('AT!="clearscanconfig"')
lte.send_at_cmd('AT!="addscanfreq band=20 dl-earfcn=6300"')
lte.send_at_cmd('AT!="zsp0:npc 1"')
lte.send_at_cmd('AT+CGDCONT=1,"IP","nb.inetd.gdsp"')
lte.send_at_cmd('AT+CFUN=1')

while not lte.isattached():
    pass

lte.connect()
while not lte.isconnected():
    pass

# now use socket as usual...
```

**IMPORTANT:** Once the LTE radio is initialised, it must be de-initialised
before going to deepsleep in order to ensure minimum power consumption. This is
required due to the LTE radio being powered independently and allowing use cases
which require the system to be taken out from deepsleep by an event from the LTE
network (data or SMS received for instance).

When using the expansion board and the FiPy together, the RTS/CTS jumpers
**MUST** be removed as those pins are being used by the LTE radio. Keeping those
jumpers in place will lead to erratic operation and higher current consumption
specially while in deepsleep.
