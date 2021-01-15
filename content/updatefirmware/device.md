---
title: "Updating Device Firmware"
aliases:
    - updatefirmware/device.html
    - updatefirmware/device.md
    - chapter/updatefirmware/device
---

We strongly recommend you to upgrade your firmware to the latest version as we are constantly making improvements and adding new features to the devices.

Here are the download links to the update tool. Please download the appropriate one for your OS and follow the instructions on the screen.

* [Windows](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=win32&redirect=true)
* [macOS](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=macos&redirect=true) (10.11 or Higher)
* [Linux](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=unix&redirect=true) (requires `dialog` and `python-serial` package)

>Previous versions of firmware are available for download [here](/advance/downgrade).

Jump to [common issues](#common-issues)
## Updating Device Firmware

The basic firmware upgrade procedure can be found below, please follow these steps carefully:

After you're done with upgrading, you can use the Pymakr Plugins to upload and run programs in your device.

1. Before connecting your module to a Pysense / Pytrack board, you should check for updates of the firmware on the Pysense/Pytrack board. Instructions on how to do this can be found [here](/updatefirmware/expansionboard/).
2. Disconnect your device from your computer
3. Insert the module into Expansion Board
    * On Expansionboard 2.0, connect a jumper cable or wire between `G23` and `GND`
4. Reconnect the board via USB to your computer
5. Run the Firmware Upgrade tool and click through the menus. There are several different firmware types available:
    * `Pybytes`: this is the most comonly used latest firmware with built in pybytes library. You can use this firmware to connect to Pybytes (or choose to not use it)
    * `Pygate`: This firmware is needed to operate the Pygate expansionboard. It contains additional features like support for the LoRa gateway and PyEthernet. On the Lopy4, you cannot use the onboard LoRa radio. This version also includes the Pybytes library
    * `Pymesh`: This firmware is only available through a package on Pybytes as you will need to agree to additional licensing. It allows you to set up a LoRa mesh of pycom devices connected through Pybytes
    
    We do not recommend using the following firmware types in a production environment:
    
    * `Development`: The latest beta-releases will be published here, they will be of the pybytes variant. There might be unkown bugs in this firmware.
    * `Legacy`: Older firmwares without support for Pybytes.
    * `Pybytes-legacy`: Older firmwares with support for Pybytes.
    
    Note that we only provide support on the latest firmware version!
    ![](/gitbook/assets/firmware_update-0.png)
    > Checking 'Include Development Releases' will check for the development releases of the Firmware Updater Tool


    ![](/gitbook/assets/firmware_update-1.png)
    > Checking 'Show Advanced Settings' will give you the option screen in the next figure.

    ![](/gitbook/assets/firmware_update-2.png)

    > In some cases, erasing the NVS and CONFIG partitions can solve issues relating to WiFi, Timers or other variables stored in the NVS / CONFIG. Erase during update will remove all Python code on the device.


6. The firmware version of your device is now upgraded to the latest version.
    * On Expansionboard 2.0, remove the jumper cable.

After you're done with upgrading, you can use the Pymakr Plugins to upload and run programs in your device.

## Common issues:

* If you are having any issues uploading firmware to your device, make sure the **TX and RX jumpers** are present on your Expansion Board, as the jumpers sometimes come loose in the box during transport. Without these jumpers, the updater will fail.
* On MacOS, the firmware upgrade tool needs access to the `/tmp` folder
* On MacOS, there is an issue with signing of the firmware tool. Go to system preferences --> Security & Privacy --> General, and click "Allow" for the Pycom Firmware Updater tool.



