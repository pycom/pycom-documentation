---
title: "FiPy"
aliases:
    - datasheets/development/fipy.html
    - datasheets/development/fipy.md
    - product-info/development/fipy
    - chapter/datasheets/development/fipy
---

![](/gitbook/assets/assets-lil0igdl11z7jos_jpx-lkn7scqkkkb6tqb3uyo-lkn82srvkf3rhetvjpi-fipy-1.png)


{{% hint style="info" %}}
 Please Note: We have removed the labels from the pictures in the documentation due to inconsistencies with label orientation.  *The LED must be aligned above the USB socket* when inserting or removing a development board from an expansion board/Pytrack/Pysense/Pyscan.
{{< /hint >}}


**Store**: [Buy Here](https://pycom.io/product/fipy/)

**Getting Started:** [Click Here](/gettingstarted/connection/fipy)


## Datasheet

The datasheet of the FiPy is available as a PDF File.

<a href="/gitbook/assets/specsheets/Pycom_002_Specsheets_FiPy_v2.pdf" target="_blank"> FiPy Datasheet </a>

The drawing of the LTE-M antenna is available as a PDF File.
<a href="/gitbook/assets/lte-m-antenna-drawing.pdf" target="_blank"> LTE-M Antenna Drawing </a>

## Pinout

The pinout of the FiPy is available as a PDF File

<a href="/gitbook/assets/fipy-pinout.pdf" target="_blank"> FiPy Pinout </a>

![](/gitbook/assets/fipy-pinout.png)

{{% hint style="info" %}}
Please note that the PIN assignments for UART1 (TX1/RX1), SPI (CLK, MOSI, MISO) and I2C (SDA, SCL) are defaults and can be changed in Software.
{{< /hint >}}

## Notes

### WiFi

By default, upon boot the FiPy will create a WiFi access point with the SSID `fipy-wlan-XXXX`, where `XXXX` is a random 4-digit number, and the password `www.pycom.io`.

The RF switch that selects between the on-board and external antenna is connected to `P12`, for this reason using `P12` should be avoided unless WiFi is disabled in your application.

### Power

The `Vin` pin on the FiPy can be supplied with a voltage ranging from `3.5v` to `5.5v`. The `3.3v` pin on the other hand is output **only**, and must not be used to feed power into the FiPy, otherwise the on-board regulator will be damaged.

### AT Commands

The AT commands for the Sequans Monarch modem on the FiPy are available in a PDF file.

<a href="/gitbook/assets/Monarch-LR5110-ATCmdRefMan-rev6_noConfidential.pdf" target="_blank"> AT Commands for Sequans </a>

## Tutorials

Tutorials on how to the FiPy module can be found in the [examples](/tutorials/introduction) section of this documentation. The following tutorials might be of specific interest for the FiPy:

* [WiFi connection](/tutorials/all/wlan)
* [LoRaWAN node](/tutorials/lora/lorawan-abp)
* [LoRaWAN nano gateway](/tutorials/lora/lorawan-nano-gateway)
* [Sigfox](/tutorials/sigfox)
* [LTE CAT-M1](/tutorials/lte/cat-m1)
* [NB-IoT](/tutorials/lte/nb-iot)
* [BLE](/tutorials/all/ble)
