---
title: "BLE Mesh"
aliases:
    - tutorials/all/ble_mesh.html
    - tutorials/all/ble_mesh.md
    - chapter/tutorials/all/ble_mesh
---

BLE Mesh module enables many-to-many device connections, based on Bluetooth module.

## Server Example

```python
from network import Bluetooth
import pycom

def blink_led(n):
    for x in range(n):
        pycom.rgbled(0xffff00) # yellow on
        time.sleep(0.3)
        pycom.rgbled(0x000000) # off
        time.sleep(0.3)

def server_cb(model, event, recv_op):
    print("Set State: ", model.value())

    # Turn on LED on board based on State
    if model.value() == True:
        pycom.rgbled(0x007f00) # green
    else:
        pycom.rgbled(0x7f0000) # red

def prov_callback(oob_type, oob_pass):
    print("OOB Pass: " + str(oob_pass))
    # Blink LED 'oob_pass' times, to see visually OOB pass
    blink_led(oob_pass)

# BLE Mesh module
BLE_Mesh = Bluetooth.BLE_Mesh

# Turn off the heartbeat behavior of the LED
pycom.heartbeat(False)

# Need to turn ON Bluetooth before using BLE Mesh
bluetooth = Bluetooth()

# Create a Primary Element with GATT Proxy feature and add a Server model to the Element
element = BLE_Mesh.create_element(primary=True, feature=BLE_Mesh.GATT_PROXY)
model_server = element.add_model(BLE_Mesh.GENERIC, BLE_Mesh.ONOFF, BLE_Mesh.SERVER, callback=server_cb)

# Initialize BLE_Mesh
BLE_Mesh.init("Pycom Server", auth=BLE_Mesh.OOB_OUTPUT)

# Turn on Provisioning Advertisement
BLE_Mesh.set_node_prov(BLE_Mesh.PROV_ADV|BLE_Mesh.PROV_GATT, callback=prov_callback)
```

## Client Example

```python
from network import Bluetooth
import pycom

def client_cb(model, event, recv_op):
    print("Set State: ", model.value())

def prov_callback(oob_type, oob_pass):
    print("OOB Pass: ", oob_pass)

# BLE Mesh module
BLE_Mesh = Bluetooth.BLE_Mesh

# Turn off the heartbeat behavior of the LED
pycom.heartbeat(False)

# Need to turn ON Bluetooth before using BLE Mesh
bluetooth = Bluetooth()

# Create a Primary Element with GATT Proxy feature and add a Server model to the Element
element = BLE_Mesh.create_element(primary=True, feature=BLE_Mesh.GATT_PROXY)
model_client = element.add_model(BLE_Mesh.GENERIC, BLE_Mesh.ONOFF, BLE_Mesh.CLIENT, callback=client_cb)

# Initialize BLE_Mesh
BLE_Mesh.init("Pycom Client")

# Turn on Provisioning Advertisement
BLE_Mesh.set_node_prov(BLE_Mesh.PROV_ADV|BLE_Mesh.PROV_GATT, callback=prov_callback)
```
