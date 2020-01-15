---
title: "Pybytes library API"
aliases:
  - pybytes/api/register_periodical_digital_pin_publish
---

**Register periodical digital pin publish**
----
  Publish periodically on the given digital pin.


**Method**
----
**pybytes.register_periodical_digital_pin_publish(persistent, pin_number, pull_mode, period)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| persistent   | Bool  | No   | False  |
| pin number   | Analog pin number  | Yes   | -  |
| pull mode   | PULL_UP or TBD  | Yes   | PULL_UP  |
| period   | Interval in seconds  | Yes   | -  |

**Example**
----
`pybytes.register_periodical_digital_pin_publish(False, PIN_NUMBER, Pin.PULL_UP, 2)`

**Success Response**
TBD
