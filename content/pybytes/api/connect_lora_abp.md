---
title: "Pybytes library API"
aliases:
  - pybytes/api/connect_lora_abp
---

**Connect LoRa ABP**
----
  Initialize LoRa ABP connection.

**Method**
----
**pybytes.connect_lora_abp(timeout, nanogateway)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| timeout   | Connection timeout  | Yes   | - |
| nanogateway   | TBD  | Yes  | - |

**Example**
----
`pybytes.connect_lora_abp(15000, false)`

**Success Response**
----
    >> Trying to join LoRa.ABP for 15000 seconds...
     >> Setting up LoRa socket...
     >> Connected using LoRa
