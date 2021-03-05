---
title: "WiPy 3.0"
aliases:
    - datasheets/development/wipy3.html
    - datasheets/development/wipy3.md
    - product-info/development/wipy3
    - chapter/datasheets/development/wipy3
---

![](/gitbook/assets/wipy2.png)

> Note: Orient the RGB LED / reset button over the USB connector on any expansion board 


**Store**: [Buy Here](https://pycom.io/product/wipy-3-0/)

**Getting Started:** [Click Here](/gettingstarted/)

## Datasheet

The datasheet of the WiPy3 is available as a [PDF File](/gitbook/assets/specsheets/Pycom_002_Specsheets_WiPy3.0_v2.pdf)

The Wipy 3 is certified for [CE RED](/gitbook/assets/17-214126_red-certificate_pycom_wipy-3.0.pdf), [RCM](/gitbook/assets/RCM-Wipy3.pdf), [ROHS certification](/gitbook/assets/RoHs_declarations/RoHS-for-WiPy-3(8286-00026P)-20190523.pdf)

## Pinout

The pinout of the WiPy3 is available as a [PDF File](/gitbook/assets/wipy3-pinout.pdf)


![](/gitbook/assets/wipy3-pinout.png)

> Please note that the PIN assignments for UART1 (TX1/RX1), SPI (CLK, MOSI, MISO) and I2C (SDA, SCL) are defaults and can be changed via software.

## Footprints & 3D files

[3D STEP file](/gitbook/assets/3D-files/WiPy.step)
[Pycom footprints](https://github.com/pycom/footprints)

## Differences from WiPy 2.0

* The Deep Sleep current draw is now fixed - it is only 19.7µA
* The RAM has been upgraded from 512KB to 4MB
* The External FLASH has been upgraded from 4MB to 8MB
* The antenna select pin has moved from GPIO16 to GPIO21 \(P12\)


## Notes

### Power
Do not use the 3.3V pin **in combination with** the Vin pin to supply the device as this will damage the voltage regulator on the board.

### Antenna placement
Always attach the appropriate antenna when using a wireless connection. For WiFi / BLE, it is not mandatory to use an external antenna when you did not explicitly specify this in your code. 


### WiFi

By default, upon booting up the WiPy3 will create a WiFi access point with the SSID `wipy-wlan-XXXX`, where `XXXX` is a random 4-digit number, and the password `www.pycom.io`.

The RF switch that chooses between the on-board and external antenna is connected to `P12`, for this reason using `P12` should be avoided unless WiFi is disabled in your application.

### Power

The `Vin` pin on the WiPy3 can be supplied with a voltage ranging from `3.5v` to `5.5v`. The `3.3v` pin on the other hand is output **only**, and must not be used to feed power into the WiPy3, otherwise the on-board regulator will be damaged.

## Tutorials

Tutorials on the WiPy3 module can be found in the [examples](/tutorials/introduction) section of this documentation. The following tutorials might be of interest for those using the WiPy3:

* [WiFi connection](/tutorials/all/wlan)
* [BLE](/tutorials/all/ble)
