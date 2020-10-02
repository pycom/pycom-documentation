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

    > If you get any kind of error message, check the WiFi credentials you entered are correct and that you are in range of this WiFi network

2. Now, in the REPL, you can type:
    ```python
    >>> pybytes.send_signal(1, "hello world")
    ```
    And it will show up on Pybytes in the `signals` tab:

![](/gitbook/assets/pybytes/add-device/send-signal.png)

You can continue to [display data from your device into the Pybytes dashboard](/pybytes/dashboard/) 

## Final remarks
If you wish to disable Pybytes, you can use `pycom.pybytes_on_boot(False)` will permanently. It is also possible to start Pybytes in a later stage (not on boot) by importing the module:
```python
from _pybytes import Pybytes
pybytes = Pybytes
```


