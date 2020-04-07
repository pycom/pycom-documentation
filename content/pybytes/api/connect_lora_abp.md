---
title: "Connect LoRa ABP"
aliases:
  - pybytes/api/connect_lora_abp
---

  Initialize LoRa ABP connection.

**Method**
----
**pybytes.connect_lora_abp(timeout, nanogateway)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| timeout   | Connection timeout  | Yes   | - |
| nanogateway   | Enable nanogateway  | Yes  | - |

**Example**
----
`pybytes.connect_lora_abp(15000, false)`

**Success Response**
----

```
>> Trying to join LoRa.ABP for 15000 seconds...
>>  Setting up LoRa socket...
>>  Connected using LoRa
```
