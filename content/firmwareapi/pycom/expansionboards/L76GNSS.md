---
Title: "GPS"
---

The L76GNSS is the GPS module that can provide location data to your application.

## Constructors

### class L76GNSS(pytrack = None, sda = 'P22', scl = 'P21', timeout = None)

Creates a L76GNSS object. Constructor must be passed a Pytrack or I2C object to successfully construct. Set the `timeout` to a period in seconds for the GPS to search for a lock. If a lock is not found by the time the `timeout` has expired, the `coordinates` method will return `(None, None)`.

## Methods

### L76GNSS.coordinates(debug = False)

Read the longitude and latitude from the `L76GNSS`. Returns a tuple with `(longitude, latitude)`. With `debug` set to `True` the output from the GPS is verbose.

### L76GNSS.dump_nmea()

Continuously print nmea sentences received from the `L76GNSS` to the REPL. This is useful if you want to use a graphical tool over UART to visualise GPS reception

### L76GNSS.write()

Send commands to the `L76GNSS`. See the datasheet of the L76 for more information. Be aware that some commands might break the communication interface.
