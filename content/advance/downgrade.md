---
title: "Firmware Downgrade"
aliases:
    - advance/downgrade.html
    - advance/downgrade.md
    - chapter/advance/downgrade
---

The firmware upgrade tool usually updates your device to the latest available firmware version. If you require to downgrade your device to a previous firmware there are two methods to achieve this.

Here you can download Pycom firmwares. Note that these are all available in the Pycom Firmware Update tool.

### Current and previous Pygate firmware
* [WiPy](https://software.pycom.io/downloads/pygate/WiPy.html)
* [GPy](https://software.pycom.io/downloads/pygate/GPy.html)
* [LoPy4](https://software.pycom.io/downloads/pygate/LoPy4.html)

### Current and previous Pybytes firmware

* [WiPy](https://software.pycom.io/downloads/pybytes/WiPy.html)
* [LoPy](https://software.pycom.io/downloads/pybytes/LoPy.html)
* [SiPy](https://software.pycom.io/downloads/pybytes/SiPy.html)
* [GPy](https://software.pycom.io/downloads/pybytes/GPy.html)
* [FiPy](https://software.pycom.io/downloads/pybytes/FiPy.html)
* [LoPy4](https://software.pycom.io/downloads/pybytes/LoPy4.html)

### Legacy and previous development firmware

* [WiPy](https://software.pycom.io/downloads/WiPy.html)
* [LoPy](https://software.pycom.io/downloads/LoPy.html)
* [SiPy](https://software.pycom.io/downloads/SiPy.html)
* [GPy](https://software.pycom.io/downloads/GPy.html)
* [FiPy](https://software.pycom.io/downloads/FiPy.html)
* [LoPy4](https://software.pycom.io/downloads/LoPy4.html)

> Prior to version `1.16.0.b1` the firmware for modules with LoRa functionality was frequency specific. From `1.16.0.b1` and onward, the firmware is region agnostic and this can either be set programatically or via the config block (see [here](../cli.md#lpwan)).


## GUI

As of version `1.12.0.b0` of the firmware update tool, you can now provide a `.tar` or `.tar.gz` archive of the firmware you wish to upload to the board. Check out the procedure [here](/updatefirmware/device/)

## Command line

You can also use the [CLI](../cli) version of the update tool to downgrade your device. Will need to get a `.tar` or `.tar.gz` archive of the firmware you wish to upload to the board. Then run the following commands:

```bash
$ pycom-fwtool-cli -v -p PORT flash -t /path/to/firmware/archive.tar.gz
```
