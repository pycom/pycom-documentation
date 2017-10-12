# Updating Firmware

To update the firmware on the Pysense/Pytrack, please see the following instructions. The firmware of both Pysense and Pytrack can be updated via the USB port using the terminal tool, DFU-util.

The latest firmware is v0.0.4. The DFU file can be downloaded from the links below:

- [Pytrack DFU](https://software.pycom.io/downloads/pytrack_0.0.6.dfu)
- [Pysense DFU](https://software.pycom.io/downloads/pysense_0.0.6.dfu)

### Installing the DFU-util Tools

##### Mac OS

If using ``homebrew``:

```bash
$ brew install dfu-util
```

If using ``MacPorts``:

```bash
port install libusb dfu-util
```

##### Linux

Ubuntu or Debian:

```bash
$ sudo apt-get install dfu-util
```

Fedora:

```bash
$ sudo yum install dfu-util
```

Arch:

```bash
$ sudo pacman -Sy dfu-util
```

##### Windows

- [DFU-util](http://dfu-util.sourceforge.net/releases/dfu-util-0.8-binaries/win32-mingw32/dfu-util-static.exe) – Tool to upload the firmware to the Pytrack/Pysense
- [Zadig](http://zadig.akeo.ie/) – Installer tool for the Pytrack/Pysense board DFU Firmware 

To uploaded the latest DFU firmware to the Pytrack/Pysense, **first install the DFU drivers** to the host computer. Open Zadig and select ``libusbK`` as the driver.

To install the drivers, the Pytrack/Pysense board must be in DFU-mode:

1. Disconnect the USB cable
2. Hold down the button on the shield
3. Connect the USB cable
4. Keep the button pressed for at least one second
5. Release the button. When the board is connected in DFU-mode, it will be in this state for 7 seconds. 
6. Click the “Install Driver” button immediately. If the driver was unsuccessful, repeat from step 1. 

Occasionally, Windows will automatically install the incorrect drivers for the board. In this case, the button will be labelled “Reinstall Driver” or “Replace Driver”.

<p align="center"><img src ="../../../img/zadig.png" width="400"></p>

Open the command prompt and navigate to the directory where the DFU-util and the firmware was downloaded (must be in same directory). Repeat the procedure to get the board in DFU-mode and run the command below but replace ``X.X.X`` with the firmware version and replace pysense with pytrack if it is the pytrack that is to be updated (e.g: ``pytrack_0.0.4.dfu``):

```bash
dfu-util-static.exe -D pysense_X.X.X.dfu
```

If the update was successful, a message, “Done!” should appear in the bottom of the command prompt.

### Using DFU-util with Pytrack and Pysense

In order to put Pyrack or Pysense in DFU mode, press and hold the button on the Pytrack/Pysense board whilst powering on the board (connecting the USB cable).

1. Press the button and keep it held
2. Next plug-in the USB cable to the host computer and wait 1 second before releasing the button.
3. After this you will have approximately 7 seconds to run the DFU-util tool.

##### MacOS and Linux:

```bash
$ dfu-util -D firmware_file.dfu
```

An output, similar to the one below, will appear upon successful installation:

```bash
dfu-util 0.8

Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2014 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to dfu-util@lists.gnumonks.org

Match vendor ID from file: 04d8
Match product ID from file: f014
Deducing device DFU version from functional descriptor length
Opening DFU capable USB device...
ID 04d8:f014
Run-time device DFU version 0100
Claiming USB DFU Runtime Interface...
Determining device status: state = dfuIDLE, status = 0
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
