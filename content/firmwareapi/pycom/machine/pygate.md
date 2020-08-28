---
title: "Pygate"
aliases:
    - firmwareapi/pycom/machine/pygate.html
    - firmwareapi/pycom/machine/pygate.md
    - chapter/firmwareapi/pycom/machine/pygate
---

The Pygate is an 8-channel LoRaWAN gateway. Connect a WiPy, Gpy or LoPy4 board to the Pygate and flash the Pygate firmware. See the [Pygate tutorial](/tutorials/all/pygate) to get started.

## Methods

### machine.pygate_init(config)

This function is used to initialize the Pygate

- `config`: the data contents of the gateway global config json file

### machine.pygate_deinit()

This shuts down the concentrator.

### machine.pygate_reset()

Resets the Pygate and inserted development module (including the LTE modem, if present). This actually power cycles the Pygate and the attached hardware and is **not** similar to `machine.reset()`.

### machine.callback(trigger, [handler=None, arg=None])

- `trigger`: A trigger event(s) for invoking the callback function `handler`, the triggers/events are:

	`machine.PYGATE_START_EVT`

	`machine.PYGATE_STOP_EVT`

	`machine.MP_QSTR_PYGATE_ERROR_EVT`

- `handler`: The callback function to be called.  When not passed to function, any pre-registered callback will be disabled/removed.

- `arg`: Optional argument to be passed to the callback function.

### machine.events()

Get the Pygate events