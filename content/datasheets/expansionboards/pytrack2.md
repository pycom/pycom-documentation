---
title: "Pytrack 2.0X"
aliases:
    - datasheets/boards/pytrack2.html
    - datasheets/boards/pytrack2.md
    - product-info/boards/pytrack2
    - chapter/datasheets/boards/pytrack2
---

![](/gitbook/assets/pytrack2_decs.png)

## Datasheet

The datasheet of the Pytrack is available as a [PDF File](/gitbook/assets/PyTrack2X_specsheet.pdf)

## Pinout


The PyPort connector is for a 6 lead mini ribbon cable. Part: Amphenol 20021511-00006T4LF.
The external IO header power pins are labelled as follows
* 3V3AUX - The power provided by the development module 
* 3V3AUX_LP - the power provided by the development module for the SD card (This can be switched off)
* 3V3 - The power provided by the Pysense 2, for the USB-Serial converter. This is also used to power the GPS in standby mode.

The pinout of the Pytrack is available as a [PDF File](
/gitbook/assets/pytrack2-pinout.pdf)

The Pytrack 2.0 X features a SMA connector that allows for the connection of an external active or passive GPS antenna. The SMA connector has an internal switch that switches the connection from the internal to the external antenna automatically upon connection of the external antenna. 


![](/gitbook/assets/pytrack2-pinout.png)
## Notes

### Antenna

The Pytrack 2.0 X board has an internal GPS antenna built in. You can find it on the front side near the bottom, labelled `RFI1`. When you are not using the external antenna, remove the jumper labeled `AON`. If you want better reception and faster fix times, you can use the external GPS antenna with the Pytrack 2.0 X. The SMA connector on the side does **NOT** work with the LoRa or WiFi whip antennas you might already have! You can purchase the appropiate GPS antenna from our webshop [here](https://pycom.io/product/external-gps-antenna/). 

### Battery Charger

The board features a single cell Li-Ion/Li-Po charger with a JST PHR‑2 connector. When the board is being powered via the micro USB connector, it will charge the battery (if connected).
> Make sure you check the polarity of the battery before plugging it in! Connect the positive side to the side marked with a `+`.



### Mechanical Dimensions

![](/gitbook/assets/Pytrack_v2.0X_MechanicalDimensions.png)

### 3D model for case design

* Please see the [3D model](/gitbook/assets/pytrack_v2.0X.step) (step format)
