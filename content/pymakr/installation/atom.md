---
title: "Atom"
aliases:
    - pymakr/installation/atom.html
    - pymakr/installation/atom.md
    - chapter/pymakr/installation/atom
---

For beginners, users getting started with MicroPython & Pycom as well as Atom text editor users, we recommend the **Pymakr Plugin for Atom**. This section will help you get started using the Atom Text Editor & Pymakr Plugin.

Please follow these steps to install the [Pymakr Plugin](https://atom.io/packages/pymakr):

1. [Download and install](https://atom.io) Atom. Ensure that you have Atom installed and open.

![](/gitbook/assets/atom_setup_step_1-1.png)

1. Navigate to the Install page, via `Atom > Preferences > Install`
![](/gitbook/assets/atom_setup_step_2-1.png)

1. Search for `Pymakr` and select the official Pycom Pymakr Plugin.
![](/gitbook/assets/atom_setup_step_3-1.png)

1. You should now see and click the Install button. This will download and install the Pymakr Plugin.
![](/gitbook/assets/atom_setup_step_4-1.png)

1. That's it! You've installed the Pymakr Plugin for Atom.
![](/gitbook/assets/atom_setup_step_5-1.png)

## Connecting via Serial USB

After installing the Pymakr Plugin, you need to take a few seconds to configure it for first time use. Please follow these steps:

1. Connect your Pycom device to your computer via USB. If you are using an Expansion Board 2.0, and have just finished a firmware upgrade, be sure to **remove the wire between GND and G23** and reset your device by pressing the button.
   Note: you don't need the wire for Expansion Board 3.0

1. Open Atom and ensure that the Pymakr Plugin has correctly installed.
![](/gitbook/assets/atom_config_step_2-1.png)

4. Pymakr has auto-connection enabled by default. In case your device didn't open right away, click on the button `Connect device` and then on your device.

![](/gitbook/assets/atom_config_step_4.png)

7. Now it should show three arrows `>>>`, indicating that you are connected!

![](/gitbook/assets/atom_config_step_7%20%281%29.png)

These settings can also be applied on a per project basis by clicking `Settings` then `Project Settings`. This will open a JSON file which you can edit to enter your desired settings.

{{% hint style="info" %}}
This process is easiest with either a Pycom Expansion Board or a Pytrack/Pysense as the addresses are automatically selected. For external products such as FTDI USB Serial Cables, the serial address may need to be copied manually. Additionally, the reset button on the device may also need to be pressed before a connection message appears.
{{% /hint %}}

## Connecting via Telnet

After installing the Pymakr Plugin, a device may be connected via the telnet interface. Please see the following steps:

1. Ensure that Pycom device is turned on
2. Connect the host computer to the WiFi Access Point named after your board (the SSID will be as follows e.g. `lopy-wlan-xxxx`, `wipy-wlan-xxxx`, etc.). The password is `www.pycom.io`.
3. Go to `Settings` > `Global Settings`

![](/gitbook/assets/atom_global_settings.png)

4. In `Devices Addresses (List)`, enter `192.168.4.1` as the address.

![](/gitbook/assets/atom_device_list.png)

4. The default username and password are `micro` and `python`, respectively.
5. Click `192.168.4.1` in the Devices List pane, Pymakr will now connect via telnet.
