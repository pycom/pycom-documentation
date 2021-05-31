---
title: "REPL"
aliases:
    - tutorials/all/repl.html
    - tutorials/all/repl.md
    - chapter/tutorials/all/repl
---

Using the Pymakr Plugin, open and connect a device or use serial terminal (PuTTY, screen, picocom, etc). Upon connecting, there should be a blank screen with a flashing cursor. Press Enter and a MicroPython prompt should appear, i.e. `>>>`. Let's make sure it is working with the obligatory test:

```python
>>> print("Hello LoPy!")
Hello LoPy!
```

In the example above, the `>>>` characters should not be typed. They are there to indicate that the text should be placed after the prompt. Once the text has been entered `print("Hello LoPy!")` and pressed `Enter`, the output should appear on screen, identical to the example above.

Basic Python commands can be tested out in a similar fashion.

If this is not working, try either a hard reset or a soft reset; see below.

Here are some other example, utilising the device's hardware features:

```python
>>> from machine import Pin
>>> led = Pin('G16', mode=Pin.OUT, value=1)
>>> led(0)
>>> led(1)
>>> led.toggle()
>>> 1 + 2
3
>>> 5 / 2
2.5
>>> 20 * 'py'
'pypypypypypypypypypypypypypypypypypypypy'
```

## Resetting the Device

If something goes wrong, the device can be reset with two methods. The first is to press `CTRL-D` at the MicroPython prompt, which will perform a soft reset. A message, as following, will appear:

```python
>>>
PYB: soft reboot
MicroPython v1.4.6-146-g1d8b5e5 on 2016-10-21; LoPy with ESP32
Type "help()" for more information.
>>>
```

If that still isn't working a hard reset can be performed (power-off/on) by pressing the `RST` switch (the small black button next to the RGB LED). Using telnet, this will end the session, disconnecting the program that was used to connect to the Pycom Device.

