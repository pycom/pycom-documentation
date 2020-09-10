## Device Settings

### What do you need for the machine learning data acquisition and testing:

To make the data acquisition you need a Pycom device + a Pysense or a Pytrack.

You also need to update the device firmware to the latest version - v1.20.2.r1

The Pysense and Pytrack require libraries, please upload the **pycoproc.py**, **LIS2HH12.py** to the device repository **lib/**. In case of Pysense upload the **pysense.py** in case of Pytrack upload **pytrack.py**.
Those libraries can be find in [**Pycom Libraries**](https://github.com/pycom/pycom-libraries).

Check this link to learn how to create the machine learning model in Pybytes [**Model features**](/pybytes/mlintegration/modelcreation)
