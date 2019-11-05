 ---
title: "PyMesh"
aliases:
    - firmwareapi/pycom/network/lora/pymesh.html
    - firmwareapi/pycom/network/lora/pymesh.md
---

The following will show the Pymesh (LoRa Mesh network created by Pycom) class for the LoPy and FiPy.

Below is a brief example demonstrating how to initialise the Pymesh network.

```python

from network import LoRa

# initialise LoRa
# the LoRa parameters (frequency, spreading factor, bandwidth) has to be the same for all
# nodes in the same Pymesh
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868,
    frequency = 863000000, bandwidth=LoRa.BW_125KHZ, sf=7)

print("Enable Pymesh")
pymesh = lora.Mesh()

# check node state inside Pymesh
# PYMESH_ROLE_DISABLED = 0, ///< The Pymesh stack is disabled.
# PYMESH_ROLE_DETACHED = 1, ///< Not currently participating in a Pymesh.
# PYMESH_ROLE_CHILD    = 2, ///< The Pymesh Child role.
# PYMESH_ROLE_ROUTER   = 3, ///< The Pymesh Router role.
# PYMESH_ROLE_LEADER   = 4, ///< The Pymesh Leader role.
print("Pymesh node role: %d"%pymesh.state())

print("IPv6 unicast addresses: %s"%pymesh.ipaddr())
```

## Examples

For various other Pymesh examples, check the [Pymesh Chapter](/pymesh).

## Constructor

#### class network.LoRa.Mesh(\*, key=masterkey)

This constructor `network.LoRa.Mesh()` creates and configures the Pymesh object.

By default, the key is `0134C0DE1AB51234C0DE1AB5CA1A110F`.

The current `masterkey` can be found using: `print("Masterkey:", pymesh.cli("masterkey"))`.

```python
import ubinascii
from network import LoRa

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
masterkey = ubinascii.unhexlify("112233")
pymesh = lora.Mesh(key=masterkey)

# as test, the masterkey can be printed
>>> print("masterkey:", pymesh.cli("masterkey"))
masterkey: 11223300000000000000000000000000
```

## Methods

#### pymesh.deinit()

This destroys the Pymesh task. Any further Pymesh commands will return no answer.
To recreate the Pymesh, use the `LoRa.Mesh()` constructor.

```python

>>> pymesh.deinit()
True
>>> pymesh.neighbors()
>>> pymesh.leader()
```

#### pymesh.state()

This receives the node's state inside of the Pymesh, which can be one of the following:
```python
# PYMESH_ROLE_DISABLED = 0, ///< The Pymesh stack is disabled.
# PYMESH_ROLE_DETACHED = 1, ///< Not currently participating in a Pymesh.
# PYMESH_ROLE_CHILD    = 2, ///< The Pymesh Child role.
# PYMESH_ROLE_ROUTER   = 3, ///< The Pymesh Router role.
# PYMESH_ROLE_LEADER   = 4, ///< The Pymesh Leader role.
```

```python

# receive node's state inside Pymesh
>>> pymesh.state()
4
```
More info: https://openthread.io/guides/thread-primer/node-roles-and-types

#### pymesh.single()

This answers `True` if this node is the only Leader or Router in the current Pymesh network.

```python

>>> pymesh.single()
True
```

#### pymesh.ipaddr()

This returns all the IPv6 unicast addresses assigned on Pymesh interface.

More info: https://openthread.io/guides/thread-primer/ipv6-addressing

```python
>>> pymesh.ipaddr()
['fdde:ad00:beef:0:0:ff:fe00:fc00', 'fdde:ad00:beef:0:0:ff:fe00:cc00', 'fdde:ad00:beef:0:86c3:6130:98cc:6633', 'fe80:0:0:0:301:101:101:104']
```

In the previous `pymesh.ipaddr()` answer, these are the individual IPv6:

* `fe80:0:0:0:301:101:101:104` - the link-local IPv6 address
 * used to discover neighbors, configure links
 * not routable
 * always has a prefix of `fe80::/16`
* `fdde:ad00:beef:0:86c3:6130:98cc:6633` - the mesh-local identifier
 * independent of network topology
 * does not change as the topology changes
 * should be used by applications
 * always has a prefix `fd00::/8`
* `fdde:ad00:beef:0:0:ff:fe00:cc00` - the routing locator (RLOC)
 * identifies a mesh interface, based on its location in the network topology
 * Changes as the topology changes
 * Generally not used by applications
* `fdde:ad00:beef:0:0:ff:fe00:fc00` - the Leader IPv6

#### pymesh.rloc()

This returns the routing locator's (RLOC) IPv6 address.

```python

>>> pymesh.rloc()
52224
>>> hex(pymesh.rloc())
'0xcc00'
```

More info: https://openthread.io/guides/thread-primer/ipv6-addressing

#### pymesh.neighbors()

This returns a list with tuples containing information about neighbour nodes. Neighbour nodes are all nodes that have a **direct** radio connection to the calling node.

For each neighbour the following properties are returned:

