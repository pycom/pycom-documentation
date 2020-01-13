---
title: "ChirpStack Setup"
aliases:
    - chapter/pybytes/networks/lora/chirpstack
---

## Overview

When a LoRa device is created or LoRa network is configured in **Pybytes → Settings -> LoRa** the user profile is automatically created at [ChirpStack](https://loraserver.pycom.io/).

## User profile

After creating a LoRa device or configure Pybytes to use ChirpStack, you should receive an email with ChirpStack username and password what you can use for accessing the data on <a href="https://loraserver.pycom.io/"> loraserver.pycom.io</a>.  

The basic configurations are made by Pybytes, but if you want to overwrite the LoRa settings, it is possible to use these credentials.

### What is created by ChirpStack:

**Network-server** - Pycom  

You can add your own server in the section Network-servers  

**User** - Value

The User will be created based on the same credentials that are used in Pybytes and it can be managed in the section Org. Users. At the same place, the Admin status of the user can be changed.  

**Organization** - Value (by default)

The Organization Value will be created based on the same credentials used by Pybytes and can be changed in the section Org. Settings.

**Service Profile** - Value (by default)

The Service Profile Name is connected to the Organization’s name.

**Device Profiles** - OTAA or ABP

There are two different devices profiles among which you should select the preferable.  

**Applications** - Value (by default)

All devices created in Pybytes will be connected to this app.

**Devices** All devices that will be created in Pybytes.


## Gateway

The user should set up their own Gateway in order to communicate with ChirpStack.

### How to set up a gateway: 

1 - Login in ChirpStack (https://loraserver.pycom.io/)

2 - Click on **Gateway** on the main sidebar

3 - Click on **Create** button

4 - Fill the form with the information below

**Gateway name**

The name may only contain words, numbers, and dashes.

**Gateway description**

The description of the gateway.

**Gateway ID**

The gateway ID.

**Network-server**

Select the network-server to which the gateway will connect. When no network-servers are available in the dropdown, make sure a service-profile exists for this organization.

**Gateway-profile**

An optional gateway-profile which can be assigned to a gateway. This configuration can be used to automatically re-configure the gateway when LoRa Gateway Bridge is configured so that it manages the packet-forwarder configuration.

**Gateway discovery enabled**

When enabled (and LoRa Server is configured with the gateway discover feature enabled), the gateway will send out periodical pings to test its coverage by other gateways in the same network.

**Gateway altitude** (meters) 

When the gateway has an on-board GPS, this value will be set automatically when the network has received statistics from the gateway.

**Gateway location** (set to current location)

For more information check out [ChirpStack official guide](https://www.chirpstack.io/guides/first-gateway-device/#add-a-lora-sup-reg-sup-gateway).    
