---
title: "The Things Stack"
aliases:
    - gettingstarted/registration/lora/ttn.html
    - gettingstarted/registration/lora/ttn.md
    - chapter/gettingstarted/registration/lora/ttn
---

> TheThingsNetwork (TTN) is migrating to TheThingsStack Community edition in 2021. Any applications running on TTN should be migrated to the new environment.

The Things Stack (TTS) is a LoRaWAN service that allows you to send and receive LoRa packets from your nodes. Registering your LoRa-enabled Pycom nodes and gateways with TTS gives access to their IoT infrastructure and integrate your devices with the cloud. For more information about The Things Stack and LoRaWAN in general, you can visit their documentation at [https://www.thethingsindustries.com/docs/](https://www.thethingsindustries.com/docs/). On this page, we will cover:

* [Create an account](#create-an-account)
* [Register a node](#register-a-node)
* [Register a gateway](#register-a-gateway)

## Create an account
In order to use TTS you should navigate to [https://console.cloud.thethings.network](https://console.cloud.thethings.network) and select your region. Following that, either login using your account, or create a new one. Already existing accounts on The Things Network (TTN) should work here as well.

![](/gitbook/assets/lorawan/tts/index.png)

![](/gitbook/assets/lorawan/tts/account.png)

Once an account has been registered, you can [create an application](#register-a-node) for your nodes, or [register a gateway](#register-a-gateway).

## Register a node

In order to register your device, you must first create an application for these devices to belong to. This way the Network will know where to send the devices data to.

Selecting the `Applications` tab at the top of the TTN console, will bring up a screen for registering applications. 

![](/gitbook/assets/lorawan/tts/application.png)

Enter a unique `Application ID` as well as a Description & Handler Registration.

Now the Pycom module nodes can be registered to send data up to the new Application. Click `+ Add end device`, then on `Manually`. Select `LoRaWAN version`: `MAC V1.0.2`. For the regional parameters, select `PHY-V1.0.2-RevA`. For Frequency plan please choose one that is compatible with your region and nearby gateways. If you're not sure which one to choose, select the one closest to your region labelled 'used by TTN'. 


Choose either `OTAA` or `ABP` as activation methods. Learn more about the difference [here](https://www.thethingsindustries.com/docs/devices/abp-vs-otaa/). In this example we'll use `OTAA`.  

![](/gitbook/assets/lorawan/tts/device.png)

Scroll down and fill in the fields for `DevEUI`, `AppEUI` and `End device ID`. 

* The `DevEUI` should be a globally unique identifier for the device. You can run the code below on you Pycom module to retrieve its EUI.
* The `AppEUI` is user specified and is unique to the device in this application, we can `Fill with zeros` in this example. 
* The `AppKey` is provided by TTN. Click `Generate`.
* The `End device ID` is a unique name for the device we're about to register, you can choose something that makes sense for your project.

```python
from network import LoRa
import ubinascii

lora = LoRa()
print("DevEUI: %s" % (ubinascii.hexlify(lora.mac()).decode('ascii')))
```
![](/gitbook/assets/lorawan/tts/credentials.png)

Finally click on `Register end device`. 
Great! Now your device is registered with TTS. You can now use the credentials in the [LoRaWAN OTAA](/tutorials/networks/lora/lorawan-otaa/) example.

## Register a Gateway

A LoRaWAN gateway receives the LoRa packets sent out by your (and other people's) nodes and forwards them to the cloud. Next to that, the gateway is able to provide a downlink to your nodes as well. In this case, we will forward the packets to TTS. From there, you can view the traffic coming through your gateway, and view the received messages in your nodes' application. You can also setup your LoRa-enabled Pycom module or Pygate to act as a LoRaWAN gateway. Below we will setup the Gateway in TTS. Have a look at the following pages for more information concerning the device setup:
* [Pygate](/tutorials/expansionboards/pygate/)
* [Nano-gateway](/tutorials/networks/lora/lorawan-nano-gateway/)

Inside the TTS Console, there are two options, `Applications` and `Gateways`. Select `Gateways` and then click on `register Gateway`. This will allow for the set up and registration of a new gateway.

![](/gitbook/assets/lorawan/tts/gateway.png)

Here, it is important we add the `Gateway ID` and `Gateway EUI`. The first can be an identifying string of characters unique to the gateway. The latter is what we'll use in the gateway configuration on the device, and exists of 16 hexadecimal characters. You can use the following to generate the `Gateway EUI`:

```python
from network import WLAN
import binascii
wl = WLAN()
binascii.hexlify(wl.mac().sta_mac)[:6] + 'fffe' + binascii.hexlify(wl.mac().sta_mac)[6:]
```

These are unique to each gateway, location and country specific frequency. Please verify that correct settings are selected otherwise the gateway will not connect to TTN. Further down the page, you will have to select a frequency plan. Select the one appropriate for your region and/or the one compatible with your nodes. After that, you can create the gateway.

![](/gitbook/assets/lorawan/tts/gateway2.png)

From here, you can select to download `global_conf.json` for your selected region. Please check the file for the correct `server_address` and `gateway_ID`. This file can be used for configuring the Pygate.
