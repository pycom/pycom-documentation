---
title: "Deep Sleep API"
aliases:
    - datasheets/boards/deepsleep/api.html
    - datasheets/boards/deepsleep/api.md
    - product-info/boards/deepsleep/api
    - chapter/datasheets/boards/deepsleep/api
---

This chapter describes the library which controls the Deep Sleep Shield. This includes the controls for external interrupts and timer set-up of the deep sleep function.

To use this library, please upload the associated [Deep Sleep Library](https://github.com/pycom/pycom-libraries/tree/master/deepsleep) to `/lib` on the relevant Pycom device.

## Quick Example

```python


from deepsleep import DeepSleep
import deepsleep

ds = DeepSleep()

# get the wake reason and the value of the pins during wake up
wake_s = ds.get_wake_status()
print(wake_s)

if wake_s['wake'] == deepsleep.PIN_WAKE:
    print("Pin wake up")
elif wake_s['wake'] == deepsleep.TIMER_WAKE:
    print("Timer wake up")
else:  # deepsleep.POWER_ON_WAKE:
    print("Power ON reset")

ds.enable_pullups('P17')  # can also do ds.enable_pullups(['P17', 'P18'])
ds.enable_wake_on_fall('P17') # can also do ds.enable_wake_on_fall(['P17', 'P18'])

ds.go_to_sleep(60)  # go to sleep for 60 seconds
```

## DeepSleep

The Deep Sleep Shield can be woken up via a user trigger, as well as an external interrupt \(i.e. Accelerometer, Button\).

### Constructors

#### class DeepSleep()

Creates a DeepSleep object that will control the board's sleep features. For example;

```python

ds = DeepSleep()
```

### Methods

#### deepsleep.enable\_auto\_poweroff()

This method sets a critical battery voltage. For example, if the external power source \(e.g. LiPo Cell\) falls below `3.3V`, the Pycom device will turn off. This is intended to protect the hardware from undervoltage.

#### deepsleep.enable\_pullups(pins)

This method allows for pull-up pins to be enabled. For example, if an external trigger occurs, wake the Pycom device from Deep Sleep. `pins` may be passed into the method as a list, i.e. `['P17', 'P18']`.

#### deepsleep.disable\_pullups(pins)

This method allows for pull-up pins to be disabled. For example, if an external trigger occurs, wake the Pycom device from Deep Sleep. `pins` may be passed into the method as a list, i.e. `['P17', 'P18']`.

#### deepsleep.enable\_wake\_on\_raise(pins)

This method allows for pull-up pins to trigger on a rising voltage. For example, if an external rising voltage triggers occurs, wake the Pycom device from Deep Sleep. `pins` may be passed into the method as a list, i.e. `['P17', 'P18']`.

#### deepsleep.disable\_wake\_on\_raise(pins)

This method allows for disabling pull-up pins that trigger on a rising voltage. `pins` may be passed into the method as a list, i.e. `['P17', 'P18']`.

#### deepsleep.enable\_wake\_on\_fall(pins)

This method allows for pull-up pins to trigger on a falling voltage. For example, if an external falling voltage trigger occurs, the Pycom device is woken from Deep Sleep. `pins` may be passed into the method as a list, i.e. `['P17', 'P18']`.

#### deepsleep.disable\_wake\_on\_fall(pins)

This method can disable the pull-up pins that trigger on a falling voltage. `pins` may be passed into the method as a list, i.e. `['P17', 'P18']`.

#### deepsleep.get\_wake\_status()

This method returns the status of the pins at wakeup from Deep Sleep. The method returns a `dict` with the states of `wake`, `P10`, `P17`, `P18`.

#### deepsleep.set\_min\_voltage\_limit(value)

This method relates to the `enable_auto_poweroff` method and allows the user to specify the minimum power off voltage as a value.

#### deepsleep.go\_to\_sleep(seconds)

This method sends the board into Deep Sleep for a period of `seconds` or until an external interrupt has triggered \(see `set_pullups`\).

#### deepsleep.hw\_reset()

This method resets the PIC controller, resetting it to the state prior to the pins/min-voltage being set.

{% hint style="info" %}
Please note that we add more functionality weekly to these libraries. If a required feature is not available, feel free to contribute with a pull request at the [Pycom Libraries](https://github.com/pycom/pycom-libraries) GitHub repository.
{% endhint %}
