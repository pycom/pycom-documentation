---
title: "Pytrack"
aliases:
    - datasheets/boards/pytrack.html
    - datasheets/boards/pytrack.md
    - product-info/boards/pytrack
    - chapter/datasheets/boards/pytrack
---
**Store**: [Buy Here](https://pycom.io/product/pytrack/)

The Pytrack shield allows you track your location using the onboard GPS and accelerometer.

## Getting started
1. Find the libraries for the Pytrack in the [Pycom libraries](https://github.com/pycom/pycom-libraries/shields/) repository on Github. 
1. Download the files and extract them into the project folder in Pymakr
1. Click the `upload project to device` button. This will store all necessary files on the device and allow you to import them in the example `main.py`.
1. Check the REPL:
```
example output
```

### Examples
The Pytrack has several examples:
* [Tracking](/tutorials/expansionboards/tracking/)

## Features

![](/gitbook/assets/pytrack.png) 


## Datasheet

The datasheet of the Pytrack is available as a [PDF File](/gitbook/assets/pytrack-specsheet-1.pdf)

[ROHS certification](/gitbook/assets/RoHs_declarations/RoHS-for-Pysense(8286-00030P)-20190523.pdf)

## Pinout

The pinout of the Pytrack is available as a [PDF File](/gitbook/assets/pytrack-pinout.pdf)


![](/gitbook/assets/pytrack-pinout-1.png)
## Notes
### Battery Charger

The board features a single cell Li-Ion/Li-Po charger with a JST PHR‑2 connector. When the board is being powered via the micro USB connector, it will charge the battery (if connected).
> Make sure you check the polarity of the battery before plugging it in! Connect the positive side to the side marked with a `+`.


### Mechanical Dimensions

![](/gitbook/assets/Pysense_v1.1_MechanicalDimensions_b.png)

### 3D model for case design

* Please see the [3D model](/gitbook/assets/PyTrack_v1.1.step) (step format)
