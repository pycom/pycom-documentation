---
title: "Get configuration"
aliases:
  - pybytes/api/get_config
---

  Returns configuration data.

**Method**
----
**pybytes.get_config(key)**

**Parameters**
----
| name  | Description   | is Required    | Default value
| ------------- |:-------------:|:-------------:|:-------------:|
| Key   | Returns a specific key-value  | No   | None  |

**Example**
----
`pybytes.get_config()`

**Success Response**
----

```json
{
	'ssl': True,
	'wifi': {
		'ssid': 'SSID',
		'password': 'PASSWORD'
	},
	'lte': {
		'apn': 'internet',
		'cid': 1,
		'reset': False,
		'carrier': 'Standard',
		'band': 3,
		'type': 'IP'
	},
	'username': 'user@email.com',
	'network_preferences': ['lte', 'lora_otaa'],
	'cfg_msg': 'Pybytes configuration read from /flash/pybytes_config.json',
	'dump_ca': True,
	'wlan_antenna': 0,
	'server': '10.0.0.61',
	'lora': {
		'otaa': {
			'app_key': '87c8105c151f885bc19ccb9484fe8185',
			'app_device_eui': '909d7afb9b82c0f6',
			'app_eui': '70B3D57ED000AFA0'
		}
	},
	'ota_server': {
		'port': 443,
		'domain': 'software.pycom.io'
	},
	'pybytes_autostart': True,
	'ssl_params': {
		'ca_certs': '/flash/cert/pycom-ca.pem'
	},
	'device_id': '139e95ed-7213-406b-b07a-a54bfbf021c8'
}
```
