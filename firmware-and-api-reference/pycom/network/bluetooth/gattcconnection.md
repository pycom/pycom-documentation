# GATTCConnection

The GATT Client is the device that requests data from the server, otherwise known as the master device \(commonly this might be a phone/tablet/PC\). All transactions are initiated by the master, which receives a response from the slave.

## Methods

#### connection.disconnect\(\)

Closes the BLE connection. Returns `None`.

#### connection.isconnected\(\)

Returns `True` if the connection is still open. `False` otherwise.

Example:

```python
from network import Bluetooth
import ubinascii
bluetooth = Bluetooth()

# scan until we can connect to any BLE device around
bluetooth.start_scan(-1)
adv = None
while True:
    adv = bluetooth.get_adv()
    if adv:
        try:
            bluetooth.connect(adv.mac)
        except:
            # start scanning again
            bluetooth.start_scan(-1)
            continue
        break
print("Connected to device with addr = {}".format(ubinascii.hexlify(adv.mac)))
```

#### connection.services\(\)

Performs a service search on the connected BLE peripheral \(server\) a returns a list containing objects of the class GATTCService if the search succeeds.

Example:

```python
# assuming that a BLE connection is already open
services = connection.services()
print(services)
for service in services:
    print(service.uuid())
```

