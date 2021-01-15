---
title: "LoRa NVRAM"
aliases:
    - tutorials/lora/nvram.html
    - tutorials/lora/nvram.md
    - chapter/tutorials/lora/nvram
---

See the example below on how to use the lora nvram methods. You can use this to for example send a packet of sensor data over LoRa, and then enter deepsleep to save power. It is also possible to use OTAA instead of ABP by changing the activation method and authentication parameters. Note that the non volatile LoRa storage will be erased after it is restored, meaning you will have to save it again before sleeping, _and_ it is not possible to restore the values twice without saving in between.

```python
import machine
import time
from network import LoRa
import socket
import ubinascii

sleep_time = 10000 # sleep for 10 seconds
print("init LoRa")
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
time.sleep(1) #Allows us to exit the code using ctrl+c

# create an ABP authentication params
dev_addr = struct.unpack(">l", ubinascii.unhexlify('00000005'))[0]
nwk_swkey = ubinascii.unhexlify('2B7E151628AED2A6ABF7158809CF4F3C')
app_swkey = ubinascii.unhexlify('2B7E151628AED2A6ABF7158809CF4F3C')

lora.nvram_restore()
if(lora.has_joined() == False):
    print("LoRa not joined yet")
    lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))
else:
    print("LoRa Joined")

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)
# send some data
print("[send_lora] sending {}".format([0,1,2]))

s.send(bytes([0, 1, 2]))
# make the socket non-blocking
# (because if there's no data received it will block forever...)
s.setblocking(False)
# get any data received (if any...)
data = s.recv(64)
lora.nvram_save()
print("received: {}".format(data))

print("sleeping for {} ms".format(sleep_time))
machine.deepsleep(sleep_time)
print("this will never get printed")
```
