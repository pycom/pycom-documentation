---
title: "Shields"
---

The API pages in this section explain the additional functionality offered by the following shields:
* Pysense
* Pysense 2.0 X
* Pytrack
* Pytrack 2.0 X
* Pyscan

Note that this functionality is not built into the firmware, and you will need to download additional libraries from our [Github libraries repository](https://github.com/pycom/pycom-libraries/tree/master/shields).

The API pages are separated per sensor:
* [Accelerometer](lis2hh12/) (LIS2HH12)
* [Light Sensor](ltr329als01/) (LTR329ALS01)
* [Temperature Sensor](si7005a20/) (SI7006A20)
* [Pressure Sensor](mpl311a2/) (MPL3115A2)
* [RFID / NFC](mfrc630/) (MFRC630)
* [GPS](l76gnss/) (L76GNSS)

Next to that, you will need either one of the supporting files needed to operate the shield:
* [Pycoproc](pycoproc/) - used on the first version of the Shields
* [Pycoproc2](pycoproc2/) - used on the second version of the Shields

## Uploading the Libraries to a Device

Place the applicable Python files for your shield into the `/lib` folder of your project. Do not forget to press `upload project to device` in Pymakr to make sure you are able to use them.

## Importing and using the libraries

Once the libraries are uploaded to the device, they can be used/imported as a typical MicroPython library would be. For example, importing and using the light sensor on the Pysense:

```python

from pycoproc import Pycoproc
from LTR329ALS01 import LTR329ALS01

py = Pycoproc()
lt = LTR329ALS01(py)

print(lt.light())
```
