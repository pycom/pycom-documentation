---
title: "WiPy 2.0"
aliases:
    - datasheets/development/wipy2.html
    - datasheets/development/wipy2.md
    - product-info/development/wipy2
    - chapter/datasheets/development/wipy2
---

![](/gitbook/assets/wipy2.png)

> Note: Orient the RGB LED / reset button over the USB connector on any expansion board 

**Store**: Discontinued, See [WiPy3](../wipy3)

**Getting Started:** [Click Here](/gettingstarted/)

## Datasheet

The datasheet of the WiPy2 is available as a [PDF File](/gitbook/assets/specsheets/Pycom_002_Specsheets_WiPy2.0_v2.pdf)

The Wipy 2 is certified for [CE RED](/gitbook/assets/16-213297_expertise_pycom_wipy-2.0r.pdf), [FCC ACC](/gitbook/assets/2091acc16_grant.pdf), [FCC BCC](/gitbook/assets/2091bcc16_grant.pdf)


## Pinout

The pinout of the WiPy2 is available as a [PDF File](/gitbook/assets/wipy2-pinout.pdf)

![](/gitbook/assets/wipy2-pinout.png)

> Please note that the PIN assignments for UART1 (TX1/RX1), SPI (CLK, MOSI, MISO) and I2C (SDA, SCL) are defaults and can be changed via software.

## Footprints & 3D files

[3D STEP file](/gitbook/assets/3D-files/WiPy.step)
[Pycom footprints](https://github.com/pycom/footprints)

## Notes

### Power
Do not use the 3.3V pin **in combination with** the Vin pin to supply the device as this will damage the voltage regulator on the board.

### Antenna placement
Always attach the appropriate antenna when using a wireless connection. For WiFi / BLE, it is not mandatory to use an external antenna when you did not explicitly specify this in your code. 

### Deep Sleep

Due to a couple of issues with the WiPy2 design, the module draws more current than it should while in Deep Sleep. The DC-DC switching regulator always stays in high performance mode, which is used to provide the lowest possible output ripple when the module is in use. In this mode, it draws a quiescent current of 10mA. When the regulator is put into ECO mode the quiescent current drops to 10uA. Unfortunately, the pin used to control this mode is out of the RTC domain. This means that it is not usable during Deep Sleep. This results in the regulator remaining in PWM mode, keeping its quiescent current at 10mA. The flash chip also doesn't enter into power down mode as the CS pin floats during Deep Sleep. This causes the flash chip to consume around 2mA of current. To work around this issue a ["deep sleep shield"]../expansionboards/deepsleep/) is available that attaches to the module and allows power to be cut off from the device. The device can then be re-enabled either through a timer or via a pin interrupt. With the Deep Sleep Shield, the current consumption during deep sleep is between 7uA and 10uA depending on the wake sources configured.

## Tutorials

Tutorials on the WiPy2 module can be found in the [examples](/tutorials/introduction) section of this documentation. The following tutorials might be of  interest for those using the WiPy2:

* [WiFi connection](/tutorials/networks/wlan)
* [BLE](/tutorials/networks/ble)
