---
title: "Connect the device to Pybytes"
aliases:
    - pybytes/connect/quick.html
    - pybytes/connect/quick.md
    - chapter/pybytes/connect/quick
---

In this section, we explain to you how to connect your device to Pybytes quickly using the Firmware Updater tool.

### 1. Download Pycom Firmware updater tool

![](/gitbook/assets/pybytes/add-device/final-step.png)

From the last step of the "Add Device" process. Download and install Pycom Firmware updater tool from the provided link (Firmware updater is also available on [pycom.io](https://pycom.io/downloads/)).

![](/gitbook/assets/pybytes/add-device/connect-your-device-component.png)

Copy the activation token by pressing the copy button. The activation token is valid for one hour. If your activation token is expired, you can create a new one.

### 2. Flash Pybytes firmware with Pycom Firmware updater tool

#### Before you start
* Connect your device to the computer
* If your device is already connected, make sure it is not connected to Pymakr

#### Firmware update process

Open the Pycom Firmware updater tool on your computer and click on the Continue button.

![](/gitbook/assets/pybytes/add-device/fw-updater/intro-screen.png)

Click again on the Continue button.

![](/gitbook/assets/pybytes/add-device/fw-updater/attention-screen.png)

{{% hint style="info" %}}
If your device is already connected to your computer, on MacOS serial port will be automatically filled for you.
At this step, you can also click on Rescan ports button to update ports listed in the Firmware updater.
{{< /hint >}}

Check the options "Erase flash file system" and "Force update Pybytes registration";

![](/gitbook/assets/pybytes/add-device/fw-updater/settings-screen.png)

Paste your activation token from Pybytes. Firmware updater should display **Registration successful!**

![](/gitbook/assets/pybytes/add-device/fw-updater/activation-token-screen.png)

Then press the Continue button. Your device will be flashed with the Pybytes firmware. This should take about a minute.

![](/gitbook/assets/pybytes/add-device/fw-updater/update-in-progress-screen.png)

After the updating process is done. You will be welcomed with the final screen. Click on Done to close the Firmware updater.

![](/gitbook/assets/pybytes/add-device/fw-updater/success-screen.png)

## Next step: Set up your device's dashboard!

[Now it's time to display data from your device into Pybytes dashboard](../../dashboard)
