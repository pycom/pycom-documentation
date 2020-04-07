---
title: "Pymesh Library API"
aliases:
  - pymesh/lib-api
---

## Overview

This Micropython library is included as frozen scripts in the Pymesh firmware release.

The code is open-sourced in [pycom-libraries repository](https://github.com/pycom/pycom-libraries/tree/master/lib/pymesh).

It is easily customisable and contributions are welcome using [Github PRs](https://github.com/pycom/pycom-libraries/pulls).

### Main features

* Start Pymesh over LoRa on 863Mhz, bandwidth 250kHz, spreading-factor 7 (please check `pymesh_config.py` defaults for exact values).
* Pymesh parameters are automatically saved in NVM, so in the next restart/deepsleep, the node will try to maintain its IP addresses and connections with neighbour nodes.
* Start Bluetooth LE server with name `PyGo <LoRa MAC>`
  * BLE is used with an RPC protocol, presented int [Pymesh library BLE RPC](/pymesh/lib-ble-rpc)
* Internal CLI for controlling/triggering Pymesh features, as explained in [Pymesh library CLI](/pymesh/lib-cli).

### Color coding LED

The LED color represents the state of the node in the Mesh network.

```

Blinking        - Send/Receive packet
Magenta         - LEADER
Green           - ROUTER
White           - CHILD,
Red             - Searching / Detached from any Pymesh
Cyan            - SINGLE LEADER (no other Router in the same Pymesh)
```

## Example of usage

A simple example of usage is in the [main.py](https://github.com/pycom/pycom-libraries/blob/master/lib/pymesh/main.py).

## Specifications

It can be easily customised, by modifying any file from [/lib folder](https://github.com/pycom/pycom-libraries/tree/master/lib/pymesh/lib) and flashing it to the board. The uploaded file will automatically be executed instead of the _frozen_ one, which is already embedded into the binary firmware.

### Structure

* `pymesh.py`
  * contains all the methods accessible from `main.py`
* `cli.py`
  * [Pymesh library CLI](/pymesh/lib-cli)
* BLE services
  * `ble_rpc.py`
    * [Pymesh library BLE RPC](/pymesh/lib-ble-rpc)
  * `ble_services.py`
    * setting BLE server
* auxiliary files:
  * `pymesh-debug.py`
    * debugging on multiple levels, allowing dynamically changing the current debug level
  * `pymesh-config.py`
    * reading/writing the Pymesh configuration file
  * `gps.py`
    * maintaining location coordinates, as an extension `Pytrack` GPS can be used
* Mesh internals
  * `mesh-interface.py`
    * methods to inquire Mesh-internal parameters
  * `mesh-internal.py` and `loramesh.py`
    * 2 layers of internal mesh maintenance
