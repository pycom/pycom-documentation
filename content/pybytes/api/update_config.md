---
title: "Pybytes library API"
aliases:
  - pybytes/api/update_config
---

**Update configuration**
----
  Update device configuration

**Method**
----
**pybytes.update_config(key, value, permanent, silent, reconnect)**

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
`pybytes.update_config(key=None, value=None, permanent=True, silent=False, reconnect=False)`

**Success Response**
TBD
