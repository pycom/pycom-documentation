---
title: "Print"
aliases:
    - tutorials/all/print.html
    - tutorials/all/print.md
    - chapter/tutorials/basic/print
---

Using the `print()` statements in your python script is quite easy. But did you know you can also concatinate strigns and variables inline? If you are familiar with C, it's functionality is similar to the `printf()` function, but with `\n` always included. 

```python
import machine
print("hello world")
print("hello world.", end='') # do not end line
#you can also specify different endings, like additional text, tabs or any other escape characters
for i in range(0,9):
    print(".", end='')
print("\n") #feed a new line
print("\t tabbed in") 
#you can specify a variable into the string as well!
print("hello world: " + str(machine.rng()) + " random number" )
#or use format
print("hello world: {} {}".format(machine.rng(), " random number"))
```