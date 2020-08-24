---
title: "Pygate"
---

The Pygate is an 8-channel LoRaWAN gateway. This page will help you get started with it.

While the Pygate shield has the radio chips required to act as a LoRaWAN gateway, it will require a WiPy3, GPy or LoPy4 to run the LoRaWAN gateway software and provide connectivity to the LoRaWAN server (TTN / ChirpStack etc.) via WiFi, Ethernet (with the optional PyEthernet adapter) or LTE-M (a GPy with a mobile subscription is required for LTE-M connectivity).

A USB connection is recommended for the initial firmware update of the Pycom development module (WiPy 3, GPy, LoPy4) and to upload the configuration & start-up script. The module can be updated over the air via WiFi / LTE-M (depending on network capabilities) or via Ethernet connection which allows installation of the gateway in remote locations. 

The Pygate board can have the PyEthernet adapter connected which allows an Ethernet connection. The PyEthernet also supports PoE. Please check the separate [page and warning for PoE-NI!](/tutorials/all/poe)

What is discussed in this example:
1. [Setup](#setup)
2. [TTN](#example-ttn-wifi)
3. [Config file](#config-file)
4. [Logs expalantion](#pygate-logs)

## Setup

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

Running the LoRa gateway on a GPy can get you close to the memory limit of the device. To avoid running out of memory one should not *run* the WiFi task and the LTE task at the same time. This shouldn't really restrict your use of the Pygate, since you wouldn't be *using* WiFi and LTE at the same time. The tasks *run* when you explicitly initialize them with ``wlan = WLAN()`` or ``lte = LTE()``, or when they get automatically started upon boot based on the settings ``pycom.wifi_on_boot(True)`` or ``pycom.lte_modem_en_on_boot(True)``. Bottom line, if you have trouble starting the LoRa packet forwarder, please double check these settings and make sure at least the network that you don't use is not automatically started.

## Example TTN WiFi

The following example shows the script and json file to run the Pygate over Wifi connecting to [The Things Network](https://www.thethingsnetwork.org/).

1. log in to https://console.thethingsnetwork.org/
1. go to Gateways and register a new gateway
1. select "I'm using a legacy packet forwarder"
1. make up a EUI (8 byte hexadecimal value) and register it on the TTN website
1. enter the EUI in your `config.json` under `gateway_ID` (Just enter the hex digits without the "eui-" prefix and without spaces)
1. select your Frequency Plan
1. select the router for your region.
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
# disable degub messages
# machine.pygate_debug_level(1)
```

## Config file
1. You can find the config file for your region [here](https://github.com/TheThingsNetwork/gateway-conf)
2. Make a file called `config.json` in your project and paste the appropriate region settings to that file
3. Add the following to the bottom of the `config.json` file:
	```json
	...
		} ],
		"gateway_ID": "XXXXXXXXXXXXXXXX",
		"keepalive_interval": 10,
		"stat_interval": 30,
		"push_timeout_ms": 100,
		"forward_crc_valid": true,
		"forward_crc_error": false,
		"forward_crc_disabled": false
		}
	}
4. Edit the `gateway_ID` to reflect yours.
5. An example for EU868 is shown here:

```json
{
	"SX1301_conf": {
		"lorawan_public": true,
		"clksrc": 1,
		"clksrc_desc": "radio_1 provides clock to concentrator for most devices except MultiTech. For MultiTech set to 0.",
		"antenna_gain": 0,
		"antenna_gain_desc": "antenna gain, in dBi",
		"radio_0": {
			"enable": true,
			"type": "SX1257",
			"freq": 867500000,
			"rssi_offset": -166.0,
			"tx_enable": true,
			"tx_freq_min": 863000000,
			"tx_freq_max": 870000000
		},
		"radio_1": {
			"enable": true,
			"type": "SX1257",
			"freq": 868500000,
			"rssi_offset": -166.0,
			"tx_enable": false
		},
		"chan_multiSF_0": {
			"desc": "Lora MAC, 125kHz, all SF, 868.1 MHz",
			"enable": true,
			"radio": 1,
			"if": -400000
		},
		"chan_multiSF_1": {
			"desc": "Lora MAC, 125kHz, all SF, 868.3 MHz",
			"enable": true,
			"radio": 1,
			"if": -200000
		},
		"chan_multiSF_2": {
			"desc": "Lora MAC, 125kHz, all SF, 868.5 MHz",
			"enable": true,
			"radio": 1,
			"if": 0
		},
		"chan_multiSF_3": {
			"desc": "Lora MAC, 125kHz, all SF, 867.1 MHz",
			"enable": true,
			"radio": 0,
			"if": -400000
		},
		"chan_multiSF_4": {
			"desc": "Lora MAC, 125kHz, all SF, 867.3 MHz",
			"enable": true,
			"radio": 0,
			"if": -200000
		},
		"chan_multiSF_5": {
			"desc": "Lora MAC, 125kHz, all SF, 867.5 MHz",
			"enable": true,
			"radio": 0,
			"if": 0
		},
		"chan_multiSF_6": {
			"desc": "Lora MAC, 125kHz, all SF, 867.7 MHz",
			"enable": true,
			"radio": 0,
			"if": 200000
		},
		"chan_multiSF_7": {
			"desc": "Lora MAC, 125kHz, all SF, 867.9 MHz",
			"enable": true,
			"radio": 0,
			"if": 400000
		},
		"chan_Lora_std": {
			"desc": "Lora MAC, 250kHz, SF7, 868.3 MHz",
			"enable": true,
			"radio": 1,
			"if": -200000,
			"bandwidth": 250000,
			"spread_factor": 7
		},
		"chan_FSK": {
			"desc": "FSK 50kbps, 868.8 MHz",
			"enable": true,
			"radio": 1,
			"if": 300000,
			"bandwidth": 125000,
			"datarate": 50000
		},
		"tx_lut_0": {
			"desc": "TX gain table, index 0",
			"pa_gain": 0,
			"mix_gain": 8,
			"rf_power": -6,
			"dig_gain": 0
		},
		"tx_lut_1": {
			"desc": "TX gain table, index 1",
			"pa_gain": 0,
			"mix_gain": 10,
			"rf_power": -3,
			"dig_gain": 0
		},
		"tx_lut_2": {
			"desc": "TX gain table, index 2",
			"pa_gain": 0,
			"mix_gain": 12,
			"rf_power": 0,
			"dig_gain": 0
		},
		"tx_lut_3": {
			"desc": "TX gain table, index 3",
			"pa_gain": 1,
			"mix_gain": 8,
			"rf_power": 3,
			"dig_gain": 0
		},
		"tx_lut_4": {
			"desc": "TX gain table, index 4",
			"pa_gain": 1,
			"mix_gain": 10,
			"rf_power": 6,
			"dig_gain": 0
		},
		"tx_lut_5": {
			"desc": "TX gain table, index 5",
			"pa_gain": 1,
			"mix_gain": 12,
			"rf_power": 10,
			"dig_gain": 0
		},
		"tx_lut_6": {
			"desc": "TX gain table, index 6",
			"pa_gain": 1,
			"mix_gain": 13,
			"rf_power": 11,
			"dig_gain": 0
		},
		"tx_lut_7": {
			"desc": "TX gain table, index 7",
			"pa_gain": 2,
			"mix_gain": 9,
			"rf_power": 12,
			"dig_gain": 0
		},
		"tx_lut_8": {
			"desc": "TX gain table, index 8",
			"pa_gain": 1,
			"mix_gain": 15,
			"rf_power": 13,
			"dig_gain": 0
		},
		"tx_lut_9": {
			"desc": "TX gain table, index 9",
			"pa_gain": 2,
			"mix_gain": 10,
			"rf_power": 14,
			"dig_gain": 0
		},
		"tx_lut_10": {
			"desc": "TX gain table, index 10",
			"pa_gain": 2,
			"mix_gain": 11,
			"rf_power": 16,
			"dig_gain": 0
		},
		"tx_lut_11": {
			"desc": "TX gain table, index 11",
			"pa_gain": 3,
			"mix_gain": 9,
			"rf_power": 20,
			"dig_gain": 0
		},
		"tx_lut_12": {
			"desc": "TX gain table, index 12",
			"pa_gain": 3,
			"mix_gain": 10,
			"rf_power": 23,
			"dig_gain": 0
		},
		"tx_lut_13": {
			"desc": "TX gain table, index 13",
			"pa_gain": 3,
			"mix_gain": 11,
			"rf_power": 25,
			"dig_gain": 0
		},
		"tx_lut_14": {
			"desc": "TX gain table, index 14",
			"pa_gain": 3,
			"mix_gain": 12,
			"rf_power": 26,
			"dig_gain": 0
		},
		"tx_lut_15": {
			"desc": "TX gain table, index 15",
			"pa_gain": 3,
			"mix_gain": 14,
			"rf_power": 27,
			"dig_gain": 0
		}
	},
	"gateway_conf": {
		"server_address": "router.eu.thethings.network",
		"serv_port_up": 1700,
		"serv_port_down": 1700,
		"servers": [ {
			"server_address": "router.eu.thethings.network",
			"serv_port_up": 1700,
			"serv_port_down": 1700,
			"serv_enabled": true
		} ],
	"gateway_ID": "XXXXXXXXXXXXXXXX",
	"keepalive_interval": 10,
	"stat_interval": 30,
	"push_timeout_ms": 100,
	"forward_crc_valid": true,
	"forward_crc_error": false,
	"forward_crc_disabled": false
	
	}

}
```
> Note: You can add the GPS coordinates to your Pygate by including the following lines in the `'gateway_conf'` object of the config file. 
>```
>"fake_gps": true,
>"ref_latitude": lat,
>"ref_longitude": lon,
>"ref_altitude": z
>```

## Pygate logs

Disambiguation of the Pygate logs:

1. By default the Pygate will print a status overview every 30 seconds (set by `stat_interval` in the config file). It will give an overview of what happened in the last 30 seconds. look sort of like this:

	```python
	[epoch time] lorapf: INFO_ [main] report
	##### [Date] [Time] GMT #####
	### [UPSTREAM] ###
	RF packets received by concentrator: 4                # <-- Amount of LoRa packets received from nodes
	CRC_OK: 75.00%, CRC_FAIL: 25.00%, NO_CRC: 0.00%       # <-- Redundancy check
	RF packets forwarded: 3 (69 bytes)                    # <-- Actual LoRa packets forwarded to TTN
	PUSH_DATA datagrams sent: 4 (728 bytes)               # <-- Packets forwarded to TTN (1 status update packet)
	PUSH_DATA acknowledged: 100.00%                       # <-- Acknowledgments received from TTN
	### [DOWNSTREAM] ###			
	PULL_DATA sent: 3 (100.00% acknowledged)              # <-- Checked TTN for Downlink packets this amount
	PULL_RESP(onse) datagrams received: 0 (0 bytes)       # <-- Actual downlink packets available from TTN
	RF packets sent to concentrator: 0 (0 bytes)          # <-- LoRa downlink packets actually sent out
	TX errors: 0                                          # <-- Amount of errors when sending LoRa packets to nodes, if there are any TX errors, they will be explained below
	### [JIT] ###                                         # <-- Just In Time TX scheduling
	[jit] queue is empty
	### [GPS] ###                                         # <-- GPS sync 
	GPS sync is disabled
	##### END #####
	```



2. Now for the actual logs in between there are a number of variants and are structured like the first line:
	```python
	[epoch time] lorapf: LEVEL_ [method] arguments
	[epoch time] lorapf: INFO_ [up  ] received pkt from mote: {redacted}, RSSI -51.0  # <-- Properly received packet from node

	[epoch time] lorapf: WARN_ [up  ] PUSH_ACK recieve timeout 0                      # <-- No acknowledgement received from TTN
	[epoch time] lorapf: WARN_ [up  ] PUSH_ACK recieve timeout 1                      # <-- No acknowledgement received from TTN, second try
	[epoch time] lorapf: WARN_ [up  ] ignored out-of sync PUSH_ACK packet {redacted}  # <-- out of sync acknowledgement from TTN
	[epoch time] lorapf: INFO_ jitqueue: Current concentrator {redacted}              # <-- sceduled a downlink packet
	[epoch time] lorapf: WARN_ jitqueue: IGNORED: not REJECTED, already too late to send it {redacted} # <-- downlink LoRa packet received too late, but sent anyways
	```
	
	Print level can be set custom using `machine.pygate_debug_level(level)` and are set as following:
	* `DEBUG`: 4
	* `INFO`: 3
	* `WARNING`: 2
	* `ERROR`: 1

