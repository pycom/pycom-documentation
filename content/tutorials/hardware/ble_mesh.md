---
title: "Pymesh BLE Examples"
aliases:
    - tutorials/all/ble_mesh.html
    - tutorials/all/ble_mesh.md
    - chapter/tutorials/all/ble_mesh
---

Pymesh BLE module enables many-to-many device connections, based on the Bluetooth module.

For the API, please check the section [Pymesh BLE API](/firmwareapi/pycom/network/bluetooth/ble_mesh/).

## Generic OnOff Example
Generic OnOff model is one of the simplest model in BLE Mesh.

This model illustrates the light-switches (OnOff Client) and light-bulbs (OnOff Server). In other words, the Client can send on/off commands to one/all nodes, and the Server is records state changes based on these commands.

### OnOff Server

OnOff Server has one boolean State. Server can Get, Set or send Status about this State to Client(s).

In the example below, during Provisioning, `Output OOB` can be selected. LED is yellow in case of Not-provisioned, and green in case of Provisioned state.

Changing the State of Server, LED's light is green or red.

```python
from network import Bluetooth
import pycom
import time

BLE_Name = "OnOff Server 18"

def blink_led(n):
    for x in range(n):
        pycom.rgbled(0xffff00) # yellow on
        time.sleep(0.3)
        pycom.rgbled(0x000000) # off
        time.sleep(0.3)

def server_cb(new_state, event, recv_op):
    print("SERVER | State: ", new_state)

    # Turn on LED on board based on State
    if new_state == True:
        pycom.rgbled(0x007f00) # green
    else:
        pycom.rgbled(0x7f0000) # red

def prov_callback(event, oob_pass):
    if(event == BLE_Mesh.PROV_REGISTER_EVT or event == BLE_Mesh.PROV_RESET_EVT):
        # Yellow if not Provision yet or Reseted
        pycom.rgbled(0x555500)
    if(event == BLE_Mesh.PROV_COMPLETE_EVT):
        # Green if Provisioned
        pycom.rgbled(0x007f00)
    if(event == BLE_Mesh.PROV_OUTPUT_OOB_REQ_EVT):
        print("Privisioning blink LED num:", oob_pass)
        blink_led(oob_pass)

# BLE Mesh module
BLE_Mesh = Bluetooth.BLE_Mesh

# Turn off the heartbeat behavior of the LED
pycom.heartbeat(False)

# Need to turn ON Bluetooth before using BLE Mesh
bluetooth = Bluetooth()

# Create a Primary Element with GATT Proxy feature and add a Server model to the Element
element = BLE_Mesh.create_element(primary=True, feature=BLE_Mesh.GATT_PROXY)
model_server = element.add_model(BLE_Mesh.GEN_ONOFF, BLE_Mesh.SERVER, callback=server_cb)

# Initialize BLE_Mesh
BLE_Mesh.init(BLE_Name, auth=BLE_Mesh.OOB_OUTPUT, callback=prov_callback)

# Turn on Provisioning Advertisement
BLE_Mesh.set_node_prov(BLE_Mesh.PROV_ADV|BLE_Mesh.PROV_GATT)

print("\nBLE Mesh started")
print(BLE_Name, "waits to be provisioned\n")

"""
# After this node was provisioned
# Current state can be read using
model_server.get_state()
"""
```

### OnOff Client

Client can Get or Set State of Server. In case of Get, or Server Status, Client Gets the Status through the Model's callback.

```python
from network import Bluetooth
import pycom
import time

BLE_Name = "OnOff Client 17"

def blink_led(n):
    for x in range(n):
        pycom.rgbled(0xffff00) # yellow on
        time.sleep(0.3)
        pycom.rgbled(0x000000) # off
        time.sleep(0.3)

def client_cb(new_state, event, recv_op):
    print("CLIENT | State: ", new_state)

def prov_callback(event, oob_pass):
    if(event == BLE_Mesh.PROV_REGISTER_EVT or event == BLE_Mesh.PROV_RESET_EVT):
        # Yellow if not Provision yet or Reseted
        pycom.rgbled(0x555500)
    if(event == BLE_Mesh.PROV_COMPLETE_EVT):
        # Green if Provisioned
        pycom.rgbled(0x007f00)
    if(event == BLE_Mesh.PROV_OUTPUT_OOB_REQ_EVT):
        print("Privisioning blink LED num:", oob_pass)
        blink_led(oob_pass)

# BLE Mesh module
BLE_Mesh = Bluetooth.BLE_Mesh

# Turn off the heartbeat behavior of the LED
pycom.heartbeat(False)

# Need to turn ON Bluetooth before using BLE Mesh
bluetooth = Bluetooth()

# Create a Primary Element with GATT Proxy feature and add a Server model to the Element
element = BLE_Mesh.create_element(primary=True, feature=BLE_Mesh.GATT_PROXY)
model_client = element.add_model(BLE_Mesh.GEN_ONOFF, BLE_Mesh.CLIENT, callback=client_cb)

# Initialize BLE_Mesh
BLE_Mesh.init(BLE_Name, auth=BLE_Mesh.OOB_OUTPUT, callback=prov_callback)

# Turn on Provisioning Advertisement
BLE_Mesh.set_node_prov(BLE_Mesh.PROV_ADV|BLE_Mesh.PROV_GATT)

print("\nBLE Mesh started")
print(BLE_Name, "waits to be provisioned\n")

"""
# After this node was provisioned
# transmit the change of state broadcasting in the Mesh

model_client.set_state(False, 0xFFFF)
model_client.set_state(True, 0xFFFF)

# or to a unique server
model_client.set_state(False, 3)
model_client.set_state(True, 5)

"""
```

