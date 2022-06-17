---
title: "Firmware Update"
aliases:
    - pylife/fwupdate.html
    - pylife/fwupdate.md
    - chapter/pylife/fwupdate
---

After installing the app, please do a firmware update immediately by following the instructions below.


## Firmware update
In PyLife, go to the devices tab and select your PyGo:

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
If the firmware update fails, you can reconnect to the PyGo and try again. It will prompt you to resume the update, and should subsequently update successfully.
A video demonstrating this is available

We have discovered a bug in the firmware the PyGo's are shipped with where in unusual circumstances involving the GPS the PyGo can enter a locked state where it does not respond to external input.
The immediate firmware update resolves this issue, but if you do encounter it leave the PyGo off the charger until the battery is discharged and when you restart do a firmware update.
