---
title: "Troubleshooting Guide"
aliases:
    - gettingstarted/troubleshooting-guide.html
    - gettingstarted/troubleshooting-guide.md
---

## How to ask for help

Always provide these details when asking for help. This helps us understand your setup and save time.

* Run `os.uname()` on your module to get the version numbers
* Your module's type & version (e.g. FiPy 1.0)
* Any shields, or devices connected (e.g. Pytrack, Extension Board 3.0 with “x" sensor)
* Your Operating System's version
* Pymakr version
* Atom / VSCode version
* Have you looked at our [documentation](https://docs.pycom.io) and similar issues on the [forum](https://forum.pycom.io)?

## Firmware Update

#### Firmware file has unexpected sha1 checksum.

If you're trying to update to the latest `development` firmware, make sure you use the development release of the Firmware Updater.

#### My module is recognised as the wrong type

Open a support ticket with the details and send us the result of this code:

```python

import machine, binascii                                                     
binascii.hexlify(machine.unique_id())
```

## Connecting  to the module

#### Module stuck in bootloader mode

Normally, the firmware updater switches back to application mode at the end of an upgrade. If that doesn't happen for some reason, re-plugging the USB cable also puts the device back into application mode.

## Pymakr

Make sure you have the latest version of Pymakr and [Atom](https://atom.io)/[VSCode](https://code.visualstudio.com) installed.

**Synchronising a project results in ‘Failed to allocate memory' error**

Synchronising takes a bit of memory, so this error can occur when code running on the board already is taking a substantial amount of memory.

**Solution:** use safe boot with [REPL](https://docs.pycom.io/gettingstarted/programming/repl) or [Expansion Board](https://docs.pycom.io/product-info/boards/expansion3) when synchronising

### Atom

**Failed to load package: Cannot find module ‘serialport'**

In some cases, this is caused by the Atom Package Manager (apm) using Python 3.x, while `node-gyp` (used for compiling the `serialport` lib) needs Python 2.x. To confirm this, `apm —version` can be run to check which Python version apm is using.

**Solution:** Tell the package manager to use python 2 instead. Running the following command switches apm to 2.7:

```text
echo “python=/usr/bin/python2.7” >> ~/.atom/.apmrc
```

Now reinstall Pymakr or run apm install from the Pymakr package located in `~/.atom/packages/pymakr`

**Could not locate the bindings file**

If the installation of the `serialport` library failed, it reverts back to the precompiled version that is included in the plugin. This is compiled for the latest versions of Atom and loses compatibility with older versions.

**Solution:** upgrade to the latest Atom (1.19.0 or higher) or install the previous version of the plugin (`apm install pymakr@1.0.3`)

**Any error where the traceback contains \.atom\packages\Pymakr\ with a capital “P”**

This happened after `Pymakr` renamed to `pymakr` (lowercase) starting at version 1.2.5, but Atom remembers the old folder name inside the packages folder.

**Solution:**

* Uninstall Pymakr
* Remove folder: `~/.atom/.apm/Pymkr`
* Empty folder: `~/.config/Atom/Cache`
* Reinstall pymakr

**Cannot connect to Pycom board via REPL**

In the case of a board that has already has code uploaded to it and is running a loop/non-exiting script, the board may not boot into a REPL.

**Solution:** If the board is currently running code, you will need to exit the current script before proceeding: 1. Ensure your board is connected to your computer 2. Press the reset button on the device 3. Press `ctrl-c` on within the Pymakr console to exit the current script/program

The REPL should then appear with the `>>>` prompt and you will be able to run/sync your code.

**Cannot connect to Pycom on Linux**

If you're a Linux user and can't connect to your board, there might be a permission issue to access the serial port.

**Solution:** Run the following command `sudo usermod -a -G dialout $USER`

### VSCode

**Terminal not opening**

If the Pymakr terminal is not opening or giving an error, this might be because NodeJS is not installed on your system. This is because the terminal process is running separate from VSCode and depends on your systems NodeJS install.

**Solution:** install NodeJS. For Windows 64 machines, install a 32 bit version of NodeJS (for example `nvm install 7.8.0 32` when using `nvm`).

