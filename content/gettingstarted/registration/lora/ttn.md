---
title: "The Things Network"
aliases:
    - gettingstarted/registration/lora/ttn.html
    - gettingstarted/registration/lora/ttn.md
    - chapter/gettingstarted/registration/lora/ttn
---

In order to use The Things Network (TTN) you should navigate to their website and create/register an account. Enter a username and an email address to verify with their platform.

![](/gitbook/assets/ttn-1.png)

Once an account has been registered, you can register your Pycom module as either a node or a nano-gateway. The steps below will detail how to do this.

## Create an application

In order to register your device to connect to the things network, you must first create an application for these devices to belong to. This way the Network will know where to send the devices data to.

Selecting the `Applications` tab at the top of the TTN console, will bring up a screen for registering applications. Click register and a new page, similar to the one below, will open.

![](/gitbook/assets/ttn-5.png)

Enter a unique `Application ID` as well as a Description & Handler Registration.

Now the Pycom module nodes can be registered to send data up to the new Application.

## Register a Device

To connect nodes to a things network gateway, devices need to be added to the application. To do this, navigate to the `Devices` tab on the `Application` home page and click the `Register Device` button.

![](/gitbook/assets/ttn-6.png)

In the `Register Device` panel, complete the forms for the `Device ID` and the `Device EUI`. The `Device ID` is user specified and is unique to the device in this application. The `Device EUI` should be a globally unique identifier for the device. You can run the following on you Pycom module to retrieve its EUI.

```python

from network import LoRa
import ubinascii

lora = LoRa()
print("DevEUI: %s" % (ubinascii.hexlify(lora.mac()).decode('ascii')))
```

Once the device has been added, change the `Activation Method` between `OTAA` and `ABP` depending on user preference. This option can be found under the `Settings` tab.

## Register a Nano-Gateway

You can also setup your Pycom module to act as a gateway with The Things Network. The code required to do this can be found [here](/tutorials/lora/lorawan-nano-gateway).

Inside the TTN Console, there are two options, `Applications` and `Gateways`. Select `Gateways` and then click on `register Gateway`. This will allow for the set up and registration of a new nano-gateway.

![](/gitbook/assets/ttn-2%20%281%29.png)

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

![](/gitbook/assets/ttn-4%20%281%29.png)

The `Gateway` should now be configured.