## Sensor Example
In case of Sensor Models, State of Server can be modified only by Server itself, Client can only Get the State by calling Client's Get, or by Servers Status call, but cannot modify the Server's State.

### Sensor Server
In this example Server takes a time measurement every 1 seconds, and send a Status message every 5 seconds, after it was provisioned.

```python
from network import Bluetooth
import pycom
import time
from machine import Timer

def read_sensor(alarm):
    # In this example sensor reads local seconds
    if(device_provisioned):
        model_server.set_state(time.localtime()[5])
        print("SENSOR | State: ", model_server.get_state())

def status_sensor(alarm):
    if (device_provisioned):
        model_server.status_state()

def prov_callback(event, oob_pass):
    global device_provisioned
    if(event == BLE_Mesh.PROV_REGISTER_EVT or event == BLE_Mesh.PROV_RESET_EVT):
        # Yellow if not Provision yet or Reseted
        pycom.rgbled(0x555500)
        device_provisioned = False
    if(event == BLE_Mesh.PROV_COMPLETE_EVT):
        # Green if Provisioned
        pycom.rgbled(0x007f00)
        device_provisioned = True

# BLE Mesh module
BLE_Mesh = Bluetooth.BLE_Mesh

# Turn off the heartbeat behavior of the LED
pycom.heartbeat(False)

# Need to turn ON Bluetooth before using BLE Mesh
bluetooth = Bluetooth()

# Create a Primary Element with GATT Proxy feature and add a Server model to the Element
element = BLE_Mesh.create_element(primary=True, feature=BLE_Mesh.GATT_PROXY)
model_server = element.add_model(BLE_Mesh.SENSOR, BLE_Mesh.SERVER, sen_min = 0, sen_max = 59, sen_res = 1)

# Initialize BLE_Mesh
BLE_Mesh.init("Pycom Sensor Server", callback=prov_callback)

# Turn on Provisioning Advertisement
BLE_Mesh.set_node_prov(BLE_Mesh.PROV_ADV|BLE_Mesh.PROV_GATT)

# Sensor takes measurement every 1 second
Timer.Alarm(read_sensor, 1, periodic=True)

# Sensor send status every 5 seconds
Timer.Alarm(status_sensor, 5, periodic=True)
```

### Sensor Client

Sensor Client is looking for measurements, as Server sends Status every 5 seconds. Between these calls, Client can Get message any time.

```python
from network import Bluetooth
import pycom

def client_cb(new_state, event, recv_op):
    print("CLIENT | State: ", new_state)

def prov_callback(event, oob_pass):
    if(event == BLE_Mesh.PROV_REGISTER_EVT or event == BLE_Mesh.PROV_RESET_EVT):
        # Yellow if not Provision yet or Reseted
        pycom.rgbled(0x555500)
    if(event == BLE_Mesh.PROV_COMPLETE_EVT):
        # Green if Provisioned
        pycom.rgbled(0x007f00)

# BLE Mesh module
BLE_Mesh = Bluetooth.BLE_Mesh

# Turn off the heartbeat behavior of the LED
pycom.heartbeat(False)

# Need to turn ON Bluetooth before using BLE Mesh
bluetooth = Bluetooth()

# Create a Primary Element with GATT Proxy feature and add a Server model to the Element
element = BLE_Mesh.create_element(primary=True, feature=BLE_Mesh.GATT_PROXY)
model_client = element.add_model(BLE_Mesh.SENSOR, BLE_Mesh.CLIENT, callback=client_cb, sen_min = 0, sen_max = 59, sen_res = 1)

# Initialize BLE_Mesh
BLE_Mesh.init("Pycom Sensor Client", callback=prov_callback)

# Turn on Provisioning Advertisement
BLE_Mesh.set_node_prov(BLE_Mesh.PROV_ADV|BLE_Mesh.PROV_GATT)
```
