## Pygate

The Pygate is an 8-channel LoRaWAN gateway. This page will help you get started with it.

>While the Pygate shield has the radio chips required to act as a LoRaWAN gateway, it will require a WiPy3, GPy or LoPy4 to run the LoRaWAN gateway software and provide connectivity to the LoRaWAN server (TTN / ChirpStack etc.) via WiFi, Ethernet (with the optional PyEthernet adapter) or LTE-M (a GPy with a mobile subscription is required for LTE-M connectivity).


A USB connection is recommended for the initial firmware update of the Pycom development module (WiPy 3, GPy, LoPy4) and to upload the configuration & start-up script. The module can be updated over the air via WiFi / LTE-M (depending on network capabilities) or via Ethernet connection which allows installation of the gateway in remote locations.

The Pygate board can have the PyEthernet adapter connected which allows an Ethernet connection. The PyEthernet also supports PoE. Please check the separate [page and warning for PoE-NI!](/tutorials/all/poe)

### Quickstart

To connect your Pygate to a LoRa server, please follow these steps:

1. Attach a WiPy 3, GPy or LoPy 4 to the Pygate. The RGB LED of the development board should be aligned with the USB port of the Pygate.
1. Attach the LoRa Antenna to the Pygate.
>Note: Do not attach the antenna to the Lopy4 module. Also, make sure you disabled the Pybytes LoRa connection.
1. Flash the Pycom Device with with a firmware build where Pygate functionality is enabled. In the firmware update tool, please choose pygate as the firmware type.
1. Create a `config.json` for your Pygate and upload it (please check the template further below).
1. Create a `main.py` that creates an uplink (wifi, ethernet or lte) and runs the LoRa packet forwarder (see example below).
1. Run the `main.py`. This file is automatically executed every time the module resets.
1. Now it is operational. The communication from other LoRa nodes such as a LoPy4 will now reach the gateway and will receive up and downlink messages via the PyGate.
1. To stop the Pygate at any time press Ctrl-C on the REPL and run `machine.pygate_deinit()`. It will take a few seconds to stop the gateway tasks and safely power-off the concentrator.


Make sure you supply a config matching your region (EU868, US915, etc), e.g. https://github.com/Lora-net/packet_forwarder/tree/master/lora_pkt_fwd/cfg. If you are in EU region, it should be sufficient to update the example below with your GW ID, the LoRa server address and port number.

{{% hint style="info" %}}
**Note** Running the LoRa gateway on a GPy can get you close to the memory limit of the device. To avoid running out of memory one should not *run* the WiFi task and the LTE task at the same time. This shouldn't really restrict your use of the Pygate, since you wouldn't be *using* WiFi and LTE at the same time. The tasks *run* when you explicitly initialize them with ``wlan = WLAN()`` or ``lte = LTE()``, or when they get automatically started upon boot based on the settings ``pycom.wifi_on_boot(True)`` or ``pycom.lte_modem_en_on_boot(True)``. Bottom line, if you have trouble starting the LoRa packet forwarder, please double check these settings and make sure at least the network that you don't use is not automatically started.{{% /hint %}}



### Example TTN Wifi

The following example shows the script and json file to run the Pygate over Wifi connecting to [The Things Network](https://www.thethingsnetwork.org/).

1. log in to https://console.thethingsnetwork.org/
1. go to Gateways and register a new gateway
1. select "I'm using a legacy packet forwarder"
1. make up a EUI (8 byte hexadecimal value) and register it on the TTN website
1. enter the EUI in your `config.json` under `gateway_ID` (Just enter the hex digits without the "eui-" prefix and without spaces)
1. select your Frequency Plan
1. select a router - also enter the hostname in your `config.json` under `server_address`
1. enter your wifi SSID and password in `main.py`
1. upload `config.json` and `main.py` and reset the board
1. you will see how it creates the uplink connection and then start the LoRa GW. It will print out some debug information while it is running. After some initialization it will print "LoRa GW started" and the LED will turn green.



```python
from network import WLAN
import time
import machine
from machine import RTC
import pycom

print('\nStarting LoRaWAN concentrator')
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

print('Connecting to WiFi...',  end='')
# Connect to a Wifi Network
wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid='<SSID>', auth=(WLAN.WPA2, "<PASSWORD>"))

while not wlan.isconnected():
    print('.', end='')
    time.sleep(1)
print(" OK")

# Sync time via NTP server for GW timestamps on Events
print('Syncing RTC via ntp...', end='')
rtc = RTC()
rtc.ntp_sync(server="pool.ntp.org")

while not rtc.synced():
    print('.', end='')
    time.sleep(.5)
print(" OK\n")

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
