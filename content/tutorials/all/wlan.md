---
title: "WLAN"
aliases:
    - tutorials/all/wlan.html
    - tutorials/all/wlan.md
    - chapter/tutorials/all/wlan
---

The WLAN is a system feature of all Pycom devices, therefore it is enabled by default.

In order to retrieve the current WLAN instance, run:

```python

>>> from network import WLAN
>>> wlan = WLAN() # we call the constructor without params
```

The current mode (`WLAN.AP` after power up) may be checked by running:

```python

>>> wlan.mode()
```

{{% hint style="danger" %}}

When changing the WLAN mode, if following the instructions below, the WLAN connection to the Pycom device will be broken. This means commands will not run interactively over WiFi.

**There are two ways around this:**

1. Put this setup code into the `boot.py` file of the Pycom device so that it gets executed automatically after reset.
2. Duplicate the REPL on UART. This way commands can be run via Serial USB.


{{< /hint >}}

## Connecting to a Router

The WLAN network class always boots in `WLAN.AP` mode; to connect it to an existing network, the WiFi class must be configured as a station:

```python

from network import WLAN
wlan = WLAN(mode=WLAN.STA)
```

Now the device may proceed to scan for networks:

```python

nets = wlan.scan()
for net in nets:
    if net.ssid == 'mywifi':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'mywifikey'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break
```

## Assigning a Static IP Address at Boot Up

If the users wants their device to connect to a home router upon boot up, using with a fixed IP address, use the following script as `/flash/boot.py`:

```python

import machine
from network import WLAN
wlan = WLAN() # get current object, without changing the mode

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(mode=WLAN.STA)
    # configuration below MUST match your home router settings!!
    wlan.ifconfig(config=('192.168.178.107', '255.255.255.0', '192.168.178.1', '8.8.8.8'))

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect('mywifi', auth=(WLAN.WPA2, 'mywifikey'), timeout=5000)
    while not wlan.isconnected():
        machine.idle() # save power while waiting
```

{{% hint style="info" %}}
Notice how we check for the reset cause and the connection status, this is crucial in order to be able to soft reset the LoPy during a telnet session without breaking the connection.
{{< /hint >}}

## Multiple Networks using a Static IP Address

The following script holds a list with nets and an optional list of `wlan_config` to set a fixed IP

```python

import os
import machine

uart = machine.UART(0, 115200)
os.dupterm(uart)

known_nets = {
    '<net>': {'pwd': '<password>'},
    '<net>': {'pwd': '<password>', 'wlan_config':  ('10.0.0.114', '255.255.0.0', '10.0.0.1', '10.0.0.1')}, # (ip, subnet_mask, gateway, DNS_server)
}

if machine.reset_cause() != machine.SOFT_RESET:
    from network import WLAN
    wl = WLAN()
    wl.mode(WLAN.STA)
    original_ssid = wl.ssid()
    original_auth = wl.auth()

    print("Scanning for known wifi nets")
    available_nets = wl.scan()
    nets = frozenset([e.ssid for e in available_nets])

    known_nets_names = frozenset([key for key in known_nets])
    net_to_use = list(nets & known_nets_names)
    try:
        net_to_use = net_to_use[0]
        net_properties = known_nets[net_to_use]
        pwd = net_properties['pwd']
        sec = [e.sec for e in available_nets if e.ssid == net_to_use][0]
        if 'wlan_config' in net_properties:
            wl.ifconfig(config=net_properties['wlan_config'])
        wl.connect(net_to_use, (sec, pwd), timeout=10000)
        while not wl.isconnected():
            machine.idle() # save power while waiting
        print("Connected to "+net_to_use+" with IP address:" + wl.ifconfig()[0])

    except Exception as e:
        print("Failed to connect to any known network, going into AP mode")
        wl.init(mode=WLAN.AP, ssid=original_ssid, auth=original_auth, channel=6, antenna=WLAN.INT_ANT)
```

## Connecting to a WPA2-Enterprise network

### Connecting with EAP-TLS:

Before connecting, obtain and copy the public and private keys to the device, e.g. under location `/flash/cert`. If it is required to validate the server's public key, an appropriate CA certificate (chain) must also be provided.

```python

from network import WLAN

wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid='mywifi', auth=(WLAN.WPA2_ENT,), identity='myidentity', ca_certs='/flash/cert/ca.pem', keyfile='/flash/cert/client.key', certfile='/flash/cert/client.crt')
```

### Connecting with EAP-PEAP or EAP-TTLS:

In case of EAP-PEAP (or EAP-TTLS), the client key and certificate are not necessary, only a username and password pair. If it is required to validate the server's public key, an appropriate CA certificate (chain) must also be provided.

```python

from network import WLAN

wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid='mywifi', auth=(WLAN.WPA2_ENT, 'username', 'password'), identity='myidentity', ca_certs='/flash/cert/ca.pem')
```

