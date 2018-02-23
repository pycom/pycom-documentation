# Quick add device

From firmware 1.16.x onward all Pycom devices come with build in *Pybytes library* in firmware
specifically in `/frozen` folder. This allows you to add your device quickly to Pybytes.
You can still upload your Pybytes library [manually](quick-add-device.md).

## Follow these steps 
Install custom Firmware updater from Pybytes beta.

<p><img src ="../../img/pybytes/firmware-updater/1.png" width="650"></p>
Put your device in firmware update mode:
<p><img src ="../../img/pybytes/firmware-updater/2.png" width="650"></p>
Select your device serial port:
<p><img src ="../../img/pybytes/firmware-updater/3.png" width="650"></p>
Copy and paste your device token from Pybytes here:
<p><img src ="../../img/pybytes/firmware-updater/4.png" width="650"></p>
Now firmware updater is updating your firmware. It is asking Pybytes for your device credentials 
like WiFi password. It will write these information to device's config block.
<p><img src ="../../img/pybytes/firmware-updater/5.png" width="650"></p>
Now your device will reboot and will be connected to Pybytes.
<p><img src ="../../img/pybytes/firmware-updater/6.png" width="650"></p>
