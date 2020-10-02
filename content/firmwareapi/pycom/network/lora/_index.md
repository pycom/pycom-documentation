---
title: "LoRa"
aliases:
  - /firmwareapi/pycom/network/lora.md
---
This class provides a LoRaWAN 1.0.2 compliant driver for the LoRa network processor in the LoPy, LoPy4 and FiPy.

> Please ensure that there is an antenna connected to your device before sending/receiving LoRa messages as improper use (e.g. without an antenna), may damage the device.

## Examples

For various complete LoRa examples, check [here](/tutorials/networks/lora/).

## Constructors

### class network.LoRa(...)

Create and configure a LoRa object. See init for params of configuration.

```python
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
```

## Methods

### lora.init(mode, [region=LoRa.EU868, frequency, tx_power, bandwidth=LoRa.BW_125KHZ, sf=7, preamble=8, coding_rate=LoRa.CODING_4_5, power_mode=LoRa.ALWAYS_ON, tx_iq=False, rx_iq=False, adr=False, public=True, tx_retries=2, device_class=LoRa.CLASS_A])

This method is used to set the LoRa subsystem configuration and to specific raw LoRa or LoRaWAN.

The arguments are:

* `mode` can be either 
    * `LoRa.LORA`: For LoRa MAC / RAW
    * `LoRa.LORAWAN`: For use in the LoRa Wide Area Network and services like TTN and Chirpstack
* `region` can take the following values: 
    * `LoRa.AS923`
    * `LoRa.AU915`
    * `LoRa.EU868`
    * `LoRa.US915`
    * `LoRa.CN470`
    * `LoRa.IN865`

    > If no region is provided, it will default to the setting provided in the CONFIG partition, set by the Firmware Updater tool.
* `frequency` accepts values within the selected Region frequency bands.
* `tx_power` is the transmit power in dBm. 
* `bandwidth` is the channel bandwidth in KHz. 
    * `LoRa.BW_125KHZ`
    * `LoRa.BW_250KHZ`
    * `LoRa.BW_500KHZ`
* `sf` sets the desired spreading factor. Accepts values between 7 and 12.
* `preamble` configures the number of pre-amble symbols. The default value is 8.
* `coding_rate` can take the following values: 
    * `LoRa.CODING_4_5`
    * `LoRa.CODING_4_6`
    * `LoRa.CODING_4_7`
    * `LoRa.CODING_4_8`
* `power_mode` can be either 
    * `LoRa.ALWAYS_ON`: the radio is always listening for incoming - packets whenever a transmission is not taking place
    * `LoRa.TX_ONLY`: he radio goes to sleep as soon as the transmission completes
    * `LoRa.SLEEP`: the radio is sent to sleep permanently and won't accept any commands until the power mode is changed.
* `tx_iq` enables TX IQ inversion.
* `rx_iq` enables RX IQ inversion.
* `adr` enables Adaptive Data Rate.
* `public` selects between the public and private sync word.
* `tx_retries` sets the number of TX retries in `LoRa.LORAWAN` mode.
* `device_class` sets the LoRaWAN device class. Can be either:
    * `LoRa.CLASS_A`
    * `LoRa.CLASS_C`

> In `LoRa.LORAWAN` mode, only `adr`, `public`, `tx_retries` and `device_class` are used. All the other params will be ignored as they are handled by the LoRaWAN stack directly. On the other hand, in `LoRa.LORA` mode from those 4 arguments, only the public one is important in order to program the sync word. In `LoRa.LORA` mode `adr`, `tx_retries` and `device_class` are ignored since they are only relevant to the LoRaWAN stack.

### lora.join(activation, auth, [timeout=None, dr=None])

Join a LoRaWAN network. Internally the stack will automatically retry every 15 seconds until a Join Accept message is received. The parameters are:

* `activation`: can be either:
    * `LoRa.OTAA`: Over the Air Activation
    * `LoRa.ABP`: Activation By Personalisation
* `auth`: is a tuple with the authentication data.
    * In the case of `LoRa.OTAA` the authentication tuple is: `(dev_eui, app_eui, app_key)` where `dev_eui` is optional. If it is not provided the LoRa MAC will be used.
    * In the case of `LoRa.ABP` the authentication tuple is: `(dev_addr, nwk_swkey, app_swkey)`.
* `timeout`: is the maximum time in milliseconds to wait for the Join Accept message to be received. If no timeout (or zero) is given, the call returns immediately and the status of the join request can be checked with `lora.has_joined()`.
* `dr`: is an optional value to specify the initial data rate for the Join Request. values are region specific.


### lora.frequency([frequency])

Get or set the frequency in raw LoRa mode (`LoRa.LORA`). The allowed range is region-specific.

### lora.bandwidth([bandwidth])	

Get or set the bandwidth in raw LoRa mode (`LoRa.LORA`). Bandwidth can be either: (depending on the region setting)
* `LoRa.BW_125KHZ`
* `LoRa.BW_250KHZ`
* `LoRa.BW_500KHZ`

### lora.coding_rate([coding_rate])

Get or set the coding rate in raw LoRa mode (`LoRa.LORA`). The allowed values are: (depending on the region setting)
* `LoRa.CODING_4_5`
* `LoRa.CODING_4_6`
* `LoRa.CODING_4_7`
* `LoRa.CODING_4_8`


