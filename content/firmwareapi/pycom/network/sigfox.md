---
title: "Sigfox"
aliases:
    - firmwareapi/pycom/network/sigfox.html
    - firmwareapi/pycom/network/sigfox.md
    - chapter/firmwareapi/pycom/network/sigfox
---

Sigfox is a Low Power Wide Area Network protocol that enables remote devices to connect using ultra-narrow band, UNB technology. The protocol is bi-directional, messages can both be sent up to and down from the Sigfox servers.

{{% hint style="info" %}}
When operating in RCZ2 and RCZ4 the module can only send messages on the default macro-channel (this is due to Sigfox network limitations). Therefore, the device needs to reset automatically to the default macro-channel after every 2 transmissions. However, due to FCC duty cycle limitations, there must a minimum of a 20s delay after resetting to the default macro-channel. Our API takes care of this, (and in real life applications you should not be in the need to send Sigfox messages that often), so it will wait for the necessary amount of time to make sure that the duty cycle restrictions are fulfilled.

This means that if you run a piece of test code like:

```python

for i in range(1, 100):
  # send something
  s.send('Hello ' + str(i))
```

There will be a 20 second delay after every 2 packets.
{{< /hint >}}

This class provides a driver for the Sigfox network processor in the Sigfox enabled Pycom devices.

## Quick Usage Example

```python

from network import Sigfox
import socket

# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

# send some bytes
s.send(bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
```

{{% hint style="danger" %}}
Please ensure that there is an antenna connected to your device before sending/receiving Sigfox messages as in proper use (e.g. without an antenna), may damage the device.
{{< /hint >}}

## Constructors

#### class network.Sigfox(id=0, ...)

Create and configure a Sigfox object. See init for params of configuration. Examples:

```python

# configure radio for the Sigfox network, using RCZ1 (868 MHz)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# configure radio for FSK, device to device across 912 MHz
sigfox = Sigfox(mode=Sigfox.FSK, frequency=912000000)
```

{{% hint style="info" %}}
Sigfox.FSK mode is not supported on LoPy 4 and FiPy.
{{< /hint >}}

## Methods

#### sigfox.init(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1, \* , frequency=None)

Set the Sigfox radio configuration.

The arguments are:

* `mode` can be either `Sigfox.SIGFOX` or `Sigfox.FSK`. `Sigfox.SIGFOX` uses the Sigfox modulation and protocol while `Sigfox.FSK` allows to create point to point communication between 2 Devices using FSK modulation. _Note:_ `Sigfox.FSK` _mode is not supported on LoPy 4 and FiPy._
* `rcz` takes the following values: `Sigfox.RCZ1`, `Sigfox.RCZ2`, `Sigfox.RCZ3`, `Sigfox.RCZ4`. The `rcz` argument is only required if the mode is `Sigfox.SIGFOX`.
* `frequency` sets the frequency value in `FSK` mode. Can take values between 863 and 928 MHz. 

{{% hint style="info" %}}
The SiPy comes in 2 different hardware flavours: a +14dBm Tx power version which can only work with `RCZ1` and `RCZ3` and a +22dBm version which works exclusively on `RCZ2` and `RCZ4`.
{{< /hint >}}

#### sigfox.mac()

Returns a byte object with the 8-Byte MAC address of the Sigfox radio.

#### sigfox.id()

Returns a byte object with the 4-Byte bytes object with the Sigfox ID.

#### sigfox.rssi()

Returns a signed integer with indicating the signal strength value of the last received packet.

#### sigfox.pac()

Returns a byte object with the 8-Byte bytes object with the Sigfox PAC.

{{% hint style="info" %}}
To return human-readable values you should import `ubinascii` and convert binary values to hexidecimal representation. For example:

```python

print(ubinascii.hexlify(sigfox.mac()))
```
{{< /hint >}}

#### sigfox.frequencies()

Returns a tuple of the form: `(uplink_frequency_hz, downlink_frequency_hz)`

#### sigfox.public\_key(\[public\])

Sets or gets the public key flag. When called passing a `True` value the Sigfox public key will be used to encrypt the packets. Calling it without arguments returns the state of the flag.

