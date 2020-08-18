---
title: "Pymesh BLE"
aliases:
    - firmwareapi/pycom/network/bluetooth/BLE_Mesh.html
    - firmwareapi/pycom/network/bluetooth/BLE_Mesh.md
---

The Pymesh BLE library provides support for connecting to a BLE Mesh Network with various Server and Client models.

For examples, please check the section [Pymesh BLE Examples](/tutorials/all/ble_mesh).

Pymesh BLE features:

* Supported Models:
 * Configuration Server Model (automatically generated together with primary Element)
 * Generic OnOff Server Model
 * Generic OnOff Client Model
 * Generic Level Server Model
 * Generic Level Client Model
 * Sensor Server Model
 * Sensor Client Model
* Supported OOB authentication types:
 * No OOB
 * Output OOB
* Supported Node Features:
 * GATT Proxy
 * Relay
* Only one Element (primary) can be added to the Node.
* Node cannot be configured as Provisioner and a mobile application should be used for Provisioning process
 * nRF Mesh (iOS and Android)
 * Silicon Labs Bluetoth Mesh (iOS)
 * ST BLE Mesh (Android)
 * EspBLEMesh (Android)


## Methods of BLE_Mesh class

### BLE_Mesh.init(name="PYCOM-ESP-BLE-MESH", *, auth=0, callback=None)

Initializes the BLE Mesh module with the pre-configured Elements and Models.

* `name` is the name which will be used to identify the device during Provisioning
* `auth` is the Out-Of-Band (OOB) method. Currently `BLE_Mesh.OOB_OUTPUT` is supported. Without specifying this argument, `NO_OOB` will be used during provisioning.
* `callback` is the callback to be registered. It must have the following arguments:
    * `event` returns current event of provisioning.
    * `oob_pass` returns the generated pass in case of `BLE_Mesh.OOB_OUTPUT`.

### BLE_Mesh.set_node_prov(bearer=BLE_Mesh.PROV_NONE, *)

Enable provisioning bearers to get the device ready for provisioning. If OOB is enabled, the callback is used to inform the user about OOB information.

* `bearer` is the transport data protocol between endpoints, can be `BLE_Mesh.PROV_ADV` and/or `BLE_Mesh.PROV_GATT`.

### BLE_Mesh.reset_node_prov()

Resets the Node Provisioning information.

### BLE_Mesh.create_element(*, primary, feature=0, beacon=true, ttl=7)

This API creates a new BLE_Mesh_Element object. The BLE_Mesh_Element on concept level is equivalent to the Element in the BLE Mesh terminology.

* `primary` shows whether this new Element will act as the Primary Element of the Node. When a Primary Element is created, the corresponding Configuration Server Model is also automatically created. There can only be 1 Primary Element per Node.
* `feature` shows what features to enable on the new Element. It is an ORED combination of `BLE_Mesh.RELAY`, `BLE_Mesh.LOW_POWER`, `BLE_Mesh.GATT_PROXY`, `BLE_Mesh.FRIEND`
* `ttl` is the default Time To Live value of the packets belonging to the new Element

## Methods of BLE_Mesh_Element object

### BLE_Mesh_Element.add_model(type=BLE_Mesh.GEN_ONOFF, server_client=BLE_Mesh.SERVER, *, callback=None, value=None, sen_min=-100, sen_max=100, sen_res=0.1)

This API creates a new BLE_Mesh_Model object. The BLE_Mesh_Model on concept level is equivalent to the Model in the BLE Mesh terminology.

* `type` is the type of the new Model.
* `server_client` shows whether the new Model will act as a Server or Client.
* `callback` is the user defined callback to call when any event happens on the Model. It accepts 3 parameters: `new_state`, `event`, `op_code`. The `new_state` is the corresponding state of BLE_Mesh_Model, the `event` and the `op_code` are belonging of the BLE Mesh packet received.
* `value` is the initial value represented by the Model.
* `sen_min` is the minimum value of Sensor State in case of Sensor Model.
* `sen_max` is the maximum value of Sensor State in case of Sensor Model.
* `sen_res` is the resolution of Sensor State in case of Sensor Model.

