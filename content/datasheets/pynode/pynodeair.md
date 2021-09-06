---
title: "Pynode+ Air"
---
**Store**: [Buy Here](https://pycom.io/product/pynode-air/)

## ![](/gitbook/assets/expansion3.png)

## Getting started

See the Pynode examples [here](/tutorials/pynode/)

## Datasheet

The datasheet of the Pynode+ Air is available as a [PDF File]()

### Certifications
The Pynode+ Air is certified for:
* [ROHS certification]()

### Dimensions

![](/gitbook/assets/pynodeair.png)

## Pinout

the Pynode+ Air is only accessible over Bluetooth. 


> Be gentle when plugging and unplugging from the USB connector. Whilst the USB connector is soldered and is relatively strong, if it breaks off it can be very difficult to fix.
## Accessories

The Pynode+ Air is compatible with the [Pynode case](../accessories/pynodecase/)
### Battery Charger
> Make sure you check the polarity of the battery before plugging it in! Connect the positive side to the side marked with a `+`. 

The Expansion Board features a single cell Li-Ion/Li-Po charger with a JST PHR‑2 connector. When the board is being powered via the micro USB connector, the Expansion Board will charge the battery (if connected). When the `CHG` jumper is present, the battery will be charged at `450mA`. If this value is too high for your application, removing the jumper lowers the charge current to `100mA`.

> To use the battery, pull `P8/G15` high (connect to `3v3`). If you want to use the SD card as well, use a 10k pull-up.

### Differences between v2.0 and v3.0

On version 3.0:
* The FTDI chip as been replaced with a custom programmed PIC, similar to the

  Pysense/Pytrack/Pyscan boards. This allows our firmware update tool to

  automatically put the module into bootloader mode.

* Added a "Safe Boot" button to enter more easily into safe boot. This button connects

  `P12` to `3.3v` and if pressed and held while the reset button is pressed on

  a Pycom module, the module will enter safe boot.

### Differences between v3.0 and v3.1
On version 3.1:
* The green USB-LED is only lit when the USB communication stack is running
* The USB-Serial converter (PIC) is powered using any power source. Previously, it would only power up when the board was powered through USB.

## Troubleshooting

* If PIC stays in bootloader mode, the [`dfu-util` update](/updatefirmware/expansionboard/) should be performed

## 3D model for case design

* Please see the [3D model](/gitbook/assets/Expansion_Board_3D.step) (step format)

