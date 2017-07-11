# Connecting via Serial USB

In order to use the Pymakr Plugin with a Pycom device via USB Serial, a couple of settings need to be configured. Below are the steps required to find, set and connect to a Pycom device over USB Serial.

1. Ensure that the Pycom device is turned on and connected (Normal or Safe Boot Mode)
2. Open Atom and verify that the Pymakr Plugins has been installed
3. Click ``Open`` on the Pymakr Console, followed by the ``More`` tab
4. Next click ``get serial ports``. This will copy the first serial port to the editor's clipboard
5. Navigate to ``Global Settings`` and paste this address into the ``Device Address`` text field
6. Click ``Connect``

{% hint style='info' %}
This process is easiest with either a Pycom Expansion Board or a Pytrack/Pysense as the addresses are automatically selected. For external products such as FTDI USB Serial Cables, the serial address may need to be copied manually. Additionally, the reset button on the device may also need to be pressed before a connection message appears.
{% endhint %}

{% hint style='info' %}
If there are issues connecting over USB with the Pymakr Plugins, ensure that the correct FTDI drivers are installed. This issue is related to missing Windows drivers.
{% endhint %}
