---
title: "PyShields"
---

The following shields offer additional functionality through sensors and other peripherals:
* Pysense
* Pysense 2.0 X
* Pytrack
* Pytrack 2.0 X
* Pyscan

These libraries are available from the [GitHub releases](https://github.com/pycom/pycom-libraries/releases) and not built directly into the firmware. You can use the Libraries with the first and second version of the Pysense, Pytrack and Pyscan. You can also download individual libraries from our [Github repository](https://github.com/pycom/pycom-libraries/).

The API pages are separated per sensor. On the first hardware version of the pyshields, the `pycoproc` is used. For the second version, we use `pycoproc2`.

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