## Methods of BLE_Mesh_Model object

### BLE_Mesh_Model.get_state(addr=BLE_Mesh.ADDR_ALL_NODES, app_idx=0, state_type=None)

Gets the State of the Sensor Model. If called from Server Model, returnes with State, in case of Client Model, it sends a Get Message, and returns State through the registered callback.

* `addr` is the address of the remote Node to send the update message.
* `app_idx` is the index of one of the registered Application IDs to use when sending out the message.
* `state_type` is the type of Get State.

### BLE_Mesh_Model.set_state(state, addr=BLE_Mesh.ADDR_ALL_NODES, app_idx=0, state_type=None)

Sets the State of the Sensor Model. If called from Server Model, sets State directly, in case of Client Model, it sends a Set Message, and updates State.

* `state` is the new value to update the current value with.
* `addr` is the address of the remote Node to send the update message.
* `app_idx` is the index of one of the registered Application IDs to use when sending out the message.
* `state_type` is the type of Set State.

### BLE_Mesh_Model.status_state(addr=BLE_Mesh.ADDR_ALL_NODES, app_idx=0, state_type=None)

Calling this function only makes sense when the BLE_Mesh_Model is a Server Model. It sends a Status message with the State to the Client Model(s).

* `addr` is the address of the remote Node to send the update message.
* `app_idx` is the index of one of the registered Application IDs to use when sending out the message.
* `state_type` is the type of Status State.

## Constants

* Advertisement options: `BLE_Mesh.PROV_ADV`, `BLE_Mesh.PROV_GATT`, `BLE_Mesh.PROV_NONE`
* Features of an Element: `BLE_Mesh.RELAY`, `BLE_Mesh.LOW_POWER`, `BLE_Mesh.GATT_PROXY`, `BLE_Mesh.FRIEND`
* Authentication options: `BLE_Mesh.OOB_INPUT`, `BLE_Mesh.OOB_OUTPUT`
* Constants for Node addresses: `BLE_Mesh.ADDR_ALL_NODES`, `BLE_Mesh.ADDR_PUBLISH`
* Constants for Model - type: `BLE_Mesh.GEN_ONOFF`, `BLE_Mesh.GEN_LEVEL`, `BLE_Mesh.GEN_SENSOR`, `BLE_Mesh.GEN_SENSOR_SETUP`
* Constants for Model - server or client: `BLE_Mesh.SERVER`, `BLE_Mesh.CLIENT`
* Constants for Model - states: `BLE_Mesh.STATE_ONOFF`, `BLE_Mesh.STATE_LEVEL`, `BLE_Mesh.STATE_LEVEL_DELTA`, `BLE_Mesh.STATE_LEVEL_MOVE`, `BLE_Mesh.SEN_DESCRIPTOR`, `BLE_Mesh.SEN`, `BLE_Mesh.SEN_COLUMN`, `BLE_Mesh.SEN_SERIES`, `BLE_Mesh.SEN_SET_CADENCE`, `BLE_Mesh.SEN_SETTINGS`, `BLE_Mesh.SEN_SETTING`
* Constants for Provision Events: `BLE_Mesh.PROV_REGISTER_EVT`, `BLE_Mesh.PROV_ENABLE_EVT`, `BLE_Mesh.PROV_DISABLE_EVT`, `BLE_Mesh.LINK_OPEN_EVT`, `BLE_Mesh.LINK_CLOSE_EVT`, `BLE_Mesh.PROV_COMPLETE_EVT`, `BLE_Mesh.PROV_RESET_EVT`, `BLE_Mesh.PROV_OUTPUT_OOB_REQ_EVT`, `BLE_Mesh.PROV_INPUT_OOB_REQ_EVT`