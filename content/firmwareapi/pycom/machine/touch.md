---
title: "Touch"
aliases:
    - firmwareapi/pycom/machine/touch.html
    - firmwareapi/pycom/machine/touch.md
    - chapter/firmwareapi/pycom/machine/touch
---

The Touch module allows for certain GPIO pins (`P2`,`P3`,`P4`,`P6`,`P8`,`P9`,`P10`,`P19`,`P20`) to accept touch inputs.

## Constructor

### class machine.touch(pin)

Create a touch object on pin.

Example:
```python
touch = Touch('P9')
touch.read()
```

## Methods

### touch.read()

Reads the value of the touch pin

### touch.config([sensitivity])

Set the threshold of the touchpad interrupt. Currently not used

### touch.init_value()

Currently not implemented
