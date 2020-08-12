---
title: "Pysense"
aliases:
    - datasheets/boards/pysense.html
    - datasheets/boards/pysense.md
    - product-info/boards/pysense
    - chapter/datasheets/boards/pysense
---
**Store**: [Buy Here](https://pycom.io/product/pysense/)


![](/gitbook/assets/pysense.png) 

## Datasheet

The datasheet of the Pysense is available as a [PDF File](/gitbook/assets/pysense-specsheet.pdf)

[ROHS certification](/gitbook/assets/RoHs_declarations/RoHS-for-Pysense(8286-00030P)-20190523.pdf)

## Pinout

The pinout of the Pysense is available as a [PDF File](/gitbook/assets/pysense-pinout.pdf)
* The user button is connected to `P14` or `G4`. This button can also be used to put the Pysense board in `dfu-bootloader` mode to update the firmware.

![](/gitbook/assets/pysense-pinout-1.png)

## Sensors
The Pysense includes 4 additional sensors:
1. Altitude/Pressure sensor [MPL3115A2 datasheet]()
2. Light sensor [datasheet]()
3. Accelerometer [LIS2HH12 datasheet]()
4. Temperature/Humidity sensor [SI7006A20 datasheet]()


## Notes 
### Battery Charger

The board features a single cell Li-Ion/Li-Po charger. When the board is being powered via the micro USB connector, it will charge the battery (if connected).
> Make sure you check the polarity of the battery before plugging it in! Connect the positive side to the side marked with a `+`.

### Mechanical Dimensions

![](/gitbook/assets/Pysense_v1.1_MechanicalDimensions_b.png)


### 3D model for case design

* Please see the [3D model](/gitbook/assets/PySense_v1.1.step) (step format)
