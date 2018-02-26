# Using the Pymakr Plugin

To make it as easy as possible we developed a series of tools known as the **Pymakr Plugins**, which allow you to connect to and program your Pycom devices. These Plugins have been built for a number of text editors and IDEs to allow for users to choose their favourite development environment.

<p align="center"><img src ="../../../img/pymakr-logo.png" width="400"></p>

Extended info about these Plugins, such as how to use the Pycom console and other features can be found under [Tools & Features](../../toolsandfeatures/README.md).

{% hint style='danger' %}
**Please be aware that Pymakr IDE has been retired** and that plugins for Atom
and Visual Studio Code are under development, with intention to replace Pymakr.
Please read this
[**forum post**](https://forum.pycom.io/topic/635/pymakr-time-of-death-09-02/)
for more information.
{% endhint %}

## Installing Pymakr Plugin (Atom)

<p align="center"><img src ="../../../img/atom-text-editor.png" width="600"></p>

For beginners, users getting started with MicroPython & Pycom as well as Atom text editor users, we recommend the **Pymakr Plugin for Atom**. This section will help you get started using the Atom Text Editor & Pymakr Plugin.

Please follow these steps to install the Pymakr Plugin:

1. Ensure that you have Atom installed and open.
<p align="center"><img src ="../../../img/atom/atom_setup_step_1.png" width="600"></p>
2. Navigate to the Install page, via Atom > Preferences > Install
<p align="center"><img src ="../../../img/atom/atom_setup_step_2.png" width="600"></p>
3. Search for Pymakr and select the official Pycom Pymakr Plugin.
<p align="center"><img src ="../../../img/atom/atom_setup_step_3.png" width="600"></p>
4. You should now see and click the Install button. This will download and install the Pymakr Plugin.
<p align="center"><img src ="../../../img/atom/atom_setup_step_4.png" width="600"></p>
5. That’s it! You’ve installed the Pymakr Plugin for Atom.
<p align="center"><img src ="../../../img/atom/atom_setup_step_5.png" width="600"></p>

## Initial Configuration

After installing the Pymakr Plugin, you need to take a few seconds to configure it for first time use. Please follow these steps:

1. Connect your Pycom device to your computer via USB. **Remove the wire between GND and G23**, before plugging in your device, if you have just finished upgrading your firmware!
2. Open Atom and ensure that the Pymakr Plugin has correctly installed.
<p align="center"><img src ="../../../img/atom/atom_config_step_2.png" width="600"></p>
3. Open the Pymakr console by clicking the '^' button, located in the lower right side of the Atom window.
<p align="center"><img src ="../../../img/atom/atom_config_step_3.png" width="600"></p>
4. Click, 'More' followed by 'Get Serial Ports'. This will copy the serial address of your expansion board to your clipboard.
<p align="center"><img src ="../../../img/atom/atom_config_step_4.png" width="600"></p>
5. Navigate to 'Settings' > 'Global Settings'
<p align="center"><img src ="../../../img/atom/atom_config_step_5.png" width="600"></p>
6. Paste the serial address you copied earlier into the text field 'Device Address'
<p align="center"><img src ="../../../img/atom/atom_config_step_6.png" width="600"></p>
7. Press connect and the Pymakr console should show three arrows '>>>', indicating that you are connected!
<p align="center"><img src ="../../../img/atom/atom_config_step_7.png" width="600"></p>


{% hint style='info' %}
You can also connect to your device via WiFi as the device can open a telnet server. For more information please see [Telnet](../../toolsandfeatures/repl/telnet.md).
{% endhint %}

## Writing Code

We'll revisit this section later on in this getting started guide but you can quickly test out MicroPython by typing commands into the Pymakr Console. For example, try changing the colour of the device's LED!

We'll first import the 'pycom' library, turn the blinking LED off and then set the LED to the hexadecimal colour '0x00ff00' (green).

```python
>>> import pycom
>>> pycom.heartbeat(False)
>>> pycom.rgbled(0x00ff00)
```
