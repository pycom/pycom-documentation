---
title: "Pymesh Library"
aliases:
  - pymesh/simple-example
---

## What is Pymesh micropython library?

Pymesh micropython library is a set of scripts included (as frozen) in the Pymesh firmware binary release (not yet released).

[Open-source on github](https://github.com/pycom/pycom-libraries/tree/master/lib/pymesh)

It allows users to use Pymesh in a few lines of code, as shown in the following code snippet.

```python

import pycom
import time

try:
    from pymesh_config import PymeshConfig
except:
    from _pymesh_config import PymeshConfig

try:
    from pymesh import Pymesh
except:
    from _pymesh import Pymesh

def new_message_cb(rcv_ip, rcv_port, rcv_data):
    ''' callback triggered when a new packet arrived '''
    print('Incoming %d bytes from %s (port %d):' %
            (len(rcv_data), rcv_ip, rcv_port))
    print(rcv_data)

    # user code to be inserted, to send packet to the designated Mesh-external interface
    for _ in range(3):
        pycom.rgbled(0x888888)
        time.sleep(.2)
        pycom.rgbled(0)
        time.sleep(.1)
    return


pycom.heartbeat(False)

# read config file, or set default values
pymesh_config = PymeshConfig.read_config()

#initialize Pymesh
pymesh = Pymesh(pymesh_config, new_message_cb)

mac = pymesh.mac()
# based on LoRa MAC address, some nodes could be forced to be
# sleep-end-devices (always Child) or to have increased Leader priority
# if mac > 10:
#     pymesh.end_device(True)
# elif mac == 5:
#     pymesh.leader_priority(255)

while not pymesh.is_connected():
    print(pymesh.status_str())
    time.sleep(3)

# send message to the Node having MAC address 5
pymesh.send_mess(5, "Hello World")

# def new_br_message_cb(rcv_ip, rcv_port, rcv_data, dest_ip, dest_port):
#     ''' callback triggered when a new packet arrived for the current Border Router,
#     having destination an IP which is external from Mesh '''
#     print('Incoming %d bytes from %s (port %d), to external IPv6 %s (port %d)' %
#             (len(rcv_data), rcv_ip, rcv_port, dest_ip, dest_port))
#     print(rcv_data)

#     # user code to be inserted, to send packet to the designated Mesh-external interface
#     # ...
#     return

# add current node as Border Router, with a priority and a message handler callback
# pymesh.br_set(PymeshConfig.BR_PRIORITY_NORM, new_br_message_cb)

# remove Border Router function from current node
#pymesh.br_remove()

# send data for Mesh-external, basically to the BR
# ip = "1:2:3::4"
# port = 5555
# pymesh.send_mess_external(ip, port, "Hello World")

print("done Pymesh init, forever loop, exit/stop with Ctrl+C multiple times")
# set BR with callback

while True:
    time.sleep(3)

```

## Output

An example of output is bellow.

At any point pressing `Enter` will try to execute CLI commands, more details are presented in [Pymesh library CLI](/pymesh/lib-cli).

```

rst:0x7 (TG0WDT_SYS_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
mode:DIO, clock div:1
load:0x3fff8020,len:8
load:0x3fff8028,len:2164
load:0x4009fa00,len:19944
entry 0x400a05e8
MAC ok 11
Settings: {'ble_api': True, 'MAC': 11, 'autostart': True, 'debug': 5, 'LoRa': {'sf': 7, 'region': 5, 'freq': 863000000,'bandwidth': 2}, 'ble_name_prefix': 'PyGo ', 'Pymesh': {'key': '112233'}}
LoRa MAC: 0xb, short: 11
OT stack: 6412
Statistics file ok?!
============ MESH THREAD >>>>>>>>>>>
3: MAC 0xb(11), State Detached, Single True
['fdde:ad00:beef:0:0:0:0:b', 'fdde:ad00:beef:0:0:ff:fe00:c400', 'fdde:ad00:beef:0:2c1a:56c0:ebbd:d46', 'fe80:0:0:0:200:0:0:b']
>>>>>>>>>>> DONE MESH THREAD ============ 40

BLE name: PyGo 11
Role 3, Single False, IPv6: ['fdde:ad00:beef:0:0:ff:fe00:c400', 'fdde:ad00:beef:0:0:0:0:b', 'fdde:ad00:beef:0:2c1a:56c0:ebbd:d46', 'fe80:0:0:0:200:0:0:b']
>Role 3, Single False, IPv6: ['fdde:ad00:beef:0:0:ff:fe00:c400', 'fdde:ad00:beef:0:0:0:0:b', 'fdde:ad00:beef:0:2c1a:56c0:ebbd:d46', 'fe80:0:0:0:200:0:0:b']
Role 3, Single False, IPv6: ['fdde:ad00:beef:0:0:ff:fe00:c400', 'fdde:ad00:beef:0:0:0:0:b', 'fdde:ad00:beef:0:2c1a:56c0:ebbd:d46', 'fe80:0:0:0:200:0:0:b']
Role 3, Single False, IPv6: ['fdde:ad00:beef:0:0:ff:fe00:c400', 'fdde:ad00:beef:0:0:0:0:b', 'fdde:ad00:beef:0:2c1a:56c0:ebbd:d46', 'fe80:0:0:0:200:0:0:b']
============ MESH THREAD >>>>>>>>>>>
13: MAC 0xb(11), State Router, Single False
['fdde:ad00:beef:0:0:ff:fe00:c400', 'fdde:ad00:beef:0:0:0:0:b', 'fdde:ad00:beef:0:2c1a:56c0:ebbd:d46', 'fe80:0:0:0:200:0:0:b']
Leader: mac 0x4, rloc 0xb800, net: 0x591354fb
Socket created on port 1234
Neighbors Table: [(mac=6, role=3, rloc16=28672, rssi=-67, age=0), (mac=4, role=3, rloc16=47104, rssi=-97, age=4)]
Neighbors: Router MAC 0xB, rloc16 0xc400, coord (51.45, 5.45313), neigh_num 2, ts 14
MAC 0x6, rloc16 0x7000, role 3, rssi -67, age 0
MAC 0x4, rloc16 0xb800, role 3, rssi -97, age 4

>>>>>>>>>>> DONE MESH THREAD ============ 76

Send message to 5, typ 0, load Hello World
Added new message for 5: Hello World
Send message b'\x00\x00\x00\x00\x00\x00\x00\x0b09\x00\x0bHello World'
Send pack: 0x10 to IP fdde:ad00:beef:0::5
done Pymesh init, forever loop, exit/stop with Ctrl+C multiple times
```
