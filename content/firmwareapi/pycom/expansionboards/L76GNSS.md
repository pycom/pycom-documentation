---
title: "L76GNSS GPS"
---


## GPS with GLONASS (Quectel L76-L GNSS)

Pytrack has a GPS (with GLONASS) that provides outputs longitude/latitude, speed and other information about the Pytrack's location.

## Constructors

### class L76GNSS(pytrack = None, sda = 'P22', scl = 'P21', timeout = None)

Creates a `L76GNSS` object, that will return values for longitude and latitude. Constructor must be passed a Pytrack or I2C object to successfully construct. Set the `timeout` to a time period (in seconds) for the GPS to search for a lock. If a lock is not found by the time the `timeout` has expired, the `coordinates` method will return `(None, None)`.

## Methods

### L76GNSS.coordinates(debug = False)

Read the longitude and latitude from the `L76GNSS`. Returns a **tuple** with the longitude and latitude. With `debug` set to `True` the output from the GPS is verbose.

{{% hint style="info" %}}
Please note that more functionality is being added weekly to these libraries. If a required feature is not available, feel free to contribute with a pull request at the [Libraries GitHub repository](https://github.com/pycom/pycom-libraries)
{{% /hint %}}