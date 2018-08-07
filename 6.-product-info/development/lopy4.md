# 6.1.4 LoPy 4

![](../../.gitbook/assets/lopy4%20%281%29.png)

**Store**: [Buy Here](http://www.pycom.io/lopy4)

**Getting Started:** [Click Here](https://docs.pycom.io/chapter/gettingstarted/connection/lopy4.html)

## Pinout

The pinout of the LoPy4 is available as a [PDF File](https://docs.pycom.io/chapter/datasheets/downloads/lopy4-pinout.pdf)

![](../../.gitbook/assets/lopy4-pinout.png)

{% hint style="info" %}
Please note that the PIN assignments for UART1 \(TX1/RX1\), SPI \(CLK, MOSI, MISO\) and I2C \(SDA, SCL\) are defaults and can be changed in Software.
{% endhint %}

## Datasheet

The datasheet of the LoPy4 is available as a [PDF File](https://docs.pycom.io/chapter/datasheets/downloads/lopy4-specsheet.pdf).

## Notes

### WiFi

By default, upon boot the LoPy4 will create a WiFi access point with the SSID `lopy4-wlan-XXXX`, where `XXXX` is a random 4-digit number, and the password `www.pycom.io`.

The RF switch that selects between the on-board and external antenna is connected to `P12`, for this reason using `P12` should be avoided unless WiFi is disabled in your application.

### Power

The `Vin` pin on the LoPy4 can be supplied with a voltage ranging from `3.5v` to `5.5v`. The `3.3v` pin on the other hand is output **only**, and must not be used to feed power into the LoPy4, otherwise the on-board regulator will be damaged.

## Tutorials

Tutorials on how to the LoPy4 module can be found in the [examples](https://docs.pycom.io/chapter/tutorials/) section of this documentation. The following tutorials might be of specific interest for the LoPy4:

* [WiFi connection](https://docs.pycom.io/chapter/tutorials/all/wlan.html)
* [LoRaWAN node](https://docs.pycom.io/chapter/tutorials/lora/lorawan-otaa.html)
* [LoRaWAN nano gateway](https://docs.pycom.io/chapter/tutorials/lora/lorawan-nano-gateway.html)
* [Sigfox](https://docs.pycom.io/chapter/tutorials/sigfox/)
* [BLE](https://docs.pycom.io/chapter/tutorials/all/ble.html)

