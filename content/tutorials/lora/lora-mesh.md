---
title: "Pymesh"
aliases:
    - tutorials/lora/lora-mesh.html
    - tutorials/lora/lora-mesh.md
    - chapter/tutorials/lora/lora-mesh
---

{{% hint style="info" %}}	
These API's are currently only available in the latest RC builds.
{{% /hint %}}

The Pymesh LoRa Mesh is implemented using [OpenThread](https://openthread.io/guides/thread-primer).

To understand the OpenThread terms and overall functionality, these guides are highly recommended:

* [What is Thread?](https://openthread.io/guides/thread-primer)
* [Node Roles and Types](https://openthread.io/guides/thread-primer/node-roles-and-types)
* [IPv6 Addressing](https://openthread.io/guides/thread-primer/ipv6-addressing) (especially, RLOC unicast address)

Important, all the OpenThread CLI commands are accessible using `LoRa.cli("command")`, the complete list of commands is [here](https://github.com/openthread/openthread/blob/c482301ec73b80985445102e4d0a936346172ddb/src/cli/README). Please note some commands, can't execute, as some functionalities are not implemented (ex: Commissioning Role, Joiner Role, DNS).

This example shows how to:

* enable LoRa-Mesh network
* find neighbors (parent, children, other router direct connections)
* send PING to neighbors
* open UDP socket for:
  * listening incoming UDP packets and answering back (ACK)
  * sending packets to all neighbors
* toggle LED as packet/ping is received.

{{% hint style="info" %}}
The LoRa-Mesh socket supports only the following socket methods: `close()`, `bind()`, `sendto()`, and `recvfrom()`.
{{< /hint >}}

**Lora Mesh example**

* Source: [https://github.com/pycom/pycom-libraries/blob/master/lib/lora\_mesh/main.py](https://github.com/pycom/pycom-libraries/blob/master/lib/lora_mesh/main.py)
* `Loramesh` micropython library is available at [https://github.com/pycom/pycom-libraries/blob/master/lib/lora\_mesh/loramesh.py](https://github.com/pycom/pycom-libraries/blob/master/lib/lora_mesh/loramesh.py).

```python

from network import LoRa
import socket
import time
import utime
import ubinascii
import pycom
import machine

from loramesh import Loramesh

pycom.wifi_on_boot(False)
pycom.heartbeat(False)

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868, bandwidth=LoRa.BW_125KHZ, sf=7)
MAC = str(ubinascii.hexlify(lora.mac()))[2:-1]
print("LoRa MAC: %s"%MAC)

mesh = Loramesh(lora)

# waiting until it connected to Mesh network
while True:
    mesh.led_state()
    print("%d: State %s, single %s"%(time.time(), mesh.cli('state'), mesh.cli('singleton')))
    time.sleep(2)
    if not mesh.is_connected():
        continue

    print('Neighbors found: %s'%mesh.neighbors())
    break

# create UDP socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
myport = 1234
s.bind(myport)

# handler responisble for receiving packets on UDP Pymesh socket
def receive_pack():
    # listen for incomming packets
    while True:
        rcv_data, rcv_addr = s.recvfrom(128)
        if len(rcv_data) == 0:
            break
        rcv_ip = rcv_addr[0]
        rcv_port = rcv_addr[1]
        print('Incomming %d bytes from %s (port %d)'%(len(rcv_data), rcv_ip, rcv_port))
        print(rcv_data)
        # could send some ACK pack:
        if rcv_data.startswith("Hello"):
            try:
                s.sendto('ACK ' + MAC + ' ' + str(rcv_data)[2:-1], (rcv_ip, rcv_port))
            except Exception:
                pass
        mesh.blink(7, .3)

pack_num = 1
msg = "Hello World! MAC: " + MAC + ", pack: "
ip = mesh.ip()
mesh.mesh.rx_cb(receive_pack)

# infinite main loop
while True:
    mesh.led_state()
    print("%d: State %s, single %s, IP %s"%(time.time(), mesh.cli('state'), mesh.cli('singleton'), mesh.ip()))

    # check if topology changes, maybe RLOC IPv6 changed
    new_ip = mesh.ip()
    if ip != new_ip:
        print("IP changed from: %s to %s"%(ip, new_ip))
        ip = new_ip

    # update neighbors list
    neigbors = mesh.neighbors_ip()
    print("%d neighbors, IPv6 list: %s"%(len(neigbors), neigbors))

    # send PING and UDP packets to all neighbors
    for neighbor in neigbors:
        if mesh.ping(neighbor) > 0:
            print('Ping OK from neighbor %s'%neighbor)
            mesh.blink(10, .1)
        else:
            print('Ping not received from neighbor %s'%neighbor)

        time.sleep(10)

        pack_num = pack_num + 1
        try:
            s.sendto(msg + str(pack_num), (neighbor, myport))
            print('Sent message to %s'%(neighbor))
        except Exception:
            pass
        time.sleep(20 + machine.rng()%20)

    # random sleep time
    time.sleep(30 + machine.rng()%30)

```
