---
title: "Pygate"
---

The Pygate is an 8-channel LoRaWAN gateway. This page will help you get started with it.

While the Pygate shield has the radio chips required to act as a LoRaWAN gateway, it will require a WiPy3, GPy or LoPy4 to run the LoRaWAN gateway software and provide connectivity to the LoRaWAN server (TTN / ChirpStack etc.) via WiFi, Ethernet (with the optional PyEthernet adapter) or LTE (a GPy with a mobile subscription is required for LTE connectivity).

A USB connection is recommended for the initial firmware update of the Pycom development module (WiPy 3, GPy, LoPy4) and to upload the configuration & start-up script. The module can be updated over the air via WiFi / LTE (depending on network capabilities) or via Ethernet connection which allows installation of the gateway in remote locations.

The Pygate board can have the PyEthernet adapter connected which allows an Ethernet connection. The PyEthernet also supports PoE. Please check the separate [page and warning for PoE-NI!](/tutorials/networkprotocols/poe/)

## Setup

To connect your Pygate to a LoRa server, please follow these steps:

1. Attach a WiPy 3, GPy or LoPy 4 to the Pygate. The RGB LED of the development board should be aligned with the USB port of the Pygate.
1. Attach the LoRa Antenna to the Pygate.
1. Flash the Pycom Device with with a firmware build where Pygate functionality is enabled. In the firmware update tool, please choose pygate as the firmware type.
1. Follow the steps to [register the gateway with TTN](/gettingstarted/registration/lora/ttn/#register-a-gateway) in our getting started guide and download the `global_config.json`.
1. Create a `main.py` that creates an uplink (wifi, ethernet or LTE) and runs the LoRa packet forwarder (see example below).
1. Upload `global_config.json` and `main.py` and reset the board. This file is automatically executed every time the module resets.
1. You will see how it creates the uplink connection and then start the LoRa GW. It will print out some debug information while it is running. After some initialization it will print "LoRa GW started" and the LED will turn green.
1. Now it is operational. The communication from other LoRa nodes such as a LoPy4 will now reach the gateway and will receive up and downlink messages via the PyGate.
1. To stop the Pygate at any time press Ctrl-C on the REPL and run `machine.pygate_deinit()`. It will take a few seconds to stop the gateway tasks and safely power-off the concentrator.

> Do not attach the antenna to the Lopy4 module. Also, make sure you disabled the Pybytes LoRa connection.

> Running the LoRa gateway on a GPy can get you close to the memory limit of the device. To avoid running out of memory one should not *run* the WiFi task and the LTE task at the same time. This shouldn't really restrict your use of the Pygate, since you wouldn't be *using* WiFi and LTE at the same time. The tasks *run* when you explicitly initialize them with ``wlan = WLAN()`` or ``lte = LTE()``, or when they get automatically started upon boot based on the settings ``pycom.wifi_on_boot(True)`` or ``pycom.lte_modem_en_on_boot(True)``. Bottom line, if you have trouble starting the LoRa packet forwarder, please double check these settings and make sure at least the network that you don't use is not automatically started.

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
with open('/flash/global_config.json','r') as fp:
    buf = fp.read()

# Start the Pygate
machine.pygate_init(buf)
# disable degub messages
# machine.pygate_debug_level(1)
```

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
