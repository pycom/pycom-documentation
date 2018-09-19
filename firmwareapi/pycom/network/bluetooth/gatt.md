# GATT

GATT stands for the Generic Attribute Profile and it defines the way that two Bluetooth Low Energy devices communicate between each other using concepts called Services and Characteristics. GATT uses a data protocol known as the Attribute Protocol \(ATT\), which is used to store/manage Services, Characteristics and related data in a lookup table.

GATT comes into use once a connection is established between two devices, meaning that the device will have already gone through the advertising process managed by GAP. It’s important to remember that this connection is exclusive; i.e. that only one client is connected to one server at a time. This means that the client will stop advertising once a connection has been made. This remains the case, until the connection is broken or disconnected.

The GATT Server, which holds the ATT lookup data and service and characteristic definitions, and the GATT Client \(the phone/tablet\), which sends requests to this server.