```python

# enable encrypted packets
sigfox.public_key(True)

# return state of public_key
sigfox.public_key()
```

## Constants

* Sigfox radio mode: `sigfox.SIGFOX`, `sigfox.FSK` .
  * `SIGFOX` to specify usage of the Sigfox Public Network.
  * `FSK` to specify device to device communication.
* Sigfox zones: `sigfox.RCZ1`, `sigfox.RCZ2`, `sigfox.RCZ3`, `sigfox.RCZ4`
  * `RCZ1` to specify Europe, Oman & South Africa.
  * `RCZ2` for the USA, Mexico & Brazil.
  * `RCZ3` for Japan.
  * `RCZ4` for Australia, New Zealand, Singapore, Taiwan, Hong Kong, Colombia & Argentina.

## Working with Sigfox Sockets

Sigfox sockets are created in the following way:

```python

import socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
```

And they must be created after initialising the Sigfox network card.

Sigfox sockets support the following standard methods from the `socket` module:

#### socket.close()

Use it to close an existing socket.

#### socket.send(bytes)

In Sigfox mode the maximum data size is 12 bytes. In FSK the maximum is 64.

```python

# send a Sigfox payload of bytes
s.send(bytes([1, 2, 3]))

# send a Sigfox payload containing a string
s.send('Hello')
```

#### socket.recv(bufsize)

This method can be used to receive a Sigfox downlink or FSK message.

```python

# size of buffer should be passed for expected payload, e.g. 64 bytes
s.recv(64)
```

#### socket.setsockopt(level, optname, value)

Set the value of the given socket option. The needed symbolic constants are defined in the socket module (`SO_*` etc.). In the case of Sigfox the values are always an integer. Examples:

```python

# wait for a downlink after sending the uplink packet
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, True)

# make the socket uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

# use the socket to send a Sigfox Out Of Band message
s.setsockopt(socket.SOL_SIGFOX, socket.SO_OOB, True)

# disable Out-Of-Band to use the socket normally
s.setsockopt(socket.SOL_SIGFOX, socket.SO_OOB, False)

# select the bit value when sending bit only packets
s.setsockopt(socket.SOL_SIGFOX, socket.SO_BIT, False)
```

Sending a Sigfox packet with a single bit is achieved by sending an empty string, i.e.:

```python

import socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# send a 1 bit
s.setsockopt(socket.SOL_SIGFOX, socket.SO_BIT, True)
s.send('')
socket.settimeout(value)
# set timeout for the socket, e.g. 5 seconds
s.settimeout(5.0)
socket.setblocking(flag)
# specifies if socket should be blocking based upon Boolean flag.
s.setblocking(True)
```

If the socket is set to blocking, your code will be wait until the socket completes sending/receiving.

## Sigfox Downlink

A Sigfox capable Pycom devices (SiPy) can both send and receive data from the Sigfox network. To receive data, a message must first be sent up to Sigfox, requesting a downlink message. This can be done by passing a `True` argument into the `setsockopt()` method.

```python

s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, True)
```

An example of the downlink procedure can be seen below:

```python

# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as DOWNLINK specified by 'True'
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, True)

# send some bytes and request DOWNLINK
s.send(bytes([1, 2, 3]))

# await DOWNLINK message
s.recv(32)
```

## Sigfox FSK (Device to Device)

To communicate between two Sigfox capable devices, it may be used in FSK mode. Two devices are required to be set to the same frequency, both using FSK.

{{% hint style="info" %}}
Sigfox.FSK mode is not supported on LoPy 4 and FiPy.
{{< /hint >}}

**Device 1**:

```python

sigfox = Sigfox(mode=Sigfox.FSK, frequency=868000000)

s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
s.setblocking(True)

while True:
  s.send('Device-1')
  time.sleep(1)
  print(s.recv(64))
```

**Device 2**:

```python

sigfox = Sigfox(mode=Sigfox.FSK, frequency=868000000)

s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
s.setblocking(True)

while True:
  s.send('Device-2')
  time.sleep(1)
  print(s.recv(64))
```

{{% hint style="danger" %}}
Remember to use the correct frequency for your region (868 MHz for Europe, 912 MHz for USA, etc.)
{{< /hint >}}

