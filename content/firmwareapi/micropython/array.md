---
title: "array"
aliases:
    - firmwareapi/micropython/array.html
    - firmwareapi/micropython/array.md
    - chapter/firmwareapi/micropython/array
---

See [Python array](https://docs.python.org/3/library/array.html) for more information.



## Classes

### class array.array(typecode, [iterable])

Create array with elements of given type. Initial contents of the array are given by an iterable. If it is not provided, an empty array is created. Supported format codes: 
* `b`: signed char, 1 byte
* `B`: unsigned char, 1 byte
* `h`: signed short, 2 bytes
* `H`: unsigned short, 2 bytes
* `i`: signed int, 2 bytes
* `I`: unsigned int, 2 bytes
* `l`: signed long, 4 bytes
* `L`: unsigned long, 4 bytes
* `q`: signed long long, 8 bytes
* `Q`: unsigned long long, 8 bytes
* `f`: foat, 4 bytes
* `d`: double, 8 bytes
Adapting the typecode to the array-type you want to create can save a lot of space on the microcontroller

## Methods

### array.append(val)

Append new element to the end of array, growing it.

### array.extend(iterable)

Append new elements as contained in an iterable to the end of array, growing it.

