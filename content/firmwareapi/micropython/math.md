---
title: "math"
aliases:
    - firmwareapi/micropython/math.html
    - firmwareapi/micropython/math.md
    - chapter/firmwareapi/micropython/math
---

The math module provides some basic mathematical functions for working with floating-point numbers. Floating point support required for this module.

## Methods

#### math.acos(x)

Return the inverse cosine of `x`.

#### math.acosh(x)

Return the inverse hyperbolic cosine of `x`.

#### math.asin(x)

Return the inverse sine of `x`.

#### math.asinh(x)

Return the inverse hyperbolic sine of `x`.

#### math.atan(x)

Return the inverse tangent of `x`.

#### math.atan2(y, x)

Return the principal value of the inverse tangent of `y/x`.

#### math.atanh(x)

Return the inverse hyperbolic tangent of `x`.

#### math.ceil(x)

Return an integer, being x rounded towards positive infinity.

#### math.copysign(x, y)

Return x with the sign of `y`.

#### math.cos(x)

Return the cosine of `x`.

#### math.cosh(x)

Return the hyperbolic cosine of `x`.

#### math.degrees(x)

Return radians `x` converted to degrees.

#### math.erf(x)

Return the error function of `x`.

#### math.erfc(x)

Return the complementary error function of `x`.

#### math.exp(x)

Return the exponential of `x`.

#### math.expm1(x)

Return `exp(x) - 1`.

#### math.fabs(x)

Return the absolute value of `x`.

#### math.floor(x)

Return an integer, being `x` rounded towards negative infinity.

#### math.fmod(x, y)

Return the remainder of `x/y`.

#### math.frexp(x)

Decomposes a floating-point number into its mantissa and exponent. The returned value is the tuple `(m, e)` such that `x == m * 2**e` exactly. If `x == 0` then the function returns `(0.0, 0)`, otherwise the relation `0.5 <= abs(m) < 1` holds.

#### math.gamma(x)

Return the gamma function of `x`.

#### math.isfinite(x)

Return `True` if `x` is finite.

#### math.isinf(x)

Return `True` if `x` is infinite.

#### math.isnan(x)

Return `True` if `x` is not-a-number

#### math.ldexp(x, exp)

Return `x * (2**exp)`.

#### math.lgamma(x)

Return the natural logarithm of the gamma function of `x`.

#### math.log(x)

Return the natural logarithm of `x`.

#### math.log10(x)

Return the base-10 logarithm of `x`.

#### math.log2(x)

Return the base-2 logarithm of `x`.

#### math.modf(x)

Return a tuple of two floats, being the fractional and integral parts of `x`. Both return values have the same sign as `x`.

#### math.pow(x, y)

Returns `x` to the power of `y`.

#### math.radians(x)

Return degrees `x` converted to radians.

#### math.sin(x)

Return the sine of `x`.

#### math.sinh(x)

Return the hyperbolic sine of `x`.

#### math.sqrt(x)

Return the square root of `x`.

#### math.tan(x)

Return the tangent of `x`.

#### math.tanh(x)

Return the hyperbolic tangent of `x`.

#### math.trunc(x)

Return an integer, being `x` rounded towards `0`.

## Constants

* `math.e`: Base of the natural logarithm
* `math.pi`: The ratio of a circle's circumference to its diameter

