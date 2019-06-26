---
title: "LoPy 4"
aliases:
    - datasheets/development/lopy4.html
    - datasheets/development/lopy4.md
    - product-info/development/lopy4
    - chapter/datasheets/development/lopy4
---

![](/gitbook/assets/assets-lil0igdl11z7jos_jpx-lkn7scqkkkb6tqb3uyo-lkn85npgnazxzxyv-nu-lopy4-1.png)


{{% hint style="info" %}}
 Please Note: We have removed the labels from the pictures in the documentation due to inconsistencies with label orientation.  *The LED must be aligned above the USB socket* when inserting or removing a development board from an expansion board/Pytrack/Pysense/Pyscan.
{{< /hint >}}


**Store**: [Buy Here](https://pycom.io/product/lopy4/)

**Getting Started:** [Click Here](/gettingstarted/connection/lopy4)

## Datasheet

The datasheet of the LoPy4 is available as a PDF File.

<a href="/gitbook/assets/specsheets/Pycom_002_Specsheets_LoPy4_v2.pdf" target="_blank"> LoPy4 Datasheet </a>

## Pinout

The pinout of the LoPy4 is available as a PDF File

<a href="/gitbook/assets/lopy4-pinout.pdf" target="_blank"> LoPy4 Pinout </a>

![](/gitbook/assets/lopy4-pinout.png)

{{% hint style="info" %}}
Please note that the PIN assignments for UART1 (TX1/RX1), SPI (CLK, MOSI, MISO) and I2C (SDA, SCL) are defaults and can be changed in Software.
{{< /hint >}}

## Notes

### WiFi

By default, upon boot the LoPy4 will create a WiFi access point with the SSID `lopy4-wlan-XXXX`, where `XXXX` is a random 4-digit number, and the password `www.pycom.io`.

The RF switch that selects between the on-board and external antenna is connected to `P12`, for this reason using `P12` should be avoided unless WiFi is disabled in your application.

### Power

The `Vin` pin on the LoPy4 can be supplied with a voltage ranging from `3.5v` to `5.5v`. The `3.3v` pin on the other hand is output **only**, and must not be used to feed power into the LoPy4, otherwise the on-board regulator will be damaged.

## Tutorials

Tutorials on how to the LoPy4 module can be found in the [examples](/tutorials/introduction) section of this documentation. The following tutorials might be of specific interest for the LoPy4:

* [WiFi connection](/tutorials/all/wlan)
* [LoRaWAN node](/tutorials/lora/lorawan-abp)
* [LoRaWAN nano gateway](/tutorials/lora/lorawan-nano-gateway)
* [Sigfox](/tutorials/sigfox)
* [BLE](/tutorials/all/ble)
