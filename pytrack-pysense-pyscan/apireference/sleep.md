# Sleep

This chapter describes the various methods for sleep and wakeup which are embedded in Pytrack and Pysense libraries. Both Pytrack and Pysense have the same methods, although the appropriate class, either `pytrack` or `pysense`, has to be instantiated.

## Quick Usage Example

The following example is also available at [Sleep Wakeup Example Libraries GitHub repository](https://github.com/pycom/pycom-libraries/blob/master/examples/accelerometer_wake/main.py)

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

## Methods

#### pytrack.get\_sleep\_remaining\(\)

In the event of a sleep session that was awoken by an asynchronous event \(Accelerometer, INT pin or Reset button\) the approximate sleep remaining interval \(expressed in **seconds**\) can be found out. The user has to manually use `setup_sleep()` to configure the next sleep interval.

#### pytrack.get\_wake\_reason\(\)

Returns the last wakeup reason. Possible values are:

```text
# WAKE_REASON_ACCELEROMETER = 1 # Accelerometer activity/inactivity detection
# WAKE_REASON_PUSH_BUTTON = 2   # Pytrack/Pysense reset buttom
# WAKE_REASON_TIMER = 4         # Normal timeout of the sleep interval
# WAKE_REASON_INT_PIN = 8       # INT pin
```

_Note: the_ `WAKE_REASON_INT_PIN` _can be used if the_ `PIC_RC1` _pin \(pin\#6 on External IO Header\) is toggled._

As in the above example, this method should be called at the beginning of the script, to find out the reset \(wakeup\) reason.

#### pytrack.go\_to\_sleep\(\[gps=True\]\)

Puts the board in sleep mode, for the duration, which has to be set previously with `pytrack.setup_sleep(timout_sec)`. The optional boolean parameter sets the GPS state during sleep.

MicroPython code, which is after this function, is not executed, as wakeup will restart MicroPython.

#### pytrack.setup\_int\_wake\_up\(rising, falling\]\)

Enables as wakeup source, the accelerometer INT pin \(PIC - RA5\). The boolean parameters will indicate rising edge \(activity detection\) and/or falling edge \(inactivity detection\) is configured.

**The accelerometer \(class** `LIS2HH12`**\)** has to be also configured for a certain acceleration threshold and duration. Code snippet:

```python
from pytrack import Pytrack
from LIS2HH12 import LIS2HH12

py = Pytrack()
acc = LIS2HH12()

# enable activity and also inactivity interrupts, using the default callback handler
py.setup_int_wake_up(True, True)

# set the acceleration threshold to 2000mG (2G) and the min duration to 200ms
acc.enable_activity_interrupt(2000, 200)
```

#### pytrack.setup\_int\_pin\_wake\_up\(\[rising\_edge = True\]\)

Enables as wakeup source, the INT pic \(PIC - RC1, pin\#6 on External IO Header\). Either rising or falling edge has to be set, by default it's rising edge.

#### pytrack.setup\_sleep\(time\_seconds\)

Sets the sleep interval, specified in seconds. The actual sleep will be started by calling `go_to_sleep()` method.

{% hint style="info" %}
Please note that more functionality is being added weekly to these libraries. If a required feature is not available, feel free to contribute with a pull request at the [Libraries GitHub repository](https://github.com/pycom/pycom-libraries)
{% endhint %}

