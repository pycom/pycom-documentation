# Notes

### Powering with an external power source
The devices can be powered by a battery or other external power source.

Be sure to connect the positive lead of the power supply to VIN, and ground to GND.

When powering via VIN:

- The input voltage must be between 3.4V and 5.5V.

When powering via 3V3:

- The input voltage must be exactly 3V3, ripple free and from a supply capable of sourcing at least 500mA of current.

The battery connector for the expansion board is a **JST SH 2P** variant. The expansion board exposes the male connector and an external battery should use a female adapter in order to connect and power the expansion board.

{% hint style='danger' %}
The GPIO pins of the modules are NOT 5V tolerant, connecting them to voltages higher than 3.3V might cause irreparable damage to the device.
{% endhint %}


{% hint style='danger' %}
Static electricity can damage components on the device and may destroy them. If there is a lot of static electricity in the area (e.g. dry and cold climates), take extra care not to shock the device. If the device came in a ESD bag (Silver packaging), the best way to store and carry the device is inside this bag as it will be protected against static discharges.
{% endhint %}
