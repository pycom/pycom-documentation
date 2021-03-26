---
title: "uzlib"
aliases:
    - firmwareapi/micropython/uzlib.html
    - firmwareapi/micropython/uzlib.md
    - chapter/firmwareapi/micropython/uzlib
---
_This module implements a subset of the corresponding_ `CPython` _module, as described below. For more information, refer to the original CPython documentation:_ `zlib`.

This module allows to decompress binary data compressed with [DEFLATE algorithm](https://en.wikipedia.org/wiki/DEFLATE) (commonly used in zlib library and gzip archiver). Compression is not yet implemented.

## Methods

### uzlib.decompress(data, wbits=0, bufsize=0)

Return decompressed data as bytes. wbits is DEFLATE dictionary window size used during compression (8-15, the dictionary size is power of 2 of that value). Additionally, if value is positive, data is assumed to be zlib stream (with zlib header). Otherwise, if it's negative, it's assumed to be raw DEFLATE stream. bufsize parameter is for compatibility with CPython and is ignored.

### class uzlib.DecompIO(stream, wbits=0)

Create a `stream` wrapper which allows transparent decompression of compressed data in another stream. This allows to process compressed streams with data larger than available heap size. In addition to values described in `decompress()`, wbits may take values 24..31 (16 + 8..15), meaning that input stream has gzip header.

## Usage

You can use this example to decompress uploaded archive files, compressed using [gzip](https://www.gzip.org/). This tool is installed by default on macOS and Linux. Note that gzip compression is _different_ from `.zip`. 

In this example, we will compress a file `test.txt` using gzip in the termial: `gzip test.txt`, with the content:
```
Hello world

```
This will create a the file `test.txt.gz`. Now include this file in your project, and allow Pymakr to upload `.gz` files (Settings --> Global settings --> Upload file types, add `.gz` in the list). In `main.py`, paste the following:
```python
import uzlib

file = open('test.txt.gz', 'r')
data = uzlib.decompress(file, 31) #31 is the default gzip header size
#now print the first line of the file
print(data.readline())
```

Next to reading files and decompressing them, it is also possible to compressed `gzip` data through a socket stream and decompress. This is a common way to reduce the amount of data transferred for metered connections. 