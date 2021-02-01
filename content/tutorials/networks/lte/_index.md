---
title: "LTE Examples"
aliases:
    - chapter/tutorials/lte
---

The following tutorial demonstrates the use of the LTE CAT-M1 and NB-IoT functionality on cellular enabled Pycom modules.

> Before you start, make sure that your Simcard is registered and activated with your carrier.

When using the LTE network, **Always** connect the appropriate antenna to your device. See the figures below for the correct antenna placement.

|  Gpy | Fipy  |   
|---|---|
| ![](/gitbook/assets/lte_ant_gpy.png) | ![](/gitbook/assets/lte_ant_fipy.png)  |  


GPy and FiPy support both LTE CAT-M1 and NB-IoT. These are newer, low power, long range, cellular protocols. They are not the same as the full version of 2G/3G/LTE supported by cell phones, and require your local carriers to support them. At the time of writing, CAT-M1 and NB-IoT connectivity is not widely available so be sure to check with local carriers if support is available where you are. Together with the SIM card, the provider will supply you with configuration details: Usually band and APN. Use these in the example code below.

## Example

```python
from network import LTE
import time
import socket

lte = LTE()
lte.init()
#some carriers have special requirements, check print(lte.send_at_cmd("AT+SQNCTM=?")) to see if your carrier is listed.
#when using verizon, use
#lte.init(carrier=verizon)
#when usint AT&T use,
#lte.init(carrier=at&t)

#some carriers do not require an APN
#also, check the band settings with your carrier
lte.attach(band=20, apn="your apn")
print("attaching..",end='')
while not lte.isattached():
    time.sleep(0.25)

    print('.',end='')
    print(lte.send_at_cmd('AT!="fsm"'))         # get the System FSM
print("attached!")

lte.connect()
print("connecting [##",end='')
while not lte.isconnected():
    time.sleep(0.25)
    print('#',end='')
    #print(lte.send_at_cmd('AT!="showphy"'))
    print(lte.send_at_cmd('AT!="fsm"'))
print("] connected!")

print(socket.getaddrinfo('pycom.io', 80))  
lte.deinit()
#now we can safely machine.deepsleep()
```
The last line of the script should return a tuple containing the IP address of the Pycom webserver.

>Note: the first time, it can take a long while to attach to the network.

## LTE Connectivity loss
> You need firmware 1.20.2.r2 or later for this functionality

It is possible that the LTE modem loses connectivity. It could be due to some radio interference, maybe the reception in the location of the module is not too good. Or if the module is being physically moved to another location with worse reception.

If the connectivity is lost this will in general not be reflected when you check `lte.isconnected()`. However, the lte modem sends a `UART break` signal. You can receive these events by using the `lte_callback` functionality. When connectivity is lost, the modem will try it's best to re-establish connectivity and this also works well in general. When connectivity is re-established, the modem will send another break signal, ie, the `lte_callback` will fire again.

This means the best practice is to capture the callback and inside the callback test whether the module is connected or not. If, with some timeout, there really is no connection, then one can try to react to this. Let's say the application is a sensor, that is most of the time in deepsleep, wakes up once in a while, measures something and then tries to send it's measurement before going back to deepsleep. In this case one could simply log the event, go back to sleep and hope that in the next interval the reception will be better. Or, if there is some alternative connectivity implemented, one could trigger it at this point.

```python
def lte_cb_handler(arg):
    ev = arg.events() # NB: reading the events also clears them
    print("LTE CB", time.time(), ev, time.gmtime())
    pycom.rgbled(0x222200)
    if ev & LTE.EVENT_BREAK:
        print("LTE CB", "uart break signal")
    print("LTE CB", time.time(), "test connection")
    # TBD: write your own test_connection function
    if test_connection():
        print("LTE CB", time.time(), "connection ok")
    else:
        print("LTE CB", time.time(), "connection not ok")
        # TBD: implement handling of lost connection
        # machine.deepsleep(deepsleeptime)

lte_callback(LTE.EVENT_BREAK, lte_cb_handler)
```

## LTE Troubleshooting guide

### Firmware version
    Use either of the following snippets to check the version of the LTE modem firmware:
    ```python
    import sqnsupgrade
    sqnsupgrade.info()
    ```
    or
    ```python
    from network import LTE
    lte = LTE()
    print(lte.send_at_cmd('ATI1'))
    ```
    * Versions LR5.xx are for CAT-M1
    * Versions LR6.xx are for NB-IoT

### Debug output

When you add `debug=True` to the initialization, e.g. `lte = LTE(debug=True)` then the AT commands sent to the modem and the responses will be printed to the REPL. This can help with diagnosing problems with the LTE module.


### State transitions

Below, we review the state transitions of the modem firmware as reported by `print(lte.send_at_cmd('AT!="fsm"'))`. If you are having trouble attaching to the network, or getting a connection up and running, this might give some direction into what you are looking for. We are mainly looking at the status of the top two indicators for now.
1. Before calling `lte.attach()`, the status will be `STOPPED`.

    ```
    SYSTEM FSM
    ==========
    +--------------------------+--------------------+
    |            FSM           |        STATE       |
    +--------------------------+--------------------+
    | RRC TOP FSM              |STOPPED             |
    | RRC SEARCH FSM           |NULL                |
    | RRC ACTIVE FSM           |NULL                |
    | PMM PLMN FSM             |NULL                |
    | EMM MAIN FSM             |NULL                |
    | EMM AUTH FSM             |NULL                |
    | EMM CONN FSM             |NULL                |
    | EMM TAU FSM              |NULL                |
    | EMM TEST FSM             |NULL                |
    | ESM BEARER FSM           |BEARER_NULL         |
    | SMS MT FSM               |IDLE                |
    | SMS MO FSM               |IDLE                |
    | HP MAIN FSM              |IDLE                |
    | HP USIM FSM              |READY               |
    | HP SMS MO FSM            |IDLE                |
    | HP SMS MT FSM            |IDLE                |
    | HP CAT FSM               |IDLE                |
    +--------------------------+--------------------+
    ```
