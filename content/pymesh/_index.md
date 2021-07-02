---
title: "Pymesh"
aliases:
  - pymesh/introduction
---
![](/gitbook/assets/pymesh/pymesh_roles.png)

## Pymesh on Pybytes

{{< youtube 4dgxvkZbF_4>}}

## Pymesh presentation  at TTN Conference

{{< youtube Ab_WFE93BQI>}}

## What is Pymesh?

Pymesh is the LoRa full-mesh network technology.

A Mesh network acts like a net, this means that any node within the network can connect with any other node.

Mesh networks essentially get rid of gateways, which decentralises the network's infrastructure. This then means that the network becomes flexible, so it can do many wonderful things – such as generate, change and fix itself. The success of the Mesh network is down to its parts, as any node within the network will automatically connect to the best radio-link available.

Pymesh works on all of our LoRa supporting development boards, the LoPy4 and FiPy as well as on our OEM modules, L01 and L04.

_**Note: For obtaining the Pymesh firmware please follow the steps from [Pybytes - Pymesh integration](/pybytes/pymeshintegration/).**_

## What does Pymesh offer you?

* An ad-hoc communication network over raw-LoRa radio
* Multi-gateway (Border Routers) Nodes that connect Mesh-internal data with the Cloud
* Each Node uses LBS - Listen Before Talk
* Security on multiple levels
 * base level: authentication and encryption using AES 128bit key, so all traffic inside Pymesh is secured
 * advanced level: RSA or AES at application level allows private communication channels above Pymesh.
* Any LoRa device (Lopy4/Fipy) can have any of the Pymesh Node Role: Leader, Router, Child or Border Router.

## Let's get started!

* [Pymesh LICENCE](/pymesh/licence)
* [Simple Example](/pymesh/simple-example)
* [Pymesh library API](/pymesh/lib-api)
* [Pymesh library CLI](/pymesh/lib-cli)
* [Pymesh library BLE RPC](/pymesh/lib-ble-rpc)
* [Border Router](/pymesh/pymesh-br)
* ​[Advanced Security Example](/pymesh/security)​
* [Pymesh Micropython API](/firmwareapi/pycom/network/lora/pymesh)
