---
title: "ChirpStack Setup"
aliases:
    - chapter/pybytes/networks/lora/chirpstack
---

## Overview

When a LoRa device is added or the LoRa network is configured in Pybytes → Settings -> LoRa, a user profile is automatically created on [ChirpStack](https://loraserver.pycom.io/). This will only happen if there is no pre-existing user profile.

## User profile

After creating a LoRa device or configuring Pybytes to use ChirpStack, you should receive an email with the ChirpStack username and password. Use this for accessing the data on <a href="https://loraserver.pycom.io/"> loraserver.pycom.io</a>.

The basic configurations are made by Pybytes. If you want to overwrite the LoRa settings, use the ChirpStack username and password to do so.

### Basic ChirpStack Settings in Pybytes

**Network-server** - Pycom  

You can add your own server in the section Network-servers  

![Network-servers](/gitbook/assets/pybytes/lora/screenshots/network_servers.png)

**User** - Value

The User will be created based on the same credentials that are used in Pybytes. This, as well as the Admin status of the user, can be managed in the Org > Users section.

**Organization** - Value (by default)

The Organization Value will be created, based on the same credentials used in Pybytes. This can be changed in the section Org > Settings.

**Service Profile** - Value (by default)

The Service Profile Name is connected to the Organization’s name.

**Device Profiles** - OTAA or ABP

There are two different devices profiles, OTAA or ABP. Select which one you prefer.  

**Applications** - Value (by default)

All LoRa devices that have been created in Pybytes and linked to the ChirpStack server will be connected to the ChirpStack app.

**Devices**

All LoRa devices that have been created in Pybytes.

## Gateway

The user should set up their own Gateway in order to communicate with ChirpStack.

![Gateway](/gitbook/assets/pybytes/lora/screenshots/gateway.png)

### How to set up a gateway

1 - Login in ChirpStack (https://loraserver.pycom.io/)

2 - Click on the **Gateway** on the main sidebar

3 - Click on the **Create** button

4 - Fill the form with the information below

**Gateway name**

The name may only contain words, numbers, and dashes.

**Gateway description**

The description of the gateway.

**Gateway ID**

The gateway ID.

**Network-server**

Select the network server that the gateway will connect to. When no network servers are available in the dropdown, make sure a service-profile exists for the organization.

**Gateway-profile**

This is an optional gateway profile that can be assigned to a gateway. This can be used to automatically re-configure the gateway when the LoRa Gateway Bridge is set up so that it manages the packet-forwarder settings.

**Gateway discovery enabled**

When enabled (and LoRa Server is configured with the 'gateway discover' feature enabled), the gateway will send out periodical pings to test its coverage by other gateways in the same network.

**Gateway altitude** (meters) 

When the gateway has an on-board GPS, this value will be set automatically when the network has received statistics from the gateway.

**Gateway location** (set to current location)

For more information check out [ChirpStack official guide](https://www.chirpstack.io/guides/first-gateway-device/#add-a-lora-sup-reg-sup-gateway).    
