---
title: "PoE"
aliases:
    - tutorials/all/PoE.html
    - tutorials/all/PoE.md
    - chapter/tutorials/all/PoE
---

The PyEthernet module has onboard Power over Ethernet (PoE) power supply. This means that you can power your hardware with only an ethernet cable coming from a power injector. However, since the PoE is non-isolated, you must adhere to the following warning!

WARNING:

PoE power supply of PyEthernet module has no galvanic isolation. This means, that in accordance with
IEEE 802.3-2005 standard you must make sure that when powered from PoE power injector there are no other external connections to any part of the module or other hardware where it is installed. Such as USB cable, serial to USB bridge, logic analyser, an oscilloscope, etc.

As in certain hardware configurations it can lead to unrecoverable damage of not only the PyEthernet module but all hardware connected to it.

Be aware - violation of that requirement voids Pycom warranty.

The use of battery with PoE is allowed.

![](/gitbook/assets/PoE-NI.png)
