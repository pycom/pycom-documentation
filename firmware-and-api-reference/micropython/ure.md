# ure

This module implements regular expression operations. Regular expression syntax supported is a subset of CPython re module \(and actually is a subset of POSIX extended regular expressions\).

Supported operators are:

`.` Match any character. `[]` Match set of characters. Individual characters and ranges are supported.

```text
^
$
?
*
+
??
*?
+?
```

Counted repetitions `({m,n})`, more advanced assertions, named groups, etc. are not supported.

## Methods

#### ure.compile\(regex\)

Compile regular expression, return `regex object`.

#### ure.match\(regex, string\)

Match regex against `string`. Match always happens from starting position in a string.

#### ure.search\(regex, string\)

Search regex in a string. Unlike match, this will search string for first position which matches regex \(which still may be 0 if regex is anchored\).

#### ure.DEBUG

Flag value, display debug information about compiled expression.

## Regex objects

Compiled regular expression. Instances of this class are created using `ure.compile()`.

#### regex.match\(string\)

#### regex.search\(string\)

#### regex.split\(string, max\_split=-1\)

## Match objects

Match objects as returned by `match()` and `search()` methods.

#### match.group\(\[index\]\)

Only numeric groups are supported.

