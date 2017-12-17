# class CAN – Controller Area Network

The CAN class supports the full CAN 2.0 specification with standard and extended frames, as well as acceptance filtering.

The ESP32 has a built-in CAN controller, but the transceiver needs to be added externally. A recommended device is the SN65HVD230.

### Quick Usage Example

```python
from machine import CAN

can = CAN(mode=CAN.NORMAL, baudrate=500000, pins=('P22', 'P23'))
can.send(id=12, data=bytes([1, 2, 3, 4, 5, 6, 7, 8]))
can.recv()
```

### Constructors

<class><i>class</i> machine.CAN(bus=0, ...)</class>

Create an CAN object. See init for parameters of initialisation.:

```python
# only 1 CAN peripheral is available, so the bus must always be 0
can = RTC(0, mode=CAN.NORMAL, baudrate=500000, pins=('P22', 'P23'))
```

### Methods

<function>can.init(mode=CAN.NORMAL, baudrate=500000, *, frame_format=CAN.FORMAT_STD, rx_queue_len=128, pins=('P22', 'P23'))</function>

Initialize the CAN controller. The arguments are:

- ``mode`` can take either <constant>CAN.NORMAL</constant> or <constant>CAN.SILENT</constant>. Silent mode is useful for sniffing the bus.
- ``baudrate`` setups the bus speed. Acceptable values are between 1 and 1000000.
- ``frame_format`` defines the frame format to be accepted by the receiver. Useful for filtering frames based on the identifier length. Can tale either <constant>CAN.FORMAT_STD</constant> or <constant>CAN.FORMAT_EXT</constant> or <constant>CAN.FORMAT_BOTH</constant>. If <constant>CAN.FORMAT_STD</constant> is selected, extended frames won't be received and viceversa.
- ``rx_queue_len`` defines the number of messages than can be queued by the receiver. Due to CAN being a high traffic bus, large values are recommended (>= 128), otherwise messages will be dropped specially when no filtering is applied.
- ``pins`` selects the Tx and Rx pins.

<function>can.deinit()</function>

Disables the CAN bus.

```python
# disable the CAN bus
can.deinit()
```

<function>can.send(id, * , data=None, rtr=False, extended=False)</function>

Send a CAN frame on the bus

- ``id`` is the identifier of the message.
- ``data`` can take up to 8 bytes. It must be left empty is the message to be sent is a remote request (rtr=True).
- ``rtr`` set it to false to send a remote request.
- ``extnted`` specifies if the message identifier width should be 11bit (standard) or 29bit (extended).

Can be used like:

```python
can.send(id=0x20, data=bytes([1, 2, 3, 4, 5]), extended=True)   # sends 5 bytes with an extended identifier

can.send(id=0x10, data=bytes([1, 2, 3, 4, 5, 6, 7, 8]))         # sends 8 bytes with an standard identifier

can.send(id=0x12, rtr=True)         # sends a remote request for message id=0x12

```

<function>can.recv(timeout=0)</function>

Get a message from the receive queue, and optionally specify a timeout value. This function returns ``None`` if no messages available.
If a message is present, it will be returned as a named tuple with the following form:

``(id, data, rtr, extended)``

```python
>>> can.recv()
(id=12, data=b'123', rtr=False, extended=False)
```

<function>can.soft_filter(filter_list)</function>

Specify a software filter accepting only the messages with identifiers falling in the range specified. With software filters all messages in the bus are received by the CAN controller, but only the matching ones are passed to the RX queue. This means that the queue won't be filled with non relevant messages, but the interrupt overhead will remain as before. The ``filter_list`` can contain up to 32 tuples stating the range of IDs to be accepted.

For example:

```python
>>> can.soft_filter([(1, 10), (20, 30), (40, 50)])  # only accept identifiers from 1 to 10, from 20 to 30 and from 40 to 50.
```

<function>can.hard_filter(codemask_list)</function>

Specify a hardware filter using code and mask. Up to 2 tuples of code and mask can be specified. In order to filter extended messages,
only 1 code and mask pair should be passed.

For example:

```python
>>> can.hard_filter([(0x10, 0xF800), (0x30, 0xF800)])  # only accept identifiers 0x10 and 0x30
```

<function>can.callback(trigger, handler=None, arg=None)</function>

Set a callback to be triggered when any of this 3 events are present: 

- trigger is the type of event that triggers the callback. Possible values are:
	- <constant>CAN.RX_FRAME</constant> interrupt whenever a new frame is received.
	- <constant>CAN.RX_FIFO_NOT_EMPTY</constant> interrupt when a frame is received on an empty FIFO.
	- <constant>CAN.RX_FIFO_OVERRUN</constant> interrupt when a message is received and the FIFO is full.

The values can be OR-ed together, for instance trigger=CAN.RX_FRAME | CAN.RX_FIFO_OVERRUN

- handler is the function to be called when the event happens. This function will receive one argument. Set handler to None to disable the callback.

- arg is an optional argument to pass to the callback. If left empty or set to None, the function will receive the CAN object that triggered it.


It can be used like this:

```python
from machine import CAN

can = CAN(mode=CAN.NORMAL, baudrate=500000, pins=('P22', 'P23'))
 
def can_cb(can_o):
    print('CAN Rx:', can_o.recv())

can.callback(handler=can_cb, trigger=CAN.RX_FRAME)
```

<function>can.events()</function>

This method returns a value with bits sets (if any) indicating the events that have occured in the bus. Please note that by calling this function the internal events registry is cleared automatically, therefore calling it immediately for a second time will most likely return a value of 0.


### Constants
<constant>CAN.NORMAL</constant> <constant>CAN.SILENT</constant> <constant>CAN.FORMAT_STD</constant> <constant>CAN.FORMAT_EXT</constant> <constant>CAN.FORMAT_BOTH</constant> <constant>CAN.RX_FRAME</constant> <constant>CAN.RX_FIFO_NOT_EMPTY</constant> <constant>CAN.RX_FIFO_OVERRRUN</constant>
