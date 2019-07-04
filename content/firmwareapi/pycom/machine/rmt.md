---
title: "RMT"
aliases:
    - firmwareapi/pycom/machine/rmt.html
    - firmwareapi/pycom/machine/rmt.md
    - chapter/firmwareapi/pycom/machine/rmt
---

The RMT (Remote Control) module is primarily designed to send and receive infrared remote control signals that use on-off-keying of a carrier frequency, but due to its design it can be used to generate various types of signals.

## Quick Usage Example: sending

```python

import machine

# create a RMT object for transmission
rmt = machine.RMT(channel=3, gpio="P20", tx_idle_level=0)
# create series of bits to send    
data = (1,0,1,0,1,0,1,0,1)
# define duration of the bits, time unit depends on the selected RMT channel  
duration = 10000
# send the signal                                         
rmt.send_pulses(duration, data)
```

## Quick Usage Example: receiving

```python

import machine
# create a RMT object
rmt = machine.RMT(channel=3)
# Configure RTM for receiving
rmt.init(gpio="P20", rx_idle_threshold=12000)     
# wait for any number of pulses until one longer than rx_idle_threshold        
data = rmt.recv_pulses()
```

## Constructors

#### class machine.RMT(channel,...)

Construct an RMT object on the given channel. `channel` can be 2-7. With no additional parameters, the RMT object is created but not initialised. If extra arguments are given, the RMT is initialised for transmission or reception. See `init` for parameters of initialisation. The resolution which a pulse can be sent/received depends on the selected channel:

| Channel | Resolution | Maximum Pulse Width |
| :--- | :--- | :--- |
| 0 | Used by on-board LED |  |
| 1 | Used by `pycom.pulses_get()` |  |
| 2 | 100nS | 3.2768 ms |
| 3 | 100nS | 3.2768 ms |
| 4 | 1000nS | 32.768 ms |
| 5 | 1000nS | 32.768 ms |
| 6 | 3125nS | 102.4   ms |
| 7 | 3125nS | 102.4   ms |

## Methods

#### rmt.init(gpio, rx\_idle\_threshold, rx\_filter\_threshold, tx\_idle\_level, tx\_carrier)

Initialise the RMT peripheral with the given parameters:

* `gpio` is the GPIO Pin to use.
* `rx_idle_threshold` is the maximum duration of a valid pulse. The represented time unit (resolution) depends on the selected channel, value can be 0-65535.
* `rx_filter_threshold` is the minimum duration of a valid pulse. The represented time unit (resolution) depends on the selected channel, value can be 0-31.
* `tx_idle_level` is the output signal's level after the transmission is finished, can be RMT.HIGH or RMT.LOW.
* `tx_carrier` is the modulation of the pulses to send.

Either `rx_idle_threshold` or `tx_idle_level` must be defined, both cannot be given at the same time because a channel can be configured in RX or TX mode only. `rx_filter_threshold` is not mandatory parameter. If not given then all pulses are accepted with duration less than `rx_idle_threshold`. `tx_carrier` is not mandatory parameters. If not given no modulation is used on the sent pulses.

The `tx_carrier` parameter is a tuple with the following structure:

* `carrier_freq_hz` is the carrier's frequency in Hz.
* `carrier_duty_percent` is the duty percent of the carrier's signal, can be 0%-100%.
* `carrier_level` is the level of the pulse to modulate, can be RMT.HIGH or RMT.LOW.

#### rmt.deinit()

Deinitialise the RMT object.

{{% hint style="info" %}}
If an RMT object needs to be reconfigured from RX/TX to TX/RX, then either first `deinit()` must be called or the `init()` again with the desired configuration.
{{< /hint >}}

#### rmt.pulses\_get(pulses, timeout)

Reads in pulses from the GPIO pin.

* `pulses` if not specified, this function will keep reading pulses until the

  `rx_idle_threshold` is exceeded. If it is specified this function will return

  the exactly that number of pulses, ignoring anything shorter than

  `rx_filter_threshold` or longer than `rx_idle_threshold`.

* `timeout` is specified, this function will return if the first pulse does

  not occur within `timeout` microseconds. If not specified, it will wait

  indefinitely.

Return value: Tuple of items with the following structure: `(level, duration)`:

* `level` represents the level of the received bit/pulse, can be 0 or 1.
* `duration` represents the duration of the received pulse, the time unit (resolution) depends on the selected channel.

{{% hint style="info" %}}
Maximum of 128 pulses can be received in a row without receiving "idle" signal. If the incoming pulse sequence contains more than 128 pulses the rest is dropped and the receiver waits for another sequence of pulses. The `pulses_get` function can be called to receive more than 128 pulses, however the above mentioned limitation should be kept in mind when evaluating the received data.
{{< /hint >}}

#### rmt.pulses\_send(duration, data, start\_level)

Generates pulses as defined by the parameters below

* `duration` represents the duration of the pulses to be sent,

  the time unit (resolution) depends on the selected channel.

* `data` Tuple that represents the sequence of pulses to be sent, must be

  composed of 0 or 1 elements.

* `start_level` defines the state (HIGH/LOW) of the first pulse given by

  `duration` if `data` is not given.

`data` must be a tuple and `duration` can be a tuple or a single number, with `data` being optional. In the case that only `duration` is provided, it must be a tuple and you must also provide `start_level` which will dictate the level of the first duration, the signal level then toggles between each duration value. If `data` is provided and `duration` is a single number, each pulse in `data` will have have an equal length as set by `duration`. If `data` and `duration` are provided as tuples, they must be of the same number of elements, with each pulse lasting its matching duration.

## Constants

* Define the level of the pulse: `RMT.LOW`, `RMT.HIGH`
