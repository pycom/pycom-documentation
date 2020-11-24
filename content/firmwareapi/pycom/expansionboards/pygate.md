---
title: "Pygate"
aliases:
    - firmwareapi/pycom/machine/pygate.html
    - firmwareapi/pycom/machine/pygate.md
    - chapter/firmwareapi/pycom/machine/pygate
---

The Pygate is an 8-channel LoRaWAN gateway. Connect a WiPy, Gpy or LoPy4 board to the Pygate and flash the Pygate firmware. See the [Pygate tutorial](/tutorials/expansionboards/pygate) to get started. 

>Note: Make sure to update the firmware of the device to the `pygate` version in order to access the functions below.

## Methods

### machine.pygate_init(buff)

This function is used to initialize the Pygate

- `buff`: the data contents of the gateway global config json file

### machine.pygate_deinit()

This shuts down the concentrator.

### machine.callback(trigger, handler=None, arg=None)

- `trigger`: A trigger event(s) for invoking the callback function `handler`, the triggers/events are:

	`machine.PYGATE_START_EVT`

	`machine.PYGATE_STOP_EVT`

	`machine.MP_QSTR_PYGATE_ERROR_EVT`

- `handler`: The callback function to be called.  When not passed to function, any pre-registered callback will be disabled/removed.

- `arg`: Optional argument to be passed to the callback function.

### machine.events()

Get the Pygate events

### machine.pygate_reset()

Hard-reset (power cycle) the Pygate and development module inserted

