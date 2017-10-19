# Firmware Update Tools

We strongly recommend you to upgrade your firmware to the latest version as we are constantly making improvements and adding new features to the devices.

Here are the download links to the update tool. Please download the appropriate one for your OS and follow the instructions on the screen.

- [Windows](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=win32&redirect=true)
- [MacOS](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=macos&redirect=true) (10.11 or Higher)
- [Linux](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=unix&redirect=true) (requires dialog package)

{% hint style='info' %}
Previous versions of firmware are available for download on the **[Pycom](https://www.pycom.io/downloads/)** website.
{% endhint %}

### Updating Device Firmware

The instructions given by the updater tool should be followed carefully. The basic procedure can be found below:

{% hint style='info' %}
If you are having trouble connecting via USB, make sure you have the correct [FTDI drivers](http://www.ftdichip.com/Drivers/D2XX.htm) installed.
{% endhint %}

1. Disconnect your device from your computer
2. Connect a jumper cable or wire between G23 and GND
3. Reconnect the board via USB to your computer, this puts the device in ‘firmware update mode’.
4. Run the Firmware Upgrade tool
5. Remove the G23 to GND jumper cable/wire
6. Reboot the device (button or power off then on)

<p align="center"><img src ="../../../img/firmware-update.png" width="500"></p>

After you’re done with upgrading, you can use the Pymakr Plugins to upload and run programs in your device.

{% hint style='danger' %}
Make sure the **TX jumper** is present on your expansion board, as the jumpers sometimes come loose in the box during transport. Without this jumper, the updater will fail.
{% endhint %}
