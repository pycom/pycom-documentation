---
title: "Pyscan"
aliases:
    - datasheets/boards/pyscan.html
    - datasheets/boards/pyscan.md
    - product-info/boards/pyscan
    - chapter/datasheets/boards/pyscan
---
**Store**: [Buy Here](https://pycom.io/product/pyscan/)

![](/gitbook/assets/pyscan-new.png)

## Datasheet

The datasheet of the Pyscan is available as a [PDF File](/gitbook/assets/pyscan-specsheet.pdf)

[ROHS certification](/gitbook/assets/RoHs_declarations/RoHS-for-Pyscan(8286-00031P)-20190523.pdf)

## Pyscan Libraries

* Pyscan libraries to use the RFID/NFC reader and sensors are located [here](https://github.com/pycom/pycom-libraries/tree/master/pyscan)

## Pyscan components:

* **Accelerometer**: ST LIS2HH12
* **Ambient light sensor**: Lite-on LTR-329ALS-01
* **RFID/NFC reader**: NXP MFRC63002HN, 151

## Driver

The Windows 7 driver for Pyscan is located [here](/pytrackpysense/installation/firmware).

For other Operating Systems, no driver is required.

## Pinout

The pinout of the Pyscan is available as a PDF File

<a href="/gitbook/assets/pyscan-pinout.pdf" target="_blank"> Pyscan Pinout </a>

![](/gitbook/assets/pyscan-pinout-1.png)
## Notes 
### Battery Charger

The board features a single cell Li-Ion/Li-Po charger. When the board is being powered via the micro USB connector, it will charge the battery if connected.

> Make sure you check the polarity of the battery before plugging it in! Connect the positive side to the side marked with a `+`.




### Mechanical Dimensionsde
![](/gitbook/assets/pyscan_V0.7_20180416_MecahnicalDimensions.png)

### 3D model for case design

* Please see the [3D model](/gitbook/assets/PyScan_v0.7.step) (step format)
