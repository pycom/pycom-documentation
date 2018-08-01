# ujson – JSON Encoding and Decoding
This modules allows to convert between Python objects and the JSON data format.

### Functions

#####<function>ujson.dumps(obj)</function>

Return `obj` represented as a JSON string.

#####<function>ujson.loads(str)</function>

Parse the JSON `str` and return an object. Raises `ValueError` if the string is not correctly formed.

#####<function>ujson.load(fp)</function>

Parse contents of `fp` (a `.read()`-supporting file-like object containing a JSON document). Raises `ValueError` if the content is not correctly formed.
