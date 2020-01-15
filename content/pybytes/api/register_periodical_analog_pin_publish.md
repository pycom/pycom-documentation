---
title: "Pybytes library API"
aliases:
  - pybytes/api/register_periodical_analog_pin_publish
---

**Register periodical analog pin publish**
----
  Publish periodically on the given analog pin.

**Method**
----
**pybytes.register_periodical_analog_pin_publish(persistent, pin_number, period)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| persistent   | Bool  | No   | False  |
| pin number   | Analog pin number  TBD| Yes   | -  |
| period   | Interval in seconds  | Yes   | -  |

**Example**
----
`pybytes.register_periodical_analog_pin_publish(False, 13, 2)`

**Success Response**
TBD
