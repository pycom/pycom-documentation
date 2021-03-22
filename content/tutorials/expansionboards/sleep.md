---
title: 'Sleep'
---
> This example can be used on a **All shields**

On these shields, an additional sleep method is available. Next to [`machine.deepsleep()`](/firmwareapi/pycom/machine/#machinedeepsleeptime_ms). there is `py.go_to_sleep()`, which is able to completely cut the power to the development board, and using only the coprocessor to keep track of when to wake up again. This way, we can save more power, which is especially useful when operating on a battery. On this page, we will cover the following:
* [Simple Pysleep](#simple-pysleep)
* [Wake up from accelerometer](#wake-up-from-accelerometer)
*
## Simple Pysleep
```python
from pycoproc import Pycoproc
py = Pycoproc
# setup the sleep time in seconds
py.setup_sleep(10)
# go to pysleep
py.go_to_sleep()
print("this will never be printed")
```
## Wake up from accelerometer
Using this method, we can also wake the board using the onboard accelerometer to wake up from pysleep after we detect movement. The example below shows how to achieve that:

```python

#from pytrack import Pytrack
from pysense import Pysense
from LIS2HH12 import LIS2HH12
import time

#py = Pytrack()
py = Pysense()

# display the reset reason code and the sleep remaining in seconds
# possible values of wakeup reason are:
# WAKE_REASON_ACCELEROMETER = 1
# WAKE_REASON_PUSH_BUTTON = 2
# WAKE_REASON_TIMER = 4
# WAKE_REASON_INT_PIN = 8

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
