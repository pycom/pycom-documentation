---
title: "Pyscan"
aliases:
    - datasheets/boards/pyscan.html
    - datasheets/boards/pyscan.md
    - product-info/boards/pyscan
    - chapter/datasheets/boards/pyscan
---
**Store**: [Buy Here](https://pycom.io/product/pyscan/)


## Getting started
1. Find the libraries for the Pyscan in the [Pycom libraries](https://github.com/pycom/pycom-libraries/shields/) repository on Github. 
1. Download the files and extract them into the project folder in Pymakr
1. Click the `upload project to device` button. This will store all necessary files on the device and allow you to import them in the example `main.py`.
1. Check the REPL:
```
example output
```

### Examples
The Pyscan has several examples:
* [Scanning](/tutorials/expansionboards/scanning/)

## Features

![](/gitbook/assets/pyscan-new.png)

## Datasheet & Pinout

The pinout and datasheet of the Pyscan is available as a [PDF File](/gitbook/assets/pyscan-pinout.pdf)

[ROHS certification](/gitbook/assets/RoHs_declarations/RoHS-for-Pyscan(8286-00031P)-20190523.pdf)

![](/gitbook/assets/pyscan-pinout-1.png)

## Pyscan Libraries

* Pyscan libraries to use the RFID/NFC reader are located [here](https://github.com/pycom/pycom-libraries/tree/master/pyscan)
* The accelerometer library is [here](https://github.com/pycom/pycom-libraries/blob/master/pytrack/lib/LIS2HH12.py)

## Pyscan components:

* **Accelerometer**: ST LIS2HH12
* **Ambient light sensor**: Lite-on LTR-329ALS-01
* **RFID/NFC reader**: NXP MFRC63002HN, 151

## Driver

The Windows 7 driver for Pyscan is located [here](/gettingstarted/software/drivers/).

For other Operating Systems, no driver is required.


## Battery Charger

The board features a single cell Li-Ion/Li-Po charger with a JST PHR‑2 connector. When the board is being powered via the micro USB connector, it will charge the battery (if connected).




## Mechanical Dimensionsde
![](/gitbook/assets/pyscan_V0.7_20180416_MecahnicalDimensions.png)

## 3D model for case design

* Please see the [3D model] (/gitbook/assets/PyScan_v0.7.step) (step format)
