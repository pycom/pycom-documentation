---
title: "Installing Drivers - Windows 7"
aliases:
    - pytrackpysense/installation/drivers.html
    - pytrackpysense/installation/drivers.md
    - chapter/pytrackpysense/installation/drivers
---

Pytrack and Pysense will work out of the box for Windows 8/10/+ (please download the correct driver through Windows Update), macOS as well as Linux. If using Windows 7, drivers to support the boards will need to be installed.

Please follow the instructions below to install the required drivers.

## Download

Please download the driver software from the link below.

[Unsigned driver for Windows 7 compatible with Pycom products](/gitbook/assets/pycom.inf.zip)
Please note that this driver is not suitable for the Expansion Board 1 & 2.
As these drivers are not signed, you may need to disable driver signing enforcement in your Windows operating system.

## Installation

First navigate open the Windows start menu and search/navigate to `Device Manager`. You should see your Pytrack/Pysense in the dropdown under **other devices**.

![](/gitbook/assets/win7-1.png)

Right click the device and select `Update Driver Software`.

![](/gitbook/assets/win7-2.png)

Select the option to **Browse my computer for driver software**.

![](/gitbook/assets/win7-3.png)

Next you will need to navigate to where you downloaded the driver to (e.g. **Downloads** Folder).

![](/gitbook/assets/win7-4.png)

Specify the folder in which the drivers are contained. If you haven't extracted the `.zip` file, please do this before selecting the folder.

![](/gitbook/assets/win7-5.png)

You may receive a warning, suggesting that windows can't verify the publisher of this driver. Click `Install this driver software anyway` as this link points to our official driver.

![](/gitbook/assets/win7-6.png)

If the installation was successful, you should now see a window specifying that the driver was correctly installed.

![](/gitbook/assets/win7-7.png)

To confirm that the installation was correct, navigate back to the `Device Manager` and click the dropdown for other devices. The warning label should now be gone and Pytrack/Pysense should be installed.

![](/gitbook/assets/win7-8.png)
