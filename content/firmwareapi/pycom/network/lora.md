---
title: "LoRa"
aliases:
    - firmwareapi/pycom/network/lora.html
    - firmwareapi/pycom/network/lora.md
    - chapter/firmwareapi/pycom/network/lora
---

This class provides a LoRaWAN 1.0.2 compliant driver for the LoRa network processor in the LoPy and FiPy. Below is an example demonstrating LoRaWAN Activation by Personalisation usage:

```python

from network import LoRa
import socket
import ubinascii
import struct

# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# create an ABP authentication params
dev_addr = struct.unpack(">l", binascii.unhexlify('00000005'))[0]
nwk_swkey = ubinascii.unhexlify('2B7E151628AED2A6ABF7158809CF4F3C')
app_swkey = ubinascii.unhexlify('2B7E151628AED2A6ABF7158809CF4F3C')

# join a network using ABP (Activation By Personalisation)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket non-blocking
s.setblocking(False)

# send some data
s.send(bytes([0x01, 0x02, 0x03]))

# get any data received...
data = s.recv(64)
print(data)
```

{{% hint style="danger" %}}
Please ensure that there is an antenna connected to your device before sending/receiving LoRa messages as improper use (e.g. without an antenna), may damage the device.
{{< /hint >}}

## Additional Examples

For various other complete LoRa examples, check here for additional examples.

## Constructors

#### class network.LoRa(id=0, ...)

Create and configure a LoRa object. See init for params of configuration.

```python

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
```

## Methods

#### lora.init(mode, \* ,region=LoRa.EU868, frequency=868000000, tx\_power=14, bandwidth=LoRa.BW\_125KHZ, sf=7, preamble=8, coding\_rate=LoRa.CODING\_4\_5, power\_mode=LoRa.ALWAYS\_ON, tx\_iq=False, rx\_iq=False, adr=False, public=True, tx\_retries=1, device\_class=LoRa.CLASS\_A)

This method is used to set the LoRa subsystem configuration and to specific raw LoRa or LoRaWAN.

The arguments are:

* `mode` can be either `LoRa.LORA` or `LoRa.LORAWAN`.
* `region` can take the following values: `LoRa.AS923`, `LoRa.AU915`, `LoRa.EU868` or `LoRa.US915`. If not provided this will default to `LoRaEU868`. If they are not specified, this will also set appropriate defaults for `frequency` and `tx_power`.
* `frequency` accepts values between `863000000` and `870000000` in the 868 band, or between `902000000` and `928000000` in the 915 band.
* `tx_power` is the transmit power in dBm. It accepts between 2 and 14 for the 868 band, and between 5 and 20 in the 915 band.
* `bandwidth` is the channel bandwidth in KHz. In the 868 band the accepted values are `LoRa.BW_125KHZ` and `LoRa.BW_250KHZ`. In the 915 band the accepted values are `LoRa.BW_125KHZ` and `LoRa.BW_500KHZ`.
* `sf` sets the desired spreading factor. Accepts values between 7 and 12.
* `preamble` configures the number of pre-amble symbols. The default value is 8.
* `coding_rate` can take the following values: `LoRa.CODING_4_5`, `LoRa.CODING_4_6`, `LoRa.CODING_4_7` or `LoRa.CODING_4_8`.
* `power_mode` can be either `LoRa.ALWAYS_ON`, `LoRa.TX_ONLY` or `LoRa.SLEEP`. In `ALWAYS_ON` mode, the radio is always listening for incoming - packets whenever a transmission is not taking place. In `TX_ONLY` the radio goes to sleep as soon as the transmission completes. In `SLEEP` mode the radio is sent to sleep permanently and won't accept any commands until the power mode is changed.
* `tx_iq` enables TX IQ inversion.
* `rx_iq` enables RX IQ inversion.
* `adr` enables Adaptive Data Rate.
* `public` selects between the public and private sync word.
* `tx_retries` sets the number of TX retries in `LoRa.LORAWAN` mode.
* `device_class` sets the LoRaWAN device class. Can be either `LoRa.CLASS_A` or `LoRa.CLASS_C`.

