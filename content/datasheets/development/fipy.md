---
title: "FiPy"
aliases:
    - datasheets/development/fipy.html
    - datasheets/development/fipy.md
    - product-info/development/fipy
    - chapter/datasheets/development/fipy
---

![](/gitbook/assets/fipy-1.png)

> Note: Orient the RGB LED / reset button over the USB connector on any expansion board 



**Store**: [Buy Here](https://pycom.io/product/fipy/)

**Getting Started:** [Click Here](/gettingstarted/)


## Datasheet

The datasheet of the FiPy is available as a [PDF File](/gitbook/assets/specsheets/Pycom_002_Specsheets_FiPy_v2.pdf)

The drawing of the LTE-M antenna is available as a [PDF File](/gitbook/assets/lte-m-antenna-drawing.pdf).

The Fipy is certified for [CE RED](/gitbook/assets/fipy_c03-b0-red-final.pdf) and [FCC DSS](/gitbook/assets/pycom-2ajmtfipy01r-fcc-grant-dss.pdf) [FCC DTS](/gitbook/assets/pycom-2ajmtfipy01r-fcc-grant-dts.pdf) [FCC DXX](/gitbook/assets/pycom-2ajmtfipy01r-fcc-grant-dxx.pdf) [FCC TNB](/gitbook/assets/pycom-2ajmtfipy01r-fcc-grant-tnb.pdf)
[RCM](/gitbook/assets/RCM-Fipy.pdf)
[ROHS certification](gitbook/assets/RoHs_declarations/RoHS-for-FiPy(8217-00091P)-20190523.pdf)
## Pinout

The pinout of the FiPy is available as a [PDF File](/gitbook/assents/fipy-pinout.pdf)

![](/gitbook/assets/fipy-pinout.png)

> Please note that the PIN assignments for UART1 \(TX1/RX1\), SPI \(CLK, MOSI, MISO\) and I2C \(SDA, SCL\) are defaults and can be changed via software.

## Notes

### Antenna connections

>Always attach the appropriate antenna when using a wireless connection (LoRa / LTE / SigFox). For WiFi / BLE, it is not mandatory to use an external antenna when you did not explicitly specify this in your code.
#### WiFi antenna
![](/gitbook/assets/wifi_pigtail_ant_fipy.png)
#### LoRa / SigFox antenna
![](/gitbook/assets/lora_sigfox_pigtail_ant_fipy.png)
#### LTE antenna
![](/gitbook/assets/lte_ant_fipy.png)
### Power
Do not use the 3.3V pin **in combination with** the Vin pin to supply the device as this will damage the voltage regulator on the board.

### Antenna placement
 


### AT Commands

The AT commands for the Sequans Monarch modem on the FiPy are available in a [PDF file](gitbook/assets/Monarch-LR5110-ATCmdRefMan-rev6_noConfidential.pdf).
