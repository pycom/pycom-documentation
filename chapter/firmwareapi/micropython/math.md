# math – Mathematical Functions

The math module provides some basic mathematical functions for working with floating-point numbers. Floating point support required for this module.

### Functions

#####<function>math.acos(x)</function>

Return the inverse cosine of `x`.

#####<function>math.acosh(x)</function>

Return the inverse hyperbolic cosine of `x`.

#####<function>math.asin(x)</function>

Return the inverse sine of `x`.

#####<function>math.asinh(x)</function>

Return the inverse hyperbolic sine of `x`.

#####<function>math.atan(x)</function>

Return the inverse tangent of `x`.

#####<function>math.atan2(y, x)</function>

Return the principal value of the inverse tangent of `y/x`.

#####<function>math.atanh(x)</function>

Return the inverse hyperbolic tangent of `x`.

#####<function>math.ceil(x)</function>

Return an integer, being x rounded towards positive infinity.

#####<function>math.copysign(x, y)</function>

Return x with the sign of `y`.

#####<function>math.cos(x)</function>

Return the cosine of `x`.

#####<function>math.cosh(x)</function>

Return the hyperbolic cosine of `x`.

#####<function>math.degrees(x)</function>

Return radians `x` converted to degrees.

#####<function>math.erf(x)</function>

Return the error function of `x`.

#####<function>math.erfc(x)</function>

Return the complementary error function of `x`.

#####<function>math.exp(x)</function>

Return the exponential of `x`.

#####<function>math.expm1(x)</function>

Return `exp(x) - 1`.

#####<function>math.fabs(x)</function>

Return the absolute value of `x`.

#####<function>math.floor(x)</function>

Return an integer, being `x` rounded towards negative infinity.

#####<function>math.fmod(x, y)</function>

Return the remainder of `x/y`.

#####<function>math.frexp(x)</function>

Decomposes a floating-point number into its mantissa and exponent. The returned value is the tuple `(m, e)` such that `x == m * 2**e` exactly. If `x == 0` then the function returns `(0.0, 0)`, otherwise the relation `0.5 <= abs(m) < 1` holds.

#####<function>math.gamma(x)</function>

Return the gamma function of `x`.

#####<function>math.isfinite(x)</function>

Return `True` if `x` is finite.

#####<function>math.isinf(x)</function>

Return `True` if `x` is infinite.

#####<function>math.isnan(x)</function>

Return `True` if `x` is not-a-number

#####<function>math.ldexp(x, exp)</function>

Return `x * (2**exp)`.

#####<function>math.lgamma(x)</function>

Return the natural logarithm of the gamma function of `x`.

#####<function>math.log(x)</function>

Return the natural logarithm of `x`.

#####<function>math.log10(x)</function>

Return the base-10 logarithm of `x`.

#####<function>math.log2(x)</function>

Return the base-2 logarithm of `x`.

#####<function>math.modf(x)</function>

Return a tuple of two floats, being the fractional and integral parts of `x`. Both return values have the same sign as `x`.

#####<function>math.pow(x, y)</function>

Returns `x` to the power of `y`.

#####<function>math.radians(x)</function>

Return degrees `x` converted to radians.

#####<function>math.sin(x)</function>

Return the sine of `x`.

#####<function>math.sinh(x)</function>

Return the hyperbolic sine of `x`.

#####<function>math.sqrt(x)</function>

Return the square root of `x`.

#####<function>math.tan(x)</function>

Return the tangent of `x`.

#####<function>math.tanh(x)</function>

Return the hyperbolic tangent of `x`.

#####<function>math.trunc(x)</function>

Return an integer, being `x` rounded towards `0`.

### Constants
<constant>math.e</constant>

Base of the natural logarithm

<constant>math.pi</constant>

The ratio of a circle’s circumference to its diameter
