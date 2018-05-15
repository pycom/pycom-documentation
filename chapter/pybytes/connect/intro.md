# Connecting your Pycom's module to Pybytes

In this section we will explain you how to connect your device to Pybytes.

# Example to quickly add a device to Pybytes

## Step 1: Add Device Wizard
On ``Devices`` Page:

1. Click on ``Add Device``.
2. Select your device (e.g., WiPy, LoPy, SiPy, etc.);
3. Select your shield (e.g., PySense, PyTrack, PyScan or other);
4. Select your network option;
5. Enter a unique name for your device;
6. Enter the Wi-Fi credentials for your device (SSID and password);
7. Download the firmware updater for your operating system and copy the device token.

<p><img src ="../../../img/pybytes/add_device_wizard.gif" width="800"></p>

## Step 2: Run the firmware updater
Install the Firmware updater on your computer.

1. Start the ``Firmware updater``;
2. Select your device serial port (Make sure your device is connected to your computer);
3. Mark the options "Erase flash file system" and "Force update Pybytes registration";
4. Paste your device token from Pybytes;
5. The firmware updater will update the device's firmware and connect to Pybytes.

<p><img src ="../../../img/pybytes/firmware_updater.gif" width="800"></p>


# Observation
In case you want to extend Pybytes library you have an option to flash Pybytes library manually. [Click here for more information!](add-device-flashlib.md).


# Next step: Device's dashboard!
Now it's time to set up your device's dashboard. You can check more about it [here!](../dashboard/intro.md)
