## Pygate

The Pygate is an 8-channel LoRaWAN gateway. You connect a WiPy or Gpy board into the Pygate and flash a firmware build where the Pygate functionality is enabled. See the [Pygate tutorial](/tutorials/all/pygate) to get started.

__To connect your Pygate to a LoRa server, follow these steps:__  

1. Attach a Wipy, or GPy to the Pygate. The RGB LED of the development board should be aligned with the USB port of the Pygate.

1. Attach the LoRa Antenna to the Pygate.

1. Flash the Pycom Device with latest Pygate Firmware.

1. Create a `config.json` for your Pygate and upload it.

1. Create a `main.py` that creates an uplink and runs the Pygate packet fowarder.

__The following example shows the simple script and json file to run the Pygate over Wifi connecting to [The Things Network](https://www.thethingsnetwork.org/)__

If you are in EU region, it should be sufficent to update:
 * `config.json` Enter your unique GW ID, the LoRa server address and port number
 * `main.py` Enter your wifi SSID and password.

In generaly, you should supply a config matching your region (EU868/US915). The format of the file is the same a TODO:Insert link

TODO: minimal TTN getting started


```python
from network import WLAN
import time
import machine
from machine import RTC
import pycom

# Disable Hearbeat
pycom.heartbeat(False)

# Define callback function for Pygate events
def machine_cb (arg):
    evt = machine.events()
    if (evt & machine.PYGATE_START_EVT):
        # Green
        pycom.rgbled(0x103300)
    elif (evt & machine.PYGATE_ERROR_EVT):
        # Red
        pycom.rgbled(0x331000)
    elif (evt & machine.PYGATE_STOP_EVT):
        # RGB off
        pycom.rgbled(0x000000)

# register callback function
machine.callback(trigger = (machine.PYGATE_START_EVT | machine.PYGATE_STOP_EVT | machine.PYGATE_ERROR_EVT), handler=machine_cb)

# Connect to a Wifi Network
wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid='<SSID>', auth=(WLAN.WPA2, "<PASSWORD>"))

while not wlan.isconnected():
    time.sleep(1)

print("Wifi Connection established")

# Sync time via NTP server for GW timestamps on Events
rtc = RTC()
rtc.ntp_sync(server="0.nl.pool.ntp.org")

# Read the GW config file from Filesystem
fp = open('/flash/config.json','r')
buf = fp.read()

# Start the Pygate
machine.pygate_init(buf)

```

A sample `config.json` file for gateway configuration in EU868 region:

```json
{
	"SX1301_conf": {
		"lorawan_public": true,
		"clksrc": 1,
		"antenna_gain": 0,
		"radio_0": {
			"enable": true,
			"type": "SX1257",
			"freq": 867500000,
			"rssi_offset": -164.0,
			"tx_enable": true,
			"tx_freq_min": 863000000,
			"tx_freq_max": 870000000
		},
		"radio_1": {
			"enable": true,
			"type": "SX1257",
			"freq": 868500000,
			"rssi_offset": -164.0,
			"tx_enable": false
		},
		"chan_multiSF_0": {
			"enable": true,
			"radio": 1,
			"if": -400000
		},
		"chan_multiSF_1": {
			"enable": true,
			"radio": 1,
			"if": -200000
		},
		"chan_multiSF_2": {
			"enable": true,
			"radio": 1,
			"if": 0
		},
		"chan_multiSF_3": {
			"enable": true,
			"radio": 0,
			"if": -400000
		},
		"chan_multiSF_4": {
			"enable": true,
			"radio": 0,
			"if": -200000
		},
		"chan_multiSF_5": {
			"enable": true,
			"radio": 0,
			"if": 0
		},
		"chan_multiSF_6": {
			"enable": true,
			"radio": 0,
			"if": 200000
		},
		"chan_multiSF_7": {
			"enable": true,
			"radio": 0,
			"if": 400000
		},
		"chan_Lora_std": {
			"enable": true,
			"radio": 1,
			"if": -200000,
			"bandwidth": 250000,
			"spread_factor": 7
		},
		"chan_FSK": {
			"enable": true,
			"radio": 1,
			"if": 300000,
			"bandwidth": 125000,
			"datarate": 50000
		},
		"tx_lut_0": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 9,
			"dig_gain": 3
		},
		"tx_lut_1": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 9,
			"dig_gain": 3
		},
		"tx_lut_2": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 9,
			"dig_gain": 3
		},
		"tx_lut_3": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 9,
			"dig_gain": 3
		},
		"tx_lut_4": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 9,
			"dig_gain": 3
		},
		"tx_lut_5": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 9,
			"dig_gain": 3
		},
		"tx_lut_6": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 9,
			"dig_gain": 3
		},
		"tx_lut_7": {
			"pa_gain": 0,
			"mix_gain": 6,
			"rf_power": 11,
			"dig_gain": 3
		},
		"tx_lut_8": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 13,
			"dig_gain": 2
		},
		"tx_lut_9": {
			"pa_gain": 0,
			"mix_gain": 8,
			"rf_power": 14,
			"dig_gain": 3
		},
		"tx_lut_10": {
			"pa_gain": 0,
			"mix_gain": 6,
			"rf_power": 15,
			"dig_gain": 2
		},
		"tx_lut_11": {
			"pa_gain": 0,
			"mix_gain": 6,
			"rf_power": 16,
			"dig_gain": 1
		},
		"tx_lut_12": {
			"pa_gain": 0,
			"mix_gain": 9,
			"rf_power": 17,
			"dig_gain": 3
		},
		"tx_lut_13": {
			"pa_gain": 0,
			"mix_gain": 10,
			"rf_power": 18,
			"dig_gain": 3
		},
		"tx_lut_14": {
			"pa_gain": 0,
			"mix_gain": 11,
			"rf_power": 19,
			"dig_gain": 3
		},
		"tx_lut_15": {
			"pa_gain": 0,
			"mix_gain": 12,
			"rf_power": 20,
			"dig_gain": 3
		}
	},

	"gateway_conf": {
		"gateway_ID": "XXXXXXXXXXXXXXXX",
		"server_address": "router.eu.thethings.network",
		"serv_port_up": 1700,
		"serv_port_down": 1700,
		"keepalive_interval": 10,
		"stat_interval": 30,
		"push_timeout_ms": 100,
		"forward_crc_valid": true,
		"forward_crc_error": false,
		"forward_crc_disabled": false
	}
}
```


To stop the Pygate at any time press Ctrl-C on the REPL and run `machine.pygate_deinit()`.

This will stop the gateway tasks and safely power-off the concentrator.


__Note__: The Pygate packet forwarder is a legacy packet forwarder, so you must make sure you use select the legacy packet forwarder option in TTN as shown below.

![alt_text](https://wiki.dragino.com/images/c/c6/TTN_Create_Gateway_0.png)


__The following example demonstrates running only the concentrator on the Pygate and running the packet forwarder software on a different device, controlling the Pygate via UART:__

```python
from machine import UART
import machine
import time
import os
import gc

machine.pygate_init(None)
time.sleep(3)

uart = UART(1, 115200, timeout_chars=40, pins=('P23', 'P22'))

while True:
    if uart.any():
        rx_data = uart.read()
        machine.pygate_cmd_decode(rx_data)
        tx_data =  machine.pygate_cmd_get()
        l = uart.write(tx_data)
    else:
        time.sleep_us(10)
```
