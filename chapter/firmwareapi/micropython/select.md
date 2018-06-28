# select – Wait for Events on a Set of Streams
This module provides functions to wait for events on streams (select streams which are ready for operations).

### Pyboard specifics
Polling is an efficient way of waiting for read/write activity on multiple objects. Current objects that support polling are: <constant>pyb.UART</constant>, <constant>pyb.USB_VCP</constant>.

### Functions

#####<function>select.poll()</function>

Create an instance of the `Poll` class.

#####<function>select.select(rlist, wlist, xlist[, timeout])</function>

Wait for activity on a set of objects.

This function is provided for compatibility and is not efficient. Usage of `Poll` is recommended instead.

#####<class><i>class</i> Poll</class>
### Methods

#####<function>poll.register(obj[, eventmask])</function>

Register `obj` for polling. `eventmask` is logical OR of:

- `select.POLLIN` - data available for reading
- `select.POLLOUT` - more data can be written
- `select.POLLERR` - error occurred
- `select.POLLHUP` - end of stream/connection termination detected
`eventmask` defaults to `select.POLLIN | select.POLLOUT`.

#####<function>poll.unregister(obj)</function>

Unregister `obj` from polling.

#####<function>poll.modify(obj, eventmask)</function>

Modify the `eventmask` for `obj`.

#####<function>poll.poll([timeout])</function>

Wait for at least one of the registered objects to become ready. Returns list of (`obj`, `event`, ...) tuples, `event` element specifies which events happened with a stream and is a combination of `select.POLL*` constants described above. There may be other elements in tuple, depending on a platform and version, so don’t assume that its size is 2. In case of timeout, an empty list is returned.

Timeout is in milliseconds.
