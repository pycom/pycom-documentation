# class LoRa

This class provides a driver for the LoRa network processor in the LoPy and FiPy. Below is an example demonstrating LoRaWAN Activation by Personalisation usage:

```python
from network import LoRa
import socket
import binascii
import struct

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an ABP authentication params
dev_addr = struct.unpack(">l", binascii.unhexlify('00 00 00 05'.replace(' ','')))[0]
nwk_swkey = binascii.unhexlify('2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C'.replace(' ',''))
app_swkey = binascii.unhexlify('2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C'.replace(' ',''))

# join a network using ABP (Activation By Personalization)
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

{% hint style='info' %}
Please ensure that there is an antenna connected to your device before sending/receiving LoRa messages as inproper use (e.g. without an antenna), may damage the device.
{% endhint %}

### Additional Examples

For various other complete LoRa examples, check here for additional examples.

### Constructors

<class><i>class</i> network.LoRa(id=0, ...)</class>

Create and configure a LoRa object. See init for params of configuration.

```python
lora = LoRa(mode=LoRa.LORAWAN)
```

### Methods

<function>lora.init(mode, * , frequency=868000000, tx_power=14, bandwidth=LoRa.BW_125KHZ, sf=7, preamble=8, coding_rate=LoRa.CODING_4_5, power_mode=LoRa.ALWAYS_ON, tx_iq=False, rx_iq=False, adr=False, public=True, tx_retries=1, device_class=LoRa.CLASS_A)</function>

This method is used to set the LoRa subsystem configuration and to specific raw LoRa or LoRaWAN.

The arguments are:

- ``mode`` can be either <constant>LoRa.LORA</constant> or <constant>LoRa.LORAWAN</constant>.
- ``frequency`` accepts values between 863000000 and 870000000 in the 868 band, or between 902000000 and 928000000 in the 915 band.
- ``tx_power`` is the transmit power in dBm. It accepts between 2 and 14 for the 868 band, and between 5 and 20 in the 915 band.
- ``bandwidth`` is the channel bandwidth in KHz. In the 868 band the accepted values are <constant>LoRa.BW_125KHZ</constant> and <constant>LoRa.BW_250KHZ</constant>. In the 915 band the accepted values are <constant>LoRa.BW_125KHZ</constant> and <constant>LoRa.BW_500KHZ</constant>.
- ``sf`` sets the desired spreading factor. Accepts values between 7 and 12.
- ``preamble`` configures the number of pre-amble symbols. The default value is 8.
- ``coding_rate`` can take the following values: <constant>LoRa.CODING_4_5</constant>, <constant>LoRa.CODING_4_6</constant>, <constant>LoRa.CODING_4_7</constant> or <constant>LoRa.CODING_4_8</constant>.
- ``power_mode`` can be either <constant>LoRa.ALWAYS_ON</constant>, <constant>LoRa.TX_ONLY</constant> or <constant>LoRa.SLEEP</constant>. In <constant>ALWAYS_ON</constant> mode, the radio is always listening for incoming - packets whenever a transmission is not taking place. In <constant>TX_ONLY</constant> the radio goes to sleep as soon as the transmission completes. In <constant>SLEEP</constant> mode the radio is sent to sleep permanently and won’t accept any commands until the power mode is changed.
- ``tx_iq`` enables TX IQ inversion.
- ``rx_iq`` enables RX IQ inversion.
- ``adr`` enables Adaptive Data Rate.
- ``public`` selects between the public and private sync word.
- ``tx_retries`` sets the number of TX retries in <constant>LoRa.LORAWAN</constant> mode.
- ``device_class`` sets the LoRaWAN device class. Can be either <constant>LoRa.CLASS_A</constant> or <constant>LoRa.CLASS_C</constant>.

{% hint style='info' %}
In <constant>LoRa.LORAWAN</constant> mode, only ``adr``, ``public``, ``tx_retries`` and ``device_class`` are used. All the other params will be ignored as they are handled by the LoRaWAN stack directly. On the other hand, in <constant>LoRa.LORA</constant> mode from those 4 arguments, only the public one is important in order to program the sync word. In <constant>LoRa.LORA</constant> mode ``adr``, ``tx_retries`` and ``device_class`` are ignored since they are only relevant to the LoRaWAN stack.
{% endhint %}


For example, you can do:

```python
# initialize in raw LoRa mode
lora.init(mode=LoRa.LORA, tx_power=14, sf=12)
```

or:

```python
# initialize in LoRaWAN mode
lora.init(mode=LoRa.LORAWAN)
```

<function>lora.join(activation, auth, * ,timeout=None, dr=None)</function>

Join a LoRaWAN network. Internally the stack will automatically retry every 15 seconds until a Join Accept message is received.
The parameters are:

- ``activation``: can be either <constant>LoRa.OTAA</constant> or <constant>LoRa.ABP</constant>.
- ``auth``: is a tuple with the authentication data.
- ``timeout``: is the maximum time in milliseconds to wait for the Join Accept message to be received. If no timeout (or zero) is given, the call returns immediatelly and the status of the join request can be checked with ``lora.has_joined()``.
- ``dr``: is an optional value to specify the initial data rate for the Join Request. Possible values are 0 to 5 for **EU868**, or 0 to 4 for **US915**.

In the case of <constant>LoRa.OTAA</constant> the authentication tuple is: (``app_eui``, ``app_key``). Example:

```python
from network import LoRa
import socket
import time
import binascii

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an OTAA authentication parameters
app_eui = binascii.unhexlify('AD A4 DA E3 AC 12 67 6B'.replace(' ',''))
app_key = binascii.unhexlify('11 B0 28 2A 18 9B 75 B0 B4 D2 D8 C7 FA 38 54 8B'.replace(' ',''))

# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')

```

In the case of <constant>LoRa.ABP</constant> the authentication tuple is: (``dev_addr``, ``nwk_swkey``, ``app_swkey``). Example:

```python
from network import LoRa
import socket
import binascii
import struct

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an ABP authentication params
dev_addr = struct.unpack(">l", binascii.unhexlify('00 00 00 05'.replace(' ','')))[0]
nwk_swkey = binascii.unhexlify('2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C'.replace(' ',''))
app_swkey = binascii.unhexlify('2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C'.replace(' ',''))

# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))
```

<function>lora.bandwidth([bandwidth])</function>

Get or set the bandwidth in raw LoRa mode (<function>LoRa.LORA</function>). Can be either <function>LoRa.BW_125KHZ</function> (0), <function>LoRa.BW_250KHZ</function> (1) or <function>LoRa.BW_500KHZ</function> (2):

```python
# get raw LoRa Bandwidth
lora.bandwidth()

# set raw LoRa Bandwidth
lora.bandwidth(LoRa.BW_125KHZ)
```

<function>lora.frequency([frequency])</function>

Get or set the frequency in raw LoRa mode (<constant>LoRa.LORA</constant>). The allowed range is between 863000000 and 870000000 Hz for the 868 MHz band version or between 902000000 and 928000000 Hz for the 915 MHz band version.:

```python
# get raw LoRa Frequency
lora.frequency()

# set raw LoRa Frequency
lora.frequency(868000000)
```

lora.coding_rate([coding_rate])
Get or set the coding rate in raw LoRa mode (LoRa.LORA). The allowed values are: <constant>LoRa.CODING_4_5</constant> (1), <constant>LoRa.CODING_4_6</constant> (2), <constant>LoRa.CODING_4_7</constant> (3) and <constant>LoRa.CODING_4_8</constant> (4).


```python
# get raw LoRa Coding Rate
lora.coding_rate()

# set raw LoRa Coding Rate
lora.coding_rate(LoRa.CODING_4_5)
```

<function>lora.preamble([preamble])</function>

Get or set the number of preamble symbols in raw LoRa mode (<constant>LoRa.LORA</constant>):

```python
# get raw LoRa preamble symbols
lora.preamble()

# set raw LoRa preamble symbols
lora.preamble(LoRa.CODING_4_5)
```

<function>lora.sf([sf])</function>

Get or set the spreading factor value in raw LoRa mode (<constant>LoRa.LORA</constant>). The minimum value is 7 and the maximum is 12:

```python
# get raw LoRa spread factor value
lora.sf()

