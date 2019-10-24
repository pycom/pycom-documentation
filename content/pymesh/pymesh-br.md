---
title: "Pymesh Border Router"
aliases:
    - tutorials/lora/pymesh-br.html
    - tutorials/lora/pymesh-br.md
---

<img src="/gitbook/assets/pymesh/pymesh_roles.png" alt="Pymesh" width="500"/>

## Overview

The Border Router role, of a Node inside Pymesh, takes the traffic from the Pymesh and forwards it to the Cloud (Pymesh-external).

Several things must be accomplished:

* The BR node should have connection with the Cloud, using another network interface (than LoRa-Pymesh), for example: BLE, Wifi or Cellular.
* The node has to be declared as BR, so all the other nodes send packets to it, with destination Cloud.
* Dynamically multiple nodes can be BR, each of them having different priorities levels (Normal, High or Low)
 * The BR with the smallest routing cost is chosen.
 * If multiple BR have the same routing cost, the priority level is used.

## Border Router using CLI

As explained in [Pymesh CLI - Border Router section](pymesh/lib-cli/#border-router-specific), using commands `br` and `brs`, a simple testing scenario can be easily implemented.

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

* declare the BR network address prefix, like `2001:dead:beef:cafe::/64`
* this piece of information is sent to the `Leader` and the dataset will increase version (it will be updated)
* the dataset is propagated to all Pymesh nodes
* all the nodes will be assigned a random IPv6 unicast address with this network prefix (like `2001:dead:beef:cafe:1234:5678:9ABC:DEF0`)
* if a node sends data to an IPv6 which is external (it doesn't have prefix from Pymesh already existent networks, like `1:2:3::4`), this UDP datagram will be routed to the BR
 * this UDP packet will have as source the random IPv6 from BR network address
* BR will receive the UDP datagrams for external with an appended header, which contains:
 * MAGIC byte: `0xBB`
 * IPv6 destination as bytearray (16 bytes)
 * port destination as 2 bytes (1-65535 values).
* the IPv6 destination is important so BR could actually route (forward) the UDP datagram content to the right interface (Wifi/BLE/cellular).
