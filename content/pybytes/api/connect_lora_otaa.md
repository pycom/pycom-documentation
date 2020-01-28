---
title: "Connect LoRa OTAA"
aliases:
  - pybytes/api/connect_lora_otaa
---

  Initialize LoRa OTAA connection.

**Method**
----
**pybytes.connect_lora_otaa(timeout, nanogateway)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| timeout   | Connection timeout  | Yes   | - |
| nanogateway   | Enable nanogateway  | Yes  | - |

**Example**
----
`pybytes.connect_lora_otaa(timeout=15, nanogateway=False)`

**Success Response**
----

```
>> Trying to join LoRa.OTAA for 15 seconds...
>>  Setting up LoRa socket...
>>  Connected using LoRa
```
