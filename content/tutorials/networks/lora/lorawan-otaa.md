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

**Note for US915 / AU915 regions:** moste LoRaWAN gateways are configured to listen to 8 channels only, while the region supports up to 64 uplink channels. In order to receive packets, please confirm the frequency plan of your gateway with the channels configured on your device. By default, our devices will transmit on all 64 channels, meaning you might receive packets intermittently. The most common configuration is `FSB2`, or channels 8-15. Uncomment the respective section in the example below to select the these uplink channels. It is possible to switch to a different sub-band by selecting a different channel set. For more information, have a look [here](https://www.thethingsindustries.com/docs/reference/frequency-plans/)


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

# Uncomment for US915 / AU915 & Pygate
# for i in range(0,8):
#     lora.remove_channel(i)
# for i in range(16,65):
#     lora.remove_channel(i)
# for i in range(66,72):
#     lora.remove_channel(i)

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
