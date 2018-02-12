# ustruct – Pack and Unpack Primitive Data Types
See Python [struct](https://docs.python.org/3/library/struct.html) for more information.

Supported size/byte order prefixes: ``@``, ``<``, ``>``, ``!``.

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``, ``L``, ``q``, ``Q``, ``s``, ``P``, ``f``, ``d`` (the latter 2 depending on the floating-point support).

### Functions

#####<function>ustruct.calcsize(fmt)</function>

Return the number of bytes needed to store the given fmt.

#####<function>ustruct.pack(fmt, v1, v2, ...)</function>

Pack the values v1, v2, ... according to the format string fmt. The return value is a bytes object encoding the values.

#####<function>ustruct.pack_into(fmt, buffer, offset, v1, v2, ...)</function>

Pack the values v1, v2, ... according to the format string fmt into a buffer starting at offset. offset may be negative to count from the end of buffer.

#####<function>ustruct.unpack(fmt, data)</function>

Unpack from the data according to the format string fmt. The return value is a tuple of the unpacked values.

#####<function>ustruct.unpack_from(fmt, data, offset=0)</function>

Unpack from the data starting at offset according to the format string fmt. offset may be negative to count from the end of buffer. The return value is a tuple of the unpacked values.
