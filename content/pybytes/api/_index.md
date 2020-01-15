---
title: "Pybytes library API"
aliases:
  - pybytes/api
---


If you are facing any issues try to enable debugging.

### Debugging
There are multiple debug levels, 0 is warnings only, 6 is currently the highest used).

#### use:

import pycom;

pycom.nvs_set('pybytes_debug', debugLevel)


#### e.g.
```
    >> import pycom;
     >> pycom.nvs_set('pybytes_debug', 6)
```    


# API List

* [Add custom method](add_custom_method)

* [Activate](activate)

* [Connect](connect)

* [Connect LTE](connect_lte)

* [Connect LoRa ABP](connect_lora_abp)

* [Connect LoRa OTAA](connect_lora_otaa)

* [Connect Sigfox](connect_sigfox)

* [Connect Wifi](connect_wifi)

* [Deepsleep](deepsleep)

* [Disconnect](disconnect)

* [Dump ca](dump_ca)

* [Enable lte](enable_lte)

* [Enable ssl](enable_ssl)

* [Enable terminal](enable_terminal)

* [Export config](export_config)

* [Get config](get_config)

* [Is connected](is_connected)

* [isconnected](isconnected)

* [Print cfg msg](print_cfg_msg)

* [Print config](print_config)

* [Read config](read_config)

* [Reconnect](reconnect)

* [Register periodical analog pin publish](register_periodical_analog_pin_publish)

* [Register periodical digital pin publish](register_periodical_digital_pin_publish)

* [Send analog pin value](send_analog_pin_value)

* [Send battery level](send_battery_level)

* [Send custom message](send_custom_message)

* [Set custom message callback](set_custom_message_callback)

* [Send custom location](send_custom_location)

* [Send digital pin value](send_digital_pin_value)

* [Send info message](send_info_message)

* [Send ping message](send_ping_message)

* [Send scan info message](send_scan_info_message)

* [Send signal](send_signal)

* [Send virtual pin value](send_virtual_pin_value)

* [Set config](set_config)

* [Start](start)

* [Update config](update_config)

* [Write config](write_config)
