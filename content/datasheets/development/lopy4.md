---
title: "LoPy 4"
aliases:
    - datasheets/development/lopy4.html
    - datasheets/development/lopy4.md
    - product-info/development/lopy4
    - chapter/datasheets/development/lopy4
---

![](/gitbook/assets/lopy4-1.png)


> Note: Orient the RGB LED / reset button over the USB connector on any expansion board

**Store**: [Buy Here](https://pycom.io/product/lopy4/)

**Getting Started:** [Click Here](/gettingstarted/)

## Datasheet

The datasheet of the LoPy4 is available as a [PDF File](/gitbook/assets/specsheets/Pycom_002_Specsheets_LoPy4_v2.pdf)

The Lopy 4 is certified for [CE RED](/gitbook/assets/c03-b0-red-final.pdf) and [FCC DSS](/gitbook/assets/Pycom-2AJMTLOPY4R-FCC-Grant-DSS.pdf)
[RCM](/gitbook/assets/RCM-LOPY4.zip)
[ROHS certification](/gitbook/assets/RoHs_declarations/RoHS-for-LoPy-4(8286-00027P)-20190523.pdf)


## Pinout

The pinout of the LoPy4 is available as a [PDF File](/gitbook/assets/lopy4-pinout.pdf)


![](/gitbook/assets/lopy4-pinout.png)


> Please note that the PIN assignments for UART1 (TX1/RX1), SPI (CLK, MOSI, MISO) and I2C (SDA, SCL) are defaults and can be changed in Software.
## Footprints & 3D files

[3D STEP file](/gitbook/assets/3D-files/LoPy4.step)
[Pycom footprints](https://github.com/pycom/footprints)

## Notes
### Power
Do not use the 3.3V pin **in combination with** the Vin pin to supply the device as this will damage the voltage regulator on the board.

### Antenna placement
Always attach the appropriate antenna when using a wireless connection (LoRa / SigFox). For WiFi / BLE, it is not mandatory to use an external antenna when you did not explicitly specify this in your code.


### Power
Do not use the 3.3V pin **in combination with** the Vin pin to supply the device as this will damage the voltage regulator on the board.

### Antenna placement
Always attach the appropriate antenna when using a wireless connection (LoRa / LTE). For WiFi / BLE, it is not mandatory to use an external antenna when you did not explicitly specify this in your code.
