---
Title: "Accelerometer"
---

The LIS2HH12 is a 3-Axis Accelerometer provides outputs for acceleration, roll and pitch

## Constructors

### class LIS2HH12(pycoproc = None, sda = 'P22', scl = 'P21')

Creates a LIS2HH12 object. Constructor must be passed a Pycoproc or I2C object to successfully construct.

## Methods

### LIS2HH12.acceleration()

Read the acceleration from the accelerometer. Returns a tuple with the 3 values of acceleration in g-force: `(x, y, z)`.

### LIS2HH12.roll()

Read the current roll from the accelerometer. Returns a float in degrees in the range -180 to 180.

### LIS2HH12.pitch()

Read the current pitch from the accelerometer. Returns a float in degrees in the range -90 to 90. Once the board tilts beyond this range the values will repeat. This is due to a lack of yaw measurement, making it not possible to know the exact orientation of the board.

### LIS2HH12.enable_activity_interrupt(threshold, duration, handler=None)

Set an activity- and inactivity interrupt for the accelerometer. This takes the arguments:
* `threshold`: the activity threshold in `mg`, between  62 - 4000
* `duration`: the duration in `ms`, between 160 - 40800
* `handler`: The interrupt handler. When not given, it will print `Activity interrupt` and `Inactivity interrupt`
The function returns a tuple containing the set values: `(threshold, duration)`. These depend on the resolution.


