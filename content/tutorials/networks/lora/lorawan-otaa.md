---
title: "LoRaWAN with OTAA"
aliases:
    - tutorials/lora/lorawan-otaa.html
    - tutorials/lora/lorawan-otaa.md
    - chapter/tutorials/lora/lorawan-otaa
---

OTAA stands for Over The Air Authentication. With this method the LoPy sends a Join request to the LoRaWAN Gateway using the `app_eui` and `app_key` provided in your LoRaWAN application (Like TheThingsNetwork, Chirpstack etc.). If the keys are correct the Gateway will reply to the LoPy with a join accept message and from that point on the LoPy is able to send and receive packets to/from the Gateway. If the keys are incorrect no response will be received and the `has_joined()` method will always return `False`.

The example below attempts to get any data received after sending the frame. Keep in mind that the Gateway might not be sending any data back, therefore we make the socket non-blocking before attempting to receive, in order to prevent getting stuck waiting for a packet that will never arrive.

If everything works correctly, the device will print `Joined` to the terminal, and you should see a data packet arrive in your LoRaWAN application containing `0x01 0x02 0x03`


Note: if the `dev_eui` it is not provided, the LoRa MAC of the device will be used in its place. You will need to change the `dev_eui` in your LoRaWAN application to the LoRa MAC address of the device. You can get the LoRa MAC using:
```python
from network import LoRa
import binascii
print(binascii.hexlify(LoRa().mac()).upper())
```

## EU868

```python
from network import LoRa
import socket
import time
import ubinascii

# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# create an OTAA authentication parameters, change them to the provided credentials
app_eui = ubinascii.unhexlify('ADA4DAE3AC12676B')
app_key = ubinascii.unhexlify('11B0282A189B75B0B4D2D8C7FA38548B')
#uncomment to use LoRaWAN application provided dev_eui
#dev_eui = ubinascii.unhexlify('70B3D549938EA1EE')

# join a network using OTAA (Over the Air Activation)
#uncomment below to use LoRaWAN application provided dev_eui
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
#lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')

print('Joined')
# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

# send some data
s.send(bytes([0x01, 0x02, 0x03]))

# make the socket non-blocking
# (because if there's no data received it will block forever...)
s.setblocking(False)

# get any data received (if any...)
data = s.recv(64)
print(data)
```

## US915

For US915, there are 64 channels available. Note that the Pygate only listens to 8 channels. To make your messages always transmitted on the channels listened to by the pygate, you can use the following:

```python

from network import LoRa
import socket
import ubinascii
import struct
import time
# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)

print("joining")
# create an OTAA authentication parameters, change them to the provided credentials
app_eui = ubinascii.unhexlify('ADA4DAE3AC12676B')
app_key = ubinascii.unhexlify('11B0282A189B75B0B4D2D8C7FA38548B')
#uncomment to use LoRaWAN application provided dev_eui
#dev_eui = ubinascii.unhexlify('70B3D549938EA1EE')



for i in range(0,64):
    lora.remove_channel(i)
    
lora.add_channel(0, frequency=903900000, dr_min=0, dr_max=3)
lora.add_channel(1, frequency=904100000, dr_min=0, dr_max=3)
lora.add_channel(2, frequency=904300000, dr_min=0, dr_max=3)
lora.add_channel(3, frequency=904500000, dr_min=0, dr_max=3)
lora.add_channel(4, frequency=904700000, dr_min=0, dr_max=3)
lora.add_channel(5, frequency=904900000, dr_min=0, dr_max=3)
lora.add_channel(6, frequency=905100000, dr_min=0, dr_max=3)
lora.add_channel(7, frequency=905300000, dr_min=0, dr_max=3)


# join a network using OTAA (Over the Air Activation)
#uncomment below to use LoRaWAN application provided dev_eui
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
#lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 3)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

# send some data
s.send(bytes([0x01, 0x02, 0x03]))

# make the socket non-blocking
# (because if there's no data received it will block forever...)
s.setblocking(False)

# get any data received (if any...)
data = s.recv(64)
print(data)

```
