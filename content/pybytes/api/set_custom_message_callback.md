---
title: "Send custom message callback"
aliases:
  - pybytes/api/set_custom_message_callback
---

  Send custom message callback.

**Method**
----
**pybytes.set_custom_message_callback(callback)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| callback   | function | Yes   | -  |

**Example**
----
`pybytes.set_custom_message_callback(print("Hello Pycom!"))`

**Success Response**
----

```
>> Hello Pycom!
```
