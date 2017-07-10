# Connecting via Telnet

After installing the Pymakr Plugin, a device may be connected via the telnet interface. Please see the following steps:

1. Ensure that Pycom device is turned on
2. Connect the host computer to the WiFi Access Point named after your board (the SSID will be as follows e.g. lopy-wlan-xxxx, wipy-wlan-xxxx). The ``password`` is www.pycom.io
3. Open Atom and verify that the Pymakr Plugins has been installed
4. In the menu, go to Atom > Preferences > Packages > Pymakr (This will vary from MacOS/Linux/Windows)
5. By default, the address will be listed as 192.168.4.1. If not, change this to 192.168.4.1
6. The default ``username`` and ``password`` are micro and python, respectively
7. Click ``Connect``

<p align="center"><img src ="../../../img/pymakr-plugin-settings.png" width="300"></p>

In the lower portion of the screen, within the console, press ``Connect`` and the connection process will take place. Upon completion, a message stating ‘Connecting on 192.168.4.1...’ will appear, followed a >>> prompt if successful.
