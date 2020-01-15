---
title: "Pybytes library API"
aliases:
  - pybytes/api/set_config
---

**Set configuration**
----
  Set device configuration.

**Method**
----
**pybytes.set_config(key, value, permanent, silent, reconnect)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| key   | key  | Yes   | None |
| value   | value  | No   | None |
| permanent   | boolean  | No   | True |
| silent   | boolean  | No   | False |
| reconnect   | boolean  | No   | False |

**Example**
----
`pybytes.set_config(key=None, value=None, permanent=True, silent=False, reconnect=False)`

**Success Response**
TBD
