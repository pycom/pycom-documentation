---
title: "LTE"
aliases:
    - firmwareapi/pycom/network/lte.html
    - firmwareapi/pycom/network/lte.md
    - chapter/firmwareapi/pycom/network/lte
---

The LTE class provides access to the LTE-M/NB-IoT modem on the GPy and FiPy. LTE-M/NB-IoT are new categories of cellular protocols developed by the [3GPP](http://www.3gpp.org) and optimised for long battery life power and longer range. These are new protocols currently in the process of being deployed by mobile networks across the world.

The GPy and FiPy support both new LTE-M protocols:

* **Cat-M1**: also known as **LTE-M** defines a 1.4 MHz radio channel size and about 375 kbps of throughput. It is optimised for coverage and long battery life, outperforming 2G/GPRS, while being similar to previous LTE standards.
* **Cat-NB1** also known as **NB-IoT**, defines a 200 kHz radio channel size and around 60 kbps of uplink speed. It's optimised for ultra low throughput and specifically designed for IoT devices with a very long battery life. NB-IoT shares some features with LTE such as operating in licensed spectrum, but it's a very different protocol. It should be noted that NB-IoT has many restrictions as does not offer full IP connectivity and does not support mobility. When moving between cells, you will need to reconnect.

> The Sequans modem used on Pycom's cellular enabled modules can only work in one of these modes at a time. In order to switch between the two protocols you need to flash a different firmware to the Sequans modem. Instructions for this can be found [here](/updatefirmware/ltemodem/).


## Band support

- Fipy/GPy v1.0 ==> supports 6 bands only (3, 4, 12, 13, 20, 28)

- Fipy/GPy v1.2  with Sequans modem Firmware (41xxx) ==> Supports Full range of 17 bands (1, 2, 3, 4, 5, 8, 12, 13, 14, 17, 18, 19, 20, 25, 26, 28, 66)

- Fipy/GPy v1.2  with Sequans older modem Firmwares  (39xxx)==> Supports 8 Bands (3, 4, 5, 8, 12, 13, 20, 28)

- Fipy/GPy v1.2  with Sequans old modem Firmwares  < (39xxx)==> Supports 6 Bands (3, 4, 12, 13, 20, 28)


## AT Commands

The AT commands for the Sequans Monarch modem on the GPy/FiPy are available in a [PDF file](/gitbook/assets/Monarch-LR5110-ATCmdRefMan-rev6_noConfidential.pdf).


## Constructors

### class network.LTE(id=0, ...)

Create and configure a LTE object. See init for params of configuration.

```python

from network import LTE
lte = LTE()
```

## Methods

### lte.init([carrier='standard', psm_period_value=0, psm_period_unit=LTE.PSM_PERIOD_DISABLED, psm_active_value=0, psm_active_unit=LTE.PSM_ACTIVE_DISABLED])

This method is used to set up the LTE subsystem. Optionally specify 
* `carrier name`. The available options are: 
    * `'at&t'`
    * `'verizon'`
    * `'standard'`
* `psm_period_value` : Configure at which period the device will connect to the network. Values from 0 to 31 are allowed
* `psm_period_unit` : Specify the _unit_ to be used for `psm_period_value`:
    * `PSM_PERIOD_2S`
    * `PSM_PERIOD_30S`
    * `PSM_PERIOD_1M`
    * `PSM_PERIOD_1H`
    * `PSM_PERIOD_10H`
    * `PSM_PERIOD_320H`
    * `PSM_PERIOD_DISABLED`: Turn off the PSM mode.
* `psm_active_value` : Configure how long the device will be connected. Values from 0 to 31 are allowed.
* `psm_active_unit` : Specify the _unit_ for `psm_active_value`:
    * `PSM_ACTIVE_2S`
    * `PSM_ACTIVE_1M`
    * `PSM_ACTIVE_6M`
    * `PSM_ACTIVE_DISABLED`: turn off the PSM mode.

Multiply the `value` with the `unit` to get the actual active or sleeping times. 

### lte.deinit([detach=True, reset=False])

Disables LTE modem completely. This reduces the power consumption to the minimum. Call this before entering deepsleep.

* `detach` : detach from network.
* `reset` : reset LTE modem.

### lte.psm()

Queries the PSM timers. Returns a 5-tuple of the following structure: `(enabled, period_value, period_unit, active_value, active_unit)`.

### lte.attach([band=None, apn=None, cid=None, type=LTE.IP, legacyattach=True])

Enable radio functionality and attach to the LTE network authorised by the inserted SIM card. Optionally specify:

* `band` : to scan for networks. If no band (or `None`) is specified, all 8 bands will be scanned. The possible values for the band are: `3, 4, 5, 8, 12, 13, 20 and 28`.
* `apn` : Specify the APN (Access point Name).
* `cid` : connection ID, see `LTE.connect()`. when the ID is set here it will be remembered when doint connect so no need to specify again
* `type` : PDP context type either `LTE.IP` or `LTE.IPV4V6`. These are options to specify PDP type ‘Packet Data protocol' either IP [Internet Protocol] or IPV4V6 ver4,6 , that depends actually on what does the Network support.
* `legacyattach` : When kept = True the API `LTE.isattached()` will return True when attached to the Network AND Network registration status is home or roaming, when flag is False, API `LTE.isattached()` will return True when attached to the Network only.



### lte.isattached()

Returns `True` if the cellular mode is attached to the network. `False` otherwise.

### lte.detach([reset=False])

Detach the modem from the LTE Cat M1 and disable the radio functionality.

* `reset` : set to True to reset the LTE modem.

### lte.connect([cid=1])

Start a data session and obtain and IP address. Optionally specify a CID (Connection ID) for the data session. The arguments are:

* `cid` is a Connection ID. This is carrier specific, for Verizon use `cid=3`. For others like Telstra it should be `cid=1`.

### lte.isconnected()

Returns `True` if there is an active LTE data session and IP address has been obtained. `False` otherwise.

### lte.disconnect()

End the data session with the network.

### lte.send_at_cmd(cmd, [delay=10000])

Send an AT command directly to the modem. Returns the raw response from the modem as a string object. You can find the possible AT commands [here](/gitbook/assets/Monarch-LR5110-ATCmdRefMan-rev6_noConfidential.pdf).

>If a data session is active (i.e. the modem is _connected_), you will need to `lte.pppsuspend()` and `lte.pppresume` around the AT command.

Example:

```python
lte.send_at_cmd('AT+CEREG?')    # check for network registration manually (sames as lte.isattached())
```

Optionally the response can be parsed for pretty printing:

* `delay` : specify the number of milliseconds the esp32 chip will wait between sending an AT command to the modem. and reading the response.

### lte.imei()

Returns a string object with the IMEI number of the LTE modem.

### lte.iccid()

Returns a string object with the ICCID number of the SIM card.

### lte.reset()

Perform a hardware reset on the cellular modem. This function can take up to 5 seconds to return as it waits for the modem to shutdown and reboot.

### lte.pppsuspend()

Suspend PPP session with LTE modem. this function can be used when needing to send AT commands which is not supported in PPP mode.

### lte.pppresume()

Resumes PPP session with LTE modem.

### lte.factory_reset()

Reset modem configuration to Factory settings.

### lte.modem_upgrade_mode()

Puts the modem in to modem upgrade mode and bridging LTE modem UART port to FiPy/GPy UART0 to enable upgrading Firmware over USB port.

> In this mode all All tasks on the board are halted and a reset is required to regain functionality.

### lte.reconnect_uart()

Reconnect esp32 UART 2 to LTE modem UART port.

### lte.ue_coverage()

Check Network Coverage for UE device (i.e LTE modem). Returns:

* `True`: There is Network Coverage.
* `False`: No Netwok Coverage.


## Constants

* `LTE.IP` : Internet Protocol IP

* `LTE.IPV4V6` : Internet protocol ver. 4/6

* `PSM_PERIOD_2S`, `PSM_PERIOD_30S`, `PSM_PERIOD_1M`, `PSM_PERIOD_10M`, `PSM_PERIOD_1H`, `PSM_PERIOD_10H`, `PSM_PERIOD_320H`: Specify the unit for the PSM period to be 2 seconds, 30 seconds, 1 minute, 10 minutes, 1 hour, 10 hours, or 320 hours, respectively.
* `PSM_PERIOD_DISABLED`: Means turning PSM off.
* `PSM_ACTIVE_2S`, `PSM_ACTIVE_1M`, `PSM_ACTIVE_6M`: Specify the unit for the PSM active duration to be 2 seconds, 1 minute, or 6 minutes, respectively.
* `PSM_ACTIVE_DISABLED`: Means turning PSM off.