1. With no SIM card detected, the `RRC TOP FSM` will keep status `CAMPED`. You will see `HP USIM FSM` marked `ABSENT`.
    ```
    SYSTEM FSM
    ==========
    +--------------------------+--------------------+
    |            FSM           |        STATE       |
    +--------------------------+--------------------+
    | RRC TOP FSM              |CAMPED              |
    | RRC SEARCH FSM           |CAMPED_ANY          |
    | RRC ACTIVE FSM           |IDLE                |
    | PMM PLMN FSM             |ANY_CAMPED          |
    | EMM MAIN FSM             |NULL                |
    | EMM AUTH FSM             |NULL                |
    | EMM CONN FSM             |NULL                |
    | EMM TAU FSM              |NULL                |
    | EMM TEST FSM             |NULL                |
    | ESM BEARER FSM           |BEARER_NULL         |
    | SMS MT FSM               |IDLE                |
    | SMS MO FSM               |IDLE                |
    | HP MAIN FSM              |IDLE                |
    | HP USIM FSM              |ABSENT              |
    | HP SMS MO FSM            |IDLE                |
    | HP SMS MT FSM            |IDLE                |
    | HP CAT FSM               |NULL                |
    +--------------------------+--------------------+
    ```
1. SIM card inserted and attaching:
    * While `SCANNING`, the `RRC SEARCH FSM` goes from `WAIT_RSSI` to `WAIT_CELL_ID`
    * Later, the `RRC TOP FSM` goes from `SCANNING` to `SYNCING`
    * There are some states in between not discussed here.
    * If it is stuck at `WAIT_RSSI`, check the antenna connection
    * If the system returns multiple times from `SYNCING` to `CAMPED`, check the network availability, simcard placement and / or the firmware version.


    ```
    SYSTEM FSM
    ==========
    +--------------------------+--------------------+
    |            FSM           |        STATE       |
    +--------------------------+--------------------+
    | RRC TOP FSM              |SCANNING            |
    | RRC SEARCH FSM           |WAIT_RSSI           |
    | RRC ACTIVE FSM           |NULL                |
    | PMM PLMN FSM             |NORM_WAITCELL       |
    | EMM MAIN FSM             |NULL                |
    | EMM AUTH FSM             |NULL                |
    | EMM CONN FSM             |NULL                |
    | EMM TAU FSM              |NULL                |
    | EMM TEST FSM             |NULL                |
    | ESM BEARER FSM           |BEARER_NULL         |
    | SMS MT FSM               |IDLE                |
    | SMS MO FSM               |IDLE                |
    | HP MAIN FSM              |IDLE                |
    | HP USIM FSM              |READY               |
    | HP SMS MO FSM            |IDLE                |
    | HP SMS MT FSM            |IDLE                |
    | HP CAT FSM               |IDLE                |
    +--------------------------+--------------------+
    ```
1. Connecting
    ```
    SYSTEM FSM
    ==========
    +--------------------------+--------------------+
    |            FSM           |        STATE       |
    +--------------------------+--------------------+
    | RRC TOP FSM              |CONNECTING          |
    | RRC SEARCH FSM           |CAMPED              |
    | RRC ACTIVE FSM           |WAIT_SMC            |
    | PMM PLMN FSM             |NORM_CAMPED         |
    | EMM MAIN FSM             |REGISTERED_INIT     |
    | EMM AUTH FSM             |WAITING_SIM_CONFIRM |
    | EMM CONN FSM             |AS_ESTABLISHED      |
    | EMM TAU FSM              |NULL                |
    | EMM TEST FSM             |NULL                |
    | ESM BEARER FSM           |BEARER_NULL_PENDING_ACTIVE|
    | SMS MT FSM               |IDLE                |
    | SMS MO FSM               |IDLE                |
    | HP MAIN FSM              |IDLE                |
    | HP USIM FSM              |READY               |
    | HP SMS MO FSM            |IDLE                |
    | HP SMS MT FSM            |IDLE                |
    | HP CAT FSM               |IDLE                |
    +--------------------------+--------------------+
    ```
1. Connected
    ```
    SYSTEM FSM
    ==========
    +--------------------------+--------------------+
    |            FSM           |        STATE       |
    +--------------------------+--------------------+
    | RRC TOP FSM              |CONNECTED           |
    | RRC SEARCH FSM           |CAMPED              |
    | RRC ACTIVE FSM           |CONNECTED           |
    | PMM PLMN FSM             |NORM_CAMPED         |
    | EMM MAIN FSM             |REGISTERED          |
    | EMM AUTH FSM             |KASME_DEFINED       |
    | EMM CONN FSM             |AS_ESTABLISHED      |
    | EMM TAU FSM              |NULL                |
    | EMM TEST FSM             |NULL                |
    | ESM BEARER FSM           |BEARER_ACTIVE       |
    | SMS MT FSM               |IDLE                |
    | SMS MO FSM               |IDLE                |
    | HP MAIN FSM              |IDLE                |
    | HP USIM FSM              |READY               |
    | HP SMS MO FSM            |IDLE                |
    | HP SMS MT FSM            |IDLE                |
    | HP CAT FSM               |IDLE                |
    +--------------------------+--------------------+
    ```


### Potential other errors
    * `OSError: [Errno 202] EAI_FAIL`: Check the data plan / SIM activation status on network
