---
title: "BLE Callback"
---

In the following examples, we'll explain how to use the callback functionality of the Bluetooth module on both the server and client side. This can be used to detect when nodes connect and disconnect from the device, and when they get subscribed and read data. 

## BLE Server
This example will create a BLE server named `FiPy 45`, which publishes 'battery levels' over a service every second, starting at 100 and going down to 0. The example will also notify you in the REPL of any BLE events.

```python
from network import Bluetooth
from machine import Timer

battery = 100
update = False
def conn_cb(chr):
    events = chr.events()
    if events & Bluetooth.CLIENT_CONNECTED:
        print('client connected')
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print('client disconnected')
        update = False

def chr1_handler(chr, data):
    global battery
    global update
    events = chr.events()
    print("events: ",events)
    if events & (Bluetooth.CHAR_READ_EVENT | Bluetooth.CHAR_SUBSCRIBE_EVENT):
        chr.value(battery)
        print("transmitted :", battery)
        if (events & Bluetooth.CHAR_SUBSCRIBE_EVENT):
            update = True

bluetooth = Bluetooth()
bluetooth.set_advertisement(name='FiPy 45', manufacturer_data="Pycom", service_uuid=0xec00)

bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)
bluetooth.advertise(True)

srv1 = bluetooth.service(uuid=0xec00, isprimary=True,nbr_chars=1)

chr1 = srv1.characteristic(uuid=0xec0e, value='read_from_here') #client reads from here

chr1.callback(trigger=(Bluetooth.CHAR_READ_EVENT | Bluetooth.CHAR_SUBSCRIBE_EVENT), handler=chr1_handler)
print('Start BLE service')
def update_handler(update_alarm):
    global battery
    global update
    battery-=1
    if battery == 1:
        battery = 100
    if update:
        chr1.value(str(battery))

update_alarm = Timer.Alarm(update_handler, 1, periodic=True)

```
## BLE Client
This example will create a BLE Client, which is able to the server example above. 

```python
from network import Bluetooth
from machine import Timer

def char_notify_callback(char, arg):
    char_value = (char.value())
    print("New value: {}".format(char_value))

bt = Bluetooth()
print('Start scanning for BLE services')
bt.start_scan(-1)
adv = None
while(True):
    adv = bt.get_adv()
    if adv:
        try:
            if bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL)=="FiPy 45":
                conn = bt.connect(adv.mac)
                print("Connected to FiPy 45")
                try:
                    services = conn.services()
                    for service in services:
                        chars = service.characteristics()
                        for char in chars:
                            c_uuid = char.uuid()
                            if c_uuid == 0xec0e:
                                if (char.properties() & Bluetooth.PROP_NOTIFY):
                                    char.callback(trigger=Bluetooth.CHAR_NOTIFY_EVENT, handler=char_notify_callback)
                                    print(c_uuid)
                                    break
                except:
                    continue
        except:
            continue

bt.stop_scan()
bt.disconnect_client()

```