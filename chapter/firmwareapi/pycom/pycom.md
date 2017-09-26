# module pycom – Pycom Device Features
The pycom module contains functions to control specific features of the pycom devices, such as the heartbeat RGB LED.

### Quick Usage Example

```python
import pycom

pycom.heartbeat(False)  # disable the heartbeat LED
pycom.heartbeat(True)   # enable the heartbeat LED
pycom.heartbeat()       # get the heartbeat state
pycom.rgbled(0xff00)    # make the LED light up in green color
```

### Functions

<function>pycom.heartbeat([enable])</function>

Get or set the state (enabled or disabled) of the heartbeat LED. Accepts and returns boolean values (True or False).

<function>pycom.rgbled(color)</function>

Set the colour of the RGB LED. The color is specified as 24 bit value representing red, green and blue, where the red colour is represented by the 8 most significant bits. For instance, passing the value ``0x00FF00`` will light up the LED in a very bright green.

<function>pycom.nvs_set(key, value)</function>

Set the value of the specified key in the NVRAM memory area of the external flash. Data sored here is preserved across resets and power cycles. Value can only take 32-bit integers at the moment. Example:

```python
import pycom

pycom.nvs_set('temp', 25)
pycom.nvs_set('count', 10)
```

<function>pycom.nvs_get(key)</function>

Get the value the specified key from the NVRAM memory area of the external flash. Example:

```python
import pycom

pulses = pycom.nvs_get('count')
```

<function>pycom.wifi_on_boot([enable])</function>

Get or set the WiFi on boot flag. When this flag is set to True, the AP with the default ssid ('lopy-wlan-xxx' for example) will be enabled as part of the boot process. If the flag is seto to False, the module will boot with WiFi disabled until it's enabled by the script via the ``WLAN`` class. This settin is stored in non-volatile memory which preserves it across resets and power cycles. Example:

```python
import pycom

pycom.wifi_on_boot(True)   # enable WiFi on boot

pycom.wifi_on_boot()       # get the wifi on boot flag

```
<function>pycom.pulses_get(pin, timeout)</function>  

Return a list of pulses at pin. The methods scans for transitions at pin and returns a list of tuples, each telling the pin value and the duration in microseconds of that value.  pin is a pin object, which must have set
to INP or OPEN_DRAIN mode. The scan stops if not transitions occurs whithin timeout microseconds.
Exmaple:
```
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

<function>pycom.ota_start()</function>  
<function>pycom.ota_write(buffer)</function>  
<function>pycom.ota_finish()</function>  
Perform a firmware update. These methods are internally used by a firmware updarte though ftp. The update starts with a call to ota_start(), followed by a series of
calls to ota_write(buffer), and is terminated with ota_finish().
After reset, the new image gets actice. buffer shall hold the image data to be written, in arbitrary sizes. A block size of 4096 is reccomended.

Example:
```
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
Instead of reading the data to be written from a file, it can obviuosly also be received from a server using any suitable protocol, without the need to store
it in the devices file system.
