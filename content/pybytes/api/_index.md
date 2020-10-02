---
title: "Pybytes library API"
aliases:
---


The Pybytes library is positioned in the [frozen](/advance/frozen/) section of the firmware. It can be imported like regular modules:
```python
from _pybytes import Pybytes
pybytes = Pybytes()
```


## Provisioning

### Pybytes.activate(activation string)

Provision the device to Pybytes. Use the `activation string` provided in Pybytes to activate the device.

### pybytes.read_config([filename='/flash/pybytes_config.json', reconnect=False])

Load the Pybytes configuration file. By default, this is found in `/flash/pybytes_config.json`

### pybytes.update_config(key, [value=None, permanent=True, silent=False, reconnect=False])

Update a `key` and `value` of the default configuration file. additional options:
* `permanent`: will call `pybytes.write_config()`. If set `False`, the update will not be stored in the configuration file.
* `silent`: set `silent` parameter of above.
* `reconnect`: calls `pybytes.reconnect()`

### set_config([key=None, value=None, permanent=True, silent=False, reconnect=False])

Same as `update_config(...)`

### pybytes.write_config([file='/flash/pybytes_config.json', silent=False])

Writes the updated configuration to the default configuration file. The parameters:
* `file`: The file name and location
* `silent`: Do not print anything

### pybytes.print_config()

Print the configuration settings to the REPL

## Connection

### pybytes.connect()

Connect the device to Pybytes following the loaded configuration file. You will need to load a configuration file before calling this.

### pybytes.start([autoconnect=True])

Same as `pybytes.connect()`, with the option to not connect


### pybytes.connect_lte()

Connect to Pybytes using LTE and the settings from the configuration file.

### pybytes.connect_wifi([reconnect=True, check_interval=0.5])

Connect to Pybytes using WiFi and the settings from the configuration file. Setting reconnect to `True` will reconnect the WiFi connection once disconnected.

### pybytes.connect_sigfox()

Connect to Pybytes using SigFox and the settings from the configuration file.

### pybytes.connect_lora_otaa([timeout=120, nanogateway=False])

Connect to Pybytes using LoRa OTAA and the settings from the configuration file.

### pybytes.connect_lora_abp([timeout, nanogateway=False])

Connect to Pybytes using LoRa ABP and the settings from the configuration file.

### pybytes.disconnect()

Disconnect from Pybytes gracefully. Closes the MQTT connection and socket.

### pybytes.reconnect()

Calls `pybytes.disconnect()` followed by `pybytes.connect()`

### pybytes.isconnected()

Returns the connection status to Pybytes, can be `True` or `False`.

### pybytes.is_connected()

Same as `pybytes.isconnected()`

### pybytes.enable_ssl()

Enable SSL on the Pybytes connection

### pybytes.dump_ca([file='/flash/cert/pycom-ca.pem'])

Write SSL certificate to file.


## Signals

### pybytes.send_signal(signal_number, value)

Send a signal to Pybytes. Arguments are:
* `signal_number`
* `value`

> This will also work in Pymesh.

### send_digital_pin_value(pin_number, pull_mode)

Similar to `pybytes.send_signal()`. Will send the value of `pin_number` to Pybytes.

### pybytes.send_analog_pin_value()

### pybytes.send_ping_message()

Sends a ping (is-alive) message to Pybytes. 

### pybytes.send_info_message()

Send an info message to Pybytes containing the device type and firmware version.

### pybytes.send_battery_level(battery_level)

Sends the battery level to Pybytes. The argument `battery_level` can be any integer.

### send_custom_message()

### pybytes.send_custom_message(persistent, message_type, message)

Send a custom message to Pybytes. Arguments are:
* `persistent`: Not used, set any value
* `message_type`: 

### pybytes.enable_terminal()

### send_digital_pin_value(persistent, pin_number, pull_mode)
### pybytes.send_analog_pin_value(persistent, pin_number)
### pybytes.send_custom_location(pin, x, y)




send_custom_message             set_custom_message_callback        send_digital_pin_value
send_analog_pin_value           send_node_signal  

register_periodical_digital_pin_publish
register_periodical_analog_pin_publish
add_custom_method               enable_terminal
send_custom_location

    

enable_lte           smart_config
## Sending messages

## Miscellaneous

### pybytes.deepsleep([pins=None, mode=None, enable_pull=None])

See [machine.deepsleep()](/firmwareapi/pycom/machine/#machinedeepsleeptime_ms) for more details. Mode can be:



## Debugging
Enable debugging if you are having any issues.
There are multiple debug levels, the lowest is 0 which is for warnings only and 99 is the highest used and will print more debugging messages

#### use:

```
>> import pycom;
>> pycom.nvs_set('pybytes_debug', debugLevel)
```

#### e.g.
```
>> import pycom;
>> pycom.nvs_set('pybytes_debug', 99)
```    


# API List


* [Activate](activate)

* [Connect](connect_device)

* [Connect LTE](connect_lte)

* [Connect LoRa ABP](connect_lora_abp)

* [Connect LoRa OTAA](connect_lora_otaa)

* [Connect Sigfox](connect_sigfox)

* [Connect Wifi](connect_wifi)

* [Deepsleep](deepsleep)

* [Disconnect](disconnect)

* [Dump CA](dump_ca)

* [Enable LTE](enable_lte)

* [Enable SSL](enable_ssl)

* [Enable terminal](enable_terminal)

