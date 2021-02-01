---
title: 'Sleep'
---

The expansionboards (Pysense 2.0 X, and Pytrack 2.0 X, DeepSleep shield) use a different mechanism to put the controller to sleep. A separate controller on the expansion board will put the main controller to sleep. This will actually cut all power from the module for the set amount of time, hard resetting it. Cutting power to the expansion board will work as well. Using this method, we can still recover the wake up reason and remaining sleep time. The example below works was written for a Pysense, but works on any of the boards by changing the first lines

```python
from pysense import Pysense
py = Pysense()
py.setup_sleep(10) # set sleep time of 10 seconds
py.go_to_sleep()
print("this will never be printed")
```
Using this method, we can also wake the board using the accelerometer interrupt method:

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
