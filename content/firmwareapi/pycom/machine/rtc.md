---
title: "RTC"
aliases:
    - firmwareapi/pycom/machine/rtc.html
    - firmwareapi/pycom/machine/rtc.md
    - chapter/firmwareapi/pycom/machine/rtc
---

The RTC is used to keep track of the date and time.

## Quick Usage Example

```python

from machine import RTC

rtc = RTC()
rtc.init((2014, 5, 1, 4, 13, 0, 0, 0))
print(rtc.now())
```

## Constructors

### class machine.RTC([id=0, ...])

Create an RTC object. See init for parameters of initialisation.

```python
# id of the RTC may be set if multiple are connected. Defaults to id = 0.
rtc = RTC(id=0)
```

## Methods

### rtc.init([datetime=None, source=RTC.INTERNAL_RC])

Initialise the RTC. The arguments are:

* `datetime` when passed it sets the current time. It is a tuple of the form: `(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])`
* `source` selects the oscillator that drives the RTC. The options are 
    * `RTC.INTERNAL_RC`: Internal RC resonator
    * `RTC.XTAL_32KHZ`: External 32KHz crystal

For example:

```python
# for 2nd of February 2017 at 10:30am (TZ 0)
rtc.init((2017, 2, 28, 10, 30, 0, 0, 0))
```

> `tzinfo` is ignored by this method. Use `time.timezone` to achieve similar results.

### rtc.ntp_sync(server, [update_period=3600, backup_server])

Inits the RTC and sets up up automatic fetch and update the time using NTP (SNTP).

* `server` is the URL of the NTP server. Can be set to `None` to disable the periodic updates.
* `update_period` is the number of seconds between updates. Shortest period is 15 seconds.
* `backup_server` is the URL of the backup NTP server. Can be set to `None` to disable the periodic updates.

Can be used like:

```python
rtc.ntp_sync("pool.ntp.org") # this is an example. You can select a more specific server according to your geographical location
```


### rtc.now()

Get get the current `datetime` tuple as `(year, month, day, hour, minute, second, usecond, None)`


### rtc.synced()

Returns `True` if the last `ntp_sync` has been completed, `False` otherwise.

### rtc.memory([data])

Reads RTC memory contents or write data in passed Buffer in to RTC memory. The buffer has space to store 2048 bytes.

Example:

```python
rtc = RTC()
rtc.memory(b'10101010') # writes data in RTC memory
rtc.memory()
```

Output:

```python
b'10101010'
```

## Constants

* Clock source: `RTC.INTERNAL_RC`, `RTC.XTAL_32KHZ`

