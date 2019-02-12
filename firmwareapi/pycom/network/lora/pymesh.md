# Pymesh - LoRa Mesh

This class provides Pymesh - LoRa Mesh protocol compliant for the LoRa network processor in the LoPy and FiPy. Below is an example demonstrating Pymesh initialisation and basic usage:

```python
from network import LoRa

# initialise LoRa
# the LoRa parameters (frecq, sf, bandwidth) has to be the same for all
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

## Additional Examples

For various other complete Pymesh examples, check Tutorials & Examples section (LoRa/Pymesh).

## Constructors

#### class network.LoRa.Mesh\(\)

Create and configure the Mesh object.

```python
from network import LoRa
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
pymesh = lora.Mesh()
```

## Methods

#### mesh.deinit\(\)

De-initialise Pymesh task. Any further Pymesh commands will return no answer.
To use again Pymesh the `LoRa.Mesh()` constructor has to be called.

```python
>>> pymesh.deinit()
True
>>> pymesh.neighbors()
>>> pymesh.leader()
```

#### mesh.state\(\)

Get node state inside Pymesh, which can be one of the following:
```
* PYMESH_ROLE_DISABLED = 0, ///< The Pymesh stack is disabled.
* PYMESH_ROLE_DETACHED = 1, ///< Not currently participating in a Pymesh.
* PYMESH_ROLE_CHILD    = 2, ///< The Pymesh Child role.
* PYMESH_ROLE_ROUTER   = 3, ///< The Pymesh Router role.
* PYMESH_ROLE_LEADER   = 4, ///< The Pymesh Leader role.
```

```python
# get node state inside Pymesh
>>> pymesh.state()
4
```
More info: https://openthread.io/guides/thread-primer/node-roles-and-types

#### mesh.single\(\)

Returns `True` if this node is the only Leader or Router in the current Mesh network. 

```python
>>> pymesh.single()
True
```

#### mesh.ipaddr\(\)

Returns all the IPv6 unicast addresses assigned on Pymesh interface.

```python
>>> pymesh.ipaddr()
['fdde:ad00:beef:0:0:ff:fe00:fc00', 'fdde:ad00:beef:0:0:ff:fe00:cc00', 'fdde:ad00:beef:0:86c3:6130:98cc:6633', 'fe80:0:0:0:301:101:101:104']
```
In the previous `pymesh.ipaddr()` answer, these are the individual IPv6:
* `fe80:0:0:0:301:101:101:104` - link-local IPv6
 * used to discover neighbors, configure links.
 * not routable.
 * always has a prefix of `fe80::/16`.
* `fdde:ad00:beef:0:86c3:6130:98cc:6633` - mesh-local identifier
 * independent of network topology.
 * does not change as the topology changes.
 * should be used by applications.
 * always has a prefix `fd00::/8`.
* `fdde:ad00:beef:0:0:ff:fe00:cc00` - routing locator (RLOC)
 * identifies a mesh interface, based on its location in the network topology.
 * Changes as the topology changes.
 * Generally not used by applications.
* `fdde:ad00:beef:0:0:ff:fe00:fc00` - Leader IPv6.

More info: https://openthread.io/guides/thread-primer/ipv6-addressing

#### mesh.rloc\(\)

Returns the routing locator (RLOC) IPv6 address.

```python
>>> pymesh.rloc()
52224
>>> hex(pymesh.rloc())
'0xcc00'
```

More info: https://openthread.io/guides/thread-primer/ipv6-addressing

#### mesh.neighbors\(\)

Returns a list with tuples containing information about neighbors, ie. all other nodes that have a direct radio connection to the calling node.

For each neighbor the following properties are returned:
* mac - LoRa MAC address.
* role - Child(2) or Router(3), implicitly Leader is shown as normal Router.
* rloc16 - the RLOC (more info [here](https://openthread.io/guides/thread-primer/ipv6-addressing)).
* rssi - the RSSI of the radio link (Received Signal Strength Indication) expressed in db.
* age - number of seconds since last data packet was received.

```python
>>> pymesh.neighbors()
[(mac=1, role=3, rloc16=25600, rssi=-37, age=19),
(mac=8121069065142870746, role=3, rloc16=55296, rssi=-27, age=15)]
>>> neighbors = pymesh.neighbors()
>>> neighbors[0].rssi
-37
```

#### mesh.routers\(\)

Returns a list with tuples containing information about all routers from Pymesh. Routers are Pymesh nodes that relay/route packets inside Pymesh.

For each Router the following properties are returned:
* mac - LoRa MAC address.
* rloc16 - the RLOC (more info [here](https://openthread.io/guides/thread-primer/ipv6-addressing)).
* id - the Pymesh internal ID, each Router has its own random unique ID.
* path_cost - the cost of the path from current node to this router.
* age - number of seconds since last keep-alive packet was received.

```python
>>> pymesh.routers()
[(mac=1, rloc16=25600, id=25, path_cost=1, age=12),
(mac=72340172838076676, rloc16=52224, id=51, path_cost=0, age=0),
(mac=8121069065142870746, rloc16=55296, id=54, path_cost=1, age=12)]
>>> routers = pymesh.routers()
>>> routers[0].rloc16
25600
```

#### mesh.leader\(\)

Returns information about Leader of the current Pymesh. can be called from any connected node. 

The following details are returned:
* part_id - partition id, the Pymesh internal network address.
* mac - the LoRa MAC address of the Leader.
* rloc16 - the Leader RLOC16.

```python
>>> pymesh.leader()
(part_id=828258, mac=72340172838076676, rloc16=52224)
```

#### mesh.rx_cb\(handler\)

Specify the callback handler executed when a new packet was received.

```python
def receive_all_data(self):
    """ receives all packages on socket """

    while True:
        rcv_data, rcv_addr = sock.recvfrom(512)
        if len(rcv_data) == 0:
            break  # out of while, no packet
        rcv_ip = rcv_addr[0]
        rcv_port = rcv_addr[1]
        print('Incomming %d bytes from %s (port %d):' %
              (len(rcv_data), rcv_ip, rcv_port))
        print(rcv_data)

