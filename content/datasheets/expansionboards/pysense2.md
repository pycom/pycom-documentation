---
title: "Pysense 2.0X"
aliases:
    - datasheets/boards/pysense2.html
    - datasheets/boards/pysense2.md
    - product-info/boards/pysense2
    - chapter/datasheets/boards/pysense2
---

The Pysense 2.0 X shield allows you to sense the environment using 5 different sensors:
* Accelerometer (LIS2HH12)
* Light Sensor (LTR329ALS01)
* Pressure Sensor (MPL3115A2)
* Temperature / Humidity Sensor (SI7006A20)

## Getting started
1. Find the libraries for the Pysense 2.0 X in the [Pycom libraries](https://github.com/pycom/pycom-libraries/tree/master/shields) repository on Github. 
1. Download the files and extract them into the project folder in Pymakr
1. Click the `upload project to device` button. This will store all necessary files on the device and allow you to import them in the example `main.py`.
1. Check the REPL:
```
example output
```

### Examples
The Pysense has several examples:
* [Sensing](/tutorials/expansionboards/sensing/)

## Features

![](/gitbook/assets/pysense2_desc.png)

## Datasheet

The datasheet of the Pysense 2.0X is available as a [PDF File](/gitbook/assets/PySense2X_specsheet.pdf)

## Pinout

The PyPort connector is for a 6 lead mini ribbon cable, part: Amphenol 20021511-00006T4LF. The external IO header power pins are labelled as follows
* 3V3AUX - The power provided by the development module 
* 3V3AUX_LP - the power provided by the development module for the SD card (This can be switched off)
* 3V3 - The power provided by the Pysense 2, for the USB-Serial converter.

The Pysense 2 can be powered through the USB port, the battery connector and the VUSB_AUX header just below the PyPort. Connecting a 5V supply to the header will result in exactly the same behaviour as powering it through the USB connector.

The pinout of the Pysense is available as a [PDF File](/gitbook/assets/pysense2-pinout.pdf)


![](/gitbook/assets/pysense2-pinout.png)
## Notes
### Battery Charger

The board features a single cell Li-Ion/Li-Po charger with a JST PHR‑2 connector. When the board is being powered via the micro USB connector, it will charge the battery (if connected).
> Make sure you check the polarity of the battery before plugging it in! Connect the positive side to the side marked with a `+`.

### Mechanical Dimensions

![](/gitbook/assets/Pysense_v2.0X_MechanicalDimensions.png)


### 3D model for case design

* Please see the [3D model](/gitbook/assets/pysense_v2.0X.step) (Step format)