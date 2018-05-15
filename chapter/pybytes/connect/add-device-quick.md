# Adding device quickly

From firmware 1.16.x onward all Pycom devices come with build in *Pybytes library* in firmware
specifically in `/frozen` folder. This allows you to add your device quickly to Pybytes.
You can still upload your Pybytes library [manually](add-device-flashlib.md).

{% hint style='danger' %}
If you [manually](add-device-flashlib.md) uploaded Pybytes library on your device before.
Make sure to do [factory reset](../../toolsandfeatures/bootmodes.md#factory-reset-the-filesystems) of your device filesystem.
Otherwise code in `/flash` folder will have priority over build in
library in `/frozen` folder.
{% endhint %}

## Follow these steps
Install custom Firmware updater from Pybytes beta.

1. Put your device in firmware update mode
2. Select your device serial port
3. Mark the options "Erase flash file system" and "Force update Pybytes registration"
4. Paste your device token from Pybytes
5. The firmware updater will update the device's firmware and connect to Pybytes.

<p><img src ="../../../img/pybytes/firmware_updater.gif" width="800"></p>
