---
title: "Drivers"
aliases:
    - gettingstarted/installation/drivers.html
    - gettingstarted/installation/drivers.md
    - chapter/gettingstarted/installation/drivers
---

## Linux

You should not need to install any drivers for our devices to be recognised by Linux. You may how ever need to adjust permissions to make sure you have access to the serial port. On most distributions this can be done by adding your user to the `dialout` user group. Please check the specific instructions for your linux distribution for how to do this.

## macOS

On macOS you shouldn't need to do anything special to get our device to work.

## Windows

All our products will work out of the box for Windows 8/10/+. If using Windows 7, drivers to support the Pysense/Pytrack/Pyscan/Expansion Board 3.0 boards will need to be installed.

### Download

Please download the driver software from the link below.

[Pysense/Pytrack/Pyscan/Expansion Board 3.0 Serial Driver (save the file to your computer)](https://raw.githubusercontent.com/pycom/pycom-documentation/master/pytrackpysense/installation/pycom.inf)


### Installation

First navigate open the Windows start menu and search/navigate to \`Device Manager. You should see your Pytrack/Pysense in the dropdown under **other devices**.

![](/gitbook/assets/win7-1.png)

Right click the device and select `Update Driver Software`.

![](/gitbook/assets/win7-2%20%281%29.png)

Select the option to **Browse my computer for driver software**.

![](/gitbook/assets/win7-3.png)

Next you will need to navigate to where you downloaded the driver to (e.g. **Downloads** Folder).

![](/gitbook/assets/win7-4%20%281%29.png)

Specify the folder in which the drivers are contained. If you haven't extracted the `.zip` file, please do this before selecting the folder.

![](/gitbook/assets/win7-5%20%281%29.png)

You may receive a warning, suggesting that Windows can't verify the publisher of this driver. Click `Install this driver software anyway` as this link points to our official driver.

![](/gitbook/assets/win7-6%20%281%29.png)

If the installation was successful, you should now see a window specifying that the driver was correctly installed.

![](/gitbook/assets/win7-7.png)

To confirm that the installation was correct, navigate back to the `Device Manager` and click the dropdown for other devices. The warning label should now be gone and Pytrack/Pysense should be installed.

![](/gitbook/assets/win7-8.png)

