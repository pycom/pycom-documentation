---
title: "uzlib"
aliases:
    - firmwareapi/micropython/uzlib.html
    - firmwareapi/micropython/uzlib.md
    - chapter/firmwareapi/micropython/uzlib
---
_This module implements a subset of the corresponding_ `CPython` _module, as described below. For more information, refer to the original CPython documentation:_ `zlib`.

This module allows to decompress binary data compressed with [DEFLATE algorithm](https://en.wikipedia.org/wiki/DEFLATE) (commonly used in zlib library and gzip archiver). Compression is not yet implemented.

## **Methods**

**uzlib.decompress(data, wbits=0, bufsize=0)**

Return decompressed data as bytes. wbits is DEFLATE dictionary window size used during compression (8-15, the dictionary size is power of 2 of that value). Additionally, if value is positive, data is assumed to be zlib stream (with zlib header). Otherwise, if it's negative, it's assumed to be raw DEFLATE stream. bufsize parameter is for compatibility with CPython and is ignored.

**class uzlib.DecompIO(stream, wbits=0)**

Create a `stream` wrapper which allows transparent decompression of compressed data in another stream. This allows to process compressed streams with data larger than available heap size. In addition to values described in `decompress()`, wbits may take values 24..31 (16 + 8..15), meaning that input stream has gzip header.

{{% hint style="info" %}}
**Difference to CPython**

This class is MicroPython extension. It's included on provisional basis and may be changed considerably or removed in later versions.
{{< /hint >}}
