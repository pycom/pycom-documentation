---
title: "Pybytes library API"
aliases:
  - pybytes/api/send_digital_pin_value
---

**Send analog pin value**
----
  Send analog pin value

**Method**
----
**pybytes.send_digital_pin_value(persistent, pin_number, pull_mode)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| persistent   | Bool  | No   | False  |
| pin number   | Analog pin number  TBD| Yes   | -  |
| pull mode   | PULL_UP or TBD  | Yes   | PULL_UP  |

**Example**
----
`pybytes.send_digital_pin_value(False, 12, Pin.PULL_UP)`

**Success Response**
TBD
