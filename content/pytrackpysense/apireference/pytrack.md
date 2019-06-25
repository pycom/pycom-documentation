---
title: "Pytrack"
aliases:
    - pytrackpysense/apireference/pytrack.html
    - pytrackpysense/apireference/pytrack.md
    - chapter/pytrackpysense/apireference/pytrack
---

This chapter describes the various libraries which are designed for the Pytrack board. This includes details about the various methods and classes available for each of the Pytrack's sensors.

## 3-Axis Accelerometer (LIS2HH12)

Pytrack has a 3-Axis Accelerometer that provides outputs for acceleration as well as roll, pitch and yaw.

### Constructors

#### class LIS2HH12(pytrack = None, sda = 'P22', scl = 'P21')

Creates a `LIS2HH12` object, that will return values for acceleration, roll, pitch and yaw. Constructor must be passed a Pytrack or I2C object to successfully construct.

### Methods

#### LIS2HH12.acceleration()

Read the acceleration from the `LIS2HH12`. Returns a **tuple** with the 3 values of acceleration (G).

#### LIS2HH12.roll()

Read the current roll from the `LIS2HH12`. Returns a **float** in degrees in the range -180 to 180.

#### LIS2HH12.pitch()

Read the current pitch from the `LIS2HH12`. Returns a **float** in degrees in the range -90 to 90. Once the board tilts beyond this range the values will repeat. This is due to a lack of yaw measurement, making it not possible to know the exact orientation of the board.

## GPS with GLONASS (Quectel L76-L GNSS)

Pytrack has a GPS (with GLONASS) that provides outputs longitude/latitude, speed and other information about the Pytrack's location.

### Constructors

#### class L76GNSS(pytrack = None, sda = 'P22', scl = 'P21', timeout = None)

Creates a `L76GNSS` object, that will return values for longitude and latitude. Constructor must be passed a Pytrack or I2C object to successfully construct. Set the `timeout` to a time period (in seconds) for the GPS to search for a lock. If a lock is not found by the time the `timeout` has expired, the `coordinates` method will return `(None, None)`.

### Methods

#### L76GNSS.coordinates(debug = False)

Read the longitude and latitude from the `L76GNSS`. Returns a **tuple** with the longitude and latitude. With `debug` set to `True` the output from the GPS is verbose.

{{% hint style="info" %}}
Please note that more functionality is being added weekly to these libraries. If a required feature is not available, feel free to contribute with a pull request at the [Libraries GitHub repository](https://github.com/pycom/pycom-libraries)
{{< /hint >}}

