---
title: "Notes"
aliases:
    - datasheets/notes.html
    - datasheets/notes.md
    - product-info/notes
    - chapter/datasheets/notes
---

## Powering with an external power source

The devices can be powered by a battery or other external power source.

Be sure to connect the positive lead of the power supply to `VIN`, and ground to `GND`.

When powering via `VIN`:

* The input voltage must be between `3.4V` and `5.5V`.

{{% hint style="danger" %}}
Please **DO NOT** power the board via the `3.3V` pin as this may damage the device. ONLY use the `VIN` pin for powering Pycom devices.
{{% /hint %}}

The battery connector for the Expansion Board is a **JST PHR-2** variant. The Expansion Board exposes the male connector and an external battery should use a female adapter in order to connect and power the expansion board. The polarity of the battery should be checked before being plugged into the expansion board as the cables may require swapping.

{{% hint style="danger" %}}
The `GPIO` pins of the modules are **NOT** `5V` tolerant, connecting them to voltages higher than `3.3V` might cause irreparable damage to the device.
{{% /hint %}}

{{% hint style="danger" %}}
Static electricity can damage components on the device and may destroy them. If there is a lot of static electricity in the area (e.g. dry and cold climates), take extra care not to shock the device. If the device came in a ESD bag (Silver packaging), the best way to store and carry the device is inside this bag as it will be protected against static discharges.
{{% /hint %}}

## LoRa
There is a known issue regarding LoRa communication on the LoPy1, L01 and FiPy where the SX1272 chip no longer receives any LoRa messages. This happens mainly with modules running continuously for extended periods of time (days) on a power supply susceptible to under-voltage spikes.

The workaround for this issue is to reset the LoRa SX1272 chip if it gets stuck in that state. If there is no way for your application to detect that situation another workaround is to reset the LoRa chip at a specified intervals (eg. once every 24hrs)


**For LO1/FiPy:**

To reset the LoRa chip you can do a Deep sleep cycle 

**For LoPy1:**

Currently a power reset is required to reset the LoRa chip , A MicroPython API will be added shortly to assert the SX1272 reset line from the Application.
