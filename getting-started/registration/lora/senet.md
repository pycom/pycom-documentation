# Senet

![](../../../.gitbook/assets/senet-logo.png)

## The Senet Developer Portal

Connecting your device begins by creating an account on the Senet Developer Portal. This will grant you free access for up to 10 devices and 5 gateways to support application development activities. [Sign-Up](https://portal.senetco.io/)

Complete Senet Developer Portal documentation is available on line at [Docs](https://docs.senetco.io/docs).

Once your account has been activated, you may want to onboard a gateway, if Senet public network access in unavailable. Onboarding your device consists of registering the device through your portal account and then provisioning your device with the information provided at the completion of the registration process. Senet supports both Over-The-Air-Activation \(OTAA\) and Activation-By-Personalization \(ABP\). As ABP is useful only in a very narrow set of use-cases, this tutorial will walk you through OTAA registration and provisioning.

## Device Identity and Security Elements

All LoRaWAN 1.0.x end-devices require three provisioning elements to join a network. Devices typically come from the factory with a unique, 64-bit EUI \(called a DevEUI\) which is the device's globally unique identifier. In the case of the Senet Developer Portal, the two additional elements \(The Application EUI or AppEUI and Application Key or AppKey\) will be generated and provided to you after registration \(in typical production environments, these additional elements are also provided during manufacturing and provisioned into the network backend\).

* Device EUI \(DevEUI\)
* Application EUI \(AppEUI\)
* Application Key \(AppKey\)

### Device EUI

This comes from the device itself and can be obtained from `lora.mac()`.  
To obtain the required hexadecimal representation you can run the following code on your LoPy:

```python
from network import LoRa
import ubinascii

lora = LoRa()
print("DevEUI: %s" % (ubinascii.hexlify(lora.mac()).decode('ascii')))
```

Use this value during the first step of device registration.

![](../../../.gitbook/assets/senet-register.png)

### Application EUI and Application Key

The Application EUI uniquely identifies the security broker \(called a Join Server in LoRaWAN terminology\) which is interogated by the network when the device attempts to join the network. The Application Key is the shared secret \(between the end-device and the Join-Server\) which forms the basis for LoRaWAN security and is used to generate the application and network session keys used for privacy and message integrity.

At the completion of your device registration process on the Senet Developer Portal, you will be presented with the Application EUI and the Application Key which you will need to provision in your device. This information is always available after the fact in the device details screen.

![](../../../.gitbook/assets/senet-register-complete.png)

## Provisioning the LoPy or FiPy

After device registration is complete, configure the device for optimal operation and provision the AppEUI and AppKey.

```python
from network import LoRa
import socket
import time
import ubinascii

# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)

# create an OTAA authentication parameters
app_eui = ubinascii.unhexlify('00250C0000010001')
app_key = ubinascii.unhexlify('00112233445566778899AABBCCDDEEFF')

# initialize LoRa
lora.init(mode=LoRa.LORAWAN, adr=True, public=True)

# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), dr=0, timeout=0)
```

You are now ready to start sending messages from your device! Each device may be provisioned to stream the datagrams to the backend service of your choice in a variety of standard and custom formats.

