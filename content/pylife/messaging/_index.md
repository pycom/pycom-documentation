---
title: "Messaging"
aliases:
---

## Pylife Messaging Functionality

Once multiple Pylife members have joined a common group, you can send messages between group members.

Messages are sent via LoRa mesh and do not require a cellular connection.

![Messaging iOS Screenshot](/gitbook/assets/pylife/messaging/messaging_ios.jpg)

The indicators next to the message will show the message status.

The first tick indicates that the message has been successfully submitted to the PyGo device for transmission

The second tick indicates that the message has been broadcast through the mesh network

## Private Messaging

By default, all devices communicate using a default encryption key. That means that all devices in a mesh network can read transmitted messages.

If you want to keep messages secure, all devices will have to share a unique mesh key.

You can generate a new random mesh key from the Devices section.

![Default Mesh Key iOS Screenshot](/gitbook/assets/pylife/messaging/default_mesh_key_ios.png)

Generate a new mesh key and deploy it to your device.

All devices you wish to communicate with need to have the same mesh key deployed. Please share with any group memembers you wish to privately communicate with.

![Private Mesh Key iOS Screenshot](/gitbook/assets/pylife/messaging/private_mesh_key_ios.jpg)

> Please note that the private mesh key is per device. You will only be able to communicate with other PyGo devices using the same key.
