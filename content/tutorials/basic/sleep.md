
---
title: "Sleep"
aliases:
    - tutorials/all/sleep.html
    - tutorials/all/sleep.md
    - chapter/tutorials/basic/sleep
---

There are several methods to make your device sleep.  First we cover the basic sleep. Similar to `delay()` used in Arduino, sleep will yield your program until the time is over. Important is that the all microcontroller functions keep running. Also the LoRa, SigFox and LTE modems can be used directly (without re-attaching) after regular sleep.

```python
import time

time.sleep(1) #sleep 1 second

time.sleep_ms(10) #sleep 10 milliseconds

time.sleep_us(10) #sleep 10 microseconds
```

Similar to `yield()`, in micropython we use
```python
import machine
machine.idle()
```

### Power saving 
To save power, we can also put the controller into sleep modes using the following examples. 

#### Light sleep

The `machine.sleep()` command will put the controller into a light sleep mode. WiFi and BLE are switched off, but the main CPU and RAM are still running. the LoRa, SigFox and LTE modems are stopped as well and have to be re-initialized after wakeup. The controller will continue running the code after waking up. GPIO states are also conserved. Setting the second argument to `True` will restore the WiFi and BLE after wakeup. 

```python
import machine
import time
print("this will be printed before: " + str(time.ticks_ms()))
machine.sleep(1000*10, True)
print("this will be printed after 10 seconds: " str(time.ticks_ms()))
```

#### Deep sleep
Deepsleep disables, next to the lightsleep, the main CPU and RAM. This leaves only a low power coprocessor and RTC timer running. After waking up, the board will start again at `boot.py`, just like with pressing the reset button. The CPU counter (`time.ticks()`) will continue to count however!
You can also leave the brackets empty to sleep indefinetely, until the reset button is pressed, the power is removed, or an external wake up signal (interrupt) is provided. Be aware that the LTE modem. ***


```python
import machine
print("Wake up")
machine.deepsleep(1000) #deepsleep 1 second
print("this will never get printed!")
```

#### Wake up reason

Sometimes, we want to know the reason the board woke up, to differentiate the difference between pressing the reset button and waking up from sleep. We can also determine the time left on the sleep timer. Try the example below:

```python
import machine
import time
(wake_reason, gpio_list) = machine.wake_reason()
print("Device running for: " + str(time.ticks_ms()) + "ms")
print("Remaining sleep time: " + str(machine.remaining_sleep_time()) + "ms" )
if wake_reason == machine.PWRON_WAKE:
    print("Woke up by reset button")
elif wake_reason == machine.PIN_WAKE:
    print("Woke up by external pin (external interrupt)")
    print(*gpio_list, sep=", ")
elif wake_reason == machine.RTC_WAKE:
    print("Woke up by RTC (timer ran out)")
elif wake_reason == machine.ULP_WAKE:
    print("Woke up by ULP (capacitive touch)")

machine.pin_sleep_wakeup(('P3', 'P4'), mode=machine.WAKEUP_ANY_HIGH, enable_pull=True)

machine.deepsleep(1000*60) #sleep for 1 minute
print("This will never be printed")
```

>Note `pybytes.deepsleep()` is fundamentally the same function as `machine.deepsleep()`, but will gracefully stop the pybytes platform functionality.

#### Other methods

The expansionboards (Pysense 2.0 X, and Pytrack 2.0 X, DeepSleep shield) use a different mechanism to put the controller to sleep. A separate controller on the expansion board will put the main controller to sleep. This will actually cut all power from the module for the set amount of time, hard resetting it. Cutting power to the expansion board will work as well. Using this method, we can still recover the wake up reason and remaining sleep time. The example below works was written for a Pysense, but works on any of the boards by changing the first lines

```python
from pysense import Pysense
py = Pysense()
py.setup_sleep(10) # set sleep time of 10 seconds
py.go_to_sleep()
print("this will never be printed")
```
Using this method, we can also wake the board using the accelerometer and external pin `P6` by rising (`True`) or falling (`False`) edge 

```python
from pysense import Pysense
from LIS2HH12 import LIS2HH12

py = Pysense()
acc = LIS2HH12()

# enable activity and also inactivity interrupts, using the default callback handler
py.setup_int_wake_up(True, True)

# set the acceleration threshold to 2000mG (2G) and the min duration to 200ms
acc.enable_activity_interrupt(2000, 200)

py.set_int_pin_wake_up(True) #wake up on rising edge on pin 6 of the expansion header

py.go_to_sleep()# the device will sleep indefinitely, until pin 6 goes high, or the accelerometer is triggered
```
LTE Power saving mode (PSM)