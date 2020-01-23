---
title: "Pybytes library API"
aliases:
---

To test Pybytes library API, connect your device to Pymakr and call the methods listed below.
You can use Pybytes library API in your MicroPython project.


### Debugging
If you are facing any issues try to enable debugging.
There are multiple debug levels, 0 is warnings only, 99 is currently the highest used).

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

* [Connect](connect)

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

* [Export configuration](export_config)

* [Get configuration](get_config)

* [Is connected](is_connected)

* [Print configuration](print_config)

* [Read configuration](read_config)

* [Reconnect](reconnect)

* [Send info message](send_info_message)

* [Send ping message](send_ping_message)

* [Send signal](send_signal)

* [Set configuration](set_config)

* [Start](start)

* [Update configuration](update_config)

* [Write configuration](write_config)
