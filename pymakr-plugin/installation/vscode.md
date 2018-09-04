# Visual Studio Code

Pycom also supports Microsoft's Visual Studio Code IDE platform with the Pymakr Plugin. To download Visual Studio Code, navigate to [VS Code](https://code.visualstudio.com/).

You will also need NodeJS installed on your PC. Please download the latest LTS version available [from the NodeJS website.](https://nodejs.org/)

Please follow these steps to install the Pymakr VSCode Extension:

1. Ensure that you have VSCode installed and open.

![](../../.gitbook/assets/vsc_setup_step_1-1.png)

2. Navigate to the Extensions page, using the 5th button in the left navigation

![](../../.gitbook/assets/vsc_setup_step_2-1.png)

3. Search for `Pymakr` and click the install button next to it.

![](../../.gitbook/assets/vsc_setup_step_3.png)

4. Within a few minutes, a reload button should appear. Press it to reload VSCode.

![](../../.gitbook/assets/vsc_setup_step_4.png)

5. That’s it! You’ve installed the Pymakr Extension for VSCode

![](../../.gitbook/assets/vsc_setup_step_5%20%281%29.png)

## Connecting via Serial USB

After installing the Pymakr Plugin, you need to take a few seconds to configure it for first time use. Please follow these steps:

1. Connect your Pycom device to your computer via USB. If you are using an

   Expansion Board, and have just finished a firmware upgrade, be sure to **Remove**

   **the wire between GND and G23** and reset your device by pressing the button.

2. Open Visual Studio Code and ensure that the Pymakr Plugin has correctly installed.

![](../../.gitbook/assets/vsc_config_step_1-1.png)

3. Click `All commands` on the bottom of the Visual Studio Code window

![](../../.gitbook/assets/vsc_config_step_2-1.png)

4. In the list that appears, click `Pymakr > Extra > List Serial Ports`

![](../../.gitbook/assets/vsc_config_step_3-1.png)

5. This will list the available serial ports. If Pymakr is able to auto-detect which to use, this will be copied to your clipboard. If not please manually copy the correct serial port.

![](../../.gitbook/assets/vsc_config_step_4.png)

6. Once again click `All commands`, then click `Pymakr > Global Settings`. This will open a JSON file. Paste the serial address you copied earlier into the field `address` and save the file.

![](../../.gitbook/assets/vsc_config_step_5-1.png)

7. Finally close the JSON file, click `All commands`, then `Pymakr > Connect` to connect your device. The Pymakr console should show three arrows `>>>`, indicating that you are connected

![](../../.gitbook/assets/vsc_config_step_6%20%281%29.png)

These settings can also be applied on a per project basis by clicking `All commands` then `Pymakr > Project Settings`. This will open a JSON file which you can edit to enter your desired settings for the currently open project.

{% hint style="info" %}
This process is easiest with either a Pycom Expansion Board or a Pytrack/Pysense as the addresses are automatically selected. For external products such as FTDI USB Serial Cables, the serial address may need to be copied manually. Additionally, the reset button on the device may also need to be pressed before a connection message appears.
{% endhint %}

## Connecting via Telnet

After installing the Pymakr Plugin, a device may be connected via the telnet interface. Please see the following steps:

1. Ensure that Pycom device is turned on
2. Connect the host computer to the WiFi Access Point named after your board

   \(the SSID will be as follows e.g. `lopy-wlan-xxxx`, `wipy-wlan-xxxx`, etc.\).

   The password is `www.pycom.io`.

3. Follow the steps as above in the "Connecting via Serial USB" section but

   enter `192.168.4.1` as the address.

4. The default username and password are `micro` and `python`,

   respectively.

5. Finally close the JSON file, click `All commands`, then `Pymakr > Connect`,

   Pymakr will now connect via telnet.

