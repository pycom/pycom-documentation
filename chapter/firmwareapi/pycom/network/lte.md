# class LTE
The LTE class provides access to the LTE-M/NB-IoT modem on the GPy and FiPy.
LTE-M/NB-IoT are new categories of cellular protocols developed by the
[3GPP](http://www.3gpp.org) and optimized for long battery life power and longer
range. These are new protocols currently in the process of being deployed by
mobile networks across the world.

The GPy and FiPy support both new LTE-M protocols:

* **Cat-M1**: also known as **LTE-M** defines a 1.4 MHz radio channel size and
about 375 kbps of throughput. It is optimized for coverage and long battery life,
 outperforming 2G/GPRS, while being similar to previous LTE standards.

* **Cat-NB1** also known as **NB-IoT**, defines a 200 kHz radio channel size and
around 60 kbps of uplink speed. It's optimized for ultra low throughput and
specifically designed for IoT devices with a very long battery life. NB-IoT
shares some features with LTE such as operating in licensed spectrum, but it's
a very different protocol. It should be noted that NB-IoT has many restrictions
as does not offer full IP connectivity and does not support mobility. When
moving between cells, you will need to reconnect.

{% hint style='tip' %}
**Please note:** The GPy and FiPy only support the two protocols above and are not
 compatible with older LTE standards.
{% endhint %}

{% hint style='tip' %}
The Sequans modem used on Pycom's cellular enabled modules can only work in one
of these modes at a time. In order to switch between the two protocols you need
to flash a different firmware to the Sequans modem. Instructions for this can
be found [here](firmware.md).
{% endhint %}

###AT Commands

The AT commands for the Sequans Monarch modem on the GPy/FiPy are available in a
<a href="../../../datasheets/downloads/Monarch_4G-EZ_LR5110_ATCommands_ReferenceManual_Rev3_NOCONFIDENTIAL.pdf">PDF file</a>.

### Constructors

#####<class><i>class</i> network.LTE(id=0, ...)</class>

Create and configure a LTE object. See init for params of configuration.

```python
from network import LTE
lte = LTE()
```

### Methods

#####<function>LTE.init(*, carrier=None)</function>

This method is used to set up the LTE subsystem. After a **deinit()** this method can take several seconds to return waiting for the LTE modem to start-up. Optionally specify a carrier name. The available options are: "verizon", "at&t" and "standard". Standard is generic for any carrier, and it's also the option used when no arguments are given.

#####<function>lte.deinit()</function>

Disables LTE modem completely. This reduces the power consumption to the minimum. Call this before
entering deepsleep.

#####<function>lte.attach(*, band=None)</function>

Enable radio functionality and attach to the LTE Cat M1 network authorized by the inserted SIM card. Optionally specify the band to scan for networks. If no band (or None) is specified, all 6 bands will be scanned. The possible values for the band are: 3, 4, 12, 13, 20 and 28.

#####<function>lte.isattached()</function>

Returns ``True`` if the cellular mode is attached to the network. ``False`` otherwise.

#####<function>lte.dettach()</function>

Dettach the modem from the LTE Cat M1 and disable the radio functionality.

#####<function>lte.connect(*, cid=1)</function>

Start a data session and obtain and IP address. Optionally specify a CID (Connection ID) for the data session.
The arguments are:

    - ``cid`` is a Connection ID. This is carrier specific, for Verizon use cid=3. For others like Telstra it should be cid=1.

#####<function>lte.isconnected()</function>

Returns ``True`` if there is an active LTE data session and IP address has been obtained. ``False`` otherwise.

#####<function>lte.disconnect()</function>

End the data session with the network.

#####<function>lte.send_at_cmd(cmd)</function>

Send an AT command directly to the modem. Returns the raw response from the modem as a string object. **IMPORTANT:** If a data session is active (i.e.: the modem is *connected*), sending the AT commands requires to pause and then resume the data session. This is all done automatically, but makes the whole request take around 2.5 seconds.

Example:

```
lte.send_at_cmd('AT+CEREG?')    # check for network registration manually (sames as lte.isattached())
```

Optionally the response can be parsed for pretty printing:

```
def send_at_cmd_pretty(cmd):
    response = lte.send_at_cmd(cmd).split('\r\n')
    for line in response:
        print(line)

send_at_cmd_pretty('AT!="showphy"')     # get the PHY status
send_at_cmd_pretty('AT!="fsm"')         # get the System FSM
```

#####<function>lte.imei()</function>

Returns a string object witht the IMEI number of the LTE modem.

#####<function>lte.iccid()</function>

Returns a string object witht the ICCID number of the SIM card.

#####<function>lte.reset()</function>

Perform a hardware reset on the cellular modem. This function can take up to 5 seconds tu return as it waits for the modem to shutdown and reboot.
