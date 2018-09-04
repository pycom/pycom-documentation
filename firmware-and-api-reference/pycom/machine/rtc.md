# RTC

The RTC is used to keep track of the date and time.

## Quick Usage Example

```python
from machine import RTC

rtc = RTC()
rtc.init((2014, 5, 1, 4, 13, 0, 0, 0))
print(rtc.now())
```

## Constructors

#### class machine.RTC\(id=0, ...\)

Create an RTC object. See init for parameters of initialisation.

```python
# id of the RTC may be set if multiple are connected. Defaults to id = 0.
rtc = RTC(id=0)
```

## Methods

#### rtc.init\(datetime=None, source=RTC.INTERNAL\_RC\)

Initialise the RTC. The arguments are:

* `datetime` when passed it sets the current time. It is a tuple of the form: `(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])`
* `source` selects the oscillator that drives the RTC. The options are RTC.INTERNAL\_RC and RTC.XTAL\_32KHZ

For example:

```python
# for 2nd of February 2017 at 10:30am (TZ 0)
rtc.init((2017, 2, 28, 10, 30, 0, 0, 0))
```

{% hint style="info" %}
`tzinfo` is ignored by this method. Use `time.timezone` to achieve similar results.
{% endhint %}

#### rtc.now\(\)

Get get the current `datetime` tuple:

```python
# returns datetime tuple
rtc.now()
```

#### rtc.ntp\_sync\(server, \* , update\_period=3600\)

Set up automatic fetch and update the time using NTP \(SNTP\).

* `server` is the URL of the NTP server. Can be set to `None` to disable the periodic updates.
* `update_period` is the number of seconds between updates. Shortest period is 15 seconds.

Can be used like:

```python
rtc.ntp_sync("pool.ntp.org") # this is an example. You can select a more specific server according to your geographical location
```

#### rtc.synced\(\)

Returns `True` if the last `ntp_sync` has been completed, `False` otherwise:

```python
rtc.synced()
```

## Constants

* Clock source: `RTC.INTERNAL_RC`, `RTC.XTAL_32KHZ`

