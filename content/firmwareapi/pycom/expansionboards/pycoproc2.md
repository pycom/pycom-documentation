---
Title: "Pycoproc2"
---

The `pycoproc2.py` file is a supporting python library for the Pysense 2 and Pytrack 2 expansionboards. 

## Constructors

### class Pycoproc(i2c=None, sda='P22', scl='P21')

Initialise I2C communication with the supervisor MCU, if no i2c object is passed, the `sda` and `scl` pins are used. On a Pysense 2 / Pytrack 2 board, the sensors are connected on these pins.

## General functions

### py.read_fw_version()

Read the PIC firmware version. Check the [update firmware](/updatefirmware/expansionboard/) if an update is available.

### py.read_hw_version()

Read the hardware version. 

### py.read_product_id()

Read the product ID

### py.button_pressed()

Returns `True` if the on-board `MCLR` button is pressed.

### py.read_battery_voltage()

Returns the battery voltage

### py.reset_cmd()

Power cycles the development module.

## Power functions

### py.sd_power([enabled=True])

This command allows switching the power supply for the SD card:
* `True`: the SD card is enabled
* `False`: the SD card is disabled

### py.sensor_power([enabled=True])

This command allows switching the power supply for the GPS module and any sensors connected through the external Pyport:
* `True`: the power is enabled
* `False`: the power is disabled

### py.gps_standby([enabled=True])

This command allows switching the GPS module into stand-by mode. The GPS module is no longer accessible via I2C in this case:
* `True`: the GPS is put in standby mode
* `False`: the GPS is activated. 

### py.setup_sleep(seconds)

Sets the sleep time in seconds for `py.go_to_sleep(...)`. This method will momentarily release the USB connection, meaning you will have to reconnect the USB in Pymakr after using this method.

### py.go_to_sleep([gps=True, pycom_module_off=True, accelerometer_off=True, wake_interrupt=False])

Puts the board in sleep mode. This sleep mode consumes less power than the `machine.deepsleep()` available from the firmware, as it turns the power to the inserted development module off.This will also disable the power to the sensors, sd card and Pyport, except for the accelerometer. Arguments are:
* `gps`: Keep the GPS (if available) in standby mode while sleeping. This reduces the power consumption, but might extend the time to location fix after wakeup.
* `pycom_module_off`: Turn off the power to the inserted development module. This dramatically reduces the power consumption, but will not allow for wake on accelerometer interrupt. See the example below on how to achieve that.
* `accelerometer_off`: Turn off the power to the accelerometer.
* `wake_interrupt`: Allow waking up from an interrupt on PIC RC1, or `EXT_IO_0` on the external IO header.

## Example

Use the following example to wake up from an accelerometer interrupt:

```python
import machine
import time
from pycoproc import Pycoproc

py = Pycoproc()
print("enable pycom module to wake up from accelerometer interrupt")
wake_pins = [Pin('P13', mode=Pin.IN, pull=Pin.PULL_DOWN)]
machine.pin_sleep_wakeup(wake_pins, machine.WAKEUP_ANY_HIGH, True)

print("put pycoproc to sleep and pycom module to deepsleep")
py.setup_sleep(sleep_time_s)
py.go_to_sleep(pycom_module_off=False, accelerometer_off=False, wake_interrupt=True)
machine.deepsleep(sleep_time_s * 1000)
```