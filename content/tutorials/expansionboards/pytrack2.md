---
title: "Pytrack 2.0 X Examples"
aliases:
    - tutorials/pysense.html
    - tutorials/pysense.md
    - chapter/tutorials/pysense
---
The Pytrack 2.0 X has an external header that allows you to attach all kinds of sensors. 
## All sensors
>Note: You can find this example in the [GitHub repository](https://github.com/pycom/pycom-libraries/). Over there, you can also find the relevant libraries. 
```python
#!/usr/bin/env python
#
# Copyright (c) 2020, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

import machine
import math
import network
import os
import time
import utime
import gc
import pycom
from machine import RTC
from machine import SD
from L76GNSS import L76GNSS
from pytrack import Pytrack

pycom.heartbeat(False)
pycom.rgbled(0x0A0A08) # white

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

time.sleep(1)
l76 = L76GNSS(py, timeout=30, buffer=512)

# sd = SD()
# os.mount(sd, '/sd')
# f = open('/sd/gps-record.txt', 'w')

# while (True):
for _ in range(5):
    coord = l76.coordinates()
    #f.write("{} - {}\n".format(coord, rtc.now()))
    print("{} - {} - {}".format(coord, rtc.now(), gc.mem_free()))

"""
# sleep procedure
time.sleep(3)
py.setup_sleep(10)
py.go_to_sleep()
"""
```

## Alternative Libraries

* [micropyGPS](https://github.com/inmcm/micropyGPS)
* [Alternative L76GNSS module](https://github.com/andrethemac/L76GLNSV4/blob/master/L76GNSV4.py)