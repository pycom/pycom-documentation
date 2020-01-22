---
title: "Print config"
aliases:
  - pybytes/api/print_config
---

  Prints current configuration in the terminal.

**Method**
----
**pybytes.print_config()**

**Example**
----
`pybytes.print_config()`

**Success Response**
----

```
>> ssl = True
>>  wifi = {'ssid': '', 'password': ''}
>>  lte = {'apn': 'apn', 'cid': 999, 'reset': False, 'carrier': 'carrier', 'band': 999, 'type': 'type'}
>>  username = user@email.com
>>  network_preferences = ['lte', 'lte', 'lte', 'lora_otaa']
>>  cfg_msg = Pybytes configuration read from file.json
>>  dump_ca = True
>>  wlan_antenna = 0
>>  server = xx.x.x.xx
>>  lora = {'otaa': {'app_key': 'app_key', 'app_device_eui': 'app_device_eui', 'app_eui': 'app_eui'}}
>>  ota_server = {'port': 000, 'domain': 'domain.com'}
>>  pybytes_autostart = True
>>  ssl_params = {'ca_certs': 'ca_certs'}
>>  device_id = device_id
```