{{% hint style="info" %}}
In `LoRa.LORAWAN` mode, only `adr`, `public`, `tx_retries` and `device_class` are used. All the other params will be ignored as they are handled by the LoRaWAN stack directly. On the other hand, in `LoRa.LORA` mode from those 4 arguments, only the public one is important in order to program the sync word. In `LoRa.LORA` mode `adr`, `tx_retries` and `device_class` are ignored since they are only relevant to the LoRaWAN stack.
{{< /hint >}}

For example, you can do:

```python

# initialize in raw LoRa mode
lora.init(mode=LoRa.LORA, tx_power=14, sf=12)
```

or

```python

# initialize in LoRaWAN mode
lora.init(mode=LoRa.LORAWAN)
```

#### lora.join(activation, auth, \* ,timeout=None, dr=None)

Join a LoRaWAN network. Internally the stack will automatically retry every 15 seconds until a Join Accept message is received.

The parameters are:

* `activation`: can be either `LoRa.OTAA` or `LoRa.ABP`.
* `auth`: is a tuple with the authentication data.
* `timeout`: is the maximum time in milliseconds to wait for the Join Accept message to be received. If no timeout (or zero) is given, the call returns immediately and the status of the join request can be checked with `lora.has_joined()`.
* `dr`: is an optional value to specify the initial data rate for the Join Request. Possible values are 0 to 5 for **EU868**, or 0 to 4 for **US915**.

In the case of `LoRa.OTAA` the authentication tuple is: `(dev_eui, app_eui, app_key)` where `dev_eui` is optional. If it is not provided the LoRa MAC will be used. Therefore, you can do OTAA in 2 different ways:

```python

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)  # the device MAC address is used as DEV_EUI
```

or

```python

lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0) # a custom DEV_EUI is specified
```

Example:

```python

from network import LoRa
import socket
import time
import ubinascii

# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# create an OTAA authentication parameters
app_eui = ubinascii.unhexlify('ADA4DAE3AC12676B')
app_key = ubinascii.unhexlify('11B0282A189B75B0B4D2D8C7FA38548B')

# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')
```

In the case of `LoRa.ABP` the authentication tuple is: `(dev_addr, nwk_swkey, app_swkey)`. Example:

```python

from network import LoRa
import socket
import ubinascii
import struct

# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# create an ABP authentication params
dev_addr = struct.unpack(">l", ubinascii.unhexlify('00000005'))[0]
nwk_swkey = ubinascii.unhexlify('2B7E151628AED2A6ABF7158809CF4F3C')
app_swkey = ubinascii.unhexlify('2B7E151628AED2A6ABF7158809CF4F3C')

# join a network using ABP (Activation By Personalisation)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))
```

#### lora.bandwidth(\[bandwidth\])

Get or set the bandwidth in raw LoRa mode (`LoRa.LORA`). Can be either `LoRa.BW_125KHZ` (0), `LoRa.BW_250KHZ` (1) or `LoRa.BW_500KHZ` (2):

```python

# get raw LoRa Bandwidth
lora.bandwidth()

# set raw LoRa Bandwidth
lora.bandwidth(LoRa.BW_125KHZ)
```

#### lora.frequency(\[frequency\])

Get or set the frequency in raw LoRa mode (`LoRa.LORA`). The allowed range is between `863000000` and `870000000` Hz for the 868 MHz band version or between `902000000` and `928000000` Hz for the 915 MHz band version.

```python

# get raw LoRa Frequency
lora.frequency()

# set raw LoRa Frequency
lora.frequency(868000000)
```

#### lora.coding\_rate(\[coding\_rate\])

Get or set the coding rate in raw LoRa mode (`LoRa.LORA`). The allowed values are: `LoRa.CODING_4_5` (1), `LoRa.CODING_4_6` (2), `LoRa.CODING_4_7` (3) and `LoRa.CODING_4_8` (4).

```python

# get raw LoRa Coding Rate
lora.coding_rate()

# set raw LoRa Coding Rate
lora.coding_rate(LoRa.CODING_4_5)
```

#### lora.preamble(\[preamble\])

Get or set the number of preamble symbols in raw LoRa mode (`LoRa.LORA`):

```python

# get raw LoRa preamble symbols
lora.preamble()

# set raw LoRa preamble symbols
lora.preamble(LoRa.CODING_4_5)
```

#### lora.sf(\[sf\])

Get or set the spreading factor value in raw LoRa mode (`LoRa.LORA`). The minimum value is 7 and the maximum is 12:

