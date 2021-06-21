---
Title: "Helium"
---

Helium is a LoRaWAN service that allows you to send and receive LoRa packets from your nodes. The network allows for cost-effective wireless infrastructure using the new HNT blockchain as an incentive for the creation of public gateways.

> At the moment, it is not possible to mine HNT on the Pygate or nano-gateway.

* [Create an account](#create-an-account)
* [Add a device](#add-a-device)
* [Registering a gateway](#registering-a-gateway)

## Create an account

Go to [console.helium.com](https://console.helium.com]) to create an account and verify your email-address. Once your account is registered, you can select to [add a device](#registering-a-devi)

![](/gitbook/assets/lorawan/helium/helium.png)

## Add a device

To add a device, click `Devices` in the left hand menu bar and `Add device` on the following page. The following screen will pop up:

![](/gitbook/assets/lorawan/helium/device.png)

Give your device a human-readable name. All other credentials should be filled in already. After successful creation, the device will be shown. You can use the credentials in the [LoRaWAN OTAA](/tutorials/networks/lora/lorawan-otaa/) example.

## Register a gateway

For more information about registering a gateway, we'd like to forward you to the [Helium Docs](https://docs.helium.com/use-the-network/build-a-packet-forwarder#packet-forwarder-architecture). Note that the Pygate uses a Semtech UDP forwarding architecture, and you will need to configure your own miner.