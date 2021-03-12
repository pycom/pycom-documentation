---
Title: "Pycoproc"
---

The `pycoproc.py` file is a supporting python library for the first version of Pysense Pytrack and Pyscan expansionboards. For version 2.0 X, see [pycoproc2](../pycoproc2/)

## Constructors

### class Pycoproc(board_type, [i2c=None, sda='P22', scl='P21'])

Initialise I2C communication with the supervisor MCU, if no i2c object is passed, the `sda` and `scl` pins are used. On the shield, the sensors are connected on these pins. Board type can be:
* `Pycoproc.PYSENSE`
* `Pycoproc.PYTRACK`
* `Pycoproc.PYSCAN`


## General functions

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

## Power functions

### py.setup_sleep(seconds)

Sets the sleep time in seconds for `py.go_to_sleep(...)`. This method will momentarily release the USB connection, meaning you will have to reconnect the USB in Pymakr after using this method.

### py.setup_int_wake_up(rising, falling)

Enables the accelerometer INT pin (PIC - RA5) as a wakeup source, if the [accelerometer interrupt](../lis2hh12/#lis2hh12enable_activity_interruptthreshold-duration-handlernone) is configured. The boolean parameters will indicate rising edge (activity detection) and/or falling edge (inactivity detection) is configured.

### py.setup_int_pin_wake_up([rising=True])

Allow waking up from an interrupt on PIC RC1, or `EXT_IO_0` on the external IO header

### py.go_to_sleep([gps=True])

Puts the board in sleep mode. This sleep mode consumes less power than the `machine.deepsleep()` available from the firmware, as it turns the power to the inserted development module off.This will also disable the power to the sensors, sd card and Pyport, except for the accelerometer. Arguments are:
* `gps`: Keep the GPS (if available) in standby mode while sleeping. This reduces the power consumption, but might extend the time to location fix after wakeup.

### py.get_sleep_remaining()

In the event of a sleep session that was awoken by an asynchronous event (Accelerometer, INT pin or Reset button) the approximate sleep remaining interval (expressed in **seconds**) can be found out. The user has to manually use `setup_sleep()` to configure the next sleep interval.