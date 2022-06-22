---
title: "Introduction to PyGos"
aliases:
    - pylife/devices.html
    - pylife/devices.md
    - chapter/pylife/devices
---

## PyGo Overview

![PyGo Top View](/gitbook/assets/pylife/devices/thumbnail_PyGoTopView.png)

![PyGo Top View](/gitbook/assets/pylife/devices/thumbnail_PyGoBottomView.png)

  * Dimensions: 41 x 24 x 12.5mm
  * Weight: 24g
  * [PyGo Datasheet](/gitbook/assets/pylife/devices/Pycom_001_Specsheets_PYGO_v1.pdf)

The optional USB cradle allows you to charge the PyGo over USB as well as to connect to the serial port for development purposes.


![PyGo Top View](/gitbook/assets/pylife/devices/thumbnail_PyGoChargeCradle.png)


## Connecting PyGos
After installing the Mobile App, you will be asked to connect your PyGos.  

Make sure:

1. Your PyGo is charging (you should see a charging symbol on screen).
2. You turn on the Bluetooth on your Mobile Phone.
3. Your PyGo is within a few meters from your phone.

This can also be done anytime in the 'Devices' tab of PyLife.

From the Mobile App, go to Add a PyGo and tap `Start Scanning`

The Pylife Mobile App will use your mobile phone's Bluetooth to look for PyGos. 

![Device Scanning](/gitbook/assets/pylife/devices/device_scanning.png)
![Device Scanning](/gitbook/assets/pylife/devices/device_active_scan.png)

At this point you can put a PyGo on to a Qi-compatible wireless charger or into a USB cradle to start charging and wake it up.
Once the screen shows it is charging, click the `Start scanning` button, and the app should find your PyGo. 
The device will have a unique ID (e.g. PyGo 12345) which cannot be changed, but you can optionally give it a name to easily identify it.

Your added PyGos are displayed under the Devices menu section.
Click 'Add PyGo', and your PyGo is now paired. Please now proceed imediately to update its firmware.

Please note: if you have more than one PyGo, we recommend you go through the complete setup process for one of them before starting with the next.

You can add more than one PyGo to your App. If you add more than one PyGo, make sure to give each PyGo an obvious name.

![Devices List](/gitbook/assets/pylife/devices/devices_list.png)

## Frequently Asked Questions
  * How do I turn my PyGo on?
    * Your PyGo is an always on device. You can wake it up by charging it, or by double tapping the screen. 
  * How do I charge my PyGo?
    * You can charge your PyGo either by placing it on a Qi-compatible wireless charger, or by putting it in a USB cradle. When it is charging a charging animation will appear on the screen. Charging from 0% takes approximately 3-4 hours on USB, or 6-8 hours on a wireless charger.
  * How will I know when the PyGo is fully charged?
    * When your PyGo is fully charged it will show this on the display, and also in the 'Devices' section of the PyLife app.
  * How long will the battery last for?
    * A PyGo has three power profiles: Performance, Standard, and Eco. Battery life is still being characterised, and depends heavily on network and physical conditions.
      * In performance mode the PyGo is most responsive and will wake up every 60 seconds unless it is woken with a double tap. In this mode the battery life is approximately 6 hours.
      * In Standard mode the PyGo will sleep for 5 minutes between updates unless it is woken up with a double tap. The battery life is approximately 12 hours.
      * In Eco mode the PyGo will sleep for 15 minutes between updates unless it is woken up with a double tap. The battery life is approximately 18 hours.
  * How do I turn my PyGo Off?
    * You do not need to turn the PyGo off. If you want to prolong battery life simply turn it to Eco mode in the app.
  * What chargers are compatible with PyGos?
    * All Qi compatible wireless chargers are compatible.
  * My PyGo gets hot while charging?
    * It is normal for devices that are using wireless charging to release heat. Due to the small size of the PyGo it can feel quite hot to touch as it radiates the heat. This is normal, and the temperature is monitored internally to keep it at safe levels. However as with all electronics you should not leave it unattended while charging.
  * Shall I leave my PyGo Charging over night or when I am not present?
    * No. As with all electronics, you should always remain prudent and charge the PyGo only when you are present and conscious.
  * Is the recessed button on the bottom of the PyGo a reset button?
    * No. The hole on the bottom with a recessed red subtance is part of the environmental sealing, so should not be pressed as this may effect the IP rating of the device.


## PyGo Settings

To open the PyGo settings, go to the 'Devices' tab and tap on the PyGo in the list.  

Here you can do:

  * Connect alerts to the device
  * Check and configure mesh details
  * Check and configure device details
  * Forget the PyGo
  * Upload device icon

![Device Settings](/gitbook/assets/pylife/devices/device_settings_with_alert.png)


