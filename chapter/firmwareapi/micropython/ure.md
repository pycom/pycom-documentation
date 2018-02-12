# ure – regular expressions
This module implements regular expression operations. Regular expression syntax supported is a subset of CPython re module (and actually is a subset of POSIX extended regular expressions).

Supported operators are:

``.``
Match any character.
``[]``
Match set of characters. Individual characters and ranges are supported.
``^``

``$``

``?``

``*``

``+``

``??``

``*?``

``+?``

Counted repetitions ({m,n}), more advanced assertions, named groups, etc. are not supported.

### Functions

#####<function>ure.compile(regex)</function>

Compile regular expression, return ``regex object``.

#####<function>ure.match(regex, string)</function>

Match regex against string. Match always happens from starting position in a string.

#####<function>ure.search(regex, string)</function>

Search regex in a string. Unlike match, this will search string for first position which matches regex (which still may be 0 if regex is anchored).

#####<function>ure.DEBUG</function>

Flag value, display debug information about compiled expression.

### Regex objects
Compiled regular expression. Instances of this class are created using ure.compile().

#####<function>regex.match(string)</function>

#####<function>regex.search(string)</function>

#####<function>regex.split(string, max_split=-1)</function>

### Match objects
Match objects as returned by match() and search() methods.

#####<function>match.group([index])</function>

Only numeric groups are supported.
