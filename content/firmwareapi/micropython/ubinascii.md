---
title: "ubinascii"
aliases:
    - firmwareapi/micropython/ubinascii.html
    - firmwareapi/micropython/ubinascii.md
    - chapter/firmwareapi/micropython/ubinascii
---

This module implements conversions between binary data and various encodings of it in ASCII form (in both directions).

## Methods

#### ubinascii.hexlify(data\[, sep\])

Convert binary data to hexadecimal representation. Returns bytes string.

{{% hint style="info" %}}
**Difference to CPython**

If additional argument, `sep` is supplied, it is used as a separator between hexadecimal values.
{{< /hint >}}

#### ubinascii.unhexlify(data)

Convert hexadecimal data to binary representation. Returns bytes string. (i.e. inverse of `hexlify`)

#### ubinascii.a2b\_base64(data)

Convert Base64-encoded data to binary representation. Returns bytes string.

#### ubinascii.b2a\_base64(data)

Encode binary data in Base64 format. Returns string.

