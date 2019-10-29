---
title: "Pybytes iOS"
aliases:
---

Pybytes iOS app will allow you to quickly provision any number of devices effortlessly to Pybytes.

<span style="background-color:#00cc96;">&nbsp;Tip:&nbsp;</span>&nbsp;Your devices will need to run **firmware 1.20.1** or newer.

Further down the page you will find the following information:

*  [Pybytes iOS installing and Device Provisioning](#installing)
*  [Take into consideration](#recommendations)
*  [Quick help/FAQ](#faq)


<a id="installing"></a>
### Pybytes iOS installing and Device Provisioning

1. Go to the App Store and download Pybytes iOS app.
2. Use your Pybytes web app account to log in.
<br/>
<br/>
<span style="background-color:#00cc96;">&nbsp;Tip:&nbsp;</span>&nbsp;Go to Pybytes web app with Safari on iOS or macOS and save your log-in credentials.
Then your iPhone will pre-fill your saved password.

3. On the next screen, you will need to enter your Wi-Fi credentials.
<br/>
<br/>
<img src="/gitbook/assets/pybytes/iOS/login.jpg" alt="Pybytes iOS login" width="200" style="padding:0px;box-shadow: 2px 2px 8px 2px #cccccc;"/>&nbsp;&nbsp;&nbsp;&nbsp;<img src="/gitbook/assets/pybytes/iOS/loginSavedPasswords.jpg" alt="Pybytes iOS login" width="200" style="padding:0px;box-shadow: 2px 2px 8px 2px #cccccc;" />

4. After pressing the START button, a list of devices will appear on the screen. It may take up to several minutes to provision all of your devices. The first device usually appears on the screen within one minute.
<br/>
<br/>
<span style="background-color:#00cc96;">&nbsp;Tip:&nbsp;</span>&nbsp;The name of a device provisioned device is its Wireless MAC address.
<br/>
<br/>
<img src="/gitbook/assets/pybytes/iOS/wifiSettings.jpg" alt="Pybytes iOS login" width="200" style="padding:0px;box-shadow: 2px 2px 8px 2px #cccccc;"/>&nbsp;&nbsp;&nbsp;&nbsp;
<img src="/gitbook/assets/pybytes/iOS/provisionedDevicesIOS.jpg" alt="Pybytes iOS login" width="200" style="padding:0px;box-shadow: 2px 2px 8px 2px #cccccc;"/>
5. As your devices are provisioning in Pybytes devices management platform, you will see notifications appearing on the screen when the provisioning is successful. You will also see the provisioned devices in the Devices section.
<br/>
<br/>
<img src="/gitbook/assets/pybytes/iOS/provisionedDevicesPybytes.png" alt="Pybytes iOS login" style="padding:0px;box-shadow: 2px 2px 8px 2px #cccccc;"/>

<a id="recommendations"></a>
### Take into consideration

* If you are using iOS 12, turn off your Wi-Fi completely on your iPhone.
* Only use a Wi-Fi network with 2.4GHz as Pycom devices cannot connect to a 5GHz network.
* Your device might be provisioned faster if you move your device closer to your Wi-Fi router.
* Make sure your devices are powered on and running firmware 1.20.1 or newer.
* You cannot provision the same devices on the different Pybytes account unless you [erased them completely](../../advance/cli/#erase-all) and flashed the latest firmware again with FW updater tool.
* If there is a spinning wheel on your screen, that means that your device is being provisioned. If it has disappeared, then press the START button again.
* Please take into account that we are developing a new feature and therefore some niggles can occur. (Please bear with us!) If any issues occur whilst you are using Pybytes iOS, then drop us a line at <a href="mailto:support@pycom.io">support@pycom.io</a>.

<a id="faq"></a>
### FAQ

<span style="background-color:#00cc96;">&nbsp;I can’t connect to Wi-Fi in Pybytes iOS&nbsp;</span>

* Firstly, check your version of iOS. If it is iOS 12, then turn off the Wi-Fi connection on your phone. Following this, try to use Pybytes iOS again, and it should now automatically connect to the WiFi.

* If you have version that is later than iOS 12, check your Wi-Fi router setting. It should run on a 2.4 HGz Wi-Fi network.

<span style="background-color:#00cc96;">&nbsp;No devices were provisioned after 5 min.&nbsp;</span>

* Check if your devices are on

* Move your devices closer to the Wi-Fi router

* Check that no-one else in the room is trying to provision devices with the Pybytes iOS app.

<span style="background-color:#00cc96;">&nbsp;How long does the provisioning take?&nbsp;</span>

* On average, it takes up to 2 minutes to provision 6 devices.

<br/>
Our hope is that Pybytes iOS will simplify the device provisioning process. However, as we are still in a development pipeline, sometimes there can be a hitch in the silk. If that happens, please let us know! Drop us a line at <a href="mailto:support@pycom.io">support@pycom.io</a>.
<br/>
<br/>
<br/>
