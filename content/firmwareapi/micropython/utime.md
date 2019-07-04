---
title: "utime"
aliases:
    - firmwareapi/micropython/utime.html
    - firmwareapi/micropython/utime.md
    - chapter/firmwareapi/micropython/utime
---

The `utime` module provides functions for getting the current time and date, measuring time intervals, and for delays.

**Time Epoch**: Pycom's ESP32 port uses standard for POSIX systems epoch of `1970-01-01 00:00:00 UTC`.

## Maintaining actual calendar date/time

This requires a Real Time Clock (RTC). On systems with underlying OS (including some RTOS), an RTC may be implicit. Setting and maintaining actual calendar time is responsibility of OS/RTOS and is done outside of MicroPython, it just uses OS API to query date/time. On baremetal ports however system time depends on `machine.RTC()` object. The current calendar time may be set using `machine.RTC().datetime(tuple)` function, and maintained by following means:

* By a backup battery (which may be an additional, optional component for a particular board).
* Using networked time protocol (requires setup by a port/user).
* Set manually by a user on each power-up (many boards then maintain RTC time across hard resets, though some may require setting it again in such case).

If actual calendar time is not maintained with a system/MicroPython RTC, functions below which require reference to current absolute time may behave not as expected.

## Methods

#### utime.gmtime(\[secs\])

Convert a time expressed in seconds since the Epoch (see above) into an 8-tuple which contains: `(year, month, mday, hour, minute, second, weekday, yearday)` If `secs` is not provided or `None`, then the current time from the RTC is used.

* `year` includes the century (for example 2014).
* `month` is 1-12
* `mday` is 1-31
* `hour` is 0-23
* `minute` is 0-59
* `second` is 0-59
* `weekday` is 0-6 for Mon-Sun
* `yearday` is 1-366

#### utime.localtime(\[secs\])

Like `gmtime()` but converts to local time. If `secs` is not provided or `None`, the current time from the RTC is used.

#### utime.mktime()

This is inverse function of `localtime`. It's argument is a full 8-tuple which expresses a time as per `localtime`. It returns an integer which is the number of seconds since `Jan 1, 2000`.

#### utime.sleep(seconds)

Sleep for the given number of `seconds`. `seconds` can be a floating-point number to sleep for a fractional number of seconds. Note that other MicroPython ports may not accept floating-point argument, for compatibility with them use `sleep_ms()` and `sleep_us()` functions.

#### utime.sleep\_ms(ms)

Delay for given number of milliseconds, should be positive or 0.

#### utime.sleep\_us(us)

Delay for given number of microseconds, should be positive or 0

#### utime.ticks\_ms()

Returns uptime, in milliseconds.

#### utime.ticks\_us()

Just like `ticks_ms` above, but in microseconds.

#### utime.ticks\_cpu()

Same as `ticks_us`, but faster.

#### utime.ticks\_diff(old, new)

Measure period between consecutive calls to `ticks_ms()`, `ticks_us()`, or `ticks_cpu()`. The value returned by these functions may wrap around at any time, so directly subtracting them is not supported. `ticks_diff()` should be used instead. "old" value should actually precede "new" value in time, or result is undefined. This function should not be used to measure arbitrarily long periods of time (because `ticks_*()` functions wrap around and usually would have short period). The expected usage pattern is implementing event polling with timeout:

```python

# Wait for GPIO pin to be asserted, but at most 500us
start = time.ticks_us()
while pin.value() == 0:
    if time.ticks_diff(start, time.ticks_us()) > 500:
        raise TimeoutError
```

#### utime.time()

Returns the number of seconds, as an integer, since the Epoch, assuming that underlying RTC is set. If an RTC is not set, this function returns number of seconds since power up or reset). If you want to develop portable MicroPython application, you should not rely on this function to provide higher than second precision. If you need higher precision, use `ticks_ms()` and `ticks_us()` functions, if you need calendar time, `localtime()` without an argument is a better choice.

#### utime.timezone(\[secs\])

Set or get the timezone offset, in seconds. If `secs` is not provided, it returns the current value.

{{% hint style="info" %}}
In MicroPython, `time.timezone` works the opposite way to Python. In [Python](https://docs.python.org/3/library/time.html#time.timezone), to get the local time, you write `local_time = utc - timezone`, while in MicroPython it is `local_time = utc + timezone`.
{{< /hint >}}

