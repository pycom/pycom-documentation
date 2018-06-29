# Documentation Syntax

The Pycom documentation follows standard Python Library format using the popular Sphinx Docs tool. There are some notable points regarding the syntax of classes, methods and constants. Please see the notes below and familiarise yourself with the specific details before reviewing the documentation.

### Keyword Arguments

`Keyword Arguments` refer to the arguments that are passed into a constructor (upon referencing a class object). When passing values into a MicroPython constructor it is not always required to specify the name of the argument and instead rely on the order of the arguments passed as to describe what they refer to. In the example below, it can be seen that the argument `mode` is passed into the `i2c.init()` method without specifying a name.

The values of the arguments (as seen in the examples/docs) refer to the default values that are passed into the constructor if nothing is provided.

<function>i2c.init(mode, * , baudrate=100000, pins=(SDA, SCL))</function>

An example of how this method might be called:

```python
i2c.init(I2C.MASTER, pins=('P12', 'P11'))
```

It can be seen that a value for `baudrate` was not passed into the method and thus MicroPython will assume a default value of `100000`. Also the first argument `mode` was not specified by name, as the constructor does not require it, denoted by the lack of an `=` symbol in the constructor documentation.

### Passing Arguments into a Method

It is important to note that there are certain class methods that can only accept a `keyword` for certain arguments as well as some that only accept a `value`. This is intentional by design but is not always apparent to the user calling specific methods. The differences between the two are outlined below, with examples referencing where differences might apply and what to be aware of.

### Keyword

An astrik `*` in a method description (in the docs), denotes that the following arguments require a keyword, i.e. `pin='P16'` in the example below.

<function>adc.channel(* , pin, attn=ADC.ATTN_0DB)</function>

```python
from machine import ADC

adc = ADC()                     # create an ADC object
apin = adc.channel(pin='P16')   # create an analog pin on P16
```

`pin` is a required argument and the method `channel` will not execute unless it is passed as with a keyword.

Another example shows how the `PWM` class, `pwm.channel()` requires a keyword argument for `pin` but does not for `id`.

```python
from machine import PWM

pwm = PWM(0, frequency=5000)
pwm_c = pwm.channel(0, pin='P12') # no keyword argument requires for id (0) but is required for pin (pin='P12')
```

### Value

The documentation may refer to a method that takes an argument listed by name but does allow for a keyword to be passed. For example, the `pycom` class contains a method `rgbled`. This lists that the method accepts a value for `color`, however this may not be specified by `keyword`, only `value`. This is intentional as the `value` being passed is the only argument valid for this method

<function>pycom.rgbled(color)</function>

If the argument is passed into the method with a keyword, it will return an error stating TypeError: function does not take keyword arguments.

```python
import pycom

pycom.rgbled(color=0xFF0000) # Incorrect
pycom.rgbled(0xFF0000) # Correct
```

Another example of a method that only accepts value input. In this case, the `RTC.init()` method require a value (`tuple`) input for the `datetime`. It will not accept a keyword.

<function>rtc.init(datetime)</function>

```python
from machine import RTC

rtc = RTC()
rtc.init(datetime=(2014, 5, 1, 4, 13, 0, 0, 0)) # Incorrect
rtc.init((2014, 5, 1, 4, 13, 0, 0, 0)) # Correct
```

### Constants

The `constants` section of a library within the docs refers to specific values from that library’s class. These might be used when constructing an object from that class or when utilising a method from within that class. These are generally listed by the library name followed by the specific value. See the example below:

<function>I2C.MASTER()</function>

{% hint style='info' %}
Be aware that you can only reference these constants upon importing and constructing a object from a library.
{% endhint %}
