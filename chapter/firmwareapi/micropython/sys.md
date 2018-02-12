# sys – System Specific Functions

### Functions

#####<function>sys.exit(retval=0)</function>

Terminate current program with a given exit code. Underlyingly, this function raise as SystemExit exception. If an argument is given, its value given as an argument to SystemExit.

#####<function>sys.print_exception(exc, file=sys.stdout)</function>

Print exception with a traceback to a file-like object file (or sys.stdout by default).

{% hint style='info' %}
Difference to CPython

This is simplified version of a function which appears in the traceback module in CPython. Unlike traceback.print_exception(), this function takes just exception value instead of exception type, exception value, and traceback object; file argument should be positional; further arguments are not supported. CPython-compatible traceback module can be found in micropython-lib.
{% endhint %}

### Constants
<constant>sys.argv</constant>

A mutable list of arguments the current program was started with.

<constant>sys.byteorder</constant>

The byte order of the system (“little” or “big”).

<constant>sys.implementation</constant>

Object with information about the current Python implementation. For MicroPython, it has following attributes:

- *name* - string “micropython”
- *version* - tuple (major, minor, micro), e.g. (1, 7, 0)
This object is the recommended way to distinguish MicroPython from other Python implementations (note that it still may not exist in the very minimal ports).

{% hint style='info' %}
Difference to CPython

CPython mandates more attributes for this object, but the actual useful bare minimum is implemented in MicroPython.
{% endhint %}

<constant>sys.maxsize</constant>

Maximum value which a native integer type can hold on the current platform, or maximum value representable by MicroPython integer type, if it’s smaller than platform max value (that is the case for MicroPython ports without long int support).

This attribute is useful for detecting “bitness” of a platform (32-bit vs 64-bit, etc.). It’s recommended to not compare this attribute to some value directly, but instead count number of bits in it:

```python
bits = 0
v = sys.maxsize
while v:
    bits += 1
    v >>= 1
if bits > 32:
    # 64-bit (or more) platform
else:
    # 32-bit (or less) platform
    # Note that on 32-bit platform, value of bits may be less than 32
    # (e.g. 31) due to peculiarities described above, so use "> 16",
    # "> 32", "> 64" style of comparisons.
```

<constant>sys.modules</constant>

Dictionary of loaded modules. On some ports, it may not include builtin modules.

<constant>sys.path</constant>

A mutable list of directories to search for imported modules.

<constant>sys.platform</constant>

The platform that MicroPython is running on. For OS/RTOS ports, this is usually an identifier of the OS, e.g. ``linux``. For baremetal ports it is an identifier of a board, e.g. ``pyboard`` for the original MicroPython reference board. It thus can be used to distinguish one board from another. If you need to check whether your program runs on MicroPython (vs other Python implementation), use ``sys.implementation`` instead.

<constant>sys.stderr</constant>

Standard error stream.

<constant>sys.stdin</constant>

Standard input stream.

<constant>sys.stdout</constant>

Standard output stream.

<constant>sys.version</constant>

Python language version that this implementation conforms to, as a string.

<constant>sys.version_info</constant>

Python language version that this implementation conforms to, as a tuple of ints.
