# Notes

## Powering with an external power source

The devices can be powered by a battery or other external power source.

Be sure to connect the positive lead of the power supply to `VIN`, and ground to `GND`.

When powering via `VIN`:

* The input voltage must be between `3.4V` and `5.5V`.

{% hint style="danger" %}
Please **DO NOT** power the board via the `3.3V` pin as this may damage the device. ONLY use the `VIN` pin for powering Pycom devices.
{% endhint %}

The battery connector for the Expansion Board is a **JST PHR-2** variant. The Expansion Board exposes the male connector and an external battery should use a female adapter in order to connect and power the expansion board. The polarity of the battery should be checked before being plugged into the expansion board, the cables may require swapping.

{% hint style="danger" %}
The `GPIO` pins of the modules are **NOT** `5V` tolerant, connecting them to voltages higher than `3.3V` might cause irreparable damage to the device.
{% endhint %}

{% hint style="danger" %}
Static electricity can damage components on the device and may destroy them. If there is a lot of static electricity in the area \(e.g. dry and cold climates\), take extra care not to shock the device. If the device came in a ESD bag \(Silver packaging\), the best way to store and carry the device is inside this bag as it will be protected against static discharges.
{% endhint %}

