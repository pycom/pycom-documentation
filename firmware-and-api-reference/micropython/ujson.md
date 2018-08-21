# ujson

This modules allows to convert between Python objects and the JSON data format.

## Methods

#### ujson.dumps\(obj\)

Return `obj` represented as a JSON string.

#### ujson.loads\(str\)

Parse the JSON `str` and return an object. Raises `ValueError` if the string is not correctly formed.

#### ujson.load\(fp\)

Parse contents of `fp` \(a `.read()`-supporting file-like object containing a JSON document\). Raises `ValueError` if the content is not correctly formed.