* mac - LoRa MAC address
* role - Child(2) or Router(3), the Leader is always shown as a normal Router
* rloc16 - the RLOC (more info [here](https://openthread.io/guides/thread-primer/ipv6-addressing))
* rssi - the RSSI(Received Signal Strength Indication) of the radio link expressed is in decibels(dB)
* age - number of seconds since last data packet was received

```python

>>> pymesh.neighbors()
[(mac=1, role=3, rloc16=25600, rssi=-37, age=19),
(mac=8121069065142870746, role=3, rloc16=55296, rssi=-27, age=15)]
>>> neighbors = pymesh.neighbors()
>>> neighbors[0].rssi
-37
```

#### pymesh.routers()

This returns a list with tuples containing information about all routers from Pymesh. Routers are Pymesh nodes that relay/route packets inside Pymesh.

For each Router the following properties are returned:

* mac - LoRa MAC address
* rloc16 - the RLOC (more info [here](https://openthread.io/guides/thread-primer/ipv6-addressing))
* id - each Router has its own random unique ID
* path_cost - the cost of the path from current node to this router
 * example: 4 nodes are connected in the sequence, A-B-C-D
  * path_cost A to B is 0(all path_cost's begin at 0)
  * path_cost A to C is 1
  * path_cost A to D is 2
* age - number of seconds since last keep-alive packet was received

```python

>>> pymesh.routers()
[(mac=1, rloc16=25600, id=25, path_cost=1, age=12),
(mac=72340172838076676, rloc16=52224, id=51, path_cost=0, age=0),
(mac=8121069065142870746, rloc16=55296, id=54, path_cost=1, age=12)]
>>> routers = pymesh.routers()
>>> routers[0].rloc16
25600
```

#### pymesh.leader()

This returns information about Leader of the Pymesh. It can be called from any node.

The following details are returned:

* part_id - partition id, the Pymesh internal network address
* mac - the LoRa MAC address of the Leader
* rloc16 - the Leader RLOC (more info [here](https://openthread.io/guides/thread-primer/ipv6-addressing))

```python

>>> pymesh.leader()
(part_id=828258, mac=72340172838076676, rloc16=52224)
```

#### pymesh.rx_cb(callback_handler, argument)

This specifies the callback handler executed when a new packet is received.

In case multiple sockets are open, this callback is executed on **any opened socket**. The callback handler has to find the correct socket for the incoming data. In order to search for the correct socket use the parameter `argument`.

Below is the callback example.

```python

# handler responsible for receiving packets on UDP Pymesh socket
def receive_pack(sockets):
    # listen for incoming packets on all sockets
    while True:
        is_new_data = False
        for sock in sockets:
            # check if data received on all sockets
            rcv_data, rcv_addr = sock.recvfrom(128)
            if len(rcv_data) > 0:
                is_new_data = True
                break # out of for sock
        if not is_new_data:
            break # out of while True
        rcv_ip = rcv_addr[0]
        rcv_port = rcv_addr[1]
        print('Incomming %d bytes from %s (port %d)'%(len(rcv_data), rcv_ip, rcv_port))

        #check if data is for the external of the Pymesh (for The Cloud)
        if rcv_data[0] == BORDER_ROUTER_MAGIC_BYTE and len(rcv_data) >= struct.calcsize(BORDER_ROUTER_HEADER_FORMAT):
            br_header = struct.unpack(BORDER_ROUTER_HEADER_FORMAT, rcv_data)
            print("IP dest: %x:%x:%x:%x:%x:%x:%x:%x (port %d)"%(
                br_header[1],br_header[2],br_header[3],br_header[4],
                br_header[5],br_header[6],br_header[7],br_header[8], br_header[9]))
            rcv_data = rcv_data[struct.calcsize(BORDER_ROUTER_HEADER_FORMAT):]

        print(rcv_data)

        # send some ACK
        if  not rcv_data.startswith("ACK"):
            print("Sent ACK back")
            sock.sendto('ACK', (rcv_ip, rcv_port))

# create the list of sockets
sockets = []
sockets.append(eid_socket)
sockets.append(br_socket)

# set RX callback
pymesh.rx_cb(receive_pack, sockets)
```

#### pymesh.border_router(\*, [ipv6_net_address, preference_level])

This method has 2 different purposes.

1. The current node can be set up as a Border Router by specifying the external IPv6 network address
2. The current node is asked if it is a Border Router, and if it is, then the external IPv6 network address is given.
</p>

For a more detailed example, [click here](/pymesh/pymesh-br).

The details of the parameters are:

* `ipv6_net_address`
 * this is a valid IPv6 network address containing IP and mask, for ex `"2001:cafe:cafe:cafe::/64"`.
 * as a consequence from this method being applied, all of the nodes from the Pymesh will receive a random additional IPv6 unicast address. This will be selected from within this network address.
* `preference_level`
 * should be a value of either -1: low, 0: normal or 1: high
 * if multiple Border Routers are declared with the same prefix and the same path cost, the one with the highest preference is used, ie. 1.

```python

# IPv6 addresses, before setting Border Router
>>> pymesh.ipaddr()
['fdde:ad00:beef:0:0:ff:fe00:fc00', 'fdde:ad00:beef:0:0:ff:fe00:cc00', 'fdde:ad00:beef:0:86c3:6130:98cc:6633', 'fe80:0:0:0:301:101:101:104']
# setting Border Router with preference_level 0
>>> pymesh.border_router("2001:cafe:cafe:cafe::/64", 0)
0
# checking a new IPv6 address is assigned
>>> pymesh.ipaddr()
['2001:cafe:cafe:cafe:a5d2:6934:9acd:66b3', 'fdde:ad00:beef:0:0:ff:fe00:fc00', 'fdde:ad00:beef:0:0:ff:fe00:cc00', 'fdde:ad00:beef:0:86c3:6130:98cc:6633', 'fe80:0:0:0:301:101:101:104']
# list the BR entries
>>> pymesh.border_router()
[(net='2001:dead:beef:cafe::/64', preference=0)]
>>>
```

#### pymesh.border_router_del(ipv6_net_address)

This returns the Border Router node to a normal node.

The parameter `ipv6_net_address` has to be the same as the one that was used when the node was set as a Border Router.

As a consequence, the random IPv6 that was allocated, will be deleted from all nodes.

```python

# BR entry
>>> pymesh.border_router()
[(net='2001:dead:beef:caff::/64', preference=1)]
# checking the Border Router IPv6 unicast address with BR prefix
>>> pymesh.ipaddr()
['2001:dead:beef:caff:2291:48a4:5229:94ca', 'fdde:ad00:beef:0:0:ff:fe00:6800', 'fdde:ad00:beef:0:4623:91c8:64b2:d9ec', 'fe80:0:0:0:200:0:0:8']
# remove the Border Router  entry
>>> pymesh.border_router_del('2001:dead:beef:caff::/64')
# this verifies the current node is no longer a Border Router
>>> pymesh.border_router()
[]
# this verifies the current node doesn't have the Border Router IPv6 network address
>>> pymesh.ipaddr()
['fdde:ad00:beef:0:0:ff:fe00:6800', 'fdde:ad00:beef:0:4623:91c8:64b2:d9ec', 'fe80:0:0:0:200:0:0:8']
```

#### pymesh.cli(command)

This sends a command to the internal Openthread engine.

The list of CLI commands is [here](https://github.com/openthread/openthread/tree/master/src/cli), please scroll down on github for the Openthread command list.
```python

# get the Leader data set
>>> print(pymesh.cli('leaderdata'))
Partition ID: 828258
Weighting: 64
Data Version: 217
Stable Data Version: 108
Leader Router ID: 51
# sending a PING to another node from Pymesh
>>> pymesh.cli('ping fdde:ad00:beef:0:0:ff:fe00:d800')
'16 bytes from fdde:ad00:beef:0:0:ff:fe00:d800: icmp_seq=2 hlim=64 time=246ms\r\n'
```

## Working with Pymesh Sockets

Pymesh supports UDP sockets. These are channels of communication. They are created in the following way:

```python
import socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
```

A maximum of 3 sockets can be created, being bound on a certain IPv6 unicast and port number.

Make sure that the Pymesh is initialised before setting up any sockets.

{{% hint style="info" %}}
The Pymesh sockets support only the following socket methods: `close()` , `bind()`, `sendto()`, and `recvfrom()`.
{{% /hint %}}

#### socket.close()

This closes the socket.

Usage:

```python
s.close()
```

#### socket.bind(port\_number)
#### socket.bind((ipv6_string, port\_number))
This binds (links) a socket with an UDP port number with values between 1024 and 63535. There is an option to bind it with an IPv6 interface.
By default, if only the `port_number` is used, then the socket binds to all IPv6 unicast addresses. It is the equivalent to using `"::"` in place of the `ipv6_string`.

Usage:

```python
# binding socket with all IPv6 interfaces, like "::"
>>> s.bind(1234)
>>> pymesh.ipaddr()
['fdde:ad00:beef:0:0:ff:fe00:6800', 'fdde:ad00:beef:0:4623:91c8:64b2:d9ec', 'fe80:0:0:0:200:0:0:8']
# binding the socket on a specific pair of (IPv6, port_number)
>>> s.bind(('fdde:ad00:beef:0:4623:91c8:64b2:d9ec', 1235))
```

**Note: Please use double brackets when using the IPV6 and port_number.**

#### socket.sendto(bytes,(ip, port))

This sends the `bytes` buffer to `ip`, on the designated UDP `port`.

It returns the number of bytes sent.

Usage:

```python
>>> s.sendto("Hello World!", ("fdde:ad00:beef:0:0:ff:fe00:d800", 1234))
12
```

#### socket.recvfrom(bufsize)

This receives the bytes buffer on the socket. The maximum number of bytes is `bufsize`.

It returns a pair in the form: `(data_bytes, (ipv6_string, port_number))`

Usage:

```python

>>> s.recvfrom(512)
(b'Hello World!', ('fdde:ad00:beef:0:86c3:6130:98cc:6633', 1234))
```
