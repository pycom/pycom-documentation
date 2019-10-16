---
title: "CAN"
aliases:
    - firmwareapi/pycom/machine/can.html
    - firmwareapi/pycom/machine/can.md
    - chapter/firmwareapi/pycom/machine/can
---

The CAN class supports the full CAN 2.0 specification with standard and extended frames, as well as acceptance filtering.

The ESP32 has a built-in CAN controller, but the transceiver needs to be added externally. A recommended device is the SN65HVD230.

## Quick Usage Example

```python

from machine import CAN

can = CAN(mode=CAN.NORMAL, baudrate=500000, pins=('P22', 'P23'))
can.send(id=12, data=bytes([1, 2, 3, 4, 5, 6, 7, 8]))
can.recv()
```

## Constructors

#### class machine.CAN(bus=0, ...)

Create an CAN object. See init for parameters of initialisation.:

```python

# only 1 CAN peripheral is available, so the bus must always be 0
can = CAN(0, mode=CAN.NORMAL, baudrate=500000, pins=('P22', 'P23'))    # pin order is Tx, Rx
```

## Methods

#### can.init(mode=CAN.NORMAL, baudrate=500000, \*, frame\_format=CAN.FORMAT\_STD, rx\_queue\_len=128, pins=('P22', 'P23'))

Initialize the CAN controller. The arguments are:

* `mode` can take either CAN.NORMAL or CAN.SILENT. Silent mode is useful for sniffing the bus.
* `baudrate` sets up the bus speed. Acceptable values are between 1 and 1000000.
* `frame_format` defines the frame format to be accepted by the receiver. Useful for filtering frames based on the identifier length. Can tale either `CAN.FORMAT_STD`, `CAN.FORMAT_EXT`, `CAN.FORMAT_BOTH`. If `CAN.FORMAT_STD` is selected, extended frames won't be received and vice-versa.
* `rx_queue_len` defines the number of messages than can be queued by the receiver. Due to CAN being a high traffic bus, large values are recommended (&gt;= 128), otherwise messages will be dropped specially when no filtering is applied.
* `pins` selects the `Tx` and `Rx` pins (in that order).

#### can.deinit()

Disables the CAN bus.

#### can.send(id, \* , data=None, rtr=False, extended=False)

Send a CAN frame on the bus

* `id` is the identifier of the message.
* `data` can take up to 8 bytes. It must be left empty is the message to be sent is a remote request (rtr=True).
* `rtr` set it to false to send a remote request.
* `extnted` specifies if the message identifier width should be 11bit (standard) or 29bit (extended).

Can be used like:

```python

can.send(id=0x0020, data=bytes([0x01, 0x02, 0x03, 0x04, 0x05]), extended=True)   # sends 5 bytes with an extended identifier

can.send(id=0x010, data=bytes([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08])) # sends 8 bytes with an standard identifier

can.send(id=0x012, rtr=True)         # sends a remote request for message id=0x12
```

#### can.recv(timeout=0)

Get a message from the receive queue, and optionally specify a timeout value in **s** (can be a floating point value e.g. `0.2`). This function returns `None` if no messages available. If a message is present, it will be returned as a named tuple with the following form:

`(id, data, rtr, extended)`

```python

>>> can.recv()
(id=0x012, data=b'123', rtr=False, extended=False)
```

#### can.soft\_filter(mode, filter\_list)

Specify a software filter accepting only the messages that pass the filter test.

There are 3 possible filter modes:

* `CAN.FILTER_LIST` allows to pass the list of IDs that should be accepted.
* `CAN.FILTER_RANGE` allows to pass a list or tuple of ID ranges that should be accepted.
* `CAN.FILTER_MASK` allows to pass a list of tuples of the form: `(filter, mask)`.

With software filters all messages in the bus are received by the CAN controller but only the matching ones are passed to the RX queue. This means that the queue won't be filled up with non relevant messages, but the interrupt overhead will remain as normal. The `filter_list` can contain up to 32 elements.

For example:

```python

can.soft_filter(CAN.FILTER_LIST, [0x100, 0x200, 0x300, 0x400])  # only accept identifiers from 0x100, 0x200, 0x300 and 0x400

can.soft_filter(CAN.FILTER_RANGE, [(0x001, 0x010), (0x020, 0x030), (0x040, 0x050)])  # only accept identifiers from 0x001 to 0x010, from 0x020 to 0x030 and from 0x040 to 0x050.

can.soft_filter(CAN.FILTER_MASK, [(0x100, 0x7FF), (0x200, 0x7FC)]) # more of the classic Filter and Mask method.

can.soft_filter(None)   # disable soft filters, all messages are accepted
```

#### can.callback(trigger, handler=None, arg=None)

Set a callback to be triggered when any of this 3 events are present:

* trigger is the type of event that triggers the callback. Possible values are:
  * `CAN.RX_FRAME` interrupt whenever a new frame is received.
  * `CAN.RX_FIFO_NOT_EMPTY` interrupt when a frame is received on an empty FIFO.
  * `CAN.RX_FIFO_OVERRUN` interrupt when a message is received and the FIFO is full.

The values can be OR-ed together, for instance `trigger=CAN.RX_FRAME | CAN.RX_FIFO_OVERRUN`

* handler is the function to be called when the event happens. This function will receive one argument. Set handler to None to disable the callback.
* arg is an optional argument to pass to the callback. If left empty or set to None, the function will receive the CAN object that triggered it.

It can be used like this:

```python

from machine import CAN

can = CAN(mode=CAN.NORMAL, baudrate=500000, pins=('P22', 'P23'))

def can_cb(can_o):
    print('CAN Rx:', can_o.recv())

can.callback(handler=can_cb, trigger=CAN.RX_FRAME)
```

#### can.events()

This method returns a value with bits sets (if any) indicating the events that have occurred in the bus. Please note that by calling this function the internal events registry is cleared automatically, therefore calling it immediately for a second time will most likely return a value of 0.

## Constants

`CAN.NORMAL`, `CAN.SILENT`, `CAN.FORMAT_STD`, `CAN.FORMAT_EXT`, `CAN.FORMAT_BOTH`, `CAN.RX_FRAME`, `CAN.RX_FIFO_NOT_EMPTY`, `CAN.RX_FIFO_OVERRUN`, `CAN.FILTER_LIST`, `CAN.FILTER_RANGE`, `CAN.FILTER_MASK`

