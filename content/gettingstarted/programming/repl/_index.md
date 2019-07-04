---
title: "REPL"
aliases:
---

REPL stands for Read Evaluate Print Loop, and is the name given to the interactive MicroPython prompt that is accessible on the Pycom devices. Using the REPL is by far the easiest way to test out Python code and run commands. You can use the REPL in addition to writing scripts in `main.py`.

The following pages will explain how to use the REPL with both Serial USB and Telnet connections.

The REPL includes the following features:

* Input history: use arrow up and arrow down to scroll through the history
* Tab completion: press tab to auto-complete variables or module names
* Halt any executing code: with `Ctrl-C`
* Copy/paste code or output: `Ctrl-C` and `Ctrl-V`

{{% hint style="info" %}}
There are a number of useful shortcuts for interacting with the MicroPython REPL. See below for the key combinations;

* `Ctrl-A` on a blank line will enter raw REPL mode. This is similar to permanent paste mode, except that characters are not echoed back.
* `Ctrl-B` on a blank like goes to normal REPL mode.
* `Ctrl-C` cancels any input, or interrupts the currently running code.
* `Ctrl-D` on a blank line will do a soft reset.
* `Ctrl-E` enters ‘paste mode' that allows you to copy and paste chunks of text. Exit this mode using `Ctrl-D`.
* `Ctrl-F` performs a "safe-boot" of the device that prevents `boot.py` and `main.py` from executing
{{< /hint >}}

