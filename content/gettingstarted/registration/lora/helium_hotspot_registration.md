---
Title: "Helium Hotspot"
aliases:
    - gettingstarted/registration/lora/helium_hotspot_registration.html
    - gettingstarted/registration/lora/helium_hotspot_registration.md
---

Helium’s network is referred to as The People's Network. It is powered by an entirely new incentive model - made possible by their Helium Blockchain.
Installing a LoRa Hotspot means you are rewarded in HNT crypto coins as soon as you have [“Proof-of-Coverage”](https://docs.helium.com/blockchain/proof-of-coverage/).

* [Add a Pycom Helium Miner](#add-a-pycom-helium-miner)
* [Assert Location](#assert-location)
* [Transfer Hotspot](#transfer-hotspot)

# Getting started
Start by connecting both antenna's to the hotspot.
> Hint: The Hotspot is delivered with a WiFi and LoRa antenna. Please check the polarity of the connector on the antenna and match it with the correct antenna connector on the Hotspot:

LoRa antenna:

![](/gitbook/assets/lorawan/helium/lora_antenna.png)

WiFi antenna:

![](/gitbook/assets/lorawan/helium/wifi_antenna.png)

Next, connect your device to the included USB-C powersupply.
Initially you will see an internal solid green light inside the case above the power lead. After around 20 seconds this should start to blink.
Leave the miner booting while you set up your phone: it takes a minute or two to boot, and after this should be ready to be paired.

## Add a Pycom Helium Miner using the app

Download and install the Pycom Helium App from the [Apple App Store](https://apps.apple.com/us/app/pycom-helium-app/id1630652083)

For the Android Version, please download the app from [pycom-helium.apk](https://software.pycom.io/downloads/pycom-helium.apk)
> Hint: Please enable Location & Nearby Devices permissions in app settings.

The app contains step-by-step instructions for getting you up and running. A summary is provided here:
  * Create an account or log in to your existing account
  * Click +Add Hotspot
    * ![](/gitbook/assets/lorawan/helium/helium_reg_1.png)
  * Add "Pycom Helium Miner BLE"
  * Follow the step-by-step instructions to pair your Helium Miner
  * The hotspot automatically goes into pairing mode for 30 minutes after first power-on.
  * It should be detected by the app.
    * ![](/gitbook/assets/lorawan/helium/helium_reg_8.png)
  * Select the WiFi network the hotspot will use to access the internet
    * ![](/gitbook/assets/lorawan/helium/helium_reg_9.png)
  * Add to the blockchain, and you are up and running
    * ![](/gitbook/assets/lorawan/helium/helium_reg_15.png)

> Hint: The Hotspot is periodically checking for updates. It may take 30 minutes for the first firmware update to be downloaded.


# Using your hotspot.

## Assert Location

If you haven't asserted your location during onboarding, you can do this via this option in the app. You can also use the official Helium Hotspot app to assert your location. Please note that only one location assertion is payed by Pycom. If you wish to change your location later, any fees charged by the Helium network are the responsibility of the Hotspot owner!

## Transfer Hotspot

You can use this option to transfer Hotspot ownership to a different wallet.

# Troubleshooting
## The app doesn't find my Helium hotspot / can't pair
This can be caused by a variety of issues. The first step is to look at the LEDs on the side of the case.
Initially you will see an internal solid green light inside the case above the power lead. After around 20 seconds this should start to blink.
If this is the case, it is likely your hotspot is working correctly.
  * On some devices, it may take several rescans before the hotspot shows in the app. Please keep retrying until it shows up.
  * If it does not start to blink, you may have a board that has vibrated loose. We have discovered a small number of units where the board-to-board connectors that hold the Raspberry Pi module in have vibrated loose in transit.
    * If you feel confident in such things, it is possible to dissasemble the hotspot case and squeeze the Raspberry Pi module so it clicks back in to the header.
  

## Hotspot won't connect to my WiFi
Some customers have encountered some issues where the hotspot doesn't connect to a particular WiFi network.
If you're WiFi router has smart setup or similar, please try deactivating it.


## App crashes when I assert location (Android)
The pairing process requires that Chrome is the default browser. If you use a different browser, please temporarily make Chrome your default browser then try again.



