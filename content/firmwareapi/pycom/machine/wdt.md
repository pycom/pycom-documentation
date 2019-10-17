---
title: "WDT"
aliases:
    - firmwareapi/pycom/machine/wdt.html
    - firmwareapi/pycom/machine/wdt.md
    - chapter/firmwareapi/pycom/machine/wdt
---

The WDT is used to restart the system when the application crashes and ends up into a non recoverable state. After enabling, the application must "feed" the watchdog periodically to prevent it from expiring and resetting the system.

## Quick Usage Example

```python

from machine import WDT
wdt = WDT(timeout=2000)  # enable it with a timeout of 2 seconds
wdt.feed()
```

## Constructors

#### class machine.WDT(id=0, timeout)

Create a WDT object and start it. The `id` can only be `0`. See the init method for the parameters of initialisation.

## Methods

#### wdt.init(timeout)

Initialises the watchdog timer. The timeout must be given in milliseconds. Once it is running the WDT cannot be stopped but the timeout can be re-configured at any point in time.

#### wdt.feed()

Feed the WDT to prevent it from resetting the system. The application should place this call in a sensible place ensuring that the WDT is only fed after verifying that everything is functioning correctly.

