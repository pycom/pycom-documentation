# array – Arrays of Numeric Data
See Python array for more information.

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``, ``L``, ``q``, ``Q``, ``f``, ``d`` (the latter 2 depending on the floating-point support).

### Classes
<class><i>class</i> array.array(typecode[, iterable])</class>

Create array with elements of given type. Initial contents of the array are given by an iterable. If it is not provided, an empty array is created.

<function>array.append(val)</function>

Append new element to the end of array, growing it.

<function>array.extend(iterable)</function>

Append new elements as contained in an iterable to the end of array, growing it.
