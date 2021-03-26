---
title: "Pysense"
aliases:
    - datasheets/boards/pysense.html
    - datasheets/boards/pysense.md
    - product-info/boards/pysense
    - chapter/datasheets/boards/pysense
---
**Store**: [Buy Here](https://pycom.io/product/pysense/)

The Pysense shield allows you to sense the environment using 5 different sensors:
* Accelerometer (LIS2HH12)
* Light Sensor (LTR329ALS01)
* Pressure Sensor (MPL3115A2)
* Temperature / Humidity Sensor (SI7006A20)

## Getting started
1. Find the libraries for the Pysense in the [Pycom libraries](https://github.com/pycom/pycom-libraries/tree/master/shields) repository on Github. 
1. Download the files and extract them into the project folder in Pymakr
1. Click the `upload project to device` button. This will store all necessary files on the device and allow you to import them in the example `main.py`.
1. Check the REPL:
```
example output
```

### Examples
The Pysense has several examples:
* [Sensing](/tutorials/expansionboards/scanning/)

## Features

![](/gitbook/assets/pysense-pinout-1.png)

## Datasheet

The datasheet of the Pysense is available as a [PDF File](/gitbook/assets/pysense-specsheet.pdf)

[ROHS certification](/gitbook/assets/RoHs_declarations/RoHS-for-Pysense(8286-00030P)-20190523.pdf)

## Pinout

The pinout of the Pysense is available as a [PDF File](/gitbook/assets/pysense-pinout.pdf)
* The user button is connected to `P14`. This button can also be used to put the Pysense board in `dfu-bootloader` mode to update the firmware.



## Notes 
### Battery Charger

The board features a single cell Li-Ion/Li-Po charger with a JST PHR‑2 connector. When the board is being powered via the micro USB connector, it will charge the battery (if connected).
> Make sure you check the polarity of the battery before plugging it in! Connect the positive side to the side marked with a `+`.

### Mechanical Dimensions

![](/gitbook/assets/Pysense_v1.1_MechanicalDimensions_b.png)


### 3D model for case design

* Please see the [3D model](/gitbook/assets/PySense_v1.1.step) (step format)
