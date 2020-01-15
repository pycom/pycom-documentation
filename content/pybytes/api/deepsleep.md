---
title: "Pybytes library API"
aliases:
  - pybytes/api/deepsleep
---

**Deepsleep**
----
  Start deepsleep mode for the given period

**Method**
----
**pybytes.deepsleep(ms, pins, mode, enable_pull)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| ms   | Sleep period in ms  | Yes   | - |
| pins   | Affected pins  | No   | None |
| mode   | Sleep mode TBD  | No   | None |
| enable_pull   | Enable pull  | No   | None |

**Example**
----
pybytes.deepsleep(1000)


**Success Response**
----
After sleep, device reconnect

    >> Connecting with SSID and PASSWORD
     >> WiFi connection established
