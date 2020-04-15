---
title: "BLE_Mesh"
aliases:
    - firmwareapi/pycom/network/bluetooth/BLE_Mesh.html
    - firmwareapi/pycom/network/bluetooth/BLE_Mesh.md
---

The BLE_Mesh library provides support for connecting to a BLE Mesh Network with various Server and Client models.
The library is under development, its current limitations:

- Only one Element (primary) can be added to the Node.
- Supported Models:
    * Configuration Server Model (automatically generated together with primary Element)
    * Generic OnOff Server Model
    * Generic OnOff Client Model
 
- Supported OOB authentication types:
    * No OOB
    * Output OOB
 
- Supported Node Features:
    * GATT Proxy
    * Relay


## Methods of BLE_Mesh class

#### BLE_Mesh.init(name="PYCOM-ESP-BLE-MESH", auth=0)

Initializes the BLE Mesh module with the pre-configured Elements and Models.

* `name` is the name which will be used to identify the device during Provisioning
* `auth` is the Out-Of-Band (OOB) method. Currently `BLE_Mesh.OOB_OUTPUT` is supported. Without specifying this argument, `NO_OOB` will be used during provisioning.

#### BLE_Mesh.set_node_prov(bearer=BLE_Mesh.PROV_NONE, *, callback=None)

Enable provisioning bearers to get the device ready for provisioning. If OOB is enabled, callback inform about OOB information.

* `bearer` is the transport data protocol between endpoints, can be `BLE_Mesh.PROV_ADV` and/or `BLE_Mesh.PROV_GATT`.
* `callback` is the callback to be registered. It must have the following arguments:
* `oob_type` returns the type of OOB authentication. 
* `oob_pass` returns the generated pass in case of `BLE_Mesh.OOB_OUTPUT`.

#### BLE_Mesh.reset_node_prov()

Resets the Node Provisioning information.

#### BLE_Mesh.create_element(*, primary, feature=0, beacon=true, ttl=7)

This API creates a new BLE_Mesh_Element object. The BLE_Mesh_Element on concept level is equivalent to the Element in the BLE Mesh terminology.

* `primary` shows whether this new Element will act as the Primary Element of the Node. When a Primary Element is created, the corresponding Configuration Server Model is also automatically created. There can only be 1 Primary Element per Node.
* `feature` shows what features to enable on the new Element. It is an ORED combination of `BLE_Mesh.RELAY`, `BLE_Mesh.LOW_POWER`, `BLE_Mesh.GATT_PROXY`, `BLE_Mesh.FRIEND`
* `ttl` is the default Time To Live value of the packets belonging to the new Element

## Methods of BLE_Mesh_Element object

#### BLE_Mesh_Element.add_model(type=BLE_Mesh.GENERIC, functionality=BLE_Mesh.ONOFF, server_client=BLE_Mesh.SERVER, *, callback=None, value=None)

This API creates a new BLE_Mesh_Model object. The BLE_Mesh_Model on concept level is equivalent to the Model in the BLE Mesh terminology.

* `type` is the type of the new Model.
* `functionality` shows what functionality the new Model will be able to perform in the context of the `type`. 
* `server_client` shows whether the new Model will act as a Server or Client.
* `callback` is the user defined callback to call when any event happens on the Model.
* `value` is the initial value represented by the Model.

## Methods of BLE_Mesh_Model object

#### BLE_Mesh_Model.value()

Updates or fetches the value of the Model.

* `value` is the new value to update the current value with.
If the method is called without a parameter, the current value is returned.

If the BLE_Mesh_Model is Server, publication message will be sent out when the value is updated.
If the BLE_Mesh_Model is Client, only the locally stored value will be returned.
When the BLE_Mesh_Model is Client and it received a publication message from a Server, the local value is automatically updated.


#### BLE_Mesh_Model.set_state(value, addr=BLE_Mesh.ADDR_ALL_NODES, *, app_idx=0)

Calling this function only makes sense when the BLE_Mesh_Model is a Client Model. It sets the value of the Server model.

* `value` is the new value to update the current value with.
* `addr` is the address of the remote Node to send the update message.
* `app_idx` is the index of one of the registered Application IDs to use when sending out the message.

## Constants

* Advertisement options: `BLE_Mesh.PROV_ADV`, `BLE_Mesh.PROV_GATT`, `BLE_Mesh.PROV_NONE`
* Features of an Element: `BLE_Mesh.RELAY`, `BLE_Mesh.LOW_POWER`, `BLE_Mesh.GATT_PROXY`, `BLE_Mesh.FRIEND`
* Authentication options: `BLE_Mesh.OOB_INPUT`, `BLE_Mesh.OOB_OUTPUT`
* Constants for Node addresses: `BLE_Mesh.ADDR_ALL_NODES`, `BLE_Mesh.ADDR_PUBLISH`
* Constants for Model - type: `BLE_Mesh.GENERIC`, `BLE_Mesh.SENSORS`, `BLE_Mesh.TIME_SCENES`, `BLE_Mesh.LIGHTNING`
* Constants for Model - functionality: `BLE_Mesh.ONOFF`, `BLE_Mesh.LEVEL`
* Constants for Model - server or client: `BLE_Mesh.SERVER`, `BLE_Mesh.CLIENT`



