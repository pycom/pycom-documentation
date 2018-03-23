# Deep Sleep API

This chapter describes the library which controls the Deep Sleep Shield. This includes the controls for external interrupts and timer setup of the deep sleep functionality.

To use this library, please upload the associated [Deep Sleep Library](https://github.com/pycom/pycom-libraries/tree/master/deepsleep) to ``/lib`` on the target Pycom Device.

### Quick Example

```python
from deepsleep import DeepSleep

ds = DeepSleep()

# get the wake reason and the value of the pins during wake up
wake_s = ds.get_wake_status()
print(wake_s)

if wake_s['wake'] == DeepSleep.PIN_WAKE:
    print("Pin wake up")
elif wake_s['wake'] == DeepSleep.TIMER_WAKE:
    print("Timer wake up")
else:  # deepsleep.POWER_ON_WAKE:
    print("Power ON reset")

ds.enable_pullups('P17')  # can also do ds.enable_pullups(['P17', 'P18'])
ds.enable_wake_on_fall('P17') # can also do ds.enable_wake_on_fall(['P17', 'P18'])

ds.go_to_sleep(60)  # go to sleep for 60 seconds
```

### DeepSleep

The Deep Sleep Shield allows for waking up via a user trigger and also via an external interrupt (i.e. Accelerometer, Button).

#### Constructors

#####<class><i>class</i> DeepSleep()</class>

Creates a DeepSleep object, that will control the board's sleep features. For example;

```python
ds = DeepSleep()
```

#### Methods

#####<function>deepsleep.enable_auto_poweroff()</function>

This method allows for a critical battery voltage to be set. For example, if the external power source (e.g. LiPo Cell) falls below 3.3V, turn off the Pycom Device. This is intended to protect the hardware from under voltage.

#####<function>deepsleep.enable_pullups(pins)</function>

This method allows for pullup pins to be enabled. For example, if an external trigger occurs, wake the Pycom Device from Deep Sleep. ``pins`` may be passed into the method as a list, i.e. ``['P17', 'P18']``.

#####<function>deepsleep.disable_pullups(pins)</function>

This method allows for pullup pins to be disabled. For example, if an external trigger occurs, wake the Pycom Device from Deep Sleep. ``pins`` may be passed into the method as a list, i.e. ``['P17', 'P18']``.

#####<function>deepsleep.enable_wake_on_raise(pins)</function>

This method allows for pullup pins to trigger on a rising voltage. For example, if an external rising voltage triggers occurs, wake the Pycom Device from Deep Sleep. ``pins`` may be passed into the method as a list, i.e. ``['P17', 'P18']``.

#####<function>deepsleep.disable_wake_on_raise(pins)</function>

This method allows for disabling pullup pins that trigger on a rising voltage. ``pins`` may be passed into the method as a list, i.e. ``['P17', 'P18']``.

#####<function>deepsleep.enable_wake_on_fall(pins)</function>

This method allows for pullup pins to trigger on a falling voltage. For example, if an external falling voltage triggers occurs, wake the Pycom Device from Deep Sleep. ``pins`` may be passed into the method as a list, i.e. ``['P17', 'P18']``.

#####<function>deepsleep.disable_wake_on_fall(pins)</function>

This method allows for disabling pullup pins that trigger on a falling voltage. ``pins`` may be passed into the method as a list, i.e. ``['P17', 'P18']``.

#####<function>deepsleep.get_wake_status()</function>

This method returns the status of the pins at wakeup from deep sleep. The method returns a ``dict`` with the states of ``wake``, ``P10``, ``P17``,``P18``.

#####<function>deepsleep.set_min_voltage_limit(value)</function>

This method relates to the enable_auto_poweroff method and allows the user to specify the minimum power off voltage as a value.

#####<function>deepsleep.go_to_sleep(seconds)</function>

This method sends the board into deep sleep for a period of ``seconds`` or until an external interrupt has triggered (see ``set_pullups``).

#####<function>deepsleep.hw_reset()</function>

This method resets the PIC controller and resets it to the state previous to the pins/min-voltage being set.

{% hint style='info' %}
Please note that more functionality is being added weekly to these libraries. If a required feature is not available, feel free to contribute with a pull request at the [Pycom Libraries](https://github.com/pycom/pycom-libraries) GitHub repository.
{% endhint %}
