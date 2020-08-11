---
title: "PyEthernet"

---


The PyEthernet is a module meant for the [Pygate](../pygate/) expansionboard, enabeling communication and Power over Ethernet. The module will fit on the Pygate in two ways, but only one is correct. Make sure the RJ45 Ethernet port is facing the other way compared to the RGB LED, like shown in the figure below. 

![](/gitbook/assets/pyethernet.png) ![](/gitbook/assets/pygate_ethernet.png)
> Note that the PyEthernet can also work without PoE, you will just need to connect it to a different power source

# Datasheet

We currently have no datasheet available for the module. On the bottom, near the pinheaders, you can find labels for the pin functions. The pins are used to connect both power and a SPI bus.


## Notes

### Power saving
The tiny jumper on the board labeled JP1 enables a default load. Older PoE adapters disable the power injection when only a tiny load is detected. Now by default, the Pygate does not always provide a big enough load for these types of power injectors Connecting the jumper will enable a default load, causing the power **not** to drop. More modern PoE injectors are designed for low power applications as well, not needing the default load. For such applications, you can disconnect the jumper and even save some power!

