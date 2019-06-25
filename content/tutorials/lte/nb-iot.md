---
title: "NB-IoT"
aliases:
    - tutorials/lte/nb-iot.html
    - tutorials/lte/nb-iot.md
    - chapter/tutorials/lte/nb-iot
---

## LTE class for Narrow Band IoT

{{% hint style="info" %}}
As shipped, Pycom modules only support CAT-M1, in order to use NB-IoT you need to flash a different firmware to the Sequans modem. Instructions for this can be found [here](../firmware).
{{< /hint >}}

## NB-IoT usage

Example with Vodafone:

```python

from network import LTE
lte = LTE()
lte.attach(band=20, apn="nb.inetd.gdsp")
while not lte.isattached():
    time.sleep(0.25)
lte.connect()       # start a data session and obtain an IP address
while not lte.isconnected():
    time.sleep(0.25)

# now use socket as usual...
```

**IMPORTANT:** Once the LTE radio is initialised, it must be de-initialised before going to deepsleep in order to ensure minimum power consumption. This is required due to the LTE radio being powered independently and allowing use cases which require the system to be taken out from deepsleep by an event from the LTE network (data or SMS received for instance).

When using the expansion board and the FiPy together, the RTS/CTS jumpers **MUST** be removed as those pins are being used by the LTE radio. Keeping those jumpers in place will lead to erratic operation and higher current consumption specially while in deepsleep.
