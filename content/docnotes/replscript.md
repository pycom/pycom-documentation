---
title: "REPL vs Scripts"
aliases:
    - docnotes/replscript.html
    - docnotes/replscript.md
    - chapter/docnotes/replscript
---

Users of this documentation should be aware that examples given in the docs are under the expectation that they are being executed using the MicroPython REPL. This means that when certain functions are called, their output may not necessarily be printed to the console if they are run from a script. When using the REPL many classes/functions automatically produce a printed output displaying the return value of the function to the console. The code snippet below demonstrates some examples of classes/functions that might display this behaviour.

## Basic Arithmetic

```python


1 + 1 # REPL will print out '2' to console
1 + 1 # Script will not return anything the console
print(1 + 1) # Both the REPL and a script will return '2' to the console
```

## Calling Methods

```python
import ubinascii

ubinascii.hexlify(b'12345') # REPL will print out "b'3132333435'" to the console
ubinascii.hexlify(b'12345') # Script will not return any the console
```

In order to use these functions that do not print out any values, you will need to either wrap them in a `print()` statement or assign them to variables and call them later when you wish to use them.

For example:

```python
# immediately print to console when using a script
print(1 + 1)
# or save variable to for later
value = 1 + 1
# do something here...
print(value)
```
