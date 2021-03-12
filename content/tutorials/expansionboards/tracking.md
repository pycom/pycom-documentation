---
title: "Asset Tracking"
---
Using the Pytrack, you are able to gather location data of your device. In this tutorial, we will go through how to set up your device, such that you can save the data on a SD card. Extending this example with a Pybytes integration on any network will allow you to forward any data to the cloud. 
On this page, we cover the following:
* [Save data to a SD card](#save-data-to-a-sd-card)
* [Forwarding data to Pybytes](#forwarding-data-to-pybytes)
* [Save power](#save-power)

## Save data to a SD card
For this example, you will need to insert a SD card into the Pytrack board to save the data locally. We will get the data every 60 seconds sleep in between.

### main.py

```python
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
from network import WLAN
 
pycom.heartbeat(False)
pycom.rgbled(0x0A0A08) # white
 
time.sleep(2)
gc.enable()
 
py = Pytrack()
 
time.sleep(1)
l76 = L76GNSS(py, timeout=30, buffer=512)
 
# Load SD card
sd = SD()
os.mount(sd, '/sd')
os.listdir('/sd')
 
# Read SD card
print('Reading from file:')
f = open('/sd/test.txt', 'r')
print(f.readlines())
f.close()
print("Read from file.")
 
time.sleep(1)
 
while (True):
    coord = l76.coordinates()
    print("{} - {}".format(coord, gc.mem_free()))
    f = open('/sd/test.txt', 'a') # Append
    f.write("{}".format(coord[1]))
    f.write(' ')
    f.write("{}".format(coord[0]))
    f.write(',\n')
    f.close()
    print('Sleep for 1 minute.')
    time.sleep(60)
```

### Visualizing data
The data in the textfile on the SD card will look like this:
```
latitude, longitude
latitude, longitude
```
We can use this data to make a .kml file, or Keyhole Makrup Language, to display our tracks on for example Google Maps. Use the following format and save the file as a `.kml` file:
```
Placemark>
  <name>Untitled Path</name>
  <LineString>
    <tessellate>1</tessellate>
    <altitudeMode>relativeToGround</altitudeMode>
    <coordinates>
        Paste location data
    </coordinates>
  </LineString>
</Placemark>
```

## Forwarding data to Pybytes

If we take the example above, and modify it such that instead of saving the data to a SD card, we send it to Pybytes. For this, make sure to [provision your device to Pybytes](/pybytes/gettingstarted/). If you already provisioned your device, make sure to start Pybytes from boot. Use the following to replace the loop:

```python
while (True):
    coord = l76.coordinates()
    print("{} - {}".format(coord, gc.mem_free()))
    pybytes.send_signal(1, coord)
    time.sleep(60)
```
Using this, you will see your data show up as signal 1 in Pybytes

##  Save power

Having the GPS enabled continuously on can drain the battery quite quickly. We can put the GPS in standby mode while we deepsleep the module to save some additional power. This will have some drawbacks, as it could take some time to regain the location fix after waking up. Instead of the loop, you could use the following example. If you're looking to wake up from movement on the accelerometer, have a look at the [accelerometer sleep](../sleep/) example.

```python
coord = l76.coordinates()
print("{} - {}".format(coord, gc.mem_free()))
f = open('/sd/test.txt', 'a') # Append
f.write("{}".format(coord[1]))
f.write(' ')
f.write("{}".format(coord[0]))
f.write(',\n')
f.close()
print('Sleep for 1 minute.')
py.setup_sleep() #sleep time in seconds
# Shield version 1
py.go_to_sleep(arguments)
# Shield version 2
py.go_to_sleep(different arguments)
```