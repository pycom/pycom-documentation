---
title: "Product info & Datasheets"
aliases:
    - firmwareapi/introduction.html
    - firmwareapi/introduction.md
    - product-info
    - chapter/firmwareapi
---
As the development for these devices are on going with additional features being added, every week, it is essential to ensure you frequently check for updates on the Pytrack/Pysense/Pyscan. As well as updating the device firmware, it is important to check the [GitHub repository](https://github.com/pycom/pycom-libraries) for the respective library files as they as also being updated, to include additional features/functionality.

> Please note that updated libraries are available for the Pytrack 2.0 X and Pysense 2.0 X in the pytrack-2 and pysense-2 directories on GitHub.
These new libraries will allow you to use the new additional features.

## Uploading the Libraries to a Device

These libraries should be uploaded to a device in the same process as a standard MicroPython library. The various `.py` files should be placed into the `/lib` folder on the device. 

Add as many or as few of the libraries that are required.

In addition to the Pysense or Pytrack specific libraries, for hardware version 1.x boards you also need to upload the `pycoproc.py` file from the `lib/pycoproc` folder inside the libraries archive. For the Pytrack 2.0 X and Pysense 2.0 X, the pycoproc.py file is included in the pytrack-2 and pysense-2 directories to avoid confusion over which library to use.

For example, if using the Pysense and the user wishes to enable the only Accelerometer and the Light Sensor, they should place the following `.py` files into the device's `/lib` folder:

```text
- pysense.py
- pycoproc.py
- LIS2HH12.py
- LTR329ALS01.py
```

## Importing/Using the Libraries

Once the libraries are uploaded to the device, they can be used/imported as a typical MicroPython library would be. For example, importing and using the light sensor on the Pysense:

```python

from pysense import Pysense
from LTR329ALS01 import LTR329ALS01

py = Pysense()
lt = LTR329ALS01(py)

print(lt.light())
```
