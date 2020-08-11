---
title: "LTE Examples"
aliases:
    - chapter/tutorials/lte
---

The following tutorial demonstrates the use of the LTE CAT-M1 and NB-IoT functionality on cellular enabled Pycom modules.

GPy and FiPy support both LTE CAT-M1 and NB-IoT. These are newer, low power, long range, cellular protocols. They are not the same as the full version of 2G/3G/LTE supported by cell phones, and require your local carriers to support them. At the time of writing, CAT-M1 and NB-IoT connectivity is not widely available so be sure to check with local carriers if support is available where you are. Together with the SIM card, the provider will supply you with configuration details: Usually band and APN. Use these in the example code below. 

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
while not lte.isattached()
    time.delay(0.25)

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

# LTE disconnecting 
When the LTE disconnects in an unexpected situation, for example when the signal is lost, `lte.isconnected()` will still return `True`. Currently, there is a solution using the callback and handler function listed below:
```python
from network import LTE
import time
from sleep import sleep
import machine
def cb_handler(arg):
    print("CB: LTE Coverage lost")
    print("CB: sleep", s)
    print("CB: deinit")
    lte.deinit()
    print("CB: reset")
    machine.reset()

lte.lte_callback(LTE.EVENT_COVERAGE_LOSS, cb_handler)

```
# LTE Troubleshooting guide



Below, we review the responses from `print(lte.send_at_cmd('AT!="fsm"'))`. If you are having trouble attaching to the network, or getting a connection up and running, this might give some direction into what you are looking for. We are mainly looking at the status of the top two indicators for now.
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

* Firmware version:
    Use the following to check the version number:
    ```python
    import sqnsupgrade
    sqnsupgrade.info()
    ```
    * Versions LR5.xx are for CAT-M1 
    * Versions LR6.xx are for NB-IoT 
* Potential other errors:
    * `OSError: [Errno 202] EAI_FAIL`: Check the data plan / SIM activation status on network 

