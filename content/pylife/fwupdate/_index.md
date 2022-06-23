---
title: "Firmware Update"
aliases:
    - pylife/fwupdate.html
    - pylife/fwupdate.md
    - chapter/pylife/fwupdate
---

After installing the app, please do a firmware update immediately by following the instructions below.


## Firmware update
In PyLife, go to the 'Devices' tab and select your PyGo:

![Devices tab iOS](/gitbook/assets/pylife/fwupdate/devices_menu_iOS.png)

Scroll down to the bottom and select 'UPDATE FIRMWARE'

![Devices tab iOS](/gitbook/assets/pylife/fwupdate/device_details_iOS.png)

If an update is available, click install

![Devices tab iOS](/gitbook/assets/pylife/fwupdate/update_available_iOS.png)

You will be prompted to join a new WiFi access point. Please click join. You will temporarily be disconnected from the internet, so if you have any active connections they will be terminated.

![Devices tab iOS](/gitbook/assets/pylife/fwupdate/update_join_wifi_iOS.png)

After a few moments the firmware update should complete, and your PyGo will automatically reboot.
Once it has reconnected, you are ready to go.


## Troubleshooting
If the firmware update fails, you can reconnect to the PyGo and try again. It will prompt you to resume the update, and should subsequently update successfully. This should fix the majority of firmware update issues.
[A video demonstrating this is available here](/gitbook/assets/pylife/fwupdate/PyGoFirmwareUpdate.mp4)


### PyGo not responding
If your PyGo stops responding in PyLife, and doesn't display a charging symbol when placed on a suitable charger, it may have entered an error state. We have discovered a bug in the firmware the PyGos are shipped with where in unusual circumstances involving the GPS the PyGo can enter this state where it does not respond to external input.
The immediate firmware update resolves this issue, but if you do encounter please do the following:
  1) Leave the PyGo off the charger until the battery is discharged (this may take a day or so, but will be much quicker if the battery is not fully charged)
  2) Wake up the PyGo using a charger, either on a Qi compatible charger or by placing it in a charging cradle
  3) Restart the update process. PyLife should prompt you to resume the update, and fix the issue.


## Manual firmware update from computer
For most people, firmware update through the app is the best option. However it is possible to update through a computer if you have the USB cradle or can connect to the PyGo's serial port through a computer.
If you want to do this, do the following:
  1) Download the relevant firmware for your PyGo. Click on the relevant link below, and download the firmware in the URL field
      * [PyGo1 firmware](https://software.pycom.io/manifest.json?sysname=pygo1&fwtype=pylife&current_ver=1.20.4)
      * [PyGo2 firmware](https://software.pycom.io/manifest.json?sysname=pygo2&fwtype=pylife&current_ver=1.20.4)
  2) Connect to your PyGo's serial terminal, and run `update()`
  3) On your computer, connect to the PyGo's access point:
      * SSID: PyCom_AP_Firmware_Update
      * Password: pycom
  4) Open up a command prompt or terminal, navigate to the directory your downloaded firmware is in, and run the following, replacing YOUR_FIRMWARE_HERE with firmware you have downloaded:
  ```
  curl -v --request GET http://192.168.4.1/status -H "FW-Header-1: ota-init"
curl -v --request GET http://192.168.4.1/status -H "FW-Header-1: ota-update"
curl --request POST --data-binary @YOUR_FIRMWARE_HERE.bin http://192.168.4.1/update
curl -v --request GET http://192.168.4.1/status -H "FW-Header-1: ota-finish"
curl -v --request GET http://192.168.4.1/status -H "FW-Header-1: ota-verify"
curl -v --request GET http://192.168.4.1/status -H "FW-Header-1: ota-reboot"
```
  5) Check that all commands have run succesfully without error. Your PyGo is now upgraded.

