---
title: "GATTSCharacteristic"
aliases:
    - firmwareapi/pycom/network/bluetooth/gattscharacteristic.html
    - firmwareapi/pycom/network/bluetooth/gattscharacteristic.md
---

The smallest concept in GATT is the Characteristic, which encapsulates a single data point (though it may contain an array of related data, such as X/Y/Z values from a 3-axis accelerometer, longitude and latitude from a GPS, etc.).

The following class allows you to manage Server characteristics.

## Methods

#### characteristic.value(\[value\])

Gets or sets the value of the characteristic. Can take an integer, a string or a bytes object.

```python

characteristic.value(123) # set characteristic value to an integer with the value 123
characteristic.value() # get characteristic value
```

#### characteristic.callback(trigger=None, handler=None, arg=None)

Creates a callback that will be executed when any of the triggers occurs. The arguments are:

* `trigger` can be either `Bluetooth.CHAR_READ_EVENT` or `Bluetooth.CHAR_WRITE_EVENT`.
* `handler` is the function that will be executed when the callback is triggered.
* `arg` is the argument that gets passed to the callback. If nothing is given, the characteristic object that owns the callback will be used.

An example of how this could be implemented can be seen in the [`characteristic.events()` ](gattscharacteristic.md#characteristic-events)section.

#### characteristic.events()

Returns a value with bit flags identifying the events that have occurred since the last call. Calling this function clears the events.

An example of advertising and creating services on the device:

```python

from network import Bluetooth

bluetooth = Bluetooth()
bluetooth.set_advertisement(name='LoPy', service_uuid=b'1234567890123456')

def conn_cb (bt_o):
    events = bt_o.events()
    if  events & Bluetooth.CLIENT_CONNECTED:
        print("Client connected")
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print("Client disconnected")

bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)

bluetooth.advertise(True)

srv1 = bluetooth.service(uuid=b'1234567890123456', isprimary=True)

chr1 = srv1.characteristic(uuid=b'ab34567890123456', value=5)

char1_read_counter = 0
def char1_cb_handler(chr):
    global char1_read_counter
    char1_read_counter += 1

    events = chr.events()
    if  events & Bluetooth.CHAR_WRITE_EVENT:
        print("Write request with value = {}".format(chr.value()))
    else:
        if char1_read_counter < 3:
            print('Read request on char 1')
        else:
            return 'ABC DEF'

char1_cb = chr1.callback(trigger=Bluetooth.CHAR_WRITE_EVENT | Bluetooth.CHAR_READ_EVENT, handler=char1_cb_handler)

srv2 = bluetooth.service(uuid=1234, isprimary=True)

chr2 = srv2.characteristic(uuid=4567, value=0x1234)
char2_read_counter = 0xF0
def char2_cb_handler(chr):
    global char2_read_counter
    char2_read_counter += 1
    if char2_read_counter > 0xF1:
        return char2_read_counter

char2_cb = chr2.callback(trigger=Bluetooth.CHAR_READ_EVENT, handler=char2_cb_handler)
```

