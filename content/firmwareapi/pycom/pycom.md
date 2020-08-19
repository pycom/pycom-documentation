---
title: "pycom"
aliases:
    - firmwareapi/pycom/pycom.html
    - firmwareapi/pycom/pycom.md
    - chapter/firmwareapi/pycom/pycom
---

The `pycom` module contains functions to control specific features of the Pycom devices, such as the heartbeat RGB LED.

## Quick Usage Example

```python
import pycom

pycom.heartbeat(False)  # disable the heartbeat LED
pycom.heartbeat(True)   # enable the heartbeat LED
pycom.heartbeat()       # get the heartbeat state
pycom.rgbled(0xff00)    # make the LED light up in green color
```

## Miscelaneous Methods

### pycom.heartbeat([boolean])

Get or set the state (enabled or disabled) of the heartbeat LED. Accepts and returns boolean values.

### pycom.heartbeat_on_boot([boolean])

Allows you permanently disable or enable the heartbeat LED. Once this setting is set, it will persist between reboots. Note, this only comes into effect on the next boot, it does not stop the already running heartbeat.

### pycom.rgbled(color)

Set the colour of the RGB LED. The colour is specified as 24 bit value representing red, green and blue, in the following order `0xRRGGBB`. For instance, passing the value `0x00FF00` will light up the LED in a very bright green.

### pycom.nvs_set(key, value)

Set the value of the specified key in the NVRAM memory area of the external flash. Data stored here is preserved across resets and power cycles. Value can only take 32-bit integers at the moment. Example:

### pycom.nvs_get(key)

Get the value the specified key from the NVRAM memory area of the external flash. Example:

If a non-existing key is given the returned value will be `None`.

### pycom.nvs_erase(key)

Erase the given key from the NVRAM memory area.

### pycom.nvs_erase_all()

Erase the entire NVRAM memory area.

### pycom.pulses_get(pin, timeout)

Return a list of pulses at `pin`. The methods scans for transitions at `pin` and returns a list of tuples, each telling the pin value and the duration in microseconds of that value. `pin` is a pin object, which must have set to `INP` or `OPEN_DRAIN` mode. The scan stops if not transitions occurs within `timeout` milliseconds.

Example:

```python
# get the raw data from a DHT11/DHT22/AM2302 sensor
from machine import Pin
from pycom import pulses_get
from time import sleep_ms

pin = Pin("G7", mode=Pin.OPEN_DRAIN)
pin(0)
sleep_ms(20)
pin(1)
data = pulses_get(pin, 100)
```

## Boot methods

### pycom.wifi_on_boot([boolean])

Get or set the WiFi on boot flag. When this flag is set to `True`, The WiFi will be enabled according to the other WiFi settings. when `False` the WiFi module will be disabled untill enabled directly via WLAN class.

This setting is stored in non-volatile memory which preserves it across resets and power cycles. Example:

### pycom.wifi_ssid_sta([ssid])

Get or set the ssid of the Access point the device should connect to on startup.
This setting is stored in non-volatile memory which preserves it across resets and power cycles

### pycom.wifi_ssid_ap([ssid])

Get or set the ssid of the Access point that should be started by the device at startup, if not set and startup Wifi mode is AP the default AP name (`Board_Name>-wlan-<last_4_digits_mac`) will be used.This setting is stored in non-volatile memory which preserves it across resets and power cycles

### pycom.wifi_pwd_sta([key])

Get or set the Password of the Access point the device should connect to on startup, leave the password unset if the AP is open.This setting is stored in non-volatile memory which preserves it across resets and power cycles

### pycom.wifi_pwd_ap([key])

Get or set the Password of the Access point that should be started by the device at startup, leave unset if the AP should be open.This setting is stored in non-volatile memory which preserves it across resets and power cycles

### pycom.smart_config_on_boot([boolean])

Read or (Enable/Disable) SmartConfig functionality on startup, this flag will be reset after successful completion of the smartConfig process after startup.This setting is stored in non-volatile memory which preserves it across resets and power cycles

### pycom.smart_config_on_boot([boolean])

Read or (Enable/Disable) SmartConfig functionality on startup, this flag will be reset after successful completion of the smartConfig process after startup.This setting is stored in non-volatile memory which preserves it across resets and power cycles

### pycom.wifi_mode_on_boot([boolean])

Set or get the Wifi Mode at startup , `WLAN.STA`, `WLAN.AP` or `WLAN.APSTA`.This setting is stored in non-volatile memory which preserves it across resets and power cycles

### pycom.wdt_on_boot_timeout([timeout])

Sets or gets the WDT on boot timeout in milliseconds. The minimum value is 5000 ms.

### pycom.wdt_on_boot([enable])

Enables the WDT at boot time with the timeout in ms set by the function `wdt_on_boot_timeout`. If this flag is set, the application needs to reconfigure the WDT with a new timeout and feed it regularly to avoid a reset

### pycom.bootmgr(boot_partition=pycom.FACTORY, fs_type=FAT, safeboot=False, reset=False)

* `boot_partition` This is to set the partition to boot from , this could be set to either `pycom.FACTORY` or `pycom.OTA_0`
* `fs_type` This is to set the filesystem to use for the flash memory (`/flash`). This could be set to `pycom.FAT` for FAT16 or `pycom.LittleFS` for LittleFS filesystem.

  _Note: When the firmware is built with option_ `FS_USE_LITTLEFS` _the file system for_ `/flash` _is forced to be LittleFS._

* `safeboot` Enable or Disable safemoot mode.
* `reset` Set `True` to reset target after updating the `bootmgr` options, `False` for not resetting.

## OTA Methods

### pycom.ota_start()

### pycom.ota_write(buffer)

### pycom.ota_finish()

Perform a firmware update. These methods are internally used by a firmware update through FTP. The update starts with a call to `ota_start()`, followed by a series of calls to `ota_write(buffer)`, and is terminated with `ota_finish()`. After reset, the new image gets active. `buffer` shall hold the image data to be written, in arbitrary sizes. A block size of 4096 is recommended.

Example:

```python
# Firmware update by reading the image from the SD card
#
from pycom import ota_start, ota_write, ota_finish
from os import mount
from machine import SD

BLOCKSIZE = const(4096)
APPIMG = "/sd/appimg.bin"

sd = SD()
mount(sd, '/sd')

with open(APPIMG, "rb") as f:
    buffer = bytearray(BLOCKSIZE)
    mv = memoryview(buffer)
    size=0
    ota_start()
    while True:
        chunk = f.readinto(buffer)
        if chunk > 0:
            ota_write(mv[:chunk])
            size += chunk
            print("\r%7d " % size, end="")
        else:
            break
    ota_finish()
```

Instead of reading the data to be written from a file, it can obviously also be received from a server using any suitable protocol, without the need to store it in the devices file system.

### pycom.diff_update_enabled()

Provides the status of the differential update feature. Returns `True` if differential update is enabled and `False` otherwise. `DIFF_UPDATE_ENABLED` build flag can be used to enable the differential update feature.

> Note: This function is only available in the firmware versions which support differential update feature. If you get an exception while calling this function, your firmware version does not support this feature.

