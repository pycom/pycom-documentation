---
title: "GPy"
aliases:
    - datasheets/development/gpy.html
    - datasheets/development/gpy.md
    - product-info/development/gpy
    - chapter/datasheets/development/gpy
---

![](/gitbook/assets/assets-lil0igdl11z7jos_jpx-lkn7scqkkkb6tqb3uyo-lkn87yf-xz772800vwc-gpy-1.png)

{{% hint style="info" %}}
 Please Note: We have removed the labels from the pictures in the documentation due to inconsistencies with label orientation.  *The LED must be aligned above the USB socket* when inserting or removing a development board from an expansion board/Pytrack/Pysense/Pyscan.
{{% /hint %}}

**Store**: [Buy Here](https://pycom.io/product/gpy)

**Getting Started:** [Click Here](/gettingstarted/)

## Datasheet

{{% hint style="info" %}}
Please Note: We have removed the labels from the pictures in the documentation due to inconsistencies with label orientation.  *The LED must be aligned above the USB socket* when inserting or removing a development board from an expansion board/Pytrack/Pysense/Pyscan.
{{% /hint %}}


The datasheet of the GPy is available as a [PDF File](/gitbook/assets/specsheets/Pycom_002_Specsheets_GPy_v2.pdf")

The drawing of the LTE-M antenna is available as a [PDF File](/gitbook/assets/lte-m-antenna-drawing.pdf")

The Gpy is certified for [CE RED](/gitbook/assets/gpy_c03-b0-red-final.pdf) and [FCC DSS](/gitbook/assets/pycom-2ajmtgpy01r-fcc-grant-dss.pdf) [FCC DTS](/gitbook/assets/pycom-2ajmtgpy01r-fcc-grant-dts.pdf) [FCC TNB](//gitbook/assets/pycom-2ajmtgpy01r-fcc-grant-tnb.pdf) 

[ROHS certification](/gitbook/assets/RoHs_declarations/RoHS-for-GPy(8217-00090P)-20190523.pdf)

## Pinout

The pinout of the GPy is available as a [PDF File](/gitbook/assets/gpy-pinout.pdf)

![](/gitbook/assets/gpy-pinout.png)

{{% hint style="info" %}}
Please note that the PIN assignments for UART1 \(TX1/RX1\), SPI \(CLK, MOSI, MISO\) and I2C \(SDA, SCL\) are defaults and can be changed via software.
{{% /hint %}}

## Notes

### WiFi

By default, upon booting up the GPy will create a WiFi access point with the SSID `gpy-wlan-XXXX`, where `XXXX` is a random 4-digit number, and the password `www.pycom.io`.

The RF switch that selects between the on-board and external antenna is connected to `P12`, so for this reason using `P12` should be avoided unless WiFi is disabled in your application.

### Power

The `Vin` pin on the GPy can be supplied with a voltage ranging from `3.5v` to `5.5v`. The `3.3v` pin on the other hand is output **only**, and must not be used to feed power into the GPy, otherwise the on-board regulator will be damaged.

### AT Commands

The AT commands for the Sequans Monarch modem on the GPy are available in a PDF file.

<a href="/gitbook/assets/Monarch-LR5110-ATCmdRefMan-rev6_noConfidential.pdf" target="_blank"> AT Commands for Sequans </a>

## Tutorials

Tutorials on how to the GPy module can be found in the [examples](/tutorials/introduction) section of this documentation. The following tutorials might be of interest for those using the GPy:

* [WiFi connection](/tutorials/all/wlan)
* [LTE CAT-M1](/tutorials/lte/cat-m1)
* [NB-IoT](/tutorials/lte/nb-iot)
* [BLE](/tutorials/all/ble)
