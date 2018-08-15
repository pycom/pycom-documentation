# Notes

## Interrupt Handling

In Pycom’s ESP32 MicroPython port there are no restrictions on what can be done within an interrupt handler. For example, other ports do not allow allocating memory inside the handler or the use of sockets.

These limitations were raised by handling the interrupt events differently. When an interrupt happens, a message is posted into a queue, notifying a separate thread that the appropriate callback handler should be called. Such handler would receive an argument. By default it is the object associated with the event.

The user can do whatever is required inside of the callback, such as creating new variables, or even sending network packets. Bear in mind that interrupts are processed sequentially and thus it is ideal to keep the handlers as short as possible in order to attend all of them in the minimum time.

Currently, there are 2 classes that support interrupts; the [`Alarm`](pycom/machine/timer.md#class-timer-alarm-handler-none-s-ms-us-arg-none-periodic-false) and [`Pin`](pycom/machine/pin.md) classes. Both classes provide the `.callback()` method that enables the interrupt and registers the given handler. For more details about interrupt usage along with examples, please visit their respective sections.

{% hint style="info" %}
Currently the interrupt system can queue up to **16 interrupts**.
{% endhint %}

