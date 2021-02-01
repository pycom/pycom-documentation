---
title: "LTE power consumption"
aliases:
    - tutorials/lte/power.html
    - tutorials/lte/power.md
    - chapter/tutorials/power
---

There are some trade offs one can do to reduce power consumption of the LTE modem. You can limit connectivity in exchange for saving power consumption.

Let's start with the simplest choice: Turn off or not. It's not very sophisticated, but for completeness, let's start with this:


## Turn LTE modem off

```python

from network import LTE
import time
import socket
import machine
import pycom

def attach():
    start = time.time()
    if lte.isattached():
        print("already attached")
    else:
        print("attach")
        lte.attach(band=20, apn="the.apn.to.be.used.with.your.simcard")
        while not lte.isattached():
            time.sleep(1)
    print("attached after", time.time() - start, "seconds")
    print(lte.psm())

def connect():
    print("connect")
    start = time.time()
    lte.connect()
    while not lte.isconnected():
        time.sleep(0.5)
    print("connected after", time.time() - start, "seconds")

def http_get(url = 'http://detectportal.firefox.com/'):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    s.close()

# main
lte = LTE()
attach()
connect()
http_get()
print("deinit")
lte.deinit()
print("deepsleep")
machine.deepsleep(55 * 60 * 1000) # 55m
```

The example above is the simple case where we attach, connect, communicate and then turn the LTE modem off: `lte.deinit()`. This will make sure the LTE modem uses minimal power after the deinit. However, it means that the subsequent attach procedure after waking up will take some seconds. During this attach time the modem already consumes power.

## Leave LTE modem on

Depending on your use case, you may want to save the time (and energy) for reattching that you get after [turning the modem off](#turn-lte-modem-off).
If your device communicates a lot, then you can choose to not turn it off at all, save the time for the reattach. However, you then trade the higher power consumption during any idle time. For this, simply remove the deinit from the example:


```python
# lte.deinit()
```

## Power Saving Mode

A more sophisticated configuration, is the _Power Saving Mode_. PSM allows you to configure the period how often the device will connect and how long it will stay actively connected. During the sleep
- the LTE modem will go into a low power state, but
- it will stay attached to the network, thus no time is spent for `attach()` after waking up.

Note that the network needs to cooperate in this, so first there is a negotiation where you propose timers. Then you attach and the network will decide which timers to actually apply. Afterwards you can query the effective values.

So you see, here you not only need to make the trade off what is best for your application, but you will also need to do some testing to see which values your provider offers you and how this works out in your application in practise.

For the following example, assume you want to wake up once per hour, connect and do some processing, then go to deepsleep for 55 minutes. We would adjust the main part of the example as follows:

```python
# main
# period 1h, active 10s
lte = LTE(psm_period_value=1, psm_period_unit=LTE.PSM_PERIOD_1H,
          psm_active_value=5, psm_active_unit=LTE.PSM_ACTIVE_2S )
print(lte.psm())
attach()
connect()
http_get()
print("deinit")
lte.deinit(detach=False, reset=False)
print("deepsleep")
machine.deepsleep(55 * 60 * 1000) # 55m
```
