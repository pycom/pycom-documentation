# Boot Modes

### Bootloader Mode
In order to put Pycom modules into bootloader mode to allow firmware to be
upgraded, ``P2`` must be pulled ``low`` during boot. When this is done the
device will print ``waiting for download``. After this it is ready to receive an
update via the firmware updater.

### Safe boot
If powering up normally or upon pressing the reset button, a Pycom device will
boot into standard mode; the ``boot.py`` file will be executed first, followed
by ``main.py``.

This boot sequence may be overridden by pulling ``P12`` (``G28`` on the
expansion board) `high` (i.e. connect it to the ``3V3`` output pin), during
reset cycle. After reset, if ``P12`` pin is held high, the heartbeat LED will
begin flashing orange slowly, this will indicate the execution of ``boot.py``
and ``main.py`` will be skipped. This can be useful when the code in these files
prevents you from accessing the device, e.g. disabling the UART and WiFi.

If after 3 seconds the pin is still held high, the LED will start blinking
faster. If the device has been updated using the OTA procedure, this will
trigger the device to boot its previous firmware (more details on this can be
found below)

### Firmware slots

Pycom modules feature two firmware slots. When you perform a firmware upgrade
using our updater tool, this is always written to slot 0. When an OTA is applied,
either by FTP or our provided [OTA functions](../firmwareapi/pycom/pycom.md), it
will be written to the currently unused slot. Once the OTA is completed and the
new firmware is verified, the active slot is swapped.

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

### Factory Reset the Filesystems

If a device’s filesystem gets corrupted, it can format it by running:

```python
>>> import os
>>> os.mkfs('/flash')
```
{% hint style='danger' %}
Be aware, resetting the flash filesystem will delete all files inside the internal device storage (not the SD card) and restores the files ``boot.py`` and ``main.py`` to their factory states after the next reset.
{% endhint%}
