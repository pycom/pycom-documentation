---
title: "MicroPython Examples"
aliases:
    - gettingstarted/programming/examples.html
    - gettingstarted/programming/examples.md
    - chapter/gettingstarted/programming/examples
---

To get you started with Python (MicroPython) syntax, we've provided you with a number of code examples.

## Variable Assignment

As with Python 3.5, variables can be assigned to and referenced. Below is an example of setting a variable equal to a string and then printing it to the console.

```python

variable = "Hello World"
print(variable)
```

## Conditional Statements

Conditional statements allow control over which elements of code run depending on specific cases. The example below shows how a temperature sensor might be implemented in code.

```python

temperature = 15
target = 10
if temperature > target:
    print("Too High!")
elif temperature < target:
    print("Too Low!")
else:
    print("Just right!")
```

## Loops (For & While loop)

Loops are another important feature of any programming language. This allows you to cycle your code and repeat functions/assignments/etc.

`for` loops allow you to control how many times a block of code runs for within a range.

```python

x = 0
for y in range(0, 9):
    x += 1
print(x)
```

`while` loops are similar to `for` loops, however they allow you to run a loop until a specific conditional is `true/false`. In this case, the loop checks if `x` is less than `9` each time the loop passes.

```python

x = 0
while x < 9:
    x += 1
print(x)
```

## Functions

Functions are blocks of code that are referred to by name. Data can be passed into it to be operated on (i.e. the parameters) and can optionally return data (the return value). All data that is passed to a function is explicitly passed.

The function below takes two numbers and adds them together, outputting the result.

```python

def add(number1, number2):
    return number1 + number2

add(1, 2) # expect a result of 3
```

The next function takes an input name and returns a string containing a welcome phrase.

```python

def welcome(name):
    welcome_phrase = "Hello, " + name + "!"
    print(welcome_phrase)

welcome("Alex") # expect "Hello, Alex!"
```

## Data Structures

Python has a number of different data structures for storing and manipulating variables. The main difference (regarding data structures) between C and Python is that Python manages memory for you. This means there's no need to declare the sizes of lists, dictionaries, strings, etc.

### Lists

A data structure that holds an ordered collection (sequence) of items.

```python

networks = ['lora', 'sigfox', 'wifi', 'bluetooth', 'lte-m']
print(networks[2]) # expect 'wifi'
```

### Dictionaries

A dictionary is like an address-book where you can find the address or contact details of a person by knowing only his/her name, i.e. keys (names) are associate with values (details).

```python

address_book = {'Alex':'2604 Crosswind Drive','Joe':'1301 Hillview Drive','Chris':'3236 Goldleaf Lane'}
print(address_book['Alex']) # expect '2604 Crosswind Drive'
```

### Tuple

Similar to lists but are immutable, i.e. you cannot modify tuples after instantiation.

```python

pycom_devices = ('wipy', 'lopy', 'sipy', 'gpy', 'fipy')
print(pycom_devices[0]) # expect 'wipy'
```

{{% hint style="info" %}}
For more Python examples, check out these [tutorials](https://www.tutorialspoint.com/python3/). Be aware of the implementation differences between MicroPython and Python 3.5.
{{< /hint >}}

