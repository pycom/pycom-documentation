---
title: "WiPy 2.0"
aliases:
    - datasheets/development/wipy2.html
    - datasheets/development/wipy2.md
    - product-info/development/wipy2
    - chapter/datasheets/development/wipy2
---

![](/gitbook/assets/assets-lil0igdl11z7jos_jpx-lkn7scqkkkb6tqb3uyo-lkn83ftusu7mke5ppmd-wipy2-1.png)

{{% hint style="info" %}}
 Please Note: We have removed the labels from the pictures in the documentation due to inconsistencies with label orientation.  *The LED must be aligned above the USB socket* when inserting or removing a development board from an expansion board/Pytrack/Pysense/Pyscan.
{{< /hint >}}


**Store**: Discontinued, See [WiPy3](../wipy3)

**Getting Started:** [Click Here](/gettingstarted/connection/wipy)

## Datasheet



The datasheet of the WiPy2 is available as a PDF File.

<a href="/gitbook/assets/specsheets/Pycom_002_Specsheets_WiPy2.0_v2.pdf" target="_blank"> WiPy 2 Datasheet </a>

## Pinout

The pinout of the WiPy2 is available as a PDF File.

<a href="/gitbook/assets/wipy2-pinout.pdf" target="_blank"> WiPy 2 Pinout </a>

![](/gitbook/assets/wipy2-pinout.png)

{{% hint style="info" %}}
Please note that the PIN assignments for UART1 (TX1/RX1), SPI (CLK, MOSI, MISO) and I2C (SDA, SCL) are defaults and can be changed in Software.
{{< /hint >}}

## Notes

### WiFi

By default, upon boot the WiPy2 will create a WiFi access point with the SSID `wipy-wlan-XXXX`, where `XXXX` is a random 4-digit number, and the password `www.pycom.io`.

### Power

The `Vin` pin on the WiPy2 can be supplied with a voltage ranging from `3.5v` to `5.5v`. The `3.3v` pin on the other hand is output **only**, and must not be used to feed power into the WiPy2, otherwise the on-board regulator will be damaged.

### Deep Sleep

Due to a couple issues with the WiPy2 design the module draws more current than it should while in deep sleep. The DC-DC switching regulator always stays in high performance mode which is used to provide the lowest possible output ripple when the modules is in use. In this mode, it draws a quiescent current of 10mA. When the regulator is put into ECO mode, the quiescent current goes down to 10uA. Unfortunately, the pin used to control this mode is out of the RTC domain, and therefore not usable during deep sleep. This causes the regulator to always stay in PWM mode, keeping its quiescent current at 10mA. Alongside this the flash chip doesn't enter power down mode because the CS pin is floating during deep sleep. This causes the flash chip to consume around 2mA of current. To work around this issue a ["deep sleep shield"](../../boards/deepsleep/) is available that attaches to the module and allows power to be cut off from the device. The device can then be re-enabled either on a timer or via pin interrupt. With the deep sleep shield the current consumption during deep sleep is between 7uA and 10uA depending on the wake sources configured.

## Tutorials

Tutorials on how to the WiPy2 module can be found in the [examples](/tutorials/introduction) section of this documentation. The following tutorials might be of specific interest for the WiPy2:

* [WiFi connection](/tutorials/all/wlan)
* [BLE](/tutorials/all/ble)
