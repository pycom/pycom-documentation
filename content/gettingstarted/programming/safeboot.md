---
title: "Safe boot"
aliases:
    - gettingstarted/programming/safeboot.html
    - gettingstarted/programming/safeboot.md
    - chapter/gettingstarted/programming/safeboot
---

If powering up normally or upon pressing the reset button, a Pycom module will boot into standard mode; the `boot.py` file will be executed first, followed by `main.py`. It is possible to alter the boot procedure of the module by tying certain pins `high` or `low` when the module boots.

## Safe Boot

Some times the code you have written will prevent you gaining access to the REPL or prevent you updating your code. Some example may be:

* You disabled the WiFi/UART
* Your code gets stuck before reaching the REPL
* You set a socket as blocking but never receive any data

In order to fix this you can safe boot your module. This will prevent `boot.py` and `main.py` from being executed and will drop you straight into the interactive REPL. After reset, if `P12` pin is held `high` (i.e. connect it to the `3V3` output pin), the heartbeat LED will begin flashing orange slowly. If after 3 seconds the pin is still held high, the LED will start blinking faster. In this mode the module will do the same as previously explained but it will also select the previous OTA image to boot if you have updated the module via the OTA update procedure (updates performed via the firmware update tool do not count). This is useful if you flashed a OTA update that breaks the device.

Pin `P12` released during:

| 1st 3 secs window | 2nd 3 secs window |
| :--- | :--- |
| Disable `boot.py` and `main.py` | Same as previous but using previous OTA firmware |

The selection made during safe boot is not persistent, therefore after the next normal reset, the latest firmware will proceed to run again.

If problems occur within the filesystem or you wish to factory reset your module to remove your code, run following code in the REPL:

```python
>>> import os
>>> os.fsformat('flash')
```

> Be aware, formatting the flash filesystem will delete all files inside the internal device storage (not the SD card) and they cannot be recovered.

## Reset

Pycom devices support both soft and hard resets. A soft reset clears the state of the MicroPython virtual machine but leaves hardware peripherals unaffected. To do a soft reset, press `Ctrl+D` on the REPL or from within a script, run:

```python
>>> import sys
>>> sys.exit()
```

A hard reset is the same as performing a power cycle to the device. In order to hard reset the device, press the `reset` switch or run:

```python
>>> import machine
>>> machine.reset()
```
