---
title: "Updating Expansion Board Firmware "
aliases:
    - updatefirmware/expansionboard.html
    - updatefirmware/expansionboard.md
    - chapter/updatefirmware/expansionboard
---

To update the firmware on any of the expansionboards, please see the following instructions. The firmware of can be updated via the USB port using the terminal tool, `DFU-util`.

> There is currently **no firmware update** released for the new **Pytrack 2.0 X** and **Pysense 2.0 X**. Please do not try to flash these boards with firmware released for the old Version 1 hardware revision. The hardware revision is printed on the bottom of the shield.


The latest firmware DFU file can be downloaded from the links below:
* [Pygate](https://software.pycom.io/findupgrade?key=pygate.dfu&type=all&redirect=true)
* [Pytrack 1 DFU](https://software.pycom.io/findupgrade?key=pytrack.dfu&type=all&redirect=true)
* [Pysense 1 DFU](https://software.pycom.io/findupgrade?key=pysense.dfu&type=all&redirect=true)
* [Expansion Board DFU v3.0](https://software.pycom.io/findupgrade?key=expansion3.dfu&type=all&redirect=true)
* [Expansion Board DFU v3.1](https://software.pycom.io/findupgrade?key=expansion31.dfu&type=all&redirect=true)


> Make sure to choose the correct firmware version for your expansion board. both 3.0 and 3.1 versions have version numbers in the silkscreen on the back of the board. See the image below for examples highlighted in Red
>![](/gitbook/assets/expansion_board_version.png)

## Product ID
In normal operation, the expansionboard is in Application mode. However when we want to update the firmware, we should put the board in DFU (Device Firmware Upgrade) mode. This is a special mode that allows us to alter the firmware of the device. Entering DFU mode changes the Product ID of the device, such that we will never accidentally update the firmware. To actually upgrade the firmware, we need to install the DFU-Util tool. Below, the USB Product ID is depicted for each case. You can check the Product ID for your board using `lsusb` on macOS and Linux, and checkin the device manager in Windows:

| Board | DFU bootloader (update mode) | Application firmware (normal mode) |
| :--- | :--- | :--- |
| Pygate | `0xED15` | `0xED14` |
| Pytrack | `0xF014` | `0xF013` |
| Pysense | `0xF011` | `0xF012` |
| Pyscan | `0xEF37` | `0xEF38` |
| Expansion Board v3 | `0xEF99` | `0xEF98` |

_Note: USB Vendor ID is always_ `0x04D8`



## Installing DFU-Util

  * MacOS

    * If using `homebrew`:

    ```bash
    $ brew install dfu-util
    ```
    * If using `MacPorts`:

    ```bash
    port install libusb dfu-util
    ```
  * Linux

    ```bash
    $ sudo apt-get install dfu-util
    ```

  * Windows

    Download and install [DFU-util v0.9](http://dfu-util.sourceforge.net/releases/dfu-util-0.9-win64.zip) 
    
    For Windows, we will need to install separate drivers for the board to recognized as a Pycom board in DFU mode.
    1. Disconnect the USB cable to your expansion board
    2. Hold down the DFU mode button on the shield

    * [Zadig](http://zadig.akeo.ie/) – Installer tool for the Pytrack/Pysense board DFU Firmware

    To install the drivers, the board must be in DFU-mode:

    1. Disconnect the USB cable
    2. Remove the development module from the expansionboard.
    3. Hold down the button on the shield
    4. Connect the USB cable
    5. Keep the button pressed for at least one second
    6. Release the button. When the board is connected in DFU-mode, it will be in this state for 7 seconds.
    7. Click the`“Install Driver` button immediately. If the driver was unsuccessful, repeat from step 1.
    If all went sucessfully, you will see the device show up in `Device Manager` as a LibusbK device.

    ![](/gitbook/assets/pytrack_dfu_mode_zadig.png)

    > If you accidentally installed the `libusbk` while the device was in Application mode, then the need to update the driver to the `Serial USB (CDC)` driver has to be installed for application mode. This will allow Windows to allocate a COM port, which is required for REPL console.
    > ![](/gitbook/assets/pytrack_app_mode_zadig.png)

## Using DFU-util

To enter update mode follow these steps:

1. Navigate the terminal to the folder where you downloaded the `.dfu` file to
2. Unplug the device
3. Remove the development module
4. Press this button on your device:

| Expansionboard 3.1 | Pygate | Pysense | Pysense 2.0 X | Pytrack | Pytrack 2.0 X | PyScan |
|:----|:----|:-----|:--------|:-----|:-----|:----|
| ![](/gitbook/assets/expansionboards/expansionboard31_dfu.png) | ![](/gitbook/assets/expansionboards/pygate_dfu.png)|![](/gitbook/assets/expansionboards/pysense1_dfu.png)] | ![](/gitbook/assets/expansionboards/pysense2_dfu.png) | ![](/gitbook/assets/expansionboards/pytrack1_dfu.png) | ![](/gitbook/assets/expansionboards/pytrack2_dfu.png) | ![](/gitbook/assets/expansionboards/pyscan_dfu.png) |

5. Plug in the USB cable to the host computer and wait 1 second before releasing the button
6. After this you will have approximately 7 seconds to run the DFU-util tool
  * For MacOS and Linux:
    ```bash
    $ dfu-util -D pytrack_0.0.8.dfu
    ```
  * For Windows:
    ```bash
    dfu-util-static.exe -D filename.dfu
    ```

If the update was successful, "Done!" should appear in the bottom of the command prompt.
The output should look like the following:

```bash
dfu-util 0.9

Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2016 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

Match vendor ID from file: 04d8
Match product ID from file: f014
Opening DFU capable USB device...
ID 04d8:f014
Run-time device DFU version 0100
Claiming USB DFU Runtime Interface...
Determining device status: state = dfuIDLE, status = 0
dfu-util: WARNING: Runtime device already in DFU state ?!?
Claiming USB DFU Interface...
Setting Alternate Setting #0 ...
Determining device status: state = dfuIDLE, status = 0
dfuIDLE, continuing
DFU mode device DFU version 0100
Device returned transfer size 64
Copying data from PC to DFU device
Download    [=========================] 100%        16384 bytes
Download done.
state(2) = dfuIDLE, status(0) = No error condition is present
Done!
```

### Debugging

Using `lsusb` command, the device should be visible in both normal and bootloader modes.

For exemple, a Pytrack board is visible as either:

* `Bus 020 Device 004: ID 04d8:f014 Microchip Technology Inc. Application Specific Device`
  * this is bootloader mode (`f014` is USB PID), active just for 7-8 seconds, if the reset button was just  pressed before plugging USB connector.
* `Bus 020 Device 005: ID 04d8:f013 Microchip Technology Inc. Pytrack Serial: Pyabcde0`
  * this is normal, application mode (`f013` is USB PID), this means the bootloader verified application partition and it boot-up correctly.