```python

# get raw LoRa spread factor value
lora.sf()

# set raw LoRa spread factor value
lora.sf(7)
```

#### lora.power\_mode(\[power\_mode\])

Get or set the power mode in raw LoRa mode (`LoRa.LORA`). The accepted values are: `LoRa.ALWAYS_ON`, `LoRa.TX_ONLY`, and `LoRa.SLEEP`:

#### lora.stats()

Return a named tuple with useful information from the last received LoRa or LoRaWAN packet. The named tuple has the following form:

`(rx_timestamp, rssi, snr, sftx, sfrx, tx_trials, tx_power, tx_time_on_air, tx_counter, tx_frequency)`

Example:

```python

lora.stats()
```

Where:

* `rx_timestamp` is an internal timestamp of the last received packet with microseconds precision.
* `rssi` holds the received signal strength in dBm.
* `snr` contains the signal to noise ratio id dB (as a single precision float).
* `sfrx` tells the data rate (in the case of LORAWAN mode) or the spreading factor (in the case of LORA mode) of the last packet received.
* `sftx` tells the data rate (in the case of LORAWAN mode) or the spreading factor (in the case of LORA mode) of the last packet transmitted.
* `tx_trials` is the number of tx attempts of the last transmitted packet (only relevant for LORAWAN confirmed packets).
* `tx_power` is the power of the last transmission (in dBm).
* `tx_time_on_air` is the time on air of the last transmitted packet (in ms).
* `tx_counter` is the number of packets transmitted.
* `tx_frequency` is the frequency used for the last transmission.

#### lora.has\_joined()

Returns `True` if a LoRaWAN network has been joined. `False` otherwise.

#### lora.add\_channel(index, \* , frequency, dr\_min, dr\_max)

Add a LoRaWAN channel on the specified `index`. If there's already a channel with that index it will be replaced with the new one.

The arguments are:

* `index`: Index of the channel to add. Accepts values between 0 and 15 for EU and between 0 and 71 for US.
* `frequency`: Centre frequency in Hz of the channel.
* `dr_min`: Minimum data rate of the channel (0-7).
* `dr_max`: Maximum data rate of the channel (0-7).

Examples:

```python

lora.add_channel(index=0, frequency=868000000, dr_min=5, dr_max=6)
```

#### lora.remove\_channel(index)

Removes the channel from the specified `index`. On the 868MHz band the channels 0 to 2 cannot be removed, they can only be replaced by other channels using the `lora.add_channel` method. A way to remove all channels except for one is to add the same channel, 3 times on indexes 0, 1 and 2. An example can be seen below:

```python

lora.remove_channel()
```

On the 915MHz band there are no restrictions around this.

#### lora.mac()

Returns a byte object with the 8-Byte MAC address of the LoRa radio.

#### lora.callback(trigger, handler=None, arg=None)

Specify a callback handler for the LoRa radio. The `trigger` types are `LoRa.RX_PACKET_EVENT`, `LoRa.TX_PACKET_EVENT`, and `LoRa.TX_FAILED_EVENT`

The `LoRa.RX_PACKET_EVENT` event is raised for every received packet. The `LoRa.TX_PACKET_EVENT` event is raised as soon as the packet transmission cycle ends, which includes the end of the receive windows (even if a downlink is received, the `LoRa.TX_PACKET_EVENT` will come last). In the case of non-confirmed transmissions, this will occur at the end of the receive windows, but, in the case of confirmed transmissions, this event will only be raised if the `ack` is received. If the `ack` is not received `LoRa.TX_FAILED_EVENT` will be raised after the number of `tx_retries` configured have been performed.

