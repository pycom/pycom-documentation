---
title: "GPy"
aliases:
    - datasheets/development/gpy.html
    - datasheets/development/gpy.md
    - product-info/development/gpy
    - chapter/datasheets/development/gpy
---

![](/gitbook/assets/gpy-1.png)

> Note: Orient the RGB LED / reset button over the USB connector on any expansion board 

**Store**: [Buy Here](https://pycom.io/product/gpy)

**Getting Started:** [Click Here](/gettingstarted/)

## Datasheet


The datasheet of the GPy is available as a [PDF File](/gitbook/assets/specsheets/Pycom_002_Specsheets_GPy_v2.pdf)

The drawing of the LTE-M antenna is available as a [PDF File](/gitbook/assets/lte-m-antenna-drawing.pdf)

The Gpy is certified for [CE RED](/gitbook/assets/c03-b0-red-gpy.pdf) and [FCC DSS](/gitbook/assets/pycom-2ajmtgpy01r-fcc-grant-dss.pdf) [FCC DTS](/gitbook/assets/pycom-2ajmtgpy01r-fcc-grant-dts.pdf) [FCC TNB](//gitbook/assets/pycom-2ajmtgpy01r-fcc-grant-tnb.pdf) 

[RCM](/gitbook/assets/RCM-Gpy.pdf)
[ROHS certification](/gitbook/assets/RoHs_declarations/RoHS-for-GPy(8217-00090P)-20190523.pdf)


## Pinout

The pinout of the GPy is available as a [PDF File](/gitbook/assets/gpy-pinout.pdf)

![](/gitbook/assets/gpy-pinout.png)

{{% hint style="info" %}}
Please note that the PIN assignments for UART1 \(TX1/RX1\), SPI \(CLK, MOSI, MISO\) and I2C \(SDA, SCL\) are defaults and can be changed via software.
{{% /hint %}}

## Notes

### Power
Do not use the 3.3V pin **in combination with** the Vin pin to supply the device as this will damage the voltage regulator on the board.

### Antenna placement
Always attach the appropriate antenna when using a wireless connection (LTE). For WiFi / BLE, it is not mandatory to use an external antenna when you did not explicitly specify this in your code. 

### AT Commands

The AT commands for the Sequans Monarch modem on the GPy are available in a [PDF file](/gitbook/assets/Monarch-LR5110-ATCmdRefMan-rev6_noConfidential.pdf)
