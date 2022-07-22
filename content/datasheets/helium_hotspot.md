---
title: "Helium Hotspot Miner"
aliases:
    - datasheets/helium_hotspot.html
    - datasheets/helium_hotspot.md
    - product-info/helium_hotspot
    - chapter/datasheets/helium_hotspot
---

**Store**: [Buy Here](https://pycom.io/product/helium-hotspot-miner-batch-3/)

This full Hotspot is compatible with Helium LongFi™ and Helium Blockchain technology.

Use it to mine [Helium HNT](https://www.helium.com/token) Crypto Coins on the [Helium LoRaWAN Network](https://www.helium.com/lorawan). Helium’s network is referred to as The People's Network. It is powered by an entirely new incentive model - made possible by their Helium Blockchain. 
Installing a LoRa Hotspot means you are rewarded in HNT crypto coins as soon as you have [“Proof-of-Coverage”](https://docs.helium.com/blockchain/proof-of-coverage/).

![](/gitbook/assets/hotspot1.png)

## What's included in the price?
When you are setting up a Hotspot Miner, there are a couple of fees to note:

* PY Hotspot Miner Kit including antennas, and power supply
* Hotspot Fee $40 ("Add a Full Hotspot")
* First Location Assertion Fee $10 ("Assert Hotspot Location")

NOTE: If you move your Hotspot Miner to a new location, you will need to pay the Location Assertion fee again. 
Pycom will only pay one Location Assertion Fee. There may be other fees. The full list of additional Helium transaction fees are [here](https://docs.helium.com/blockchain/transaction-fees/).

## Hotspot Overview
This fully certified Helium Hotspot contains

* Pygate: 2 variants: 868 Mhz (EU and Africa) and 915 Mhz (North/South America and APAC). Check certifications are confirmed for your region.
* LoRa Antenna
* WiFi Antenna
* Pygate Case for Indoor use
* Power supply

### Optional extras

* Power over Ethernet adaptor 

### Certifications

* Certified by Helium [Dewi](https://www.helium.com/ecosystem)


### Regulatory certifications

* CE completed, [Certificate Here](/gitbook/assets/lorawan/helium/CECert.pdf)
* FCC completed, [Certificate Here](/gitbook/assets/lorawan/helium/FCCCert.pdf)
* IC completed, [Certificate Here](/gitbook/assets/lorawan/helium/ICCert.pdf)
* RCM pending

## Helium Hotspot miner (Full Hotspot) specifications

* Raspberry Pi Compute Module 4 (CM4102000)
* Broadcom BCM2711, Quad core Cortex-A72 (ARM v8) 64-bit SoC @ 1.5GHz
* 2GB LPDDR4-3200 SDRAM with ECC
* WiFi 2.4 GHz and 5 GHz IEEE 802.11 b/g/n/ac wireless
* Bluetooth 5.0, BLE
* On board electronic switch to select between PCB trace or external antenna
* Baseband processor: SX1308
* Dual SX1257 transceivers for a total of 8 channels support
* Maximum TX power (LoRaWAN) 23.45 dBm
* Frequencies: EU 863-870 MHz or US 902-928 MHz
* 32GB uSD card with Operating System and Helium Miner software stack
* Powered via USB-C or optional Ethernet + PoE adapter daughter board

Choose your gateway frequency using this detailed [country list](https://lora-alliance.org/sites/default/files/2020-06/rp_2-1.0.1.pdf)

## Full Specifications

Data Sheet [Here](https://pycom.io/wp-content/uploads/2022/07/Hotspot_Spec-sheet-V1.13-First-Release.pdf)

There is more information about how to mine HNT and much more on the [Helium docs site.](https://docs.helium.com/)

## Getting started
1. Follow the [tutorial](https://docs.pycom.io/gettingstarted/registration/lora/helium_hotspot_registration/) to register and connect your Hotspot  to the Helium Network.

## Notes
### Battery Charger

The Pygate features a single cell Li-Ion/Li-Po charger with a JST PHR‑2 connector. When the board is being powered via the USB-C connector, the Pygate will charge the battery if connected.
> Make sure you check the polarity of the battery before plugging it in! Connect the positive side to the side marked with a `+`.


