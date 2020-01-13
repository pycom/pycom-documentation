---
title: "Pybytes library API"
aliases:
  - pybytes/api/enable_lte
---

**Enable LTE**
----
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
| fallback   | Fallbackena  | No   | False  |

**Example**
----
`pybytes.enable_lte('Standard', 1, 3, 'internet', 'IP', False)`

**Success Response**
`TBD`
