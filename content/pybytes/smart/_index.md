---
title: "Pybytes App"
aliases:
---

The Pybytes app will allow you to quickly provision any number of devices effortlessly to Pybytes. This is especially useful if you are planning to provision multiple devices, as the device type, WiFi network and name get automatically assigned in the Pybytes application, and all you will need to do is power up the devices that need provisioning.

> Your devices will need to run **firmware 1.20.1** or newer.

Further down the page you will find the following information:

*  [Pybytes app installing and Device Provisioning](#pybytes-app-installing-and-device-provisioning)
*  [Take into consideration](#take-into-consideration)
*  [Quick help/FAQ](#faq)

> Before starting, make sure you have enabled Pybytes smart config on the devices you want to provision by using `pybytes.smart_config(True)`, or by checking the option in the firmware updater tool. New devices will come with pybytes and smart config enabled by default.

## Pybytes app installing and Device Provisioning

1. Install the app for [iPhone](https://apps.apple.com/us/app/pybytes/id1465696479) or [Android](https://play.google.com/store/apps/details?id=io.pycom.pybytes_android&hl=en).
2. Use your Pybytes account to log in.
3. On the next screen, you will need to enter your Wi-Fi credentials.
4. After pressing the START button, a list of devices will appear on the screen. It may take up to several minutes to provision all of your devices. The first device usually appears on the screen within one minute.

![](/gitbook/assets/pybytes/iOS/login.jpg) 
![](/gitbook/assets/pybytes/iOS/wifiSettings.jpg)
![](/gitbook/assets/pybytes/iOS/provisionedDevicesIOS.jpg)

> The name of a device provisioned device is its Wireless MAC address.

5. As your devices are provisioning in Pybytes devices management platform, you will see notifications appearing on the screen when the provisioning is successful. You will also see the provisioned devices in the Devices section.

![](/gitbook/assets/pybytes/iOS/provisionedDevicesPybytes.png)

## Take into consideration

* If you are using iOS 12, turn off your Wi-Fi completely on your iPhone.
* Only use a Wi-Fi network with 2.4GHz as Pycom devices cannot connect to a 5GHz network.
* Your device might be provisioned faster if you move your device closer to your Wi-Fi router.
* Make sure your devices are powered on and running firmware 1.20.1 or newer.
* You cannot provision the same devices on the different Pybytes account unless you [erased them completely](../../advance/cli/#erase-all) and flashed the latest firmware again with FW updater tool.
* If there is a spinning wheel on your screen, that means that your device is being provisioned. If it has disappeared, then press the START button again.


## FAQ

### I can’t connect to Wi-Fi in Pybytes iOS

* Firstly, check your version of iOS. If it is iOS 12, then turn off the Wi-Fi connection on your phone. Following this, try to use Pybytes iOS again, and it should now automatically connect to the WiFi.

* If you have version that is later than iOS 12, check your Wi-Fi router setting. It should run on a 2.4 HGz Wi-Fi network.

### No devices were provisioned after 5 min.

* Check if your devices are on

* Move your devices closer to the Wi-Fi router

* Check that no-one else in the room is trying to provision devices with the Pybytes iOS app.

### How long does the provisioning take?

* On average, it takes up to 2 minutes to provision 6 devices.