### lora.preamble([preamble])

Get or set the number of preamble symbols in raw LoRa mode (`LoRa.LORA`).

### lora.sf([sf])

Get or set the spreading factor value in raw LoRa mode (`LoRa.LORA`). The minimum value is 7 and the maximum is 12:

### lora.power_mode([power_mode])

Get or set the power mode in raw LoRa mode (`LoRa.LORA`). The accepted values are: 
* `LoRa.ALWAYS_ON`
* `LoRa.TX_ONLY`
* `LoRa.SLEEP`

### lora.stats()

Return a named tuple with useful information from the last received LoRa or LoRaWAN packet. The named tuple has the following form:

`(rx_timestamp, rssi, snr, sftx, sfrx, tx_trials, tx_power, tx_time_on_air, tx_counter, tx_frequency)`

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

### lora.has_joined()

Returns `True` if a LoRaWAN network has been joined. `False` otherwise.

### lora.add_channel(index, frequency, dr_min, dr_max)

Add a LoRaWAN channel on the specified `index`. If there's already a channel with that index it will be replaced with the new one.

The arguments are:

* `index`: Index of the channel to add. Accepts values between 0 and 15 for EU and between 0 and 71 for US.
* `frequency`: Centre frequency in Hz of the channel.
* `dr_min`: Minimum data rate of the channel (0-7).
* `dr_max`: Maximum data rate of the channel (0-7).

Example:

```python
lora.add_channel(index=0, frequency=868000000, dr_min=5, dr_max=6)
```

### lora.remove_channel(index)

Removes the channel from the specified `index`. On the 868MHz band the channels 0 to 2 cannot be removed, they can only be replaced by other channels using the `lora.add_channel` method. A way to remove all channels except for one is to add the same channel, 3 times on indexes 0, 1 and 2. An example can be seen below:

```python
lora.remove_channel()
```

### lora.mac()

Returns a byte object with the 8-Byte MAC address of the LoRa radio.

### lora.callback(trigger, [handler=None, arg=None])

Specify a callback handler for the LoRa radio. The `trigger` types are 
* `LoRa.RX_PACKET_EVENT` is raised for every received packet
* `LoRa.TX_PACKET_EVENT` is raised as soon as the packet transmission cycle ends, which includes the end of the receive windows. In the case of non-confirmed transmissions, this will occur at the end of the receive windows, but, in the case of confirmed transmissions, this event will only be raised if the `ack` is received.
* `LoRa.TX_FAILED_EVENT` will be raised after the number of `tx_retries` configured have been performed and no `ack` is received.

An example of how this callback functions can be seen the in method [`lora.events()`](../lora#lora-events).

### lora.ischannel_free(rssi_threshold)

This method is used to check for radio activity on the current LoRa channel, and if the `rssi` of the measured activity is lower than the `rssi_threshold` given, the return value will be `True`, otherwise `False`. Example:

```python
lora.ischannel_free(-100)
```

### lora.set_battery_level(level)

Set the battery level value that will be sent when the LoRaWAN MAC command that retrieves the battery level is received. This command is sent by the network and handled automatically by the LoRaWAN stack. The values should be according to the LoRaWAN specification:

* `0` means that the end-device is connected to an external power source.
* `1..254` specifies the battery level, 1 being at minimum and 254 being at maximum.
* `255` means that the end-device was not able to measure the battery level.

```python
lora.set_battery_level(127) # 50% battery
```

### lora.events()

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

### lora.nvram_save()

Save the LoRaWAN state (joined status, network keys, packet counters, etc) in non-volatile memory in order to be able to restore the state when coming out of deepsleep or a power cycle.

```python
lora.nvram_save()
```

### lora.nvram_restore()

Restore the LoRaWAN state (joined status, network keys, packet counters, etc) from non-volatile memory. State must have been previously stored with a call to `nvram_save` before entering deepsleep. This is useful to be able to send a LoRaWAN message immediately after coming out of deepsleep without having to join the network again. This can only be used if the current region matches the one saved.

### lora.nvram_erase()

Remove the LoRaWAN state (joined status, network keys, packet counters, etc) from non-volatile memory.


### lora.mesh()

Enable the Mesh network. Only after Mesh enabling the `lora.cli()` and `socket` can be used.

### lora.cli()

Send OpenThread CLI commands, the list is [here](https://github.com/openthread/openthread/tree/master/src/cli/). The output is multiline string, having as line-endings the `\r\n`.

```bash
>>> print(lora.cli("ipaddr"))
fdde:ad00:beef:0:0:ff:fe00:fc00
fdde:ad00:beef:0:0:ff:fe00:e800
fdde:ad00:beef:0:e1f0:783c:1e8f:c763
fe80:0:0:0:2c97:cb65:3219:c86
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

## Exceptions

* `LoRa.timeout`

## Working with LoRa and LoRaWAN Sockets

LoRa sockets are created in the following way:

```python
import socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
```

And they must be created after initialising the LoRa network card.

LoRa-Mesh socket is created, if the Mesh was enabled before (`lora.mesh()` was called).

> The LoRa-Mesh socket supports only the following socket methods: `close()` , `bind()`, `sendto()`, and `recvfrom()`.
