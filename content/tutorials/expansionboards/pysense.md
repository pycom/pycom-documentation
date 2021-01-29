---
title: "Pysense Examples"
aliases:
    - tutorials/pysense.html
    - tutorials/pysense.md
    - chapter/tutorials/pysense
---
The Pysense board includes 4 additional sensors to be used with your pycom device! You can find an example on how to use the sensors below, but first we need to install the libraries. You can find more information about the Pysense and its sensors in the [datasheet section](/datasheets/expansionboards/pysense/)

## Install libraries
To use the Pysense board, you will first need to add some libraries to your project: 
1. Go the the [GitHub repository](https://github.com/pycom/pycom-libraries/) and download the archive. 
2. Extract the archive and copy the files from the pysense folder into your project folder
3. Upload the project to your device. This will enable the functionality. 

## Use sensors
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

# See https://docs.pycom.io for more information regarding library specifics

import time
import pycom
from pysense import Pysense
import machine

from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE

pycom.heartbeat(False)
pycom.rgbled(0x0A0A08) # white

py = Pysense()

mp = MPL3115A2(py,mode=ALTITUDE) # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals
print("MPL3115A2 temperature: " + str(mp.temperature()))
print("Altitude: " + str(mp.altitude()))
mpp = MPL3115A2(py,mode=PRESSURE) # Returns pressure in Pa. Mode may also be set to ALTITUDE, returning a value in meters
print("Pressure: " + str(mpp.pressure()))


si = SI7006A20(py)
print("Temperature: " + str(si.temperature())+ " deg C and Relative Humidity: " + str(si.humidity()) + " %RH")
print("Dew point: "+ str(si.dew_point()) + " deg C")
t_ambient = 24.4
print("Humidity Ambient for " + str(t_ambient) + " deg C is " + str(si.humid_ambient(t_ambient)) + "%RH")


lt = LTR329ALS01(py)
print("Light (channel Blue lux, channel Red lux): " + str(lt.light()))

li = LIS2HH12(py)
print("Acceleration: " + str(li.acceleration()))
print("Roll: " + str(li.roll()))
print("Pitch: " + str(li.pitch()))

print("Battery voltage: " + str(py.read_battery_voltage()))

time.sleep(3)
py.setup_sleep(10)
py.go_to_sleep()
```
## Accelerometer example

This basic example shows how to read pitch and roll from the on-board accelerometer and output it in comma separated value (CSV) format over serial.

```python

from LIS2HH12 import LIS2HH12
from pytrack import Pytrack
py = Pytrack()
acc = LIS2HH12()

while True:
   pitch = acc.pitch()
   roll = acc.roll()
   print('{},{}'.format(pitch, roll))
   time.sleep_ms(100)
```

>Note: Use [Processing](https://processing.org/) to visualize the orientation of your board using the example. You can find the Processing sketch [here](https://github.com/pycom/pycom-libraries/tree/master/examples/pytrack_pysense_accelerometer)
>
>![](/gitbook/assets/accelerometer_visualiser.png)

