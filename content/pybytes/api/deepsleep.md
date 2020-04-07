---
title: "Deepsleep"
aliases:
  - pybytes/api/deepsleep
---

  Start deepsleep mode for the given period

**Method**
----
**pybytes.deepsleep(ms, pins, mode, enable_pull)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| ms   | Sleep period in ms  | Yes   | - |
| pins   | A list or tuple containing the GPIO to setup for deepsleep wakeup  | No   | None |
| mode   | Configure how GPIOs can wake up -> **machine.WAKEUP_ALL_LOW** or **machine.WAKEUP_ANY_HIGH**  | No   | None |
| enable_pull   | If set to **True** keeps the pull up or pull down resistors enabled during deep sleep  | No   | None |

**Example**
----
`>> pybytes.deepsleep(1000)`


**Success Response**
----
After deepsleep, the device reconnects.

```
>> Connecting with SSID and PASSWORD
>>  WiFi connection established
```
