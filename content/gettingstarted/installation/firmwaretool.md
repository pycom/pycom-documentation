---
title: "Updating Firmware"
aliases:
    - gettingstarted/installation/firmwaretool.html
    - gettingstarted/installation/firmwaretool.md
    - chapter/gettingstarted/installation/firmwaretool
---

We strongly recommend you to upgrade your firmware to the latest version as we are constantly making improvements and adding new features to the devices.

Here are the download links to the update tool. Please download the appropriate one for your OS and follow the instructions on the screen.

* [Windows](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=win32&redirect=true)
* [macOS](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=macos&redirect=true) (10.11 or Higher)
* [Linux](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=unix&redirect=true) (requires `dialog` and `python-serial` package)

{{% hint style="info" %}}
Previous versions of firmware are available for download [**here**](/advance/downgrade).
{{< /hint >}}

## Updating Device Firmware

The basic firmware upgrade procedure can be found below, please follow these steps carefully:

After you're done with upgrading, you can use the Pymakr Plugins to upload and run programs in your device.


### Expansion Board 3.0

When using a Pysense/Pytrack/Pyscan/Expansion Board 3.0 to update your module you are not required to make a connection between "G23" and "GND", the Pysense/Pytrack/Pyscan/Expansion Board 3.0 will do this automatically.

1. Before connecting your module to a Pysense/Pytrack board, you should update the firmware on the Pysense/Pytrack. Instructions on how to do this can be found [here](/pytrackpysense/installation/firmware).
2. Disconnect your device from your computer
3. Insert module into Expansion Board
4. Reconnect the board via USB to your computer
5. Run the Firmware Upgrade tool

![](/gitbook/assets/firmware-update-2.png)

6. Disconnect the USB cable from the board and reconnect it, your device is now ready to use

### Expansion Board 2.0

1. Disconnect your device from your computer
2. Insert module into the Expansion Board
3. Connect a jumper cable or wire between `G23` and `GND`
4. Reconnect the board via USB to your computer, this puts the device in ‘firmware update mode'.
5. Run the Firmware Upgrade tool

![](/gitbook/assets/firmware-update.png)

6. Remove the `G23` to `GND` jumper cable/wire

7. Reboot the device (button or power off then on), your device is now ready to use

If you are having any issues, make sure the **TX and RX jumpers** are present on your Expansion Board, as the jumpers sometimes come loose in the box during transport. Without these jumpers, the updater will fail.


After you're done with upgrading, you can use the Pymakr Plugins to upload and run programs in your device.
