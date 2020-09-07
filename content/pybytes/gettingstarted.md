---
title: "Getting Started with Pybytes"
aliases:
    - pybytes/getstarted.html
    - pybytes/getstarted.md
    - chapter/pybytes/getstarted/intro
---

If you did not get started with our devices yet, please follow [this guide ](/gettingstarted/) first.

## Step 1: Create a Pybytes Account

If you already have a Forum or Webshop account, you can use the same credentials to log into [Pybytes](https://pybytes.pycom.io/)

Else, go to [Pybytes](https://pybytes.pycom.io) and create an account

## Step 2: Create a device 
1. Click on [Add Device](https://pybytes.pycom.io/devices). You can either add a device using USB, or the Pybytes App for [iPhone](https://apps.apple.com/us/app/pybytes/id1465696479) or [Android](https://play.google.com/store/apps/details?id=io.pycom.pybytes_android&hl=en). In this guide, we will describe the process using USB.
![](/gitbook/assets/pybytes/add-device/add-device-btn.png)

1. Select your device (WiPy, LoPy, SiPy, etc.).
![](/gitbook/assets/pybytes/add-device/select-device-type.png)

1. Select your network options. This will be how your device connects to both Pybytes and the internet. For now, we will choose WiFi. This will show a subwindow where you enter your WiFi credentials. This will only be used to connect your device with a WiFi network to access pybytes.
![](/gitbook/assets/pybytes/add-device/network-step.png)

1. Enter a unique name for your device and hit save!

![](/gitbook/assets/pybytes/add-device/customize-step.png)

1. At the end, Pybytes will show that your device profile was successfully created.

## Step 3: Provision your device

After creation, you will land on the provisioning page. This is where we 'inform' the device about the Pybytes connection and how to set it up. The first time you set up the device for use with Pybytes, you will need to provision it using the Firmware Updater Tool. This is a good moment to become familiar with the tool [here](/updatefirmware/device/).

1. Open the tool, select your board and select the bottom two checkboxes on this page

![](/gitbook/assets/pybytes/add-device/pybytes-provisioning.png)

1. This will ask for a `Pybytes activation token`. Generate a token from pybytes and paste it in the Firmware Updater tool. This will instantly generate a success message in Pybytes.

1. Continue with the firmware update to the device.

## Step 4: Your first signal

1. Reset your Pycom device using the reset button. This will reboot the device and activate the Pybytes connection automatically. The output will look similar to this:
    ```
    >>> ets Jun  8 2016 00:22:57

    rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
    configsip: 0, SPIWP:0xee
    clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
    mode:DIO, clock div:1
    load:0x3fff8020,len:8
    load:0x3fff8028,len:2140
    ho 0 tail 12 room 4
    load:0x4009fa00,len:19760
    entry 0x400a05bc
    WMAC: {redacted}
    Firmware: {latest version}
    Pybytes: {latest version}
    Initialized watchdog for WiFi and LTE connection with timeout 1260000 ms
    Error connecting using WIFI: Connection to AP Timeout!
    ERROR! Could not connect to Pybytes!
    Pybytes configuration read from /flash/pybytes_config.json

    ```







## Final remarks
If you wish to disable Pybytes, yo ucan use `pycom.pybytes_on_boot(False)` will permanently
## Step 1: Go to the registration page

1. Go to [https://pybytes.pycom.io](https://pybytes.pycom.io/?utm_source=docs&utm_medium=web&utm_campaign=pybytes-getting-started).
2. Enter your full name, email address and set a password for your account.
3. Confirm the verification message sent to your email address.
4. Click on the link and complete your login.

## Go Invent!

Now it's time to explore Pybytes. You can start by [connecting your Pycom board to Pybytes](../connect).
