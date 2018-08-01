# uhashlib – Hashing Algorithm
This module implements binary data hashing algorithms. MD5 and SHA are supported. By limitations in the hardware, only one active hashing operation is supported at a time.

### Constructors
#####<class><i>class</i> uhashlib.md5([data])</class>

Create a MD5 hasher object and optionally feed data into it.

#####<class><i>class</i> uhashlib.sha1([data])</class>

Create a SHA-1 hasher object and optionally feed data into it.

#####<class><i>class</i> uhashlib.sha224([data])</class>

Create a SHA-224 hasher object and optionally feed data into it.

#####<class><i>class</i> uhashlib.sha256([data])</class>

Create a SHA-256 hasher object and optionally feed data into it.

#####<class><i>class</i> uhashlib.sha384([data])</class>

Create a SHA-384 hasher object and optionally feed data into it.

#####<class><i>class</i> uhashlib.sha512([data])</class>

Create a SHA-512 hasher object and optionally feed data into it.

### Methods
#####<function>hash.update(data)</function>

Feed more binary data into hash.

#####<function>hash.digest()</function>

Return hash for all data passed through hash, as a bytes object. After this method is called, more data cannot be fed into hash any longer.

#####<function>hash.hexdigest()</function>

This method is NOT implemented. Use `ubinascii.hexlify(hash.digest())` to achieve a similar effect.
