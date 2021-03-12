---
title: "Sensing"
---
The Pysense has a variety of sensors available:
* Accelerometer
* Light sensor
* Temperature / Humidity sensor
* Pressure / Altitude sensor

Lets make use of all of them:
```python
import time
import pycom
import machine

from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE

pycom.heartbeat(False)
pycom.rgbled(0x0A0A08) # white

py = Pycoproc()

alt = MPL3115A2(py,mode=ALTITUDE) # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals
print("MPL3115A2 temperature: " + str(alt.temperature()))
print("Altitude: " + str(alt.altitude()))
pres = MPL3115A2(py,mode=PRESSURE) # Returns pressure in Pa. Mode may also be set to ALTITUDE, returning a value in meters
print("Pressure: " + str(press.pressure()))
# send to pybytes


dht = SI7006A20(py)
print("Temperature: " + str(dht.temperature())+ " deg C and Relative Humidity: " + str(dht.humidity()) + " %RH")
print("Dew point: "+ str(dht.dew_point()) + " deg C")
#change to your ambient temperature
t_ambient = 24.4
print("Humidity Ambient for " + str(t_ambient) + " deg C is " + str(dht.humid_ambient(t_ambient)) + "%RH")


li = LTR329ALS01(py)
print("Light (channel Blue lux, channel Red lux): " + str(li.light()))

acc = LIS2HH12(py)
print("Acceleration: " + str(acc.acceleration()))
print("Roll: " + str(acc.roll()))
print("Pitch: " + str(acc.pitch()))

print("Battery voltage: " + str(py.read_battery_voltage()))
```