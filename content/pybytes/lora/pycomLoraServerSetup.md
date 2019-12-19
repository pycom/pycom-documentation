---
title: "ChirpStack Setup"
aliases:
    - pybytes/lora/pycomLoraServerSetup.html
    - pybytes/pycomLoraServerSetup.md
    - chapter/pybytes/lora/pycomLoraServerSetup
---

## Overview

When a LoRa device is created or LoRa network is configured in **Pybytes → Settings -> LoRa** the user profile is automatically created at [ChirpStack](https://loraserver.pycom.io/).

## User profile

After creating a loRa device or configure Pybytes to use ChirpStack, the user should receive an email with ChirpStack username and password.

The basic configurations are made by Pybytes, but if the user wants to overwrite it, it is possible using these credentials.

### What is created by Pybytes?

Network-server - **Pycom**  

User and Organization - Created based on the same credentials used by Pybytes.

Service Profile - Connected to organization.

Device Profile - Two different profiles, for OTAA and ABP devices.

Application - All devices will be connected to this app.

Device - All devices will be created by Pybytes.


## Gateway

The user should set up their own Gateway in order to communicate with ChirpStack.

### How to set up a gateway?

* Login in ChirpStack (https://loraserver.pycom.io/)

* Click on **Gateway** on the main sidebar

* Click on **Create** button

* Fill the form with the information below

    * *Gateway name* - The name may only contain words, numbers, and dashes.

    * *Gateway description* - The description of the gateway.

    * *Gateway ID* - The gateway ID.

    * *Network-server* - Select the network-server to which the gateway will connect. When no network-servers are available in the dropdown, make sure a service-profile exists for this organization.

    * *Gateway-profile* - An optional gateway-profile which can be assigned to a gateway. This configuration can be used to automatically re-configure the gateway when LoRa Gateway Bridge is configured so that it manages the packet-forwarder configuration.

    * *Gateway discovery enabled* - When enabled (and LoRa Server is configured with the gateway discover feature enabled), the gateway will send out periodical pings to test its coverage by other gateways in the same network.

    * *Gateway altitude* (meters) - When the gateway has an on-board GPS, this value will be set automatically when the network has received statistics from the gateway.

    * *Gateway location* (set to current location)

## Further reading
For more information check out [ChirpStack official guide](https://www.chirpstack.io/guides/first-gateway-device/#add-a-lora-sup-reg-sup-gateway).    
