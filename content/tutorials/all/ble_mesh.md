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
import time

def blink_led(n):
    for x in range(n):
        pycom.rgbled(0x000000) # off
        time.sleep(0.3)
        pycom.rgbled(0x555500) # yellow on
        time.sleep(0.3)

def server_cb(new_state, event, recv_op):
    print("Set State: ", new_state)

def prov_callback(event, oob_pass):
    if(event == BLE_Mesh.PROV_REGISTER_EVT or event == BLE_Mesh.PROV_RESET_EVT):
        # Yellow if not Provision yet or Reseted
        pycom.rgbled(0x555500)
    if(event == BLE_Mesh.PROV_COMPLETE_EVT):
        # Green if Provisioned
        pycom.rgbled(0x007f00)
    if(event == BLE_Mesh.PROV_OUTPUT_OOB_REQ_EVT):
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
model_server = element.add_model(BLE_Mesh.SENSOR, BLE_Mesh.SERVER, callback=server_cb, sen_min = -1, sen_max = 1, sen_res = 0.1)

# Initialize BLE_Mesh
BLE_Mesh.init("Pycom Server", auth=BLE_Mesh.OOB_OUTPUT, callback=prov_callback)

# Turn on Provisioning Advertisement
BLE_Mesh.set_node_prov(BLE_Mesh.PROV_ADV|BLE_Mesh.PROV_GATT)
```

## Client Example

```python
from network import Bluetooth
import pycom

def prov_callback(event, oob_pass):
    if(event == BLE_Mesh.PROV_REGISTER_EVT or event == BLE_Mesh.PROV_RESET_EVT):
        # Yellow if not Provision yet or Reseted
        pycom.rgbled(0x555500)
    if(event == BLE_Mesh.PROV_COMPLETE_EVT):
        # Green if Provisioned
        pycom.rgbled(0x007f00)

def client_cb(new_state, event, recv_op):
    print("Set State: ", new_state)

# BLE Mesh module
BLE_Mesh = Bluetooth.BLE_Mesh

# Turn off the heartbeat behavior of the LED
pycom.heartbeat(False)

# Need to turn ON Bluetooth before using BLE Mesh
bluetooth = Bluetooth()

# Create a Primary Element with GATT Proxy feature and add a Server model to the Element
element = BLE_Mesh.create_element(primary=True, feature=BLE_Mesh.GATT_PROXY)
model_client = element.add_model(BLE_Mesh.SENSOR, BLE_Mesh.CLIENT, callback=client_cb, sen_min = -1, sen_max = 1, sen_res = 0.1)

# Initialize BLE_Mesh
BLE_Mesh.init("Pycom Client", callback=prov_callback)

# Turn on Provisioning Advertisement
BLE_Mesh.set_node_prov(BLE_Mesh.PROV_ADV|BLE_Mesh.PROV_GATT)
```