# set RX callback
pymesh.rx_cb(receive_all_data)
```

#### mesh.border_router\(ipv6_net_address, preference_level\)

Sets as Border Router the current node, by specifying the external IPv6 network address(prefix), which should be used for any IPv6 packet to be sent outside of Pymesh. The parameters details are:
* ipv6_net_address
 * has to be a valid IPv6 network address containing IP and mask, for ex `"2001:cafe:cafe:cafe::/64"`.
 * all the nodes from the Pymesh will receive a random additional IPv6 unicast address, from this network address.
 * a IPv6 packet which has as destination this prefix, will be routed to this node.
 * to actually catch this IPv6 packet, a socket has to be created on a port.
* preference_level - should be a value (-1: low, 0: normal, 1: high)
  * in case multiple Border Routers are being declared with the same prefix and the same path cost, the one with the highest preference is used.

```python
# IPv6 addresses, before setting Border Router
>>> pymesh.ipaddr()
['fdde:ad00:beef:0:0:ff:fe00:fc00', 'fdde:ad00:beef:0:0:ff:fe00:cc00', 'fdde:ad00:beef:0:86c3:6130:98cc:6633', 'fe80:0:0:0:301:101:101:104']
# setting Border Router
>>> pymesh.border_router("2001:cafe:cafe:cafe::/64", 0)
0
#checking a new IPv6 address is assigned
>>> pymesh.ipaddr()
['2001:cafe:cafe:cafe:a5d2:6934:9acd:66b3', 'fdde:ad00:beef:0:0:ff:fe00:fc00', 'fdde:ad00:beef:0:0:ff:fe00:cc00', 'fdde:ad00:beef:0:86c3:6130:98cc:6633', 'fe80:0:0:0:301:101:101:104']
>>>
```

#### mesh.cli\(\)

Sends a CLI command to the internal openthread engine; the list of CLI commands is [here](https://github.com/openthread/openthread/blob/c482301ec73b80985445102e4d0a936346172ddb/src/cli/README.md)
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

## Working with Pymesh LoRa Sockets

Pymesh supports only UDP sockets (not-acknowledged). They are created in the following way:

```python
import socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
```

Pymesh socket is created, if the Mesh was enabled before \(`lora.Mesh()` was called\).

{% hint style="info" %}
The Pymesh sockets supports only the following socket methods: `close()` , `bind()`, `sendto()`, and `recvfrom()`.
{% endhint %}

LoRa sockets support the following standard methods from the socket module:

#### socket.close\(\)

Closes the socket.

Usage:

```python
s.close()
```

#### socket.bind\(port\_number\)

Binds (links) an UDP port number (values 1024 to 63535), with the Pymesh network interface (implicitly `"::"` - all IPv6 unicast addresses).

Usage:

```python
s.bind(1234)
```

#### socket.sendto\(bytes,\(ip, port\)\)

Sends `bytes` buffer to `ip`, on the designated UDP `port`. Returns the number of bytes sent.

Usage:

```python
>>> s.sendto("Hello World!", ("fdde:ad00:beef:0:0:ff:fe00:d800", 1234))
12
```

#### socket.recvfrom\(bufsize\)

This method is useful to know the destination port number of the message received. Returns a pair of the form: `(data_bytes, (ipv6_string, port_number))`

Usage:

```python
>>> s.recvfrom(512)
(b'Hello World!', ('fdde:ad00:beef:0:86c3:6130:98cc:6633', 1234))
```
