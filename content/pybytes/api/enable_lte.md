---
title: "Enable LTE"
aliases:
  - pybytes/api/enable_lte
---

  Enable LTE connection

**Method**
----
**pybytes.enable_lte(carrier, cid, band, apn, type, reset, fallback)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| carrier   | Carrier  | No   | None  |
| cid   | Cid  | No   | None  |
| band   | Band  | No   | None  |
| apn   | APN  | No   | None  |
| type   | Type  | No   | None  |
| reset   | Reset  | No   | None  |
| fallback   | If **True** extends network preferences with the given LTE information| No   | False  |

**Example**
----
`pybytes.enable_lte('standard', 1, 8, 'soracom.io', 'IP', False)`

**Success Response**
----

```
>> Pybytes configuration written to /flash/pybytes_config.json
>> Watchdog timeout has been increased to 2147483647 ms
>> Initialized watchdog for WiFi and LTE connection with timeout 1260000 ms
```
