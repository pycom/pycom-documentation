# LoRaWAN

## Raw LoRa

When using raw LoRa, you do not have to register your module in any way. The modules can talk to each other directly.

## LoRaWAN

In order to connect your LoRa capable Pycom module to a LoRaWAN network you will have to register your device with the desired network. We are unable to provide instructions for all LoRaWAN networks but below you will find some generic instructions, along with links to any specific guides we are aware of.

### Generic instructions

Firstly you will need to get your modules `Device EUI`, this can be achieved using the following code:

```python
from network import LoRa
import ubinascii

lora = LoRa(mode=LoRa.LORAWAN)
print(ubinascii.hexlify(lora.mac()).upper().decode('utf-8'))
```

The output will be a hex string like: `70B3D5499585FCA1`. Once you have this you will need to provide it to your LoRaWAN network which will then provide you with the details need to connect via Over-the-Air Activation \(OTAA\) or Activation by Personalisation \(ABP\)

#### OTAA

If you wish to connect via OTAA \(which is the recommended method\) the network will provide you with an `Application EUI` and `Application Key`. The former identifies what application your device is connecting to, the latter is a shared secret key unique to your device to generate the session keys that prove its identity to the network. Once you have these you can use the [LoRaWAN OTAA example](../../../tutorials/lora/lorawan-otaa.md) code to connect to the network.

#### ABP

With ABP the encryption keys enabling communication with the network are preconfigured in the device. The network will need to provide you with a `Device Address`, `Network Session Key` and `Application Session Key`. Once you have these you can use the [LoRaWAN ABP example](../../../tutorials/lora/lorawan-abp.md) code to connect to the network.

### Networks

[![](../../../.gitbook/assets/ttn-logo.png)](ttn.md)

[![](../../../.gitbook/assets/senet-logo-2.png)](senet.md)

{% hint style="info" %}
If you cannot find your favourite LoRaWAN network in the list above, please consider writing a tutorial for how to connect a Pycom module with it and contribute it to this documentation via a [GitHub pull request](https://github.com/pycom/pycom-documentation).
{% endhint %}

