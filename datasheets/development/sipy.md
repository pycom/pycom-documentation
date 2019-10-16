# SiPy

![](../../.gitbook/assets/sipy-2.png)

**Store**: [Buy Here](http://www.pycom.io/sipy)

**Getting Started:** [Click Here](../../gettingstarted/connection/sipy.md)

## Pinout

The pinout of the SiPy is available as a PDF File

{% file src="../../.gitbook/assets/sipy-pinout.pdf" caption="SiPy Pinout" %}

![](../../.gitbook/assets/sipy-pinout.png)

{% hint style="info" %}
Please note that the PIN assignments for UART1 \(TX1/RX1\), SPI \(CLK, MOSI, MISO\) and I2C \(SDA, SCL\) are defaults and can be changed via software.
{% endhint %}

## Datasheet

The datasheet of the SiPy is available as a PDF File.

{% file src="../../.gitbook/assets/sipy-specsheet.pdf" caption="SiPy Datasheet" %}

## Notes

### WiFi

By default, upon booting up the SiPy will create a WiFi access point with the SSID `sipy-wlan-XXXX`, where `XXXX` is a random 4-digit number, and the password `www.pycom.io`.

### Power

The `Vin` pin on the SiPy can be supplied with a voltage ranging from `3.5v` to `5.5v`. The `3.3v` pin on the other hand is output **only**, and must not be used to feed power into the SiPy, otherwise the on-board regulator will be damaged.

### Deep Sleep

Due to a couple of issues with the SiPy design, the module draws more current than it should while in Deep Sleep. The DC-DC switching regulator always stays in high performance mode, which is used to provide the lowest possible output ripple when the module is in use. In this mode, it draws a quiescent current of 10mA. When the regulator is put into ECO mode the quiescent current drops to 10uA. Unfortunately, the pin used to control this mode is out of the RTC domain. This means that it is not usable during Deep Sleep. This results in the regulator remaining in PWM mode, keeping its quiescent current at 10mA. The flash chip also doesn't enter into power down mode as the CS pin floats during Deep Sleep. This causes the flash chip to consume around 2mA of current. To work around this issue a ["deep sleep shield"](../boards/deepsleep/) is available that attaches to the module and allows power to be cut off from the device. The device can then be re-enabled either through a timer or via a pin interrupt. With the Deep Sleep Shield, the current consumption during deep sleep is between 7uA and 10uA depending on the wake sources configured.


## Tutorials

Tutorials on the SiPy module can be found in the [examples](../../tutorials/introduction.md) section of this documentation. The following tutorials might be of  interest for those using the SiPy:

* [WiFi connection](../../tutorials/all/wlan.md)
* [Sigfox](../../tutorials/sigfox.md)
* [BLE](../../tutorials/all/ble.md)
