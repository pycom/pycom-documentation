---
title: "Pymesh Library CLI"
aliases:
  - pymesh/simple-example
---

## Overview

The Pymesh micropython library is included as a `frozen python script` in the Pymesh firmware releases. It is also available as [open-source micropython script](https://github.com/pycom/pycom-libraries/blob/master/pymesh/pymesh_frozen/lib/cli.py).

Instead of REPL, a specific Pymesh CLI interprets commands. This is shown by `>`. The CLI is executed on a separate thread inside the Pymesh library.

{{% hint style="info" %}}
* The CLI needs to be started using the `pymesh.cli_start()` method.
* In the CLI the `h` command will print the list of available commands.
* The command `stop` will break the CLI thread.
{{% /hint %}}


For example:
```
>mml
mesh_mac_list  [1, 6, 2]
```

## Internal CLI

```
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

### Debug commands

```
>stop
CLI stopped
>>>
```
This command stops the CLI thread.

```
> debug
5
```
This command displays or sets the debug level. Possible values are:
```
# recommended debug levels, from the most verbose to off
DEBUG_DEBG = const(5)
DEBUG_INFO = const(4)
DEBUG_NOTE = const(3)
DEBUG_WARN = const(2)
DEBUG_CRIT = const(1)
DEBUG_NONE = const(0)
```

```
>pause
Pymesh pausing
>resume
Pymesh resuming
```
This pair of commands stops temporarily and resumes the Pymesh executing threads.

A possible application is to use LoRaWAN when Pymesh is paused. [An example is here](https://github.com/pycom/pycom-libraries/blob/master/pymesh/pymesh_frozen/lorawan/main.py).

```
>rst
Mesh Reset NVM settings ...
deepsleep_init
>deepsleep_now
Cleanup code, all Alarms cb should be stopped
Going to deepsleep for 1 seconds
```
This resets the Pymesh parameters saved in NVM, and resets the Node.

```
>sleep
(time[sec])<10
deepsleep_init
>deepsleep_now
Cleanup code, all Alarms cb should be stopped
Going to deepsleep for 10 seconds
```
This puts the device into deepsleep for a designated number of seconds.

```
>buf
Buffer info: total: 200
free: 200
6lo send: 0 0
6lo reas: 0 0
ip6: 0 0
mpl: 0 0
mle: 0 0
arp: 0 0
coap: 0 0
coap secure: 0 0
application coap: 0 0
```
This displays the number of buffers for each layer of the Pymesh.

```
>ot
(openthread cli)<leaderdata
Partition ID: 1494439163
Weighting: 64
Data Version: 66
Stable Data Version: 108
Leader Router ID: 46
```
This executes an Openthread CLI command. The list of CLI commands is [here](https://github.com/openthread/openthread/tree/master/src/cli), please scroll down on github for the Openthread command list.

### Commands showing Pymesh internal data

```
>mac
1
```
This shows the LoRa MAC or sets it to a known value. This address is used as a unique identifier within the Pymesh.

This can be useful for debugging and the MAC could be set to  consecutive small numbers, such as `0x1`, `0x2`, ...

```
>mml
mesh_mac_list  [1, 6, 2]
```
This shows the list of all MAC Nodes attached to Pymesh. It inquires the Leader, which centralises this data.

```
>mp
Send pack: 0xF3 to IP fdde:ad00:beef:0:0:ff:fe00:fc00
last_mesh_pairs [[2, 6, -87], [1, 6, -77]]
```
This shows the Mesh Pairs list. It lists each directly connected node (by their MAC address) and the averaged RSSI value.

```
>mni
last_mesh_node_info {1: {"ip": 2048, "l": {"lng": 5.45313, "lat": 51.45}, "a": 10, "r": 3, "nn": 1, "nei": [[6, 55296, 3, -76, 23]]}, 6: {"ip": 55296, "l": {"lng": 5.45313, "lat": 51.45}, "a": 7, "r": 3, "nn": 2, "nei": [[2, 50176, 3, -89, 28], [1, 2048, 3, -77, 23]]}, 2: {"ip": 50176, "l": {"lng": 5.45313, "lat": 51.45}, "a": 7, "r": 3, "nn": 1, "nei": [[6, 55296, 3, -86, 25]]}}
```
This shows the properties for all the nodes in this Pymesh, together with its neighbours.

```
>s
(to)<1
(txt)<Hello World!
1945688: Send Msg ---------------------->>>>>>>>
Added new message for 1: Hello World!
Send pack: 0x10 to IP fdde:ad00:beef:0::1
True
>Incoming 13 bytes from fdde:ad00:beef:0:f67b:3d1e:f07:8341 (port 1234):
PACK_MESSAGE_ACK received
1945883 =================  ACK RECEIVED :) :) :)
```
This sends text messages to another Node within the Pymesh. The messaging node waits for acknowledgement (ACK message type) from the destination node.

```
>ws
(to)<1
ACK? mac 1, id 12345 => 1
True
```
This shows if the message was acknowledged by the destination Node.

```
>rm
{'b': (b'Hello World!',), 'id': 12345, 'ts': 3301, 'from': 6}
```
This shows the received messages.

### Auxiliary commands
```
>gps
(lat [Enter for read])<
Gps: (51.45, 5.45313)

> gps
(lat [Enter for read])<11.234
(lon)<23.45
Gps: (11.234, 23.45)
```

This reads the GPS coordinates or sets them to known values.

```
>config
{'ble_api': True, 'MAC': 6, 'autostart': True, 'debug': 5, 'LoRa': {'sf': 7, 'region': 5, 'freq': 863000000, 'bandwidth': 2}, 'ble_name_prefix': 'PyGo ', 'Pymesh': {'key': '112233'}}
```
This displays the configuration, stored on `/flash/pymesh_config.json`.

### Border Router specific

```
>br
(state 0=Disable, 1=Enable, 2=Display [Default Display])<
Border Router state:  []

>br
(state 0=Disable, 1=Enable, 2=Display [Default Display])<1
(priority -1=Low, 0=Normal or 1=High [Default Normal])<
State: True BR:  []
Force add BR
BR:  [(net='2001:cafe:cafe:cafe::/64', preference=0)]

>br
(state 0=Disable, 1=Enable, 2=Display [Default Display])<
Border Router state:  [(net='2001:cafe:cafe:cafe::/64', preference=0)]
```
This enables/disables the Border Router functionality of the current node. It also shows the state of the current node as Border Router.

```
>brs
brs
(message<)
(IP destination, Mesh-external [Default: 1:2:3::4])<
(port destination [Default: 5555])<
Send BR message: {'ip': '1:2:3::4', 'b': '', 'port': 5555}
```
This sends a packet to an external IP address, outside of the Pymesh. The packet will be received by the designated Border Router and it can be further forwarded to another network interface, such as: BLE, Wifi, Sigfox or Cellular (Fipy only).
