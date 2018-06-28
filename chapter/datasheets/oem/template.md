<p align="center"><img src ="../../../img/{{module | lower}}.png" width="300"></p>

### Pinout
The pinout of the {{module}} is available as a <a href="../downloads/{{module|lower}}-pinout.pdf" target="_blank">PDF File</a>.

<a href="../downloads/{{module|lower}}-pinout.pdf" target="_blank" align="center"><img src ="../../../img/{{module|lower}}-pinout.png"></a>

### Specsheets

The specsheet of the {{module}} is available as a <a href="../downloads/{{module|lower}}-specsheet.pdf" target="_blank">PDF File</a>.

### Drawings

The drawings for the {{module}} is available as a <a href="../downloads/{{module|lower}}-drawing.pdf" target="_blank">PDF File</a>.

Please note that the PIN assignments for UART1 (TX1/RX1), SPI (CLK, MOSI, MISO) and I2C (SDA, SCL) are defaults and can be changed in Software.

{% if module=="G01" %}
###AT Commands

The AT commands for the Sequans Monarch modem on the {{module}} are available in a
<a href="../downloads/Monarch_4G-EZ_LR5110_ATCommands_ReferenceManual_Rev3_NOCONFIDENTIAL.pdf">PDF file</a>.
{% endif %}

## Tutorials
Tutorials on how to the {{ module }} module can be found in the
[examples](../../tutorials/README.md) section of this documentation. The following tutorials might be of
specific interest for the {{ module }}:

- [WiFi connection](../../tutorials/all/wlan.md)
{% if module=="L01" or module=="L04" %}
- [LoRaWAN node](../../tutorials/lora/lorawan-otaa.md)
- [LoRaWAN nano gateway](../../tutorials/lora/lorawan-nano-gateway.md)
{% endif %}
{% if module=="L04" %}
- [Sigfox](../../tutorials/sigfox/README.md)
{% endif %}
{% if module=="G01" %}
- [LTE CAT-M1](../../tutorials/lte/cat_m1.md)
- [NB-IoT](../../tutorials/lte/nb_iot.md)
{% endif %}
- [BLE](../../tutorials/all/ble.md)