An example of how this callback functions can be seen the in method [`lora.events()`](../lora#lora-events).

#### lora.ischannel\_free(rssi\_threshold)

This method is used to check for radio activity on the current LoRa channel, and if the `rssi` of the measured activity is lower than the `rssi_threshold` given, the return value will be `True`, otherwise `False`. Example:

```python

lora.ischannel_free(-100)
```

#### lora.set\_battery\_level(level)

Set the battery level value that will be sent when the LoRaWAN MAC command that retrieves the battery level is received. This command is sent by the network and handled automatically by the LoRaWAN stack. The values should be according to the LoRaWAN specification:

* `0` means that the end-device is connected to an external power source.
* `1..254` specifies the battery level, 1 being at minimum and 254 being at maximum.
* `255` means that the end-device was not able to measure the battery level.

```python

lora.set_battery_level(127) # 50% battery
```

#### lora.events()

This method returns a value with bits sets (if any) indicating the events that have triggered the callback. Please note that by calling this function the internal events registry is cleared automatically, therefore calling it immediately for a second time will most likely return a value of 0.

Example:

```python

def lora_cb(lora):
    events = lora.events()
    if events & LoRa.RX_PACKET_EVENT:
        print('Lora packet received')
    if events & LoRa.TX_PACKET_EVENT:
        print('Lora packet sent')

lora.callback(trigger=(LoRa.RX_PACKET_EVENT | LoRa.TX_PACKET_EVENT), handler=lora_cb)
```

#### lora.nvram\_save()

Save the LoRaWAN state (joined status, network keys, packet counters, etc) in non-volatile memory in order to be able to restore the state when coming out of deepsleep or a power cycle.

```python

lora.nvram_save()
```

#### lora.nvram\_restore()

Restore the LoRaWAN state (joined status, network keys, packet counters, etc) from non-volatile memory. State must have been previously stored with a call to `nvram_save` before entering deepsleep. This is useful to be able to send a LoRaWAN message immediately after coming out of deepsleep without having to join the network again. This can only be used if the current region matches the one saved.

```python

lora.nvram_restore()
```

#### lora.nvram\_erase()

Remove the LoRaWAN state (joined status, network keys, packet counters, etc) from non-volatile memory.

```python

lora.nvram_erase()
```

## Constants

* LoRa stack mode: `LoRa.LORA`, `LoRa.LORAWAN`
* LoRaWAN join procedure: `LoRa.OTAA`, `LoRa.ABP`
* Raw LoRa power mode: `LoRa.ALWAYS_ON`, `LoRa.TX_ONLY`, `LoRa.SLEEP`
* Raw LoRa bandwidth: `LoRa.BW_125KHZ`, `LoRa.BW_250KHZ`, `LoRa.BW_500KHZ`
* Raw LoRa coding rate: `LoRa.CODING_4_5`, `LoRa.CODING_4_6`, `LoRa.CODING_4_7`, `LoRa.CODING_4_8`
* Callback trigger types (may be ORed): `LoRa.RX_PACKET_EVENT`, `LoRa.TX_PACKET_EVENT`, `LoRa.TX_FAILED_EVENT`
* LoRaWAN device class: `LoRa.CLASS_A`, `LoRa.CLASS_C`
* LoRaWAN regions: `LoRa.AS923`, `LoRa.AU915`, `LoRa.EU868`, `LoRa.US915`

## Working with LoRa and LoRaWAN Sockets

LoRa sockets are created in the following way:

```python

import socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
```

And they must be created after initialising the LoRa network card.

LoRa sockets support the following standard methods from the socket module:

#### socket.close()

Usage:

```python

s.close()
```

#### socket.bind(port\_number)

Usage:

```python

s.bind(1)
```

{{% hint style="info" %}}
The `bind()` method is only applicable when the radio is configured in `LoRa.LORAWAN` mode.
{{< /hint >}}

#### socket.send(bytes)

Usage:

```python

s.send(bytes([1, 2, 3]))
```

or

```python

s.send('Hello')
```

#### socket.recv(bufsize)

Usage:

```python

s.recv(128)
```

#### socket.recvfrom(bufsize)

This method is useful to know the destination port number of the message received. Returns a tuple of the form: `(data, port)`

Usage:

```python

s.recvfrom(128)
```

#### socket.setsockopt(level, optname, value)

Set the value of the given socket option. The needed symbolic constants are defined in the socket module (`SO_*` etc.). In the case of LoRa the values are always integers. Examples:

```python

# configuring the data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# selecting non-confirmed type of messages
s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, False)

# selecting confirmed type of messages
s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, True)
```

{{% hint style="info" %}}
Socket options are only applicable when the LoRa radio is used in LoRa.LORAWAN mode. When using the radio in LoRa.LORA mode, use the class methods to change the spreading factor, bandwidth and coding rate to the desired values.
{{< /hint >}}

#### socket.settimeout(value)

Sets the socket timeout value in seconds. Accepts floating point values.

Usage:

```python

s.settimeout(5.5)
```

#### socket.setblocking(flag)

Usage:

```python

s.setblocking(True)
```
