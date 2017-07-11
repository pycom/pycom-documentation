# Pymakr Plugin Installation for Atom

For beginners, users getting started with MicroPython & Pycom as well as Atom text editor users, we recommend the **Pymakr Plugin for Atom**. This section will help you get started using the Atom Text Editor & Pymakr Plugin.

Please follow these steps to install the Pymakr Plugin:

1. Ensure that you have Atom installed and open.
2. Navigate to the Install page, via Atom > Preferences > Install
3. Search for Pymakr and select the official Pycom Pymakr Plugin.
4. You should now see and Install button. Click this to download and install the Pymakr Plugin.
5. That’s it! You’ve installed the Pymakr Plugin for Atom.

<p align="center"><img src ="../../../img/atom-text-editor.png" width="600"></p>


## Initial Configuration

After installing the Pymakr Plugin, you need to take a few seconds to configure it for first time use. Please follow these steps:

1. Connect your Pycom device to your computer via USB. **Remove the wire between GND and G23**, before plugging in your device, if you have just finished upgrading your firmware!
2. Open Atom and ensure that the Pymakr Plugin has correctly installed.
3. In the menu, go to Atom > Preferences > Packages > Pymakr. This may vary depending on your operating system!
4. Open the Pymakr console by clicking the 'Open' button, located in the lower right side of the Atom window.
5. Click, 'More' followed by 'Get Serial Ports'. This will copy the serial address of your expansion board to your clipboard.
6. Navigate to 'Settings' > 'Global Settings'
7. Paste this into the text field 'Device Address'
8. Press connect and the Pymakr console should show three arrows '>>>', indicating that you are connected!

{% hint style='info' %}
You can also connect to your device via WiFi as the device can open a telnet server. For more information please see [XYZ]().
{% endhint %}
