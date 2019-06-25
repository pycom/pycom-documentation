---
title: "WiPy"
aliases:
    - gettingstarted/connection/wipy.html
    - gettingstarted/connection/wipy.md
    - chapter/gettingstarted/connection/wipy
    - gettingstarted/wipy.html
---

## Basic connection

<div>
<v-tabs
    dark
    color="#1E1E3C"
    slider-color="red">
    <v-tab ripple key="1">Exp Board 3.0</v-tab>      
    <v-tab ripple key="2">Exp Board 2.0</v-tab>
    <v-tab ripple key="3"> Pytrack/Pysense/Pyscan</v-tab>
    <v-tab ripple key="4">USB UART Adapter</v-tab>
    <v-tab ripple key="5">WiFi</v-tab>
      <v-tabs-items>

<!-- Tab 1 -->
<v-tab-item key="1">
<ul>
<li>Before connecting your module to an Expansion Board 3.0, you should
<a href="/pytrackpysense/installation/firmware">
update the firmware on the Expansion Board 3.0. Instructions on how to do this can be found here</a>.</li>
<li> Look for the reset button on the module (located at a corner of the board, next to the LED).</li>
<li> Locate the USB connector on the expansion board.</li>
<li> Insert the WiPy module on the Expansion Board with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.</li>

<img src="">
</li>
</ul>
</v-tab-item>

<!-- Tab 2 -->
<v-tab-item key="2">
  <ul>
    <li>Look for the reset button on the module (located at a corner of the board, next to the LED).</li>
    <li> Locate the USB connector on the expansion board.</li>
    <li> Insert the WiPy module on the the expansion board with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.
    </li>
  </ul>
  <img src="/gitbook/assets/expansion_board_2_wipy.png">
</v-tab-item>

<!-- Tab 3 -->
<v-tab-item key="3">
<ul>
  <li>Before connecting your module to a Pysense/Pytrack/Pyscan board, you should
  <a href="/pytrackpysense/installation/firmware">
  update the firmware on the Pysense/Pytrack/Pyscan. Instructions on how to do this can be found here</a>.</li>
  <li>Look for the reset button on the WiPy module (located at a corner of the board, next to the LED).
  <li>Locate the USB connector on the Pysense/Pytrack/Pyscan.</li>
  <li>Insert the module on the Pysense/Pytrack/Pyscan with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.
  <img src="/gitbook/assets/pysense_wipy.png">
  <img src="/gitbook/assets/pytrack_wipy.png">
  </li>
</ul>


</v-tab-item>

<!-- Tab 4 -->
<v-tab-item key="4">
<ul>
<li>Firstly you will need to connect power to your WiPy. You will need to supply
<code>3.5v</code>-<code>5.5v</code> to the <code>Vin</code> pin.

Do **not** feed <code>3.3v</code> directly to the <code>3.3v</code> supply pin, this will damage the regulator.
</li>

<li>The connect the <code>RX</code> and <code>TX</code> of your USB UART to the <code>TX</code> and <code>RX</code> of the WiPy respectively.

Please ensure you have the signal level of the UART adapter set to <code>3.3v</code> before connecting it.
</li>
<li>In order to put the WiPy into bootloader mode to update the device firmware you will need to connect <code>P2</code> to <code>GND</code>. We recommend you connect a button between the two to make this simpler.
</li>
</ul>
<img src="/gitbook/assets/uart_wipy.png">
</v-tab-item>

<!-- Tab 5 -->
<v-tab-item key="5">
  <b>Note:</b> This method of connection is not recommended for first time users. It is possible to lock yourself out of the device, requiring a USB connection.
  <ul>
  <li>In order to access the WiPy via WiFi you only need to provide <code>3.5v</code> - <code>5.5v</code> on the <code>Vin</code> pin of the WiPy:
  <img src="/gitbook/assets/bare_wipy.png">
  <li>By default, when the WiPy boots, it will create a WiFi access point with the following credentials:
  <ul>
    <li> SSID: <code>wipy-wlan</code></li>
    <li>  password: <code>www.pycom.io</code></li>
  </ul>
  <li>Once connected to this network you will be able to access the telnet and FTP servers running on the WiPy. For both of these the login details are:
  <ul>
    <li>username: <code>micro</code></li>
    <li>password: <code>python</code></li>
  </li>
  </ul>
</v-tab-item>

</v-tabs-items>
</v-tabs>
</div>

---

## Antennas

### WiFi/Bluetooth (optional)

All Pycom modules, including the WiPy, come with a on-board WiFi antenna as well as a U.FL connector for an external antenna. The external antenna is optional and only required if you need better performance or are mounting the WiPy in such a way that the WiFi signal is blocked. Switching between the antennas is done via software, instructions for this can be found [here.](/firmwareapi/pycom/network/wlan)

![](/gitbook/assets/wifi_pigtail_ant_wipy.png)

## Deep Sleep current issue

The LoPy, SiPy, and WiPy 2.0 experience an issue where the modules maintain a high current consumption in deep sleep mode. This issue has been resolved in all newer products. The cause for this issue is the DC to DC switch mode converter remains in a high performance mode even when the device is in deep sleep. The flash memory chip also does not power down. A more detailed explanation can be found [here.](https://forum.pycom.io/topic/1022/root-causes-of-high-deep-sleep-current)

## WiPy 2.0 vs WiPy 3.0

The WiPy 3.0 is an upgraded version of the WiPy 2.0 with the following changes:

* The FLASH has been upgraded from 4MB to 8MB.
* The RAM has been upgraded from 512KB to 4MB.
* The deepsleep current consumption issue has been fixed
* The antenna select pin has moved to GPIO21 (P12)
