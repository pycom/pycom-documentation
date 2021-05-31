---
title: "The Things Stack"
aliases:
    - gettingstarted/registration/lora/ttn.html
    - gettingstarted/registration/lora/ttn.md
    - chapter/gettingstarted/registration/lora/ttn
---

> TheThingsNetwork (TTN) is migrating to TheThingsStack Community edition in 2021. Any applications running on TTN should be migrated to the new environment.

## Create an account
In order to use The Things Stack (TTN) you should navigate to [https://console.cloud.thethings.network](https://console.cloud.thethings.network) and select your region. Following that, either login using your account, or create a new one. Existing accounts on TTN should work here as well.

![](/gitbook/assets/lorawan/tts/index.png)

![](/gitbook/assets/lorawan/tts/account.png)

    Once an account has been registered, you can [create an application](#create-an-application) for your nodes, or [register a gateway](#register-a-gateway). For more information about The Things Stack and LoRaWAN in general, you can visit their documentation at [https://www.thethingsindustries.com/docs/](https://www.thethingsindustries.com/docs/)

## Create an application

In order to register your device, you must first create an application for these devices to belong to. This way the Network will know where to send the devices data to.

Selecting the `Applications` tab at the top of the TTN console, will bring up a screen for registering applications. 

![](/gitbook/assets/lorawan/tts/application.png)

Enter a unique `Application ID` as well as a Description & Handler Registration.

Now the Pycom module nodes can be registered to send data up to the new Application.

## Register a Device

You'll need to register your devices as nodes to the application. Click the button `+ Add device`. Next, you'll need to enter the specifics. You can choose either `OTAA` or `ABP` as activation methods. Learn more about the difference [here](https://www.thethingsindustries.com/docs/devices/abp-vs-otaa/). In this application we'll choose `OTAA`. Select `LoRaMAC V1.0.2` and check whether the region servers are set correctly. 

![](/gitbook/assets/lorawan/tts/device.png)

In the `Register Device` panel, complete the forms for the `Device ID` and the `Device EUI`. The `Device ID` is user specified and is unique to the device in this application. The `Device EUI` should be a globally unique identifier for the device. You can run the following on you Pycom module to retrieve its EUI.

```python

from network import LoRa
import ubinascii

lora = LoRa()
print("DevEUI: %s" % (ubinascii.hexlify(lora.mac()).decode('ascii')))
```

Once the device has been added, change the `Activation Method` between `OTAA` and `ABP` depending on user preference. This option can be found under the `Settings` tab.

## Register a Nano-Gateway

You can also setup your Pycom module to act as a gateway with The Things Network. The code required to do this can be found [here](/tutorials/networks/lora/lorawan-nano-gateway).

Inside the TTN Console, there are two options, `Applications` and `Gateways`. Select `Gateways` and then click on `register Gateway`. This will allow for the set up and registration of a new nano-gateway.

![](/gitbook/assets/ttn-2.png)

On the Register Gateway page, you will need to set the following settings:

![](/gitbook/assets/ttn-gatewayreg-11-2017-2.jpg)

These are unique to each gateway, location and country specific frequency. Please verify that correct settings are selected otherwise the gateway will not connect to TTN.

**You need to tick the "I'm using the legacy packet forwarder" to enable the right settings.** This is because the Nano-Gateway uses the 'de facto' standard Semtech UDP protocol.

| Option | Value |
| :--- | :--- |
| Protocol | Packet Forwarder |
| Gateway EUI | User Defined (must match `config.py`) |
| Description | User Defined |
| Frequency Plan | Select Country (e.g. EU - 868 MHz) |
| Location | User Defined |
| Antenna Placement | Indoor or Outdoor |

Most LoRaWAN network servers expect a Gateway ID in the form of a unique 64-bit hexadecimal number (called a EUI-64). The recommended practice is to produce this ID from your board by expanding the WiFi MAC address (a 48-bit number, called MAC-48). You can obtain that by running this code prior to configuration:

```python

 from network import WLAN
 import binascii
 wl = WLAN()
 binascii.hexlify(wl.mac())[:6] + 'FFFE' + binascii.hexlify(wl.mac())[6:]
```

Once these settings have been applied, click `Register Gateway`. A Gateway Overview page will appear, with the configuration settings showing. Next click on the `Gateway Settings` and configure the Router address to match that of the gateway (default: `router.eu.thethings.network`).

![](/gitbook/assets/ttn-4.png)

The `Gateway` should now be configured.
