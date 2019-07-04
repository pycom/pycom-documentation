---
title: "Telnet REPL"
aliases:
    - gettingstarted/programming/repl/telnet.html
    - gettingstarted/programming/repl/telnet.md
    - chapter/gettingstarted/programming/repl/telnet
---

Pycom devices also support a connection via `telnet`, using the device's on board WiFi/WLAN. Connect to the device's WiFi Access Point (AP) and using the following credentials to connect to the AP. The WiFi `SSID` will appear upon powering on a Pycom Device for the first time (e.g. `lopy-`). To re-enable this feature at a later date, please see [network.WLAN](/firmwareapi/pycom/network/wlan).

* password: `www.pycom.io`

## Telnet Server

Additionally, to use the MircoPython REPL over telnet, further authentication is required. The default credentials for the telnet server are:

* username: `micro`
* password: `python`

See [network.server](/firmwareapi/pycom/network/server) for info on how to change the default authentication.

## All platforms

By far the easiest way to access the Telnet REPL is via the our [Pymakr plug-in](/pymakr/installation/) for Atom and Visual Studio Code. This adds a pane to the bottom of the editors that allows you to directly access the REPL and any output from the device. Detailed instructions on how to setup Pymakr can be found [here](/pymakr/installation/).

## macOS and Linux

Once the host machine is connected to the Pycom device's Access Point, a telnet connection may be opened from a terminal instance.

```bash
$ telnet 192.168.4.1
```

Upon connection, the telnet program will prompt for the `username` and `password` in the section above.

## Windows

A terminal emulator is needed to open a telnet connection from Windows; the easiest option is to download the free program, [PuTTY](http://www.putty.org/).

1. With PuTTY open, select telnet as connection type and leave the default port (`23`)
2. Next enter the IP address of the Pycom device (e.g. `192.168.4.1`)
3. Finally click `Open`

{{% hint style="info" %}}
When using a Pycom device with a personal, home or office WiFi access point, the telnet connection may still be used. In this instance, the user will need to determine the Pycom device's local IP address and substitute this for `192.168.4.1`, referred to in the earlier sections.
{{< /hint >}}
