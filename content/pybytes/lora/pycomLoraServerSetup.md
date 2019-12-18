---
title: "Pycom LoRa Server Setup"
aliases:
    - pybytes/lora/pycomLoraServerSetup.html
    - pybytes/pycomLoraServerSetup.md
    - chapter/pybytes/lora/pycomLoraServerSetup
---

## Overview

When a LoRa device is created or LoRa network is configured in ```Pybytes → Settings``` the user profile is automacally created at [Pycom LoRa Server](https://loraserver.pycom.io/).

## User profile

After create a loRa device or configure Pybytes to use Pycom LoRa Server, the user should receive a email with Pycom LoRa Server username and password.

To use the service the basic configurations are done by Pybytes, but if the user wants to overwrite it, it is possible using this credentials.

## Gateway

The user should setup the Gateway in order to communicate with Pycom Lora Server.

### How to setup a gateway?

* Pycom LoRa Server (https://loraserver.pycom.io/)

* Click on `Gateway` on the sidebar

* Click on `Create` button

* Fulfill the form with the informations below

    Gateway name - The name may only contain words, numbers and dashes

    Gateway description 

    Gateway ID

    Network-server - Select the network-server to which the gateway will connect. When no network-servers are available in the dropdown, make sure a service-profile exists for this organization.

    Gateway-profile - An optional gateway-profile which can be assigned to a gateway. This configuration can be used to automatically re-configure the gateway when LoRa Gateway Bridge is configured so that it manages the packet-forwarder configuration.

    Gateway discovery enabled - When enabled (and LoRa Server is configured with the gateway discover feature enabled), the gateway will send out periodical pings to test its coverage by other gateways in the same network.

    Gateway altitude (meters) - When the gateway has an on-board GPS, this value will be set automatically when the network has received statistics from the gateway.

    Gateway location (set to current location)

For more information look at [ChirpStack official documentation](https://www.chirpstack.io/guides/first-gateway-device/#add-a-lora-sup-reg-sup-gateway)    
