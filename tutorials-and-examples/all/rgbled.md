# RGB LED

By default the heartbeat LED flashes in blue colour once every 4s to signal that the system is alive. This can be overridden through the `pycom` module.

```python
import pycom

pycom.heartbeat(False)
pycom.rgbled(0xff00)           # turn on the RGB LED in green colour
```

The heartbeat LED is also used to indicate that an error was detected.

The following piece of code uses the RGB LED to make a traffic light that runs for 10 cycles.

```python
import pycom
import time

pycom.heartbeat(False)
for cycles in range(10): # stop after 10 cycles
    pycom.rgbled(0x007f00) # green
    time.sleep(5)
    pycom.rgbled(0x7f7f00) # yellow
    time.sleep(1.5)
    pycom.rgbled(0x7f0000) # red
    time.sleep(4)
```

Here is the expected result:

![](../../.gitbook/assets/traffic.gif)

