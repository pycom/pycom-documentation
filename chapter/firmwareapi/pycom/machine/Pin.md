# class Pin – Control I/O Pins
A pin is the basic object to control I/O pins (also known as GPIO - general-purpose input/output). It has methods to set the mode of the pin (input, output, etc) and methods to get and set the digital logic level. For analog control of a pin, see the ADC class.

### Quick Usage Example
```python
from machine import Pin

# initialize ``P9`` in gpio mode and make it an output
p_out = Pin('P9', mode=Pin.OUT)
p_out.value(1)
p_out.value(0)
p_out.toggle()
p_out(True)

# make ``P10`` an input with the pull-up enabled
p_in = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP)
p_in() # get value, 0 or 1
```

### Constructors

#####<class><i>class</i> machine.Pin(id, ...)</class>

Create a new Pin object associated with the string id. If additional arguments are given, they are used to initialise the pin. See <function>pin.init()</function>.

```python
from machine import Pin
p = Pin('P10', mode=Pin.OUT, pull=None, alt=-1)
```

### Methods

#####<function>pin.init(mode, pull, * , alt)</function>

Initialise the pin:

- ``mode`` can be one of:
	- <constant>Pin.IN</constant> - input pin.
	- <constant>Pin.OUT</constant> - output pin in push-pull mode.
	- <constant>Pin.OPEN_DRAIN</constant> - input or output pin in open-drain mode.
- ``pull`` can be one of:
	- ``None`` - no pull up or down resistor.
	- <constant>Pin.PULL_UP</constant> - pull up resistor enabled.
	- <constant>Pin.PULL_DOWN</constant> - pull down resistor enabled.
- ``alt`` is the id of the alternate function.

Returns: ``None``.

#####<function>pin.id()</function>

Get the pin id.

#####<function>pin.value([value])</function>

Get or set the digital logic level of the pin:
- With no argument, return 0 or 1 depending on the logic level of the pin.
- With value given, set the logic level of the pin. value can be anything that converts to a boolean. If it converts to True, the pin is set high, otherwise it is set low.

#####<function>pin([value])</function>

Pin objects are callable. The call method provides a (fast) shortcut to set and get the value of the pin.

Example:

```python
from machine import Pin
pin = Pin('P12', mode=Pin.IN, pull=Pin.PULL_UP)
pin()   # fast method to get the value
```

See <function>pin.value()</function> for more details.

#####<function>pin.toggle()</function>

Toggle the value of the pin.

#####<function>pin.mode([mode])</function>

Get or set the pin mode.

#####<function>pin.pull([pull])</function>

Get or set the pin pull.

#####<function>pin.hold([hold])</function>

Get or set the pin hold. Can be used to retain the pin state through a core
reset and system reset triggered by watchdog time-out or Deep-sleep events.
This only work for:  `P2`, `P3`, `P4`, `P6`, `P8`, `P9`, `P10`, `P13`, `P14`,
 `P15`, `P16`, `P17`, `P18`, `P19`, `P20`, `P21`, `P22`, and `P23`.

#####<function>pin.callback(trigger, handler=None, arg=None)</function>

Set a callback to be triggered when the input level at the pin changes.

- trigger is the type of event that triggers the callback. Possible values are:
	- <constant>Pin.IRQ_FALLING</constant> interrupt on falling edge.
	- <constant>Pin.IRQ_RISING</constant> interrupt on rising edge.
	- <constant>Pin.IRQ_LOW_LEVEL</constant> interrupt on low level.
	- <constant>Pin.IRQ_HIGH_LEVEL</constant> interrupt on high level.

The values can be OR-ed together, for instance trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING

- handler is the function to be called when the event happens. This function will receive one argument. Set handler to None to disable it.

- arg is an optional argument to pass to the callback. If left empty or set to None, the function will receive the Pin object that triggered it.

Example:

```python
from machine import Pin

def pin_handler(arg):
    print("got an interrupt in pin %s" % (arg.id()))

p_in = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP)
p_in.callback(Pin.IRQ_FALLING | Pin.IRQ_RISING, pin_handler)
```

{% hint style='info' %}
For more information on how Pycom’s products handle interrupts, see [here](../../../toolsandfeatures/notes.md).
{% endhint %}


### Attributes

#####<class><i>class</i> pin.exp_board</class>

Contains all Pin objects supported by the expansion board. Examples:

```python
Pin.exp_board.G16
led = Pin(Pin.exp_board.G16, mode=Pin.OUT)
Pin.exp_board.G16.id()
```

#####<class><i>class</i>  pin.module</class>
Contains all ``Pin`` objects supported by the module. Examples:

```python
Pin.module.P9
led = Pin(Pin.module.P9, mode=Pin.OUT)
Pin.module.P9.id()
```

### Constants
The following constants are used to configure the pin objects. Note that not all constants are available on all ports.

<constant>Pin.IN</constant> <constant>Pin.OUT</constant> <constant>Pin.OPEN_DRAIN</constant>

Selects the pin mode.

<constant>Pin.PULL_UP</constant> <constant>Pin.PULL_DOWN</constant>

Enables the pull up or pull down resistor.
