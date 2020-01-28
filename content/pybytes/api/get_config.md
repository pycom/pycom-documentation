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
		'apn': 'apn',
		'cid': 999,
		'reset': False,
		'carrier': 'carrier',
		'band': 999,
		'type': 'type'
	},
	'username': 'user@email.com',
	'network_preferences': ['lte', 'lora_otaa'],
	'cfg_msg': 'Pybytes configuration read from file.json',
	'dump_ca': True,
	'wlan_antenna': 0,
	'server': 'xx.x.x.xx',
	'lora': {
		'otaa': {
			'app_key': 'app_key',
			'app_device_eui': 'app_device_eui',
			'app_eui': 'app_eui'
		}
	},
	'ota_server': {
		'port': 999,
		'domain': 'software.pycom.io'
	},
	'pybytes_autostart': True,
	'ssl_params': {
		'ca_certs': 'ca_certs'
	},
	'device_id': 'device_id'
}
```
