# class Timer – Measure Time and Set Alarms

Timers can be used for a great variety of tasks, like measuring time spans or being notified that a specific interval has elapsed.

These two concepts are grouped into two different subclasses:

`Chrono`: used to measure time spans.
`Alarm`: to get interrupted after a specific interval.

{% hint style='tip' %}
You can create as many of these objects as needed.
{% endhint %}

### Constructors

#####<class><i>class</i> Timer.Chrono()</class>

Create a chronometer object.

#####<class><i>class</i> Timer.Alarm(handler=None, s, * , ms, us, arg=None, periodic=False)</class>

Create an Alarm object.

- `handler`: will be called after the interval has elapsed. If set to `None`, the alarm will be disabled after creation.
- `arg`: an optional argument can be passed to the callback handler function. If `None` is specified, the function will receive the object that triggered the alarm.
- `s, ms, us`: the interval can be specified in seconds (float), miliseconds (integer) or microseconds (integer). Only one at a time can be specified.
- `periodic`: an alarm can be set to trigger repeatedly by setting this parameter to `True`.

### Methods

#####<function>Timer.sleep_us()</function>

Delay for a given number of microseconds, should be positive or 0 (for speed, the condition is not enforced). Internally it uses the same timer as the other elements of the `Timer` class. It compensates for the calling overhead, so for example, 100us should be really close to 100us. For times bigger than 10,000us it releases the GIL to let other threads run, so exactitude is not guaranteed for delays longer than that.

# class Chrono

Can be used to measure time spans.

### Methods

#####<function>chrono.start()</function>

Start the chronometer.

#####<function>chrono.stop()</function>

Stop the chronometer.

#####<function>chrono.reset()</function>

Reset the time count to 0.

#####<function>chrono.read()</function>

Get the elapsed time in seconds.

#####<function>chrono.read_ms()</function>

Get the elapsed time in milliseconds.

#####<function>chrono.read_us()</function>

Get the elapsed time in microseconds.

Example:

```python
from machine import Timer
import time

chrono = Timer.Chrono()

chrono.start()
time.sleep(1.25) # simulate the first lap took 1.25 seconds
lap = chrono.read() # read elapsed time without stopping
time.sleep(1.5)
chrono.stop()
total = chrono.read()

print()
print("\nthe racer took %f seconds to finish the race" % total)
print("  %f seconds in the first lap" % lap)
print("  %f seconds in the last lap" % (total - lap))
class Alarm – get interrupted after a specific interval
```

### Methods

#####<function>alarm.callback(handler, * , arg=None)</function>

Specify a callback handler for the alarm. If set to `None`, the alarm will be disabled.

An optional argument `arg` can be passed to the callback handler function. If `None` is specified, the function will receive the object that triggered the alarm.

#####<function>alarm.cancel()</function>

Disables the alarm.

Example:

```python
from machine import Timer

class Clock:

    def __init__(self):
        self.seconds = 0
        self.__alarm = Timer.Alarm(self._seconds_handler, 1, periodic=True)

    def _seconds_handler(self, alarm):
        self.seconds += 1
        print("%02d seconds have passed" % self.seconds)
        if self.seconds == 10:
            alarm.cancel() # stop counting after 10 seconds

clock = Clock()
```

{% hint style='info' %}
For more information on how Pycom’s products handle interrupts, see [notes](../../../toolsandfeatures/notes.md).
{% endhint %}
