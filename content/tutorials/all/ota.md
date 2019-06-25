---
title: "OTA update"
aliases:
    - tutorials/all/ota.html
    - tutorials/all/ota.md
    - chapter/tutorials/all/ota
---

## Overview

Pycom modules come with the ability to update the devices firmware, while it is still running, we call this an "over the air" (OTA) update. The [`pycom`](/firmwareapi/pycom/pycom) library provides several functions to achieve this. This example will demonstrate how you could potentially use this functionality to update deployed devices. The full source code of this example can be found [here](https://github.com/pycom/pycom-libraries/tree/master/examples/OTA).

## Method

Here we will describe one possible update methodology you could use that is implemented by this example.

Imagine you a smart metering company and you wish to roll out an update for your Pycom based smart meter. These meters usually send data back via LoRa. Unfortunately LoRa downlink messages have a very limited size and several hundred if not thousand would be required to upload a complete firmware image. To get around this you can have your devices sending their regular data via LoRa and when they receive a special command via a downlink message, the devices will connect to a WiFi network. It is unfeasible to ask customers to allow your device to connect to their home network so instead this network could be provided by a vehicle. This vehicle will travel around a certain geographic area in which the devices have been sent the special downlink message to initiate the update. The devices will look for the WiFi network being broadcast by the vehicle and connect. The devices will then connect to a server running on this WiFi network. This server (also shown in this example) will generate manifest files that instruct the device on what it should update, and where to get the update data from.

## Server

Code available [here](https://github.com/pycom/pycom-libraries/blob/master/examples/OTA/OTA_server.py).

This script runs a HTTP server on port `8000` that provisions over the air (OTA) update manifests in JSON format as well as serving the update content. This script should be run in a directory that contains every version of the end devices code, in the following structure:

```text
  - server directory
    |- this_script.py
    |- 1.0.0
    |  |- flash
    |  |   |- lib
    |  |   |  |- lib_a.py
    |  |   |- main.py
    |  |   |- boot.py
    |  |- sd
    |     |- some_asset.txt
    |     |- asset_that_will_be_removed.wav
    |- 1.0.1
    |  |- flash
    |  |   |- lib
    |  |   |  |- lib_a.py
    |  |   |  |- new_lib.py
    |  |   |- main.py
    |  |   |- boot.py
    |  |- sd
    |     |- some_asset.txt
    |- firmware_1.0.0.bin
    |- firmware_1.0.1.bin
```

The top level directory that contains this script can contain one of two things:

* Update directory: These should be named with a version number compatible

  with the python LooseVersion versioning scheme

  ([http://epydoc.sourceforge.net/stdlib/distutils.version.LooseVersion-class.html](http://epydoc.sourceforge.net/stdlib/distutils.version.LooseVersion-class.html)).

  They should contain the entire file system of the end device for the

  corresponding version number.

* Firmware: These files should be named in the format `firmare_VERSION.bin`, where VERSION is a a version number compatible with the python LooseVersion versioning scheme ([http://epydoc.sourceforge.net/stdlib/distutils.version.LooseVersion-class.html](http://epydoc.sourceforge.net/stdlib/distutils.version.LooseVersion-class.html)).

  This file should be in the format of the `appimg.bin` created by the Pycom

  firmware build scripts.

### How to use

Once the directory has been setup as described above you simply need to start this script using python3. Once started this script will run a HTTP server on port `8000` (this can be changed by changing the PORT variable). This server will serve all the files in directory as expected along with one additional special file, `manifest.json`. This file does not exist on the file system but is instead generated when requested and contains the required changes to bring the end device from its current version to the latest available version. You can see an example of this by pointing your web browser at:

`http://127.0.0.1:8000/manifest.json?current_ver=1.0.0`

The `current_ver` field at the end of the URL should be set to the current firmware version of the end device. The generated manifest will contain lists of which files are new, have changed or need to be deleted along with SHA1 hashes of the files. Below is an example of what such a manifest might look like:

```text
{
   "delete": [
      "flash/old_file.py",
      "flash/other_old_file.py"
   ],
   "firmware": {
       "URL": "http://192.168.1.144:8000/firmware_1.0.1b.bin",
       "hash": "ccc6914a457eb4af8855ec02f6909316526bdd08"
   },
   "new": [
       {
           "URL": "http://192.168.1.144:8000/1.0.1b/flash/lib/new_lib.py",
           "dst_path": "flash/lib/new_lib.py",
           "hash": "1095df8213aac2983efd68dba9420c8efc9c7c4a"
       }
   ],
   "update": [
       {
           "URL": "http://192.168.1.144:8000/1.0.1b/flash/changed_file.py",
           "dst_path": "flash/changed_file.py",
           "hash": "1095df8213aac2983efd68dba9420c8efc9c7c4a"
       }
   ],
   "version": "1.0.1b"
}
```

The manifest contains the following fields:

* `delete`: A list of paths to files which are no longer needed
* `firmware`: The URL and SHA1 hash of the firmware image
* `new`: the URL, path on end device and SHA1 hash of all new files
* `update`: the URL, path on end device and SHA1 hash of all files which

  existed before but have changed.

* `version`: The version number that this manifest will update the client to
* `previous_version`: The version the client is currently on before applying

  this update

_Note_: The version number of the files might not be the same as the firmware. The highest available version number, higher than the current client version is used for both firmware and files. This may differ between the two.

In order for the URL's to be properly formatted you are required to send a "host" header along with your HTTP get request e.g:

```text
GET /manifest.json?current_ver=1.0.0 HTTP/1.0\r\nHost: 192.168.1.144:8000\r\n\r\n
```

## Client Library

A MicroPyton library for interfacing with the server described above is available [here](https://github.com/pycom/pycom-libraries/blob/master/examples/OTA/1.0.0/flash/lib/OTA.py).

This library is split into two layers. The top level `OTA` class implements all the high level functionality such as parsing the JSON file, making back copies of files being updated incase the update fails, etc. The layer of the library is agnostic to your chosen transport method. Below this is the `WiFiOTA` class. This class implements the actual transport mechanism of how the device fetches the files and update manifest (via WiFi as the class name suggests). The reason for this split is so that the high level functionality can be reused regardless of what transport mechanism you end up using. This could be implemented on top of Bluetooth for example, or the sever changed from HTTP to FTP.

{{% hint style="danger" %}}
Although the above code is functional, it is provided only as an example of how an end user might implement a OTA update mechanism. It is not 100% feature complete e.g. even though it does backup previous versions of files, the roll back procedure is not implemented. This is left of the end user to do.
{{< /hint >}}

## Example

Below is am example implementing the methodology previously explained in this tutorial to initiate an OTA update.

{{% hint style="info" %}}
The example below will only work on a Pycom device with LoRa capabilities. If want to test it out on a device without LoRa functionality then simply comment out any code relating to LoRa. Leaving just the `WiFiOTA` initialisation and they `ota.connect()` and `ota.update()`
{{< /hint >}}

```python

from network import LoRa, WLAN
import socket
import time
from OTA import WiFiOTA
from time import sleep
import pycom
import ubinascii

from config import WIFI_SSID, WIFI_PW, SERVER_IP

# Turn on GREEN LED
pycom.heartbeat(False)
pycom.rgbled(0xff00)

# Setup OTA
ota = WiFiOTA(WIFI_SSID,
              WIFI_PW,
              SERVER_IP,  # Update server address
              8000)  # Update server port

# Turn off WiFi to save power
w = WLAN()
w.deinit()

# Initialise LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

app_eui = ubinascii.unhexlify('70B3D57ED0008CD6')
app_key = ubinascii.unhexlify('B57F36D88691CEC5EE8659320169A61C')

# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

while True:
    # send some data
    s.send(bytes([0x04, 0x05, 0x06]))

    # make the socket non-blocking
    # (because if there's no data received it will block forever...)
    s.setblocking(False)

    # get any data received (if any...)
    data = s.recv(64)

    # Some sort of OTA trigger
    if data == bytes([0x01, 0x02, 0x03]):
        print("Performing OTA")
        # Perform OTA
        ota.connect()
        ota.update()

    sleep(5)
```

