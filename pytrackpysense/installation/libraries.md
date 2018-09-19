# Installing Libraries

To utilise the sensors on the Pytrack and Pysense, Pycom has written libraries to make reading to/from the various sensors accessible via an API. These libraries reside at the Pycom GitHub repository and the latest versions can be found under the releases page.

[GitHub Repository](https://github.com/pycom/pycom-libraries)

Download the repository as a `.zip` file, navigate to the correct device \(Pysense/Pytrack\), extract the files and then upload the desired files to the device in the instructions below.

## Uploading the Libraries to a Device

These libraries should be uploaded to a device \(LoPy, SiPy, WiPy 2.0, etc.\) in the same process as a standard MicroPython library. The various `.py` files should be placed into the `/lib` folder on the device. For example, if using the Pysense and the user wishes to enable the only Accelerometer and the Light Sensor, they should place the following `.py` files into the device's `/lib` folder:

```text
- pysense.py
- LIS2HH12.py
- LTR329ALS01.py
```

Add as many or as few of the libraries that are required.

In addition to the Pysense or Pytrack specific libraries, you also need to upload the `pycoproc.py` file from the `_lib/pycoproc_` folder inside the libraries archive.

{% hint style="info" %}
The Pytrack and Pysense boards behave the same as the Expansion Board. `Upload`, `Run` and upload code to Pycom modules via the Pymakr Plugin, in exactly the same process.
{% endhint %}

## Importing/Using the Libraries

Once the libraries are uploaded to the device, they can be used/imported as a typical MicroPython library would be. For example, importing and using the light sensor on the Pysense:

```python
from pysense import Pysense
from LTR329ALS01 import LTR329ALS01

py = Pysense()
lt = LTR329ALS01(py)

print(lt.light())
```

