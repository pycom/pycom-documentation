# machine

The `machine` module contains specific functions related to the board.

### Quick Usage Example

```python
import machine

help(machine) # display all members from the machine module
machine.freq() # get the CPU frequency
machine.unique_id() # return the 6-byte unique id of the board (the LoPy's WiFi MAC address)
```

## Reset Functions

#### machine.reset\(\)

Resets the device in a manner similar to pushing the external RESET button.

#### machine.reset\_cause\(\)

Get the reset cause. See constants for the possible return values.

## Interrupt Functions

#### machine.disable\_irq\(\)

Disable interrupt requests. Returns and integer representing the previous IRQ state. This return value can be passed to `enable_irq` to restore the IRQ to its original state.

#### machine.enable\_irq\(\[state\]\)

Enable interrupt requests. The most common use of this function is to pass the value returned by `disable_irq` to exit a critical section. Another options is to enable all interrupts which can be achieved by calling the function with no parameters.

## Power Functions

#### machine.freq\(\)

Returns CPU frequency in hertz.

#### machine.idle\(\)

Gates the clock to the CPU, useful to reduce power consumption at any time during short or long periods. Peripherals continue working and execution resumes as soon as any interrupt is triggered \(on many ports this includes system timer interrupt occurring at regular intervals on the order of millisecond\).

#### machine.deepsleep\(\[time\_ms\]\)

Stops the CPU and all peripherals, including the networking interfaces \(except for LTE\). Execution is resumed from the main script, just as with a reset. If a value in milliseconds is given then the device will wake up after that period of time, otherwise it will remain in deep sleep until the reset button is pressed.

The products with LTE connectivity \(FiPy, GPy, G01\), require the LTE radio to be disabled separately via the LTE class before entering deepsleep. This is required due to the LTE radio being powered independently and allowing use cases which require the system to be taken out from deepsleep by an event from the LTE network \(data or SMS received for instance\).

#### machine.pin\_deepsleep\_wakeup\(pins, mode, enable\_pull\)

Configure pins to wake up from deep sleep mode. The pins which have this capability are: `P2, P3, P4, P6, P8 to P10 and P13 to P23`.

The arguments are:

* `pins` a list or tuple containing the `GPIO` to setup for deepsleep wakeup.
* `mode` selects the way the configure `GPIO`s can wake up the module. The possible values are: `machine.WAKEUP_ALL_LOW` and `machine.WAKEUP_ANY_HIGH`.
* `enable_pull` if set to `True` keeps the pull up or pull down resistors enabled during deep sleep. If this variable is set to `True`, then `ULP` or capacitive touch wakeup cannot be used in combination with `GPIO` wakeup.

#### machine.wake\_reason\(\)

Get the wake reason. See constants for the possible return values. Returns a tuple of the form: `(wake_reason, gpio_list)`. When the wakeup reason is either GPIO or touch pad, then the second element of the tuple is a list with GPIOs that generated the wakeup.

#### machine.remaining\_sleep\_time\(\)

Returns the remaining timer duration \(in milliseconds\) if the ESP32 is woken up from deep sleep by something other than the timer. For example, if you set the timer for 30 seconds \(30000 ms\) and it wakes up after 10 seconds then this function will return `20000`.

## Miscellaneous Functions

#### machine.main\(filename\)

Set the `filename` of the main script to run after `boot.py` is finished. If this function is not called then the default file `main.py` will be executed.

It only makes sense to call this function from within `boot.py`.

#### machine.rng\(\)

Return a 24-bit software generated random number.

#### machine.unique\_id\(\)

Returns a byte string with a unique identifier of a board/SoC. It will vary from a board/SoC instance to another, if underlying hardware allows. Length varies by hardware \(so use substring of a full value if you expect a short ID\). In some MicroPython ports, ID corresponds to the network MAC address.

{% hint style="info" %}
Use `ubinascii.hexlify()` to convert the byte string to hexadecimal form for ease of manipulation and use elsewhere.
{% endhint %}

#### machine.info\(\)

Returns the high water mark of the stack associated with various system tasks, in words \(1 word = 4 bytes on the ESP32\). If the value is zero then the task has likely overflowed its stack. If the value is close to zero then the task has come close to overflowing its stack.

## Constants

### Reset Causes

`machine.PWRON_RESET`, `machine.HARD_RESET`, `machine.WDT_RESET,` `machine.DEEPSLEEP_RESET`, `machine.SOFT_RESET`, `machine.BROWN_OUT_RESET`

### Wake Reasons

`machine.PWRON_WAKE`, `machine.PIN_WAKE`, `machine.RTC_WAKE`, `machine.ULP_WAKE`

### Pin Wakeup Modes

`machine.WAKEUP_ALL_LOW`, `machine.WAKEUP_ANY_HIGH`

