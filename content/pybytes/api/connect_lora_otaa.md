---
title: "Pybytes library API"
aliases:
  - pybytes/api/connect_lora_otaa
---

**Connect LoRa OTAA**
----
  Initialize LoRa OTAA connection.

**Method**
----
**pybytes.connect_lora_otaa(timeout, nanogateway)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| timeout   | Connection timeout  | Yes   | - |
| nanogateway   | TBD  | Yes  | - |

**Example**
----
`pybytes.connect_lora_otaa(timeout=15, nanogateway=False)`

**Success Response**
----
    >> Trying to join LoRa.OTAA for 15 seconds...
     >> Setting up LoRa socket...
     >> Connected using LoRa
