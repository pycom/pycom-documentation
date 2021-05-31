---
title: "Pymesh Border Router"
aliases:
    - tutorials/lora/pymesh-br.html
    - tutorials/lora/pymesh-br.md
---

<img src="/gitbook/assets/pymesh/pymesh_roles.png" alt="Pymesh" width="500"/>

## Overview

Any node inside of the Pymesh can take on the role as a Border Router, which takes the traffic from the Pymesh and forwards it to the Cloud (Pymesh-external).

Several things must be accomplished:

* The Border Router node should have connection with the Cloud. This should occur using another network interface (other than LoRa-Pymesh), for example: BLE, Wifi or Cellular.
* The node has to be declared as a Border Router, so that all the other nodes send packets to it. The final destination is the Cloud.
* To add flexibility, at runtime (dynamically), multiple nodes can act as Border Routers. Each of them can have different priority levels (Normal, High or Low).
 * The Border Router with the smallest routing cost is selected.
 * If multiple Border Routers have the same routing cost, then the priority level is used.

## Border Router using CLI

As explained in [Pymesh CLI - Border Router section](/pymesh/lib-cli/#border-router-specific), using commands `br` and `brs`, a simple test scenario can be easily implemented.

## Border Router using Pymesh API

```
def new_br_message_cb(rcv_ip, rcv_port, rcv_data, dest_ip, dest_port):
    ''' callback triggered when a new packet arrived for the current Border Router,
    having destination an IP which is external from Mesh '''
    print('Incoming %d bytes from %s (port %d), to external IPv6 %s (port %d)' %
            (len(rcv_data), rcv_ip, rcv_port, dest_ip, dest_port))
    print(rcv_data)

    # user code to be inserted, to send packet to the designated Mesh-external interface
    # ...
    return

add current node as Border Router, with a priority and a message handler callback
pymesh.br_set(PymeshConfig.BR_PRIORITY_NORM, new_br_message_cb)

remove Border Router function from current node
pymesh.br_remove()

send data for Mesh-external, basically to the BR
ip = "1:2:3::4"
port = 5555
pymesh.send_mess_external(ip, port, "Hello World")

```

## Technical deep dive

Internally, the Border Router mechanism is implemented with the following steps:

* Declare the Border Router network address prefix, for example `2001:dead:beef:cafe::/64`
* The network address prefix is then sent to the `Leader` and the dataset will increase the version, meaning that it will be updated.
* The dataset is propagated to all Pymesh nodes.
* All the nodes will be assigned a random IPv6 unicast address with this network prefix (for example `2001:dead:beef:cafe:1234:5678:9ABC:DEF0`)
* If a node sends data to an IPv6 which is external (meaning it doesn't have a prefix from already existent networks in Pymesh, for example `1:2:3::4`), then the UDP datagram will be routed to the Border Router
 * This UDP packet will have as source the random IPv6 from BR network address
* The Border Router will receive the external UDP datagrams with an appended header, which contains:
 * MAGIC byte: `0xBB`
 * IPv6 destination as bytearray (16 bytes)
 * port destination as 2 bytes (1-65535 values).
* The IPv6 destination is important, because it means that the Border Router can route (forward) the UDP datagram content to the correct interface (Wifi/BLE/cellular).
