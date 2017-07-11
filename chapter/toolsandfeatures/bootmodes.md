# Boot Modes

If powering up normally or upon pressing the reset button, a Pycom device will boot into standard mode; the ``boot.py`` file will be executed first, followed by ``main.py``.

This boot sequence may be overridden by pulling ``P12`` (``G28`` on the expansion board) high (i.e. connect it to the ``3V3`` output pin), during reset cycle. This procedure also allows for the firmware to be reverted to earlier versions. A Pycom device can hold up to 3 different firmware versions; the factory firmware plus 2 OTA images.

After reset, if ``P12`` pin is held high, the heartbeat LED begin flashing orange slowly. If after 3 seconds the pin is still held high, the LED will start blinking faster and the device will select the previous OTA image to boot. If this image is the desired firmware, ``P12`` must be released before 3 more seconds elapse. If an additional 3 seconds later, the pin is still high, the factory firmware will be selected. The LED will then flash quickly for another 1.5 seconds and the device will then proceed to boot. The firmware selection mechanism is as follows:

### Safe Boot

Pin ``P12`` released during:

| 1st 3 secs window | 2nd 3 secs window   | Final 1.5 secs window |
|:-----------------:|:-------------------:|:---------------------:|
|``latest firmware``|``previous firmware``| ``factory firmware``  |


With all of the 3 above scenarios, safe boot mode is entered. This means that the execution of both ``boot.py`` and ``main.py`` is skipped. This may be useful to recover from crash situations produced by the user scripts. The selection made during safe boot is not persistent, therefore after the next normal reset, the latest firmware will proceed to run again.

If problems occur within the filesystem, the user may wish to format the internal flash drive.

### Reset

Pycom devices support both soft and hard resets. A soft reset clears the state of the MicroPython virtual machine but leaves hardware peripherals unaffected. To do a soft reset, press ``Ctrl+D`` on the REPL or from within a script, run:

```python
>>> import sys
>>> sys.exit()
```

A hard reset is the same as performing a power cycle to the device. In order to hard reset the device, press the ``reset`` switch or run:

```python
>>> import machine
>>> machine.reset()
```

### Factory Reset the Filesystem

If a device’s filesystem gets corrupted, it can format it by running:

```python
>>> import os
>>> os.mkfs('/flash')
```
{% hint style='danger' %}
Be aware, resetting the flash filesystem will delete all files inside the internal device storage (not the SD card) and restores the files ``boot.py`` and ``main.py`` to their factory states after the next reset.
{% endhint%}
