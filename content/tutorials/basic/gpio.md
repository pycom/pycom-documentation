---
title: "GPIO"
aliases:
    - tutorials/basic/gpio.html
    - tutorials/basic/gpio.md
    - chapter/tutorials/basic/gpio
---
The module has several spare General Purpose Input-Output (GPIO) pins available for you to use with your own sensors and actuators.

## Output
Controlling the GPIO pins of the modules is rather easy. In the example below, we can let the orange LED on the expansion board blink.

```python
from machine import Pin
import time
led = Pin('P9', mode=Pin.OUT)

while True:
    print("high")
    led.value(1)
    time.sleep(1)
    print("low")
    led.value(0)
    time.sleep(1)
```
## Input

Sometimes, it would be useful to know the state of a pin. For example, you could use the button on the xpansion board to toggle the led

```python
from machine import Pin
import time
led = Pin('P9', mode = Pin.OUT)
button = Pin('P10', mode = Pin.IN)

while True:
    if(button() == 1):
        led.value(1)
    else:
        led.value(0)
```

