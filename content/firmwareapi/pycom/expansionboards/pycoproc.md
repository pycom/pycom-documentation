---
Title: "Pycoproc"
---

The `pycoproc.py` file is a supporting python library for the Pysense, Pytrack and Pyscan expansionboards.

## Pytrack class to control supervisor MCU

### Constructors

#### class Pytrack(i2c=None, sda='P22', scl='P21')

Initialise I2C communication with the supervisor MCU

### Methods

#### Pytrack.sd_power(enabled=True)

This command allows switching the power supply for the SD card (VCC + PullUP resistors).

#### Pytrack.sensor_power(enabled=True)

This command allows switching the power supply for the GPS module and any sensors connected through the external 6-pin connector.

#### Pytrack.gps_standby(enabled=True)

This command allows switching the GPS module into stand-by mode. The GPS module is no longer accessible via I2C in this case.
