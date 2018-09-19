# uhashlib

This module implements binary data hashing algorithms. MD5 and SHA are supported. By limitations in the hardware, only one active hashing operation is supported at a time.

## Constructors

#### class uhashlib.md5\(\[data\]\)

Create a MD5 hasher object and optionally feed data into it.

#### class uhashlib.sha1\(\[data\]\)

Create a SHA-1 hasher object and optionally feed data into it.

#### class uhashlib.sha224\(\[data\]\)

Create a SHA-224 hasher object and optionally feed data into it.

#### class uhashlib.sha256\(\[data\]\)

Create a SHA-256 hasher object and optionally feed data into it.

#### class uhashlib.sha384\(\[data\]\)

Create a SHA-384 hasher object and optionally feed data into it.

#### class uhashlib.sha512\(\[data\]\)

Create a SHA-512 hasher object and optionally feed data into it.

## Methods

#### hash.update\(data\)

Feed more binary data into hash.

#### hash.digest\(\)

Return hash for all data passed through hash, as a bytes object. After this method is called, more data cannot be fed into hash any longer.

#### hash.hexdigest\(\)

This method is NOT implemented. Use `ubinascii.hexlify(hash.digest())` to achieve a similar effect.

