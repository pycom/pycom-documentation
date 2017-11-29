---
search:
    keywords: ['RMT', 'Remote', 'Remote Controller']
---

# class RMT – Remote Controller

The RMT (Remote Control) module is primarily designed to send and receive infrared remote control signals that
use on-off-keying of a carrier frequency, but due to its design it can be used to generate various types of signals.

### Quick Usage Example: sending

```python
import machine

rmt = machine.RMT(channel=3, gpio="P20", tx_idle_level=0)     # create a RMT object for transmission
data = (1,0,1,0,1,0,1,0,1,0)                                  # create series of bits to send
duration = 10000                                              # define duration of the bits: 1 ms
rmt.send_pulses(data, duration)                               # send the data
```

### Quick Usage Example: receiving

```python
import machine

rmt = machine.RMT(channel=3)                                          # create a RMT object
rmt.init(gpio="P20", rx_idle_threshold=12000)                         # Configure init for receiving
data = rmt.recv_pulses(8)                                             # wait for 8 pulses/bits  
```

### Constructors
<class><i>class</i> machine.RMT(channel,...)</class>

Construct an RMT object on the given channel. ``channel`` can be 2-7. With no additional parameters, the RMT object is created but not initialised. If extra arguments are given, the RMT is initialised for transmission or receiving. See ``init`` for parameters of initialisation.

### Methods

<function>rmt.init(gpio, rx_idle_threshold, rx_filter_threshold, tx_idle_level, tx_carrier)</function>

Initialize the RMT peripheral with the given parameters:

- ``gpio`` is the GPIO Pin to use.
- ``rx_idle_threshold`` is the maximum duration of a valid pulse. The value is interpreted in 100 nano seconds, can be 0-65535.
- ``rx_filter_threshold`` is the minimum duration of a valid pulse. The value is interpreted in 100 nano seconds, can be 0-31.
- ``tx_idle_level`` is the output signal's level after the transmission is finished, can be <constant>RMT.HIGH</constant> or <constant>RMT.LOW</constant>.
- ``tx_carrier`` is the modulation of the pulses to send.

Either ``rx_idle_threshold`` or ``tx_idle_level`` must be defined, both cannot be given at the same time because a channel can be configured in RX or TX mode only.
``rx_filter_threshold`` is not mandatory parameter. If not given then all pulses are accepeted with duration less than ``rx_idle_threshold`.
``tx_carrier`` is not mandatory parameters. If not given no modulation is used on the sent pulses.

The ``tx_carrier`` parameter is a tuple with the following structure:
- ``carrier_freq_hz`` is the carrier's frequency in Hz.
- ``carrier_duty_percent`` is the duty percent of the carrier's signal, can be 0-100.
- ``carrier_level`` is the level of the pulse to modulate, can be <constant>RMT.HIGH</constant> or <constant>RMT.LOW</constant>.

<function>rmt.deinit()</function>

Deinitialize the RMT object.

{% hint style='info' %}
If an RMT object needs to be reconfigured from RX/TX to TX/RX, then either first ``deinit()`` must be called or the ``init()`` again with the desired configuration.
{% endhint %}

<function>rmt.recv_pulses(bits_in)</function>

Wait until ``bits_in`` number of pulses have been received.
Return value: Tuple of items with the following structure:
(level, duration):
- ``level`` represents the received bit/pulse, can be 0 or 1.
- ``duration`` represents the duration of the received pulse, given in 100 nano seconds.

{% hint style='info' %}
Maximum of 128 pulses can be received in a row without receiving "idle" signal. If the incoming pulse sequence contains more than 128 pulses the rest is dropped and the receiver waits for another sequence of pulses.
The ``recv_pulses`` function can be called to receive more than 128 pulses, however the above mentioned limitation should be kept in mind when evaluating the
received data. 
{% endhint %}

<function>rmt.send_pulses(data, duration, bit_num)</function>

Send pulses given in ``data`` with ``duration`` pulse duration.
- ``data`` represents the sequence of bits/pulses to be sent.
- ``duration`` represents the duration of the pulses to be sent in 100 nano seconds.
- ``bit_num`` defines the length of ``data`` if it is given as a number.

Both the ``data`` and ``duration`` can be a tuple or a single number.
In case ``data`` is a tuple it must be composed by 0 or 1 elements.
In case ``data`` is a number, the bits compose the number are sent out in a little-endian fashion.

``bit_num`` is not mandatory. If not given, and ``bit_num`` is given as a number, the ``data`` is interpreted as 32 bit number

In case ``duration`` is a tuple it must be composed by unsigned integer numbers.
In case ``duration`` is a number, the given duration is applied on all pulses/bits defined by ``data``.
If both ``data`` and ``duration`` are tuples, their length must be the same.

### Constants
<constant>RMT.LOW</constant> <constant>RMT.HIGH</constant> 

Defines the level of the signal.
