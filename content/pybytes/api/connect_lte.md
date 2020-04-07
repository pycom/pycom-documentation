---
title: "Connect LTE"
aliases:
  - pybytes/api/connect_lte
---

  Initialize watchdog for WiFi and LTE connection.

**Method**
----
**pybytes.connect_lte(reconnect=True, check_interval=0.5)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| reconnect   | Boolean  | Yes   | - |
| check_interval   | interval in seconds  | Yes  | - |

**Example**
----
`pybytes.connect_lte(reconnect=True, check_interval=0.5)`

**Success Response**
----

```
>> LTE connection established
```
