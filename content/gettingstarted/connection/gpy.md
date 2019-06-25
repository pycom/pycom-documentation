---
title: "GPy"
aliases:
    - gettingstarted/connection/gpy.html
    - gettingstarted/connection/gpy.md
    - chapter/gettingstarted/connection/gpy
    - gettingstarted/gpy.html
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
      <v-tab-item key="1">
      <ul>
      <li> Before connecting your module to an Expansion Board 3.0, you should
      <a href="/pytrackpysense/installation/firmware">
      update the firmware on the Expansion Board 3.0. Instructions on how to do this can be found here</a></li>
      <li> Look for the reset button on the module (located at a corner of the board, next to the LED).</li>
      <li> Locate the USB connector on the expansion board.</li>
      <li> Insert the GPy module on the Expansion Board with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.</li>
      <img src="/gitbook/assets/expansion_board_3_gpy.png">
      </ul>
      </v-tab-item>
      <v-tab-item key="2">
        <ul>
      <li> Look for the reset button on the module (located at a corner of the board, next to the LED).
      <li> Locate the USB connector on the expansion board.
      <li> Insert the GPy module on the the expansion board with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.
      </ul>
      <img src="/gitbook/assets/expansion_board_2_gpy.png">

      </v-tab-item>

      <v-tab-item key="3">
      <ul>
      <li> Before connecting your module to a Pysense/Pytrack/Pyscan board, you should
      <a href="/pytrackpysense/installation/firmware">
      update the firmware on the Pysense/Pytrack/Pyscan. Instructions on how to do this can be found here</a>
      <li> Look for the reset button on the GPy module (located at a corner of the board, next to the LED).</li>
      <li> Locate the USB connector on the Pysense/Pytrack/Pyscan.</li>
      <li> Insert the module on the Pysense/Pytrack/Pyscan with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.</li>
      <img src="/gitbook/assets/pysense_gpy.png">
      <img src="/gitbook/assets/pytrack_gpy.png">

      </ul>
      </v-tab-item>

      <v-tab-item key="4">
      <ul>
        <li> Firstly you will need to connect power to your GPy. You will need to supply <code>3.5v</code>-<code>5.5v</code> to the <code>Vin</code> pin.
        Do <b>not</b> feed <code>3.3v</code> directly to the <code>3.3v</code> supply pin, this will damage the regulator.</li>

        <li>  The connect the <code>RX</code> and <code>TX</code> of your USB UART to the <code>TX</code> and <code>RX</code> of the GPy respectively.
        Please ensure you have the signal level of the UART adapter set to <code>3.3v</code> before connecting it.</li>


        <li>  In order to put the GPy into bootloader mode to update the device firmware you will need to connect <code>P2</code> to <code>GND</code>. We recommend you connect a button between the two to make this simpler.</li>
        </ul>

        </v-tab-item>
        <v-tab-item key="5">

        <b>Note:</b> This method of connection is not recommended for first time users. It is possible to lock yourself out of the device, requiring a USB connection.
        <ul>
        <li>In order to access the GPy via WiFi you only need to provide
        <code>3.5v</code> - <code>5.5v</code> on the <code>Vin</code> pin of the GPy:
        <img src="/gitbook/assets/bare_gpy.png">
        </li>
        <li>By default, when the GPy boots, it will create a WiFi access point with the following credentials:
        <ul>
          <li>SSID:<code>gpy-wlan</code></li>
          <li> password: <code>www.pycom.io</code></li>
          </ul>
        </li>
        <li>Once connected to this network you will be able to access the telnet and FTP servers running on the GPy. For both of these the login details are:
          <ul>
            <li>username: <code>micro</code></li>
            <li>password: <code>python</code></li>
          </li>        
          </ul>
        </li>
      </ul>
      </v-tab-item>                        
      </v-tabs-items>
  </v-tabs>
</div>

---

## Antennas

### LTE Cat-M1/NB-IoT

{{% hint style="danger" %}}
If you intend on using the LTE CAT-M1 or NB-IoT connectivity of the GPy you **must** connect a LTE CAT-M1/NB-IoT antenna to your GPy before trying to use LTE Cat-M1 or NB-IoT otherwise you risk damaging the device.
{{< /hint >}}

* You will need to connect the antenna to the GPy using the U.FL connector on the same side of the GPy as the LED.

![](/gitbook/assets/lte_ant_gpy.png)

### WiFi/Bluetooth (optional)

All Pycom modules, including the GPy, come with a on-board WiFi antenna as well as a U.FL connector for an external antenna. The external antenna is optional and only required if you need better performance or are mounting the GPy in such a way that the WiFi signal is blocked. Switching between the antennas is done via software, instructions for this can be found [here.](/firmwareapi/pycom/network/wlan)

![](/gitbook/assets/wifi_pigtail_ant_gpy.png)

### SIM card <a id="sim-card"></a>

If you intend on using the LTE CAT-M1 or NB-IoT connectivity of the GPy you will need to insert a SIM card into your GPy. It should be noted that the GPy does not support regular LTE connectivity and you may require a special SIM. It is best to contact your local cellular providers for more information on acquiring a LTE CAT-M1/NB-IoT enabled nano SIM.

![](/gitbook/assets/sim_gpy.png)
