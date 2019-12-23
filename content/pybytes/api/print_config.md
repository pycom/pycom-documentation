---
title: "Pybytes library API"
aliases:
  - pybytes/api/print_config
---

**Print config**
----
  Prints current configuration in the terminal


**Method**
----
**pybytes.print_config()**

**Example**
----
`pybytes.print_config()`

## Success Response
    ssl = True
    wifi = {'ssid': '', 'password': ''}
    lte = {'apn': 'internet', 'cid': 1, 'reset': False, 'carrier': 'Standard', 'band': 3, 'type': 'IP'}
    username = alipsilv@hotmail.com
    network_preferences = ['lte', 'lte', 'lte', 'lora_otaa']
    cfg_msg = Pybytes configuration read from /flash/pybytes_config.json
    dump_ca = True
    wlan_antenna = 0
    server = 10.0.0.61
    lora = {'otaa': {'app_key': '87c8105c151f885bc19ccb9484fe8185', 'app_device_eui': '909d7afb9b82c0f6', 'app_eui': '70B3D57ED000AFA0'}}
    ota_server = {'port': 443, 'domain': 'software.pycom.io'}
    pybytes_autostart = True
    ssl_params = {'ca_certs': '/flash/cert/pycom-ca.pem'}
    device_id = 139e95ed-7213-406b-b07a-a54bfbf021c8
