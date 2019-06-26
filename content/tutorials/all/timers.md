---
title: "Timers"
aliases:
    - tutorials/all/timers.html
    - tutorials/all/timers.md
    - chapter/tutorials/all/timers
---

Detailed information about this class can be found in [`Timer`](/firmwareapi/pycom/machine/timer).

## Chronometer

The Chronometer can be used to measure how much time has elapsed in a block of code. The following example uses a simple stopwatch.

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
```

## Alarm

The Alarm can be used to get interrupts at a specific interval. The following code executes a callback every second for 10 seconds.

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
            alarm.callback(None) # stop counting after 10 seconds

clock = Clock()
```

{{% hint style="info" %}}
There are no restrictions to what can be done in an interrupt. For example, it is possible to even do network requests with an interrupt. However, it is important to keep in mind that interrupts are handled sequentially, so it's good practice to keep them short. More information can be found in [`Interrupt Handling`](/firmwareapi/notes#interrupt-handling).
{{< /hint >}}
