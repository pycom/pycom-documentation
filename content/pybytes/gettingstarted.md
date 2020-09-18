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

2. Select your device (WiPy, LoPy, SiPy, etc.).
![](/gitbook/assets/pybytes/add-device/select-device-type.png)

3. Select your network options. This will be how your device connects to both Pybytes and the internet. For now, we will choose WiFi. This will show a subwindow where you enter your WiFi credentials. This will only be used to connect your device with a WiFi network to access pybytes.
![](/gitbook/assets/pybytes/add-device/network-step.png)

4. Enter a unique name for your device and hit save!

![](/gitbook/assets/pybytes/add-device/customize-step.png)

5. At the end, Pybytes will show that your device profile was successfully created.

![](/gitbook/assets/pybytes/add-device/final-step.png)

## Step 3: Provision your device

After creation, you will land on the provisioning page. This is where we 'inform' the device about the Pybytes connection and how to set it up. The first time you set up the device for use with Pybytes, you will need to provision it using the Firmware Updater Tool. This is a good moment to become familiar with the tool [here](/updatefirmware/device/).

1. Open the tool, select your board and select the bottom two checkboxes on this page

![](/gitbook/assets/pybytes/add-device/pybytes-provisioning.png)

2. This will ask for a `Pybytes activation token`. Generate a token from pybytes and paste it in the Firmware Updater tool. This will instantly generate a success message in Pybytes.

![](/gitbook/assets/pybytes/add-device/pybytes-provisioning2.png)

3. Continue with the firmware update to the device.

## Step 4: Your first signal

1. Reset your Pycom device using the reset button. This will reboot the device and activate the Pybytes connection automatically. The output will look similar to this. You should see the `Last Connection` status in Pybytes change from `Never` to `Seconds ago`
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
    WiFi connection established
    Connected to MQTT mqtt.pybytes.pycom.io
    Pybytes connected successfully (using the built-in pybytes library)
    Pybytes configuration read from /flash/pybytes_config.json

    ```

    > If you get any kind of error message, check the WiFi credentials you entered are correct and that you are in range of this WiFi network

2. Use the opportunity to define a signal in Pybytes. The signal number can be anywhere from 0-254 (255 is reserved)

![](/gitbook/assets/pybytes/add-device/define-signal.png)

3. Now, in the REPL, you can type:
    ```python
    >>> pybytes.send_signal(1, "hello world")
    ```
    And it will show up on Pybytes in the `signals` tab:

![](/gitbook/assets/pybytes/add-device/send-signal.png)

> Next to `pybytes.send_signal(...)`, we can use ...



## Final remarks
If you wish to disable Pybytes, you can use `pycom.pybytes_on_boot(False)` will permanently

Continue to [display data from your device into the Pybytes dashboard](/pybytes/dashboard/) 
