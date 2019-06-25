---
title: "Bluetooth"
aliases:
    - tutorials/all/ble.html
    - tutorials/all/ble.md
    - chapter/tutorials/all/ble
---

At present, basic BLE functionality is available. More features will be implemented in the near future, such as pairing. This page will be updated in line with these features.

Full info on `bluetooth` can be found within [Bluetooth page]() of the Firmware API Reference.

## Scan for BLE Devices

Scan for all of the advertising devices within range of the scanning device.

```python

bluetooth.start_scan(10)  # starts scanning and stop after 10 seconds
bluetooth.start_scan(-1)  # starts scanning indefinitely until bluetooth.stop_scan() is called
```

## Raw Data from a BLE Device

A quick usage example that scans and prints the raw data from advertisements.

```python

from network import Bluetooth

bluetooth = Bluetooth()
bluetooth.start_scan(-1)    # start scanning with no timeout

while True:
    print(bluetooth.get_adv())
```

## Connect to a BLE Device

Connecting to a device that is sending advertisements.

```python

from network import Bluetooth
import ubinascii
bluetooth = Bluetooth()

# scan until we can connect to any BLE device around
bluetooth.start_scan(-1)
adv = None
while True:
    adv = bluetooth.get_adv()
    if adv:
        try:
            bluetooth.connect(adv.mac)
        except:
            # start scanning again
            bluetooth.start_scan(-1)
            continue
        break
print("Connected to device with addr = {}".format(ubinascii.hexlify(adv.mac)))
```

## Connect to a BLE Device and Retrieve Data

Connecting to a device named 'Heart Rate' and receiving data from it's services.

```python

from network import Bluetooth
import time
bt = Bluetooth()
bt.start_scan(-1)

while True:
  adv = bt.get_adv()
  if adv and bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL) == 'Heart Rate':
      try:
          conn = bt.connect(adv.mac)
          services = conn.services()
          for service in services:
              time.sleep(0.050)
              if type(service.uuid()) == bytes:
                  print('Reading chars from service = {}'.format(service.uuid()))
              else:
                  print('Reading chars from service = %x' % service.uuid())
              chars = service.characteristics()
              for char in chars:
                  if (char.properties() & Bluetooth.PROP_READ):
                      print('char {} value = {}'.format(char.uuid(), char.read()))
          conn.disconnect()
          break
      except:
          pass
  else:
      time.sleep(0.050)
```

## Retrieve the Name & Manufacturer from a BLE Device

Using `resolve_adv_data()` to attempt to retrieve the name and manufacturer data from the advertiser.

```python

import ubinascii
from network import Bluetooth
bluetooth = Bluetooth()

bluetooth.start_scan(20)
while bluetooth.isscanning():
    adv = bluetooth.get_adv()
    if adv:
        # try to get the complete name
        print(bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL))

        mfg_data = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_MANUFACTURER_DATA)

        if mfg_data:
            # try to get the manufacturer data (Apple's iBeacon data is sent here)
            print(ubinascii.hexlify(mfg_data))
```

