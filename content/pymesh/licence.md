---
title: "Obtaining Pymesh"
aliases:
  - pymesh/simple-example
---

## Obtaining Pymesh

In order to receive access to the Pymesh firmware releases (for Lopy4, Fipy, L01 or L04), please follow the steps from [Pybytes - Pymesh integration](/pybytes/pymeshintegration/).

## Test Pymesh firmware loading

### Method 1

The simplest way to check if the Pymesh class has been successfully instantiated (and started inside Pybytes) is to try the following code, directly in REPL:

```python
# todo: add try/except for checking pybytes object exists
>>> pymesh = pybytes.__pymesh.__pymesh
>>> pymesh.cli_start()
>h
List of available commands
br - enable/disable or display the current Border Router functionality
brs - send packet for Mesh-external, to BR, if any
buf - display buffer info
config - print config file contents
debug - set debug level
gps - get/set location coordinates
h - help, list of commands
ip - display current IPv6 unicast addresses
mac - set or display the current LoRa MAC address
mml - display the Mesh Mac List (MAC of all nodes inside this Mesh), also inquires Leader
mp - display the Mesh Pairs (Pairs of all nodes connections), also inquires Leader
ot - sends command to openthread internal CLI
pause - suspend Pymesh
resume - resume Pymesh
rm - verifies if any message was received
rst - reset NOW, including NVM Pymesh IPv6
s - send message
self - display all info about current node
sleep - deep-sleep
stop - close this CLI
tx_pow - set LoRa TX power in dBm (2-20)
ws - verifies if message sent was acknowledged

```

### Method 2

Upload the `main.py` from the [Simple Example](/pymesh/simple-example).
