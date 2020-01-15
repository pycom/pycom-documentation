---
title: "Pybytes library API"
aliases:
  - pybytes/api/write_config
---

**Update configuration**
----
  Update device configuration.

**Method**
----
**pybytes.write_config(file='/flash/pybytes_config.json', silent=False)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| file   | File path  | Yes   | '/flash/pybytes_config.json' |
| silent   | boolean  | No   | False |

**Example**
----
`pybytes.write_config(file='/flash/pybytes_config.json', silent=False)`

**Success Response**

    >> Pybytes configuration written to /flash/pybytes_config.json
