# ubinascii – Binary/ASCII Conversions
This module implements conversions between binary data and various encodings of it in ASCII form (in both directions).

### Functions

<function>ubinascii.hexlify(data[, sep])</function>

Convert binary data to hexadecimal representation. Returns bytes string.

{% hint style='info' %}
Difference to CPython

If additional argument, sep is supplied, it is used as a separator between hexadecimal values.
{% endhint %}

<function>ubinascii.unhexlify(data)</function>

Convert hexadecimal data to binary representation. Returns bytes string. (i.e. inverse of hexlify)

<function>ubinascii.a2b_base64(data)</function>

Convert Base64-encoded data to binary representation. Returns bytes string.

<function>ubinascii.b2a_base64(data)</function>

Encode binary data in Base64 format. Returns string.
