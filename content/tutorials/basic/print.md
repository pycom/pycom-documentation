---
title: "Print"
aliases:
    - tutorials/all/print.html
    - tutorials/all/print.md
    - chapter/tutorials/basic/print
---

Using the `print()` statements in your python script is quite easy. But did you know you can also concatinate strigns and variables inline? If you are formiliar with C, it's functionality is similar to the `printf()` function, but with `\n` always included. 

```python
import machine
print("hello world: " + str(machine.rng()) + " random number" )
```