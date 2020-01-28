---
title: "Enable SSL"
aliases:
  - pybytes/api/enable_ssl
---

  Enable SSL

**Method**
----
**pybytes.enable_ssl(ca_file, dump_ca)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| ca_file   | File Path  | No   | /flash/cert/pycom-ca.pem  |
| dump_ca   | Dump_ca  | No   | Yes  |

**Example**
----
`pybytes.enable_ssl('/flash/cert/pycom-ca.pem', True)`

**Success Response**
----

```
>> Please reset your module to apply the new settings
```
