---
title: "LTE Examples"
aliases:
    - chapter/tutorials/lte
---

The following tutorials demonstrate the use of the LTE CAT-M1 and NB-IoT functionality on cellular enabled Pycom modules.

Our cellular modules support both LTE CAT-M1 and NB-IoT, these are new lower power, long range, cellular protocols. These are not the same as the full version of 2G/3G/LTE supported by cell phones, and require your local carriers to support them. At the time of writing, CAT-M1 and NB-IoT connectivity is not widely available so be sure to check with local carriers if support is available where you are.

Both networks make can make use of the same example:
(Make sure you check the coverage map of your provider to confirm coverage in your area)
```python

from network import LTE
import time
import socket
lte = LTE()
lte.attach(band=20, apn="your apn")
while not lte.isattached()
    time.delay(0.25)
    print('.', end='')
    print(lte.send_at_cmd('AT!="fsm"')         # get the System FSM
print("LTE modem attached!")
lte.connect()
while not lte.isconnected():
    time.sleep(0.25)
    print('#')
    #print(lte.send_at_cmd('AT!="showphy"'))
    print(lte.send_at_cmd('AT!="fsm"'))
print("LTE modem connected!")

print(socket.getaddrinfo('pycom.io', 80))  

lte.disconnect()
lte.detach()
#now we can do 
#machine.deepsleep()

```
>Note: the first time, it can take a long while to attach to the network. 

If you want to check the status of the modem while attaching, you can use the following commands:
```python
print(lte.send_at_cmd('AT!="fsm"')         # get the System FSM
```

# LTE Troubleshooting guide

Reviewing the responses from `print(lte.send_at_cmd('AT!="fsm"')) from the script above:
* Before calling `lte.attach()` :
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
* With no SIM card detected:
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
* SIM card inserted and attaching:
    * Scanning `RRC SEARCH FSM` goes from `WAIT_RSSI` to `WAIT_CELL_ID`
    * Scanning `RRC TOP FSM` goes from `SCANNING` to `SYNCING`
    * If it is stuck at `WAIT_RSSI`, check the antenna connection
    * If the system returns from `SYNCING` to `CAMPED`, check the network availability, simcard placement and / or the firmware version. 
    >Note: Use the following to check the version number:
    >```python
    >import sqnsupgrade
    >print(sqnsupgrade.info()
    >```
    Versions LR5.xx are for CAT-M1 

    Versions LR6.xx are for NB-IoT 

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
* Connecting
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
* Connected
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
* Potential other errors:
    * `OSSError: [Errno 202] EAI_FAIL`: Check the data plan / sim activation status on network 