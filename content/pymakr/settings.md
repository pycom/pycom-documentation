---
title: "Settings"
aliases:
    - pymakr/settings.html
    - pymakr/settings.md
    - chapter/pymakr/settings
---

Below you will find a description of the various settings available for Pymakr.

## address

This is the address of the Pycom module you want Pymakr can connect to. This can be either a serial port (e.g `COM1` on windows or `/dev/cu.usbserial-DQ0054ES` on Linux/macOS) or an IP address (Telnet) (e.g. `192.168.4.1` if connected to the AP created by the Pycom module).

## username

If a IP address was provided for the `address` therefore Pymakr is connecting via Telnet, you will also need to provide a username, the default is `micro`.

## password

If an IP address was provided for the address, Pymakr is connecting via Telnet. You will also need to provide a password, the default is `python`.

## sync\_folder

If left blank, all directories inside the project will be synced to the device when the user clicks `upload`. If directories are specified, only these directories will be synced, all others will be ignored

## open\_on\_start

If set to `true`, the Pymakr console will open and try to connect when the editor is started, or a project is opened.

## safe\_boot\_on\_upload

If set to `true`, Pymakr will reboot the connected device into safe-mode before uploading. This is useful if your code uses a lot of RAM causing issues with the upload procedure.

This feature is only available on modules running firmware version `1.17.0.b1` or higher.

## sync\_file\_types

Only files ending with the extensions listed in this setting will be synced to the device when performing an upload. All other files are ignored. By default this is set to include: `py, txt, log, json, xml`

## ctrl\_c\_on\_connect

If set to `true`, Pymakr will sent the `ctrl-c` signal to the connected module before uploading. This should stop the script currently running on the device and improve the reliability of the upload process.

