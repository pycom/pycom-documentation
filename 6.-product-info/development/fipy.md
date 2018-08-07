# 6.1.7 FiPy

![](../../.gitbook/assets/fipy%20%281%29.png)

**Store**: [Buy Here](http://www.pycom.io/fipy)

**Getting Started:** [Click Here](https://docs.pycom.io/chapter/gettingstarted/connection/fipy.html)

## Pinout

The pinout of the FiPy is available as a [PDF File](https://docs.pycom.io/chapter/datasheets/downloads/fipy-pinout.pdf)

![](../../.gitbook/assets/fipy-pinout.png)

{% hint style="info" %}
Please note that the PIN assignments for UART1 \(TX1/RX1\), SPI \(CLK, MOSI, MISO\) and I2C \(SDA, SCL\) are defaults and can be changed in Software.
{% endhint %}

## Datasheet

The datasheet of the FiPy is available as a [PDF File](https://docs.pycom.io/chapter/datasheets/downloads/fipy-specsheet.pdf).

## Notes

### WiFi

By default, upon boot the FiPy will create a WiFi access point with the SSID `fipy-wlan-XXXX`, where `XXXX` is a random 4-digit number, and the password `www.pycom.io`.

The RF switch that selects between the on-board and external antenna is connected to `P12`, for this reason using `P12` should be avoided unless WiFi is disabled in your application.

### Power

The `Vin` pin on the FiPy can be supplied with a voltage ranging from `3.5v` to `5.5v`. The `3.3v` pin on the other hand is output **only**, and must not be used to feed power into the FiPy, otherwise the on-board regulator will be damaged.

### AT Commands

The AT commands for the Sequans Monarch modem on the FiPy are available in a [PDF file](https://docs.pycom.io/chapter/datasheets/downloads/Monarch_4G-EZ_LR5110_ATCommands_ReferenceManual_Rev3_NOCONFIDENTIAL.pdf).

## Tutorials

Tutorials on how to the FiPy module can be found in the [examples](https://docs.pycom.io/chapter/tutorials/) section of this documentation. The following tutorials might be of specific interest for the FiPy:

* [WiFi connection](https://docs.pycom.io/chapter/tutorials/all/wlan.html)
* [LoRaWAN node](https://docs.pycom.io/chapter/tutorials/lora/lorawan-otaa.html)
* [LoRaWAN nano gateway](https://docs.pycom.io/chapter/tutorials/lora/lorawan-nano-gateway.html)
* [Sigfox](https://docs.pycom.io/chapter/tutorials/sigfox/)
* [LTE CAT-M1](https://docs.pycom.io/chapter/tutorials/lte/cat_m1.html)
* [NB-IoT](https://docs.pycom.io/chapter/tutorials/lte/nb_iot.html)
* [BLE](https://docs.pycom.io/chapter/tutorials/all/ble.html)

