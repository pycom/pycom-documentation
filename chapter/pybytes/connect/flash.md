# Connecting a device to Pybytes by flashing Pybytes library manually

In this section, we will explain to you how to connect your device to Pybytes by flashing Pybytes library manually.

{% hint style='tip' %}
From firmware 1.16.x onwards all Pycom devices come with Pybytes library build-in `/frozen` folder.
That means that you can add your device quickly without the need of flashing Pybytes library manually. [Click here for more information.](quick.md)
{% endhint %}

## Step 1: Download your Pybytes Library
At the last step of the "Add Device" process:
<p><img src ="../../../img/pybytes/add-device-wizard/7.png" width="800"></p>

1. Click on download *Pybytes library*
<p><img src ="../../../img/pybytes/pybytes-library-wizard.png" width="550"></p>

{% hint style='info' %}
You can also download *Pybytes library* at the device's settings page:
1. Navigate to your device in Pybytes;
2. Click on settings tab;
3. Click on *Download Pybytes library* button;
<p><img src ="../../../img/pybytes/pybytes-library-settings.png"></p>
{% endhint %}

## Step 2. Flash your device with Pymakr

{% hint style='info' %}
In case you haven't installed Pymakr plugin, follow [these instructions](../../pymakr/installation/atom.md).
{% endhint %}

1. Connect your device to your computer with USB cable.
2. Extract download Pybytes library and open extracted folder with Atom.
3. Get your device serial port: in Pymakr plugin click on *More* > *get serial ports*
4. Paste your device's serial port to `pymakr.conf` file:
        {
            "address": "PASTE_YOUR_SERIAL_PORT_HERE",
            "username": "micro",
            "password": "python",
            "sync_folder": "flash"
        }
5. Checkout your `flash/config.py` file. It will be pre-filled with your information from Pybytes
Like deviceToken or WiFi credentials. You can change e.g. your WiFy password here.
6. Put your device in [safe boot mode](../../toolsandfeatures/bootmodes.md#safe-boot).
7. Upload code to your device by clicking on *Upload* button in Pymakr.
After all Pybytes library files are uploaded to device, device will restart and will connect to Pybytes.

{% hint style='tip' %}
Pybytes library is written to `/flash` folder and will take precedence over build in firmware libraries in `/frozen` folder.
{% endhint %}

# Next step: Set up your device's dashboard!
Now it's time to display data from your device into Pybytes dashboard. You can check more about it [here!](../dashboard/intro.md)
