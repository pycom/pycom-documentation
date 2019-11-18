---
title: "Connect the device to Pybytes"
aliases:
    - pybytes/connect/quick.html
    - pybytes/connect/quick.md
    - chapter/pybytes/connect/quick
---

In this section, we explain to you how to connect your device to Pybytes quickly using the Firmware Updater tool.

### Download Pycom Firmware Updater tool

1. At the final step of the "Add Device" process, you can download and install the [Pycom Firmware Updater tool](https://pycom.io/downloads/)).
![](/gitbook/assets/pybytes/add-device/connect-your-device-component.png)

1. Copy the activation token by pressing the Copy button. The activation token is valid for one hour. If your activation token has expired, you can create a new one.


### Flash Pybytes firmware with Pycom Firmware Updater tool

#### Before you start
* Connect your device to the computer
* If your device is already connected, make sure it is not connected to Pymakr

#### Firmware update process

1. Open the Pycom Firmware Updater tool on your computer and click on the Continue button.
![](/gitbook/assets/pybytes/add-device/fw-updater/intro-screen.png)

1. Click again on the Continue button.
![](/gitbook/assets/pybytes/add-device/fw-updater/attention-screen.png)

{{% hint style="info" %}}
If your device is already connected to your computer, on MacOS serial port will be automatically filled for you.
At this step, you can also click on Rescan ports button to update ports listed in the Firmware Updater.
{{% /hint %}}

1. Check the options "Erase flash file system" and "Force update Pybytes registration";
![](/gitbook/assets/pybytes/add-device/fw-updater/settings-screen.png)

1. Paste your activation token from Pybytes. Firmware Updater should display **Registration successful!**
![](/gitbook/assets/pybytes/add-device/fw-updater/activation-token-screen.png)

1. Then press the Continue button. Your device will be flashed with the Pybytes firmware. This should take about a minute.
![](/gitbook/assets/pybytes/add-device/fw-updater/update-in-progress-screen.png)

1. After the updating process is done, you will see the final screen. Click on Done to close the Firmware Updater.
![](/gitbook/assets/pybytes/add-device/fw-updater/success-screen.png)

## Next step: Set up your device's dashboard!

[Now it's time to display data from your device into Pybytes dashboard](../../dashboard)
