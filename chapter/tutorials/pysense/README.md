# Sensor Demos

## Accelerometer

This basic example shows how to read pitch and roll from the on-board accelerometer and output it in comma separated value \(CSV\) format over serial.

```py
from LIS2HH12 import LIS2HH12
from pytrack import Pytrack
py = Pytrack()
acc = LIS2HH12()

while True:
   pitch = acc.pitch()
   roll = acc.roll()
   print('{},{}'.format(pitch,roll))
   time.sleep_ms(100)
```

<p align="center"><img src ="../../../img/accelerometer_visualiser.png" width="400"></p>

If you want to visualise the data output by this script a Processing sketch is available [here](https://github.com/pycom/pycom-libraries/tree/master/examples/pytrack_pysense_accelerometer) that will show the board orientation in 3D.
