---
title: "Pymesh Library"
aliases:
  - pymesh/library
---

## What is Pymesh micropython library?

Pymesh micropython library is a set of scripts included (as frozen) in the Pymesh firmware binary release (Not yet released).

[Open-source on github](https://github.com/pycom/pycom-libraries/tree/master/lib/pymesh)

It allows users to use Pymesh in a few lines of code, as shown in the following code snippet.

```python

import pycom
import time

from _pymesh_config import PymeshConfig
from _pymesh import Pymesh

# stop LED heartbeat, because it will be used to indicate current Node role 
pycom.heartbeat(False)

# read config file, or set default values
pymesh_config = PymeshConfig.read_config()

#initialize Pymesh
pymesh = Pymesh(pymesh_config, new_message_cb)

while not pymesh.is_connected():
    print(pymesh.status_str())
    time.sleep(3)

# send message to the Node having MAC address 6
pymesh.send_mess(6, "Hello World")

def new_message_cb(rcv_ip, rcv_port, rcv_data):
    ''' callback triggered when a new packet arrived '''
    print('Incoming %d bytes from %s (port %d):' %
            (len(rcv_data), rcv_ip, rcv_port))
    print(rcv_data)

    # user code to be inserted, to send packet to the designated Mesh-external interface
    # ...
    return

######################################################################################
# Adding current node as Border Router, with a normal priority and a message handler callback
pymesh.br_set(PymeshConfig.BR_PRIORITY_NORM, new_br_message_cb)

# remove Border Router function from current node
#pymesh.br_remove()

# send data for Mesh-external, basically to the BR
ip = "1:2:3::4"
port = 5555
pymesh.send_mess_external(ip, port, "Hello World")

def new_br_message_cb(rcv_ip, rcv_port, rcv_data, dest_ip, dest_port):
    ''' callback triggered when a new packet arrived for the current Border Router,
    having destination an IP which is external from Mesh '''
    print('Incoming %d bytes from %s (port %d), to external IPv6 %s (port %d)' %
            (len(rcv_data), rcv_ip, rcv_port, dest_ip, dest_port))
    print(rcv_data)

    # user code to be inserted, to send packet to the designated Mesh-external interface
    # ...
    return

```
