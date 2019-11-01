---
title: "Pymesh Library Bluetooth LE RPC"
aliases:
  - pymesh/simple-example
---

## RPC protocol

It is implemented in [ble_rpc.py](https://github.com/pycom/pycom-libraries/blob/master/lib/pymesh/lib/ble_rpc.py).

In the class `RPCHandler` methods can be added to expand RPC set.

The internal RPC are calling methods from file `mesh_interface.py`.

## Methods

#### mesh_is_connected()

This returns `True` if Node is connected to a Pymesh.

#### mesh_ip()

This returns the IP RLOC16 in a string.

#### set_gps(latitude, longitude)

This sets the location coordinates.

#### get_mesh_mac_list()

This returns the list of distinct MAC address that are within this mesh network, for example `[mac1, mac2, mac 3]`.`

#### get_mesh_pairs()

This returns the list of pairs that form a mesh connection, as shown bellow:

```
[
    ('mac1', 'mac2', rssi),
    ('mac1', 'mac3', rssi),
    #...
]
```

#### get_node_info(mac_id = ' ')

This returns the node data for a specified mac address, or own data if `mac_id` is not specified. Node data is dictionary with the following structure:

```        
{
    'ip': 4c00,   # last 2bytes from the ip v6 RLOC16 address
    'r': 3,    # not_connected:0 | child:1 | leader:2 | router:3
    'a': 100,  # age[sec], time since last info about this node
    'nn' : 20 # neighbours number
    'nei': {  # neighbours enumerated, if any
    (mac, ip, role, rssi, age),
    (mac, ip, role, rssi, age)
    }
    'l': { # location, if available
    'lng': 7,
    'lat': 20,
    },
    'b' : { # BLE infos
    'a': 100    # age, seconds since last ping with that device, None if properly disconnected
    'id': '<UUID>' # 16byte
    'n': '',           # name, max. 16 chars
    }
}
```

#### send_message(data)

This sends a message to another node. It return True if there is a buffer to store it (to be sent onwards).

`data` is a dictionary with the following structure:
```
{
    'to': 0x5,
    'b': 'text',
    'id': 12345,
    'ts': 123123123,
}
```


#### send_message_was_sent(mac, msg_id)

This checks if acknowledgement was received from the specified  `mac` and `msg_id`. It returns `True` if message was delivered.

#### receive_message()

This returns the received messages, in a dictionary with the following structure:
```
{
  'b': 'text',
  'from': 'ble_device_id',
  'ts': 123123123,
  'id': '<uuid>',
}
```