# set raw LoRa spread factor value
lora.sf(7)
```

<function>lora.power_mode([power_mode])</function>

Get or set the power mode in raw LoRa mode (<constant>LoRa.LORA</constant>). The accepted values are: <constant>LoRa.ALWAYS_ON</constant>, <constant>LoRa.TX_ONLY</constant> and <constant>LoRa.SLEEP</constant>:

<function>lora.stats()</function>

Return a named tuple with useful information from the last received LoRa or LoRaWAN packet. The named tuple has the following form:

(``rx_timestamp``, ``rssi``, ``snr``, ``sftx``, ``sfrx``, ``tx_trials``)

Example:

```python
lora.stats()
```

Where:

- ``rx_timestamp`` is an internal timestamp of the last received packet with microseconds precision.
- ``rssi`` holds the received signal strength in dBm.
- ``snr`` contains the signal to noise ratio id dB (as a single precision float).
- ``sfrx`` tells the data rate (in the case of LORAWAN mode) or the spreading factor (in the case of LORA mode) of the last packet received.
- ``sftx`` tells the data rate (in the case of LORAWAN mode) or the spreading factor (in the case of LORA mode) of the last packet transmitted.
- ``tx_trials`` is the number of tx attempts of the last transmitted packet (only relevant for LORAWAN confirmed packets).

<function>lora.has_joined()</function>

Returns ``True`` if a LoRaWAN network has been joined. ``False`` otherwise.:

<function>lora.add_channel(index, * , frequency, dr_min, dr_max)</function>

Add a LoRaWAN channel on the specified index. If there’s already a channel with that index it will be replaced with the new one.

The arguments are:

- ``index``: Index of the channel to add. Accepts values between 0 and 15 for EU and between 0 and 71 for US.
- ``frequency``: Centre frequency in Hz of the channel.
- ``dr_min``: Minimum data rate of the channel (0-7).
- ``dr_max``: Maximum data rate of the channel (0-7).

Examples:

```python
lora.add_channel(index=0, frequency=868000000, dr_min=5, dr_max=6)
```

<function>lora.remove_channel(index)</function>

Removes the channel from the specified index. On the 868MHz band the channels 0 to 2 cannot be removed, they can only be replaced by other channels using the lora.add_channel method. A way to remove all channels except for one is to add the same channel, 3 times on indexes 0, 1 and 2. An example can be seen below:

```python
lora.remove_channel()
```

On the 915MHz band there are no restrictions around this.

<function>lora.mac()</function>

Returns a byte object with the 8-Byte MAC address of the LoRa radio.

<function>lora.callback(trigger, handler=None, arg=None)</function>

Specify a callback handler for the LoRa radio. The trigger types are <constant>LoRa.RX_PACKET_EVENT</constant>, <constant>LoRa.TX_PACKET_EVENT</constant> and <constant>LoRa.TX_FAILED_EVENT</constant>

The <constant>LoRa.RX_PACKET_EVENT</constant> event is raised for every received packet. The <constant>LoRa.TX_PACKET_EVENT</constant> event is raised as soon as the packet transmission cycle ends, which includes the end of the receive windows (even if a downlink is received, the <constant>LoRa.TX_PACKET_EVENT</constant> will come last). In the case of non-confirmed transmissions, this will occur at the end of the receive windows, but, in the case of confirmed transmissions, this event will only be raised if the ``ack`` is received. If the ack is not received <constant>LoRa.TX_FAILED_EVENT<constant> will be raised after the number of ``tx_retries`` configured have been performed.

An example of how this callback functions can be seen the in method <function>lora.events()<function>.

<function>lora.ischannel_free(rssi_threshold)</function>

This method is used to check for radio activity on the current LoRa channel, and if the ``rssi`` of the measured activity is lower than the ``rssi_threshold`` given, the return value will be ``True``, otherwise ``False``. Example:

```python
lora.ischannel_free(-100)
```

<function>lora.set_battery_level(level)</function>

Set the battery level value that will be sent when the LoRaWAN MAC command that retrieves the battery level is received. This command is sent by the network and handled automatically by the LoRaWAN stack. The values should be according to the LoRaWAN specification:

- ``0`` means that the end-device is connected to an external power source.
- ``1..254`` specifies the battery level, 1 being at minimum and 254 being at maximum.
- ``255`` means that the end-device was not able to measure the battery level.

```python
lora.set_battery_level(127)    # 50% battery
```

<function>lora.events()</function>

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

<function>lora.nvram_save()</function>

Save the LoRaWAN state (joined status, network keys, packet counters, etc) in non-volatile memory in order to be able to restore the state when coming out of deepsleep or a power cycle.

```python
lora.nvram_save()
```

<function>lora.nvram_restore()</function>

Restore the LoRaWAN state (joined status, network keys, packet counters, etc) from non-volatile memory. State must have been previously stored with a call to ``nvram_save`` before entering deepsleep. This is useful to be able to send a LoRaWAN message immediately after coming out of deepsleep without having to join the network again.

```python
lora.nvram_restore()
```

### Constants

<constant>LoRa.LORA</constant> <constant>LoRa.LORAWAN</constant>
LoRa stack mode

<constant>LoRa.OTAA</constant> <constant>LoRa.ABP</constant>
LoRaWAN join procedure

<constant>LoRa.ALWAYS_ON</constant> <constant>LoRa.TX_ONLY</constant> <constant>LoRa.SLEEP</constant>
Raw LoRa power mode

<constant>LoRa.BW_125KHZ</constant> <constant>LoRa.BW_250KHZ</constant> <constant>LoRa.BW_500KHZ</constant>
Raw LoRa bandwidth

<constant>LoRa.CODING_4_5</constant> <constant>LoRa.CODING_4_6</constant> <constant>LoRa.CODING_4_7</constant> <constant>LoRa.CODING_4_8</constant>
Raw LoRa coding rate

<constant>LoRa.RX_PACKET_EVENT</constant> <constant>LoRa.TX_PACKET_EVENT</constant> <constant>LoRa.TX_FAILED_EVENT</constant>
Callback trigger types (may be ORed)

<constant>LoRa.CLASS_A</constant> <constant>LoRa.CLASS_C</constant>
LoRaWAN device class

### Working with LoRa and LoRaWAN Sockets

LoRa sockets are created in the following way:

```python
import socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
```

And they must be created after initialising the LoRa network card.

LoRa sockets support the following standard methods from the socket module:

<function>socket.close()</function>

Usage:

```python
s.close()
```

<function>socket.bind(port_number)</function>

Usage:

```python
s.bind(1)
```

{% hint style='info' %}
The <function>bind()</function> method is only applicable when the radio is configured in <constant>LoRa.LORAWAN</constant> mode.
{% endhint %}

<function>socket.send(bytes)</function>

Usage:
```python
s.send(bytes([1, 2, 3]))
```
or:
```python
s.send('Hello')
```

<function>socket.recv(bufsize)</function>

Usage:
```python
s.recv(128)
```

<function>socket.recvfrom(bufsize)</function>

This method is useful to know the destination port number of the message received. Returns a tuple of the form: ``(data, port)``

Usage:
```python
s.recvfrom(128)
```

<function>socket.setsockopt(level, optname, value)</function>

Set the value of the given socket option. The needed symbolic constants are defined in the socket module (SO_* etc.). In the case of LoRa the values are always integers. Examples:

```python
# configuring the data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# selecting non-confirmed type of messages
s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, False)

# selecting confirmed type of messages
s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, True)
```

{% hint style='info' %}
Socket options are only applicable when the LoRa radio is used in <constant>LoRa.LORAWAN</constant> mode. When using the radio in LoRa.LORA mode, use the class methods to change the spreading factor, bandwidth and coding rate to the desired values.
{% endhint %}

<function>socket.settimeout(value)</function>

Sets the socket timeout value in seconds. Accepts floating point values.

Usage:
```python
s.settimeout(5.5)
```

<function>socket.setblocking(flag)</function>

Usage:
```python
s.setblocking(True)
```
