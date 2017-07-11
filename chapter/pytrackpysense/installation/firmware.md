# Updating Firmware

To update the firmware on the Pysense/Pytrack, please see the following instructions. The firmware of both Pysense and Pytrack can be updated via the USB port using the terminal tool, DFU-util.

The latest firmware is v0.0.3. The DFU file can be downloaded from the links below:

- [Pytrack DFU](https://software.pycom.io/downloads/pytrack_0.0.3.dfu)
- [Pysense DFU](https://software.pycom.io/downloads/pysense_0.0.3.dfu)

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
