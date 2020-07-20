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

1. Before connecting your module to a Pysense / Pytrack board, you should update the firmware on the Pysense/Pytrack board. Instructions on how to do this can be found [here](/updatefirmware/expansionboard/).
2. Disconnect your device from your computer
3. Insert module into Expansion Board
    * On Expansionboard 2.0, connect a jumper cable or wire between `G23` and `GND`
4. Reconnect the board via USB to your computer
5. Run the Firmware Upgrade tool and click through the menus

![](/gitbook/assets/firmware-update-2.png)

6. The firmware version of your device is now upgraded to the latest version.
    * On Expansionboard 2.0, remove the jumper cable.

After you're done with upgrading, you can use the Pymakr Plugins to upload and run programs in your device.

## Common issues:

* If you are having any issues, make sure the **TX and RX jumpers** are present on your Expansion Board, as the jumpers sometimes come loose in the box during transport. Without these jumpers, the updater will fail.
* On MacOS, the firmware upgrade tool needs access to the `/tmp` folder
* On MacOS, there is an issue with signing of the firmware tool. Go to system preferences --> Security & Privacy --> General, and click "Allow" for the Pycom Firmware Updater tool.



