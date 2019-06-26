---
title: "Flash Pybytes-library (advanced)"
aliases:
    - pybytes/connect/flash.html
    - pybytes/connect/flash.md
    - chapter/pybytes/connect/flash
---

In this section, we will explain to you how to connect your device to Pybytes by flashing the Pybytes library.
Use this, if you want to have full control over the Pybytes library on your device.

{{% hint style="info" %}}
Pybytes firmware already contains [Pybytes library](https://github.com/pycom/pycom-micropython-sigfox/tree/pybytes-master/esp32/frozen/Base). That means that you can [add your device quickly](../quick) without the need of flashing Pybytes library.
{{< /hint >}}

### Step 1: Flash stable firmware to your device with Pycom firmware updater tool
1. Open Pycom firmware updater tool
2. Select a stable firmware
3. Click on continue

Here's more information about [firmware updates](/gettingstarted/installation/firmwaretool).

### Step 2: Download your Pybytes Library

You can download _Pybytes library_ at the device's settings page:

2. Navigate to your device in Pybytes;

3. Click on the settings tab;

4. Click on the _Download_ button at Pybytes library section;

![](/gitbook/assets/pybytes/flash-pybytes-library/settingsTab.png)

### Step 3. Flash your device with Pymakr

{{% hint style="info" %}}
In case you haven't installed Pymakr plugin, follow [these instructions](/pymakr/installation/atom).
We recommend to install Pymakr in Atom.
{{< /hint >}}

1. Connect your device to the computer with a USB cable.
2. Open zip archive of Pybytes library and extract a containing folder.
3. Check your `flash/pybytes_config.json` file. It should be pre-filled with your Pybytes credentials (deviceToken, WiFi credentials, ...)
3. Open Pybytes library folder as a project folder in Atom.
4. Click on the Connect button in Pymakr. Pymakr should connect to your device.
7. Upload code to your device by clicking on the _Upload_ button in Pymakr.

   After all the Pybytes library files are uploaded to your device, the device will restart and connect to Pybytes.
