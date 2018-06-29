## Basic connection

{% tabs exp2="Exp Board 2.0", exp3="Exp Board 3.0", pic="Pysense/Pytrack/Pyscan", diy="USB UART Adapter", wifi="WiFi"%}

{% content "exp2" %}

{% if module=="FiPy" %}
- When using the expansion board with a {{module}}, you will need to remove the
CTS and RTS jumpers as these interfere with communication with the cellular
modem.
{% endif %}
- Look for the reset button on the module (located at a corner of the board,
  next to the LED).
- Locate the USB connector on the expansion board.
- Insert the {{ module }} module on the the expansion board with the reset button
pointing towards the USB connector. It should firmly click into place and the
pins should now no longer be visible.

<p align="center"><img src ="../img/Expansion_Board_2_{{ module }}.png" style="max-height: 400px;"></p>

{% content "exp3" %}
- Before connecting your module to an Expansion Board 3.0, you should update the firmware on the Expansion Board 3.0. Instructions on how to do this can be found [here](../../pytrackpysense/installation/firmware.md).
{% if module=="FiPy" %}
- When using the expansion board with a {{module}}, you will need to remove the
CTS and RTS jumpers as these interfere with communication with the cellular
modem.
{% endif %}
- Look for the reset button on the module (located at a corner of the board,
  next to the LED).
- Locate the USB connector on the expansion board.
- Insert the {{ module }} module on the Expansion Board with the reset button
pointing towards the USB connector. It should firmly click into place and the
pins should now no longer be visible.

<p align="center"><img src ="../img/Expansion_Board_3_{{ module }}.png" style="max-height: 400px;"></p>


{% content "pic" %}
- Before connecting your module to a Pysense/Pytrack/Pyscan board, you should update
  the firmware on the Pysense/Pytrack/Pyscan. Instructions on how to do this can be
  found [here](../../pytrackpysense/installation/firmware.md).
- Look for the reset button on the {{ module }} module (located at a corner of
the board, next to the LED).
- Locate the USB connector on the Pysense/Pytrack/Pyscan.
- Insert the module on the Pysense/Pytrack/Pyscan with the reset button pointing
towards the USB connector. It should firmly click into place and the pins
 should now no longer be visible.

<p align="center"><img src ="../img/Pysense_{{ module }}.png" style="max-height: 400px;"><img src ="../img/Pytrack_{{ module }}.png" style="max-height: 400px;"></p>


Once you have completed the above steps successfully you should see the on-board
LED blinking blue. This indicates the device is powered up and running.

{% content "diy" %}
- Firstly you will need to connect power to your {{ module }}. You will need to
supply `3.5v`-`5.5v` to the `Vin` pin. **Note:** Do *not* feed `3.3v` directly to
the `3.3v` supply pin, this will damage the regulator.
- The connect the `RX` and `TX` of your USB UART to the `TX` and `RX` of the
{{ module }} respectively. **Note:** Please ensure you have the signal level of
the UART adapter set to `3.3v` before connecting it.
- In order to put the {{ module }} into bootloader mode to update the device
firmware you will need to connect `P2` to `GND`. We recommend you connect a
button between the two to make this simpler.

<p align="center"><img src ="../img/UART_{{ module }}.png" style="max-height: 400px;"></p>

{% content "wifi" %}
**Note:** This method of connection is not recommended for first time users.
It is possible to lock yourself out of the device, requiring a USB connection.

 - In order to access the {{ module }} via WiFi you only need to provide `3.5v` - `5.5v` on
the `Vin` pin of the {{ module }}:
<p align="center"><img src ="../img/Bare_{{ module }}.png" style="max-height: 400px;"></p>

- By default, when the {{ module }} boots, it will create a WiFi access point with
the following credentials:
  - SSID: `{{ module | lower }}-wlan`
  - password: `www.pycom.io`

 - Once connected to this network you will be able to access the telnet and FTP
servers running on the {{ module }}. For both of these the login details are:
  - username: `micro`
  - password: `python`

{% endtabs %}

## Antennas

