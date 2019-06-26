---
title: "Pysense"
aliases:
    - pytrackpysense/apireference/pysense.html
    - pytrackpysense/apireference/pysense.md
    - chapter/pytrackpysense/apireference/pysense
---

This chapter describes the various libraries which are designed for the Pysense board. This includes details about the various methods and classes available for each of the Pysense's sensors.

## 3-Axis Accelerometer (LIS2HH12)

Pysense has a 3-Axis Accelerometer that provides outputs for acceleration as well as roll, pitch and yaw.

### Constructors

#### class LIS2HH12(pysense = None, sda = 'P22', scl = 'P21')

Creates a `LIS2HH12` object, that will return values for acceleration, roll, pitch and yaw. Constructor must be passed a Pysense or I2C object to successfully construct.

### Methods

#### LIS2HH12.acceleration()

Read the acceleration from the `LIS2HH12`. Returns a **tuple** with the 3 values of acceleration (G).

#### LIS2HH12.roll()

Read the current roll from the `LIS2HH12`. Returns a **float** in degrees in the range -180 to 180.

#### LIS2HH12.pitch()

Read the current pitch from the `LIS2HH12`. Returns a **float** in degrees in the range -90 to 90. Once the board tilts beyond this range the values will repeat. This is due to a lack of yaw measurement, making it not possible to know the exact orientation of the board.

## Digital Ambient Light Sensor (LTR-329ALS-01)

Pysense has a dual light sensor that provides outputs for external light levels in lux. See the datasheet for more information about the wavelengths of the two sensors.

### Constructors

#### class LTR329ALS01(pysense = None, sda = 'P22', scl = 'P21', gain = ALS\_GAIN\_1X, integration = ALS\_INT\_100, rate = ALS\_RATE\_500)

Creates a `LTR329ALS01` object, that will return values for light in lux. Constructor must be passed a Pysense or I2C object to successfully construct.

### Methods

#### LTR329ALS01.light()

Read the light levels of both `LTR329ALS01` sensors. Returns a **tuple** with two values for light levels in lux.

### Arguments

The following arguments may be passed into the constructor.

* gain: `ALS_GAIN_1X`,`ALS_GAIN_2X`, `ALS_GAIN_4X`, `ALS_GAIN_8X`, `ALS_GAIN_48X`, `ALS_GAIN_96X`
* integration: `ALS_INT_50`, `ALS_INT_100`, `ALS_INT_150`, `ALS_INT_200`, `ALS_INT_250`, `ALS_INT_300`, `ALS_INT_350`, `ALS_INT_400`
* rate: `ALS_RATE_50`, `ALS_RATE_100`, `ALS_RATE_200`, `ALS_RATE_500`, `ALS_RATE_1000`, `ALS_RATE_2000`

## Humidity and Temperature Sensor (SI7006A20)

Pysense has a Humidity and Temperature sensor that provides values of relative humidity and external temperature.

### Constructors

#### class SI7006A20(pysense = None, sda = 'P22', scl = 'P21')

Creates a `SI7006A20` object, that will return values for humidity (%) and temperature ('C). Constructor must be passed a Pysense or I2C object to successfully construct.

### Methods

#### SI7006A20.humidity()

Read the relative humidity of the `SI7006A20`. Returns a **float** with the percentage relative humidity.

#### SI7006A20.temperature()

Read the external temperature of the `SI7006A20`. Returns a **float** with the temperature.

## Barometric Pressure Sensor with Altimeter (MPL3115A2)

Pysense has a Barometric Pressure sensor that provides readings for pressure, altitude as well as an additional temperature sensor.

### Constructors

#### class MPL3115A2(pysense = None, sda = 'P22', scl = 'P21', mode = PRESSURE)

Creates a `MPL3115A2` object, that will return values for pressure (Pa), altitude (m) and temperature ('C). Constructor must be passed a Pysense or I2C object to successfully construct.

### Methods

#### MPL3115A2.pressure()

Read the atmospheric pressure of the `MPL3115A2`. Returns a **float** with the pressure in (Pa).

#### MPL3115A2.altitude()

Read the altitude of the `MPL3115A2`. Returns a **float** with the altitude in (m).

#### MPL3115A2.temperature()

Read the temperature of the `MPL3115A2`. Returns a **float** with the temperature in ('C).

### Arguments

The following arguments may be passed into the constructor.

* mode: `PRESSURE`, `ALTITUDE`

{{% hint style="info" %}}
Please note that more functionality is being added weekly to these libraries. If a required feature is not available, feel free to contribute with a pull request at the [Libraries GitHub repository](https://github.com/pycom/pycom-libraries)
{{< /hint >}}

