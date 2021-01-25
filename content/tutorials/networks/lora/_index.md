---
title: "LoRa Examples"
aliases:
---

The following tutorials demonstrate the use of the LoRa functionality on the LoPy. LoRa can work in 2 different modes; **LoRa-MAC** (which we also call Raw-LoRa) and **LoRaWAN** mode.

When using Lora, **Always** connect the appropriate LoRa antenna to your device. See the figures below for the correct antenna placement

| Lopy / Fipy | Lopy4 |
|:---|:---|
| ![](/gitbook/assets/lora_pigtail_lopy.png) | ![](/gitbook/assets/lora_sigfox_pigtail_lopy4.png) |

* **LoRaWAN mode** implements the full LoRaWAN stack for a class A device. It supports both OTAA and ABP connection methods, as well as advanced features like adding and removing custom channels to support "special" frequencies plans like the those used in New Zealand. There are two basic ways of accessing the LoraWAN network:
    * [LoRaWAN ABP](../lora/lorawan-abp/)
    * [LoRaWAN OTAA](../lora/lorawan-otaa/)
>Note: When using LoRaWAN, first register with one of the [networks](/gettingstarted/registration/lora/)

* **LoRa-MAC mode** basically accesses de radio directly and packets are sent using the LoRa modulation on the selected frequency without any headers, addressing information or encryption. Only a CRC is added at the tail of the packet and this is removed before the received frame is passed on to the application. This mode can be used to build any higher level protocol that can benefit from the long range features of the LoRa modulation. Typical uses cases include LoPy to LoPy direct communication and a LoRa packet forwarder.
    * [LoRa-MAC](../lora/lora-mac/)


* **Lopy to Lopy** You are also able to connect two devices to each other using LoRa frequencies. We have one example explaining more about that
    * [Lopy to Lopy](../lora/module-module/)

* **Pygate** Go to the [Expansionboard tutorials](/tutorials/expansionboards/pygate/) for the Pygate tutorial