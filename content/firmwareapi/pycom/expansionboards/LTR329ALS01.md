---
Title: "Ambient Light sensor"
---

The LTR329ALS01 is a dual light sensor that provides outputs for external light levels in lux. See the datasheet for more information about the wavelengths of the two sensors.

### Constructors

### class LTR329ALS01(pycoproc = None, sda = 'P22', scl = 'P21', gain = LTR329ALS01.ALS_GAIN_1X, integration = LTR329ALS01.ALS_INT_100, rate = LTR329ALS01.ALS_RATE_500)

Creates a LTR329ALS01 object. Constructor must be passed a Pycoproc or I2C object to successfully construct. The additional arguments are:
* `gain`: The light sensor ADC gain. see the Constants for values
* `integration`: Controls the integration time of the periodic measurement. See the Constants for values
* `rate`: The used sample rate in ms, must be set larger than the integration period. See the Constants for values

## Methods

### LTR329ALS01.light()

Read the light levels of both light sensors. Returns a tuple with two values for light levels: `(blue, red)`, between 0-65535.

### LTR329ALS01.lux()

Calculate the illuminance using the readings of the light sensor. Returns a single value in lux.

## Constants

The following arguments may be passed into the constructor.

* gain: `ALS_GAIN_1X`,`ALS_GAIN_2X`, `ALS_GAIN_4X`, `ALS_GAIN_8X`, `ALS_GAIN_48X`, `ALS_GAIN_96X`
* integration: `ALS_INT_50`, `ALS_INT_100`, `ALS_INT_150`, `ALS_INT_200`, `ALS_INT_250`, `ALS_INT_300`, `ALS_INT_350`, `ALS_INT_400`
* rate: `ALS_RATE_50`, `ALS_RATE_100`, `ALS_RATE_200`, `ALS_RATE_500`, `ALS_RATE_1000`, `ALS_RATE_2000`