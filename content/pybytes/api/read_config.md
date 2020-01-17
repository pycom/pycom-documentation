---
title: "Read configuration"
aliases:
  - pybytes/api/read_config
---

  Reads configuration from the given file.

**Method**
----
**pybytes.read_config(file', reconnect)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| file   | File Path  | No   | /flash/pybytes_config.json  |
| reconnect   | Reconnect after changes  | No   | False  |

**Example**
----
`pybytes.read_config()`

**Success Response**
----

```
>> Pybytes configuration read from /flash/pybytes_config.json
```
