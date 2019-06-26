---
title: "LoPy"
aliases:
    - datasheets/development/lopy.html
    - datasheets/development/lopy.md
    - product-info/development/lopy
    - chapter/datasheets/development/lopy
---

![](/gitbook/assets/assets-lil0igdl11z7jos_jpx-lkn7scqkkkb6tqb3uyo-lkn80ythqnrgah01r2m-lopy-1.png)


{{% hint style="info" %}}
Please Note: We have removed the labels from the pictures in the documentation due to inconsistencies with label orientation.  *The LED must be aligned above the USB socket* when inserting or removing a development board from an expansion board/Pytrack/Pysense/Pyscan.
{{< /hint >}}


**Store**: [Buy Here](https://pycom.io/product/lopy)

**Getting Started:** [Click Here](/gettingstarted/connection/lopy)

## Datasheet

The datasheet of the LoPy is available as a PDF File.

<a href="/gitbook/assets/specsheets/Pycom_002_Specsheets_LoPy_v2.pdf" target="_blank"> LoPy Datasheet </a>
## Pinout

The pinout of the LoPy is available as a PDF File

<a href="/gitbook/assets/lopy-pinout.pdf" target="_blank"> LoPy Pinout </a>

![](/gitbook/assets/lopy-pinout.png)

{{% hint style="info" %}}
Please note that the PIN assignments for UART1 (TX1/RX1), SPI (CLK, MOSI, MISO) and I2C (SDA, SCL) are defaults and can be changed in Software.
{{< /hint >}}

## Notes

### WiFi

By default, upon boot the LoPy will create a WiFi access point with the SSID `lopy-wlan-XXXX`, where `XXXX` is a random 4-digit number, and the password `www.pycom.io`.

### Power

The `Vin` pin on the LoPy can be supplied with a voltage ranging from `3.5v` to `5.5v`. The `3.3v` pin on the other hand is output **only**, and must not be used to feed power into the LoPy, otherwise the on-board regulator will be damaged.

### Deep Sleep

Due to a couple issues with the LoPy design the module draws more current than it should while in deep sleep. The DC-DC switching regulator always stays in high performance mode which is used to provide the lowest possible output ripple when the modules is in use. In this mode, it draws a quiescent current of 10mA. When the regulator is put into ECO mode, the quiescent current goes down to 10uA. Unfortunately, the pin used to control this mode is out of the RTC domain, and therefore not usable during deep sleep. This causes the regulator to always stay in PWM mode, keeping its quiescent current at 10mA. Alongside this the flash chip doesn't enter power down mode because the CS pin is floating during deep sleep. This causes the flash chip to consume around 2mA of current. To work around this issue a ["deep sleep shield"](../../boards/deepsleep/) is available that attaches to the module and allows power to be cut off from the device. The device can then be re-enabled either on a timer or via pin interrupt. With the deep sleep shield the current consumption during deep sleep is between 7uA and 10uA depending on the wake sources configured.

## Tutorials

Tutorials on how to the LoPy module can be found in the [examples](/tutorials/introduction) section of this documentation. The following tutorials might be of specific interest for the LoPy:

* [WiFi connection](/tutorials/all/wlan)
* [LoRaWAN node](/tutorials/lora/lorawan-abp)
* [LoRaWAN nano gateway](/tutorials/lora/lorawan-nano-gateway)
* [BLE](/tutorials/all/ble)
