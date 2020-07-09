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
{{% /hint %}}


**Store**: [Buy Here](https://pycom.io/product/lopy4/)

**Getting Started:** [Click Here](/gettingstarted/)

## Datasheet

The datasheet of the LoPy4 is available as a [PDF File](/gitbook/assets/specsheets/Pycom_002_Specsheets_LoPy4_v2.pdf)

The Lopy 4 is certified for [CE RED](/gitbook/assets/C03-B0-RED-final.pdf) and [FCC DSS](/gitbook/assets/Pycom-2AJMTLOPY4R-FCC-Grant-DSS.pdf)

[ROHS certification](/gitbook/assets/RoHs_declarations/RoHS-for-LoPy-4(8286-00027P)-20190523.pdf)


## Pinout

The pinout of the LoPy4 is available as a [PDF File](/gitbook/assets/lopy4-pinout.pdf)


![](/gitbook/assets/lopy4-pinout.png)

{{% hint style="info" %}}
Please note that the PIN assignments for UART1 (TX1/RX1), SPI (CLK, MOSI, MISO) and I2C (SDA, SCL) are defaults and can be changed in Software.
{{% /hint %}}

## Notes

### WiFi

By default, upon booting up the LoPy4 will create a WiFi access point with the SSID `lopy4-wlan-XXXX`, where `XXXX` is a random 4-digit number and the password `www.pycom.io`.

The RF switch that chooses between the on-board and external antenna is connected to `P12`, so for this reason using `P12` should be avoided unless WiFi is disabled in your application.

### Power

The `Vin` pin on the LoPy4 can be supplied with a voltage ranging from `3.5v` to `5.5v`. The `3.3v` pin on the other hand is output **only**, and must not be used to feed power into the LoPy4, otherwise the on-board regulator will be damaged.

## Tutorials

Tutorials on the LoPy4 module can be found in the [examples](/tutorials/introduction) section of this documentation. The following tutorials might be of  interest for those using the LoPy4:

* [WiFi connection](/tutorials/all/wlan)
* [LoRaWAN node](/tutorials/lora/lorawan-abp)
* [LoRaWAN nano gateway](/tutorials/lora/lorawan-nano-gateway)
* [Sigfox](/tutorials/sigfox)
* [BLE](/tutorials/all/ble)
