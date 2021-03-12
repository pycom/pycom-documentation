---
title: "Pytrack Examples"
aliases:
    - tutorials/pytrack.html
    - tutorials/pytrack.md
    - chapter/tutorials/pytrack
---

Both the Pysense and Pytrack use the same accelerometer. Please see the [Pysense Examples](../pysense) to see how to use the accelerometer.
>Note: You can find this example in the [GitHub repository](https://github.com/pycom/pycom-libraries/). Over there, you can also find the relevant libraries.

## GPS Example

```python

import machine
import math
import network
import os
import time
import utime
import gc
from machine import RTC
from machine import SD
from L76GNSS import L76GNSS
from pytrack import Pytrack

time.sleep(2)
gc.enable()

# setup rtc
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
utime.sleep_ms(750)
print('\nRTC Set from NTP to UTC:', rtc.now())
utime.timezone(7200)
print('Adjusted from UTC to EST timezone', utime.localtime(), '\n')

py = Pytrack()
l76 = L76GNSS(py, timeout=30)

# sd = SD()
# os.mount(sd, '/sd')
# f = open('/sd/gps-record.txt', 'w')

while (True):
    coord = l76.coordinates()
    #f.write("{} - {}\n".format(coord, rtc.now()))
    print("{} - {} - {}".format(coord, rtc.now(), gc.mem_free()))
```

## Alternative Libraries

* [micropyGPS](https://github.com/inmcm/micropyGPS)
* [Alternative L76GNSS module](https://github.com/andrethemac/L76GLNSV4/blob/master/L76GNSV4.py)
