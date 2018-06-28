<p align="center"><img src ="../../../img/{{module|lower}}.png" width="300"></p>

{% if module=="WiPy2" %}
**Store**: Discontinued, See [WiPy3](./wipy3.md)

**Getting Started** [Click Here](../../gettingstarted/connection/wipy.md)
{% elif module=="WiPy3" %}
**Store**: [Buy Here](http://www.pycom.io/wipy-3)

**Getting Started** [Click Here](../../gettingstarted/connection/wipy.md)
{% else %}
**Store**: [Buy Here](http://www.pycom.io/{{module | lower}})

**Getting Started** [Click Here](../../gettingstarted/connection/{{module|lower}}.md)
{% endif %}


## Pinout
The pinout of the {{module}} is available as a
<a href="../downloads/{{module | lower}}-pinout.pdf" target="_blank">PDF File</a>.

<a href="../downloads/{{module | lower}}-pinout.pdf" target="_blank" align="center"><img src ="../../../img/{{module | lower}}-pinout.png"></a>

{% hint style='info' %}
Please note that the PIN assignments for UART1 (TX1/RX1), SPI (CLK,MOSI,MISO)
and I2C (SDA,SCL) are defaults and can be changed in Software.
{% endhint %}

{% if module=="WiPy3" %}
##Differences from WiPy 2.0
 - Deep sleep current draw fixed, now only 19.7µA
 - Upgraded RAM from 512KB to 4MB
 - Upgraded External FLASH from 4MB to 8MB
 - Antenna select pin moved from GPIO16 to GPIO21 (P12)
{% endif %}

## Datasheet
The datasheet of the {{module}} is available as a
<a href="../downloads/{{module | lower}}-specsheet.pdf" target="_blank">PDF File</a>.

## Notes

### WiFi
By default, upon boot the {{module}} will create a WiFi access point with the
SSID {% if module=="WiPy2" or module=="WiPy3" or module=="W01" %}
`wipy-wlan-XXXX`
{% elif module=="LoPy" or module=="L01" %}
`lopy-wlan-XXXX`
{% elif module=="LoPy4" or module=="L04" %}
`lopy4-wlan-XXXX`
{% elif module=="GPy" or module=="G01" %}
`gpy-wlan-XXXX`
{% else %}
`{{module|lower}}-wlan-XXXX`
{% endif %}, where `XXXX` is a random 4-digit number, and the password
`www.pycom.io`.

{% if module=="WiPy3" or module=="LoPy4" or module=="GPy" or module=="FiPy"%}
The RF switch that selects between the on-board and external antenna is connected
to `P12`, for this reason using `P12` should be avoided unless WiFi is disabled
in your application.
{% endif %}

{% if module=="WiPy2" or module=="WiPy3" or module=="LoPy" or module=="LoPy4" or module=="GPy" or module=="FiPy" or module=="SiPy"%}
### Power
The `Vin` pin on the {{module}} can be supplied with a voltage ranging from
`3.5v` to `5.5v`. The `3.3v` pin on the other hand is output **only**, and must
not be used to feed power into the {{module}}, otherwise the on-board regulator
will be damaged.
{% endif %}

{% if module=="LoPy" or module=="SiPy" or module=="WiPy2"%}
### Deep Sleep
Due to a couple issues with the {{module}} design the module draws more current
than it should while in deep sleep. The DC-DC switching regulator always stays
in high performance mode which is used to provide the lowest possible output
ripple when the modules is in use. In this mode, it draws a quiescent current of
10mA. When the regulator is put into ECO mode, the quiescent current goes down
to 10uA. Unfortunately, the pin used to control this mode is out of the RTC
domain, and therefore not usable during deep sleep. This causes the regulator to
always stay in PWM mode, keeping its quiescent current at 10mA. Alongside this
the flash chip doesn't enter power down mode because the CS pin is floating
during deep sleep. This causes the flash chip to consume around 2mA of current.
To work around this issue a ["deep sleep shield"](../boards/deepsleep.md) is
available that attaches to the module and allows power to be cut off from the
device. The device can then be re-enabled either on a timer or via pin
interrupt. With the deep sleep shield the current consumption during deep sleep
is between 7uA and 10uA depending on the wake sources configured.
{% endif %}

{% if module=="GPy" or module=="FiPy" %}
###AT Commands

The AT commands for the Sequans Monarch modem on the {{module}} are available in a
<a href="../downloads/Monarch_4G-EZ_LR5110_ATCommands_ReferenceManual_Rev3_NOCONFIDENTIAL.pdf">PDF file</a>.
{% endif %}

## Tutorials
Tutorials on how to the {{ module }} module can be found in the
[examples](../../tutorials/README.md) section of this documentation. The following tutorials might be of
specific interest for the {{ module }}:

- [WiFi connection](../../tutorials/all/wlan.md)

{% if module=="LoPy" or module=="LoPy4" or module=="FiPy" %}
- [LoRaWAN node](../../tutorials/lora/lorawan-otaa.md)

- [LoRaWAN nano gateway](../../tutorials/lora/lorawan-nano-gateway.md)

{% endif %}
{% if module=="SiPy" or module=="LoPy4" or module=="FiPy" %}
- [Sigfox](../../tutorials/sigfox/README.md)

{% endif %}
{% if module=="GPy" or module=="FiPy" %}
- [LTE CAT-M1](../../tutorials/lte/cat_m1.md)

- [NB-IoT](../../tutorials/lte/nb_iot.md)

{% endif %}
- [BLE](../../tutorials/all/ble.md)