{% if module=="LoPy" or module=="SiPy" or module=="LoPy4" or module=="FiPy" %}
{% if module=="LoPy" %}
  {% set comm="LoRa" %}
{% elif module=="SiPy" %}
  {% set comm="Sigfox" %}
{% else %}
  {% set comm="LoRa/Sigfox" %}
{% endif %}

### {{ comm }}
{% hint style='danger' %}
If you intend on using the {{ comm }} connectivity of the {{ module }} you **must**
connect a {{ comm }} antenna to your {{ module }} before trying to use
{{ comm }} otherwise you risk damaging the device.
{% endhint %}

{% if module=="LoPy" or module=="FiPy"%}
  {% hint style='danger' %}
  The {{ module }} only supports LoRa on the 868MHz or 915MHz bands. It does not
  support 433MHz. For this you will require a LoPy4.
  {% endhint %}
{% endif %}

{% if module=="LoPy4"%}
- Firstly you will need to connect the U.FL to SMA pig tail to the {{module}}
using one of the two the U.FL connectors on the same side of the {{ module }}
as the LED. The one on the left hand side is for 433MHz (LoRa only), the one of
the right hand side is for 868MHz/915MHz (LoRa & Sigfox). **Note:** This is
different from the LoPy.
{% else %}
- Firstly you will need to connect the U.FL to SMA pig tail to the {{module}}
using the U.FL connector on the same side of the {{ module }} as the LED.
{% endif %}

<p align="center"><img src ="../img/{{comm | replace("/", "_")}}_Pigtail_{{module}}.png" style="max-height: 400px;"></p>

- If you are using a pycase, you will next need to put the SMA connector through
the antenna hole, ensuring you align the flat edge correctly, and screw down the
connector using the provided nut.
- Finally you will need to screw on the antenna to the SMA connector.
<p align="center"><img src ="../img/{{comm | replace("/", "_")}}_Pigtail_ANT_{{module}}.png" style="max-height: 400px;"></p>
{% endif %}

{% if module=="GPy" or module=="FiPy" %}
### LTE Cat-M1/NB-IoT
If you intend on using the LTE CAT-M1 or NB-IoT connectivity of the {{ module }}
you **must** connect a LTE CAT-M1/NB-IoT antenna to your {{ module }} before
trying to use LTE Cat-M1 or NB-IoT otherwise you risk damaging the device.

- You will need to connect the antenna to the {{module}} using the U.FL
connector on the
{% if module=="GPy" %} same side of the {{ module }} as the LED.
{% else %} under side of the {{ module }}.
{% endif %}
<p align="center"><img src ="../img/LTE_ANT_{{module}}.png" style="max-height: 400px;"></p>
{% endif %}

### WiFi/Bluetooth (optional)
All Pycom modules, including the {{ module }}, come with a on-board WiFi antenna
as well as a U.FL connector for an external antenna. The external antenna is
optional and only required if you need better performance or are mounting the
{{ module }} in such a way that the WiFi signal is blocked. Switching between
the antennas is done via software, instructions for this can be found
[here.](../../firmwareapi/pycom/network/wlan.md)

<p align="center"><img src ="../img/WiFi_Pigtail_ANT_{{module}}.png" style="max-height: 400px;"></p>

{% if module=="GPy" or module=="FiPy" %}
## SIM card
If you intend on using the LTE CAT-M1 or NB-IoT connectivity of the {{ module }}
you will need to insert a SIM card into your {{ module }}. It should be noted
that the {{ module }} does not support regular LTE connectivity and you may
require a special SIM. It is best to contact your local cellular providers for
more information on acquiring a LTE CAT-M1/NB-IoT enabled nano SIM.

<p align="center"><img src ="../img/SIM_{{ module }}.png"></p>

{% endif %}
{% if module=="LoPy" or module=="SiPy" or module=="WiPy" %}
## Deep Sleep current issue

The LoPy, SiPy, and WiPy 2.0 experience an issue where the modules maintain a
high current consumption in deep sleep mode. This issue has been resolved in
all newer products. The cause for this issue is the DC to DC switch mode
converter remains in a high performance mode even when the device is in deep
sleep. The flash memory chip also does not power down. A more detailed
explanation can be found
[here.](https://forum.pycom.io/topic/1022/root-causes-of-high-deep-sleep-current)

{% endif %}
