---
title: "Pybytes library API"
aliases:
  - pybytes/api/dump_ca
---

**Dump CA**
----
  Make a dump_ca

**Method**
----
**pybytes.dump_ca(ca_file)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| ca_file   | File path  | No   | /flash/cert/pycom-ca.pem  |


**Example**
----
`pybytes.dump_ca(ca_file='/flash/cert/pycom-ca.pem')`

**Success Response**
`Successfully created /flash/cert/pycom-ca.pem`
