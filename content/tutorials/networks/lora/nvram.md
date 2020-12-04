---
title: "non-volatile RAM"
aliases:
    - tutorials/lora/nvram.html
    - tutorials/lora/nvram.md
    - chapter/tutorials/lora/nvram
---

See the example below on how to use the lora nvram methods: 

```python
import machine
import time
from network import LoRa
import socket
import ubinascii

sleep_time = 1000
print("init LoRa")
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
for i in range(0,10):
    time.sleep(0.1) #be able to ctrl+c out of this
# create an ABP authentication params
dev_addr = struct.unpack(">l", ubinascii.unhexlify(''))[0]
nwk_swkey = ubinascii.unhexlify('')
app_swkey = ubinascii.unhexlify('')
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
```