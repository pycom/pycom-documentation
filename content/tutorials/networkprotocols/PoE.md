---
title: "PoE"
aliases:
    - tutorials/all/PoE.html
    - tutorials/all/PoE.md
    - chapter/tutorials/all/PoE
---

![](/gitbook/assets/PoE-NI.png)

The PyEthernet module offers an optional onboard Power over Ethernet (PoE) power supply circuit. This means that you can power your hardware with only an ethernet cable coming from a power injector or PoE enabled Ethernet switch. However, since the PoE is non-isolated, you must adhere to the following warning!

{{% hint style="danger" %}}
WARNING: Before you use the PoE adapter for the first time, please make sure you read and follow the below instructions as failure to do so might damanage your devices!
{{% /hint %}}

The PoE power supply integrated in the PyEthernet module with UPC code 604565285911 has no galvanic isolation. This means that in accordance with
IEEE 802.3-2005 standard, you must <b>NOT</b> connect any other devices / cables / chargers if the GND connection is connected to mains earth!
This is typically the case with PCs, Oscilloscopes, Logic Analysers, current consumption measurement devices etc.

Incorrect usages of Power over Ethernet can lead to unrecoverable damage of not only the PyEthernet module but all hardware connected to it.

A battery can be connected to the PyGate without issues. The battery can be charged either via USB-C or PoE power.


## Setup Options
In the following diagram, we clarify what is, and what is not allowed:

### Power over Ethernet


![](/gitbook/assets/poe-ni-warn1.png)

| Connection type | OK?|
|--- |--- |
|USB-C cable connected to a PC with mains ground protection|NOT OK|
|USB-C cable connected to a Notebook without mains ground protection|OK|
|USB-C charger with mains ground protection|NOT OK|
|USB-C charger without mains ground protection|OK|
|Oscilloscope / Logic Analyser / Other equipment with mains ground protection|NOT OK|
|Battery|OK|

### Power over USB-C / External

![](/gitbook/assets/poe-ni-warn2.png)

| Connection type | OK?|
|--- |--- |
|USB-C cable connected to a PC with mains ground protection| OK|
|USB-C cable connected to a Notebook without mains ground protection|OK|
|USB-C charger with mains ground protection| OK|
|USB-C charger without mains ground protection|OK|
|Oscilloscope / Logic Analyser / Other equipment with mains ground protection| OK|
|Battery|OK|