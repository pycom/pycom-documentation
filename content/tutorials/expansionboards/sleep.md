---
title: 'Sleep'
---
> This example can be used on a **All shields**

On these shields, an additional sleep method is available. Next to [`machine.deepsleep()`](/firmwareapi/pycom/machine/#machinedeepsleeptime_ms). there is `py.go_to_sleep()`, which is able to completely cut the power to the development board, and using only the coprocessor to keep track of when to wake up again. This way, we can save more power, which is especially useful when operating on a battery. On this page, we will cover the following:
* [Simple Pysleep](#simple-pysleep)
* [Wake up from accelerometer](#wake-up-from-accelerometer)


## Simple Pysleep
```python
from pycoproc import Pycoproc
py = Pycoproc()
# setup the sleep time in seconds
py.setup_sleep(10)
# go to pysleep
py.go_to_sleep()
print("this will never be printed")
```
## Wake up from accelerometer

> This example can be used on the first generation boards

Using this method, we can also wake the board using the onboard accelerometer to wake up from pysleep after we detect movement. The example below shows how to achieve that:

```python

#from pytrack import Pytrack
from pysense import Pysense
from LIS2HH12 import LIS2HH12
import time

# display the reset reason code and the sleep remaining in seconds
# possible values of wakeup reason are:
# WAKE_REASON_ACCELEROMETER = 1
# WAKE_REASON_PUSH_BUTTON = 2
# WAKE_REASON_TIMER = 4
# WAKE_REASON_INT_PIN = 8

py = Pysense()
print("Wakeup reason: " + str(py.get_wake_reason()))
print("Approximate sleep remaining: " + str(py.get_sleep_remaining()) + " sec")
time.sleep(0.5)

# enable wakeup source from INT pin
py.setup_int_pin_wake_up(False)

acc = LIS2HH12()

# enable activity and also inactivity interrupts, using the default callback handler
py.setup_int_wake_up(True, True)

# set the acceleration threshold to 2000mG (2G) and the min duration to 200ms
acc.enable_activity_interrupt(2000, 200)

# go to sleep for 5 minutes maximum if no accelerometer interrupt happens
py.setup_sleep(300)
py.go_to_sleep()
```

## Pysleep Accelerometer 2
Use this example for a **Pysense 2** or **Pytrack 2** shield:
```python

# This script demonstrates two examples:
# * go to ultra low power mode (~10uA @3.75V) with all sensors, incl accelerometer and also pycom module (Fipy, Gpy, etc) off - tap the MCLR button for this
# * go to low power mode (~165uA @3.75V) with accelerometer on, pycom module in deepsleep and wake from accelerometer interrupt - hold the MCLR button down for this

# See https://docs.pycom.io for more information regarding library specifics

import time
import pycom
from machine import Pin
from pycoproc import Pycoproc
import machine

from LIS2HH12 import LIS2HH12

def accelerometer():
    print("ACCELEROMETER:", "accel:", accelerometer_sensor.acceleration(), "roll:", accelerometer_sensor.roll(), "pitch:", accelerometer_sensor.pitch(), "x/y/z:", accelerometer_sensor.x, accelerometer_sensor.y, accelerometer_sensor.z )

def activity_int_handler(pin_o):
    if pin_o():
        print('[Activity]')
        pycom.rgbled(0x00000A) # blue
    else:
        print('[Inactivity]')
        pycom.rgbled(0x0A0A00) # yellow

###############################################################
sleep_time_s = 300 # 5 min
pycom.heartbeat(False)
pycom.rgbled(0x0a0a0a) # white
print("pycoproc init")
py = Pycoproc()
print("battery {:.2f} V".format(py.read_battery_voltage()))
py.setup_sleep(sleep_time_s)

# init accelerometer
accelerometer_sensor = LIS2HH12()
# read accelerometer sensor values
accelerometer()
print("enable accelerometer interrupt")

# enable_activity_interrupt( [mG], [ms], callback)
# accelerometer_sensor.enable_activity_interrupt(8000, 200, activity_int_handler) # low sensitivty
# accelerometer_sensor.enable_activity_interrupt(2000, 200, activity_int_handler) # medium sensitivity
accelerometer_sensor.enable_activity_interrupt( 100, 200, activity_int_handler) # high sensitivity
# accelerometer_sensor.enable_activity_interrupt(63, 160, activity_int_handler) # ultra sensitivty

print("enable pycom module to wake up from accelerometer interrupt")
wake_pins = [Pin('P13', mode=Pin.IN, pull=Pin.PULL_DOWN)]
machine.pin_sleep_wakeup(wake_pins, machine.WAKEUP_ANY_HIGH, True)

print("put pycoproc to sleep and pycom module to deepsleep")
py.go_to_sleep(pycom_module_off=False, accelerometer_off=False, wake_interrupt=True)
machine.deepsleep(sleep_time_s * 1000)

print("we never reach here!")
```