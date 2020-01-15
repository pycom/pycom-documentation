---
title: "Pybytes library API"
aliases:
  - pybytes/api/export_config
---

**Export configuration file**
----
  Exports configuration file at specified path.

**Method**
----
**pybytes.export_config(file)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| file   | File Path  | No   | /flash/pybytes_config.json  |

**Example**
----
`pybytes.export_config()`

**Success Response**
`Pybytes configuration exported to /flash/pybytes_config.json`
