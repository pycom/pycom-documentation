---
title: "FiPy"
aliases:
    - gettingstarted/connection/fipy.html
    - gettingstarted/connection/fipy.md
    - chapter/gettingstarted/connection/fipy
    - gettingstarted/fipy.html
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
      <li>Before connecting your module to an Expansion Board 3.0, you should <a href="/pytrackpysense/installation/firmware">update the firmware on the Expansion Board 3.0. Instructions on how to do this can be found here. </a></li>
      <li>When using the expansion board with a FiPy, you will need to remove the CTS and RTS jumpers as these interfere with communication with the cellular modem.</li>
      <li>Look for the reset button on the module (located at a corner of the board, next to the LED).</li>
      <li>Locate the USB connector on the expansion board.</li>
      <li>Insert the FiPy module on the Expansion Board with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.</li>
      </ul>
      <img src="/gitbook/assets/expansion_board_3_fipy.png">
      </v-tab-item>
      <!-- Tab 2 -->
      <v-tab-item key="2">
      <ul>
      <li> When using the expansion board with a FiPy, you will need to remove the CTS and RTS jumpers as these interfere with communication with the cellular modem.</li>
      <li> Look for the reset button on the module (located at a corner of the board, next to the LED).</li>
      <li> Locate the USB connector on the expansion board.</li>
      <li> Insert the FiPy module on the the expansion board with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.</li>
      </ul>
      <img src="/gitbook/assets/expansion_board_2_fipy.png">

      </v-tab-item>

      <v-tab-item key="3">
      <div>
      <ul>
      <li> Before connecting your module to a Pysense/Pytrack/Pyscan board, you should <a href="/pytrackpysense/installation/firmware">update the firmware on the Pysense/Pytrack/Pyscan. Instructions on how to do this can be found here</a>.</li>
      <li> Look for the reset button on the FiPy module (located at a corner of the board, next to the LED).</li>
      <li> Locate the USB connector on the Pysense/Pytrack/Pyscan.</li>
      <li> Insert the module on the Pysense/Pytrack/Pyscan with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.</li>
      </ul>
      <img src="/gitbook/assets/pysense_fipy.png">
      <img src="/gitbook/assets/pytrack_fipy.png">
      </div>
      </v-tab-item>     
      <v-tab-item key="4">
      <div>
      <ul>
      <li>Firstly you will need to connect power to your FiPy. You will need to supply <code>3.5v</code>-<code>5.5v</code> to the <code>Vin</code> pin.

      Do **not** feed <code>3.3v</code> directly to the <code>3.3v</code> supply pin, this will damage the regulator.</li>

      <li>The connect the <code>RX</code> and <code>TX</code> of your USB UART to the <code>TX</code> and <code>RX</code> of the FiPy respectively.

      Please ensure you have the signal level of the UART adapter set to <code>3.3v</code> before connecting it.</li>

      <li>In order to put the FiPy into bootloader mode to update the device firmware you will need to connect <code>P2</code> to <code>GND</code>. We recommend you connect a button between the two to make this simpler.</li>

      </ul>

      <img src="/gitbook/assets/uart_fipy.png">
      </div>
      </v-tab-item>

      <v-tab-item key="5">
      <div>
      <p>
      <b>Note:</b> This method of connection is not recommended for first time users. It is possible to lock yourself out of the device, requiring a USB connection.
      </p>
      <ul>
      <li>In order to access the FiPy via WiFi you only need to provide <code>3.5v</code> - <code>5.5v</code> on the <code>Vin</code> pin of the FiPy:

      <img src="/gitbook/assets/bare_fipy.png">

      </li>

      <li>By default, when the FiPy boots, it will create a WiFi access point with the following credentials:
        <ul>
        <li> SSID: <code>fipy-wlan</code></li>
        <li> password: <code>www.pycom.io</code></li>
        </ul>
      </li>
      <li>Once connected to this network you will be able to access the telnet and FTP servers running on the FiPy. For both of these the login details are:
    
        <ul>
        <li>username: <code>micro</code></li>
        <li>password: <code>python</code></li>
        </ul>

      </li>
      </ul>
      </div>
      </v-tab-item>
      </v-tabs-item>
    </v-tab>
</div>


## Antennas

### Lora/Sigfox

{{% hint style="danger" %}}
If you intend on using the LoRa/Sigfox connectivity of the FiPy you **must** connect a LoRa/Sigfox antenna to your FiPy before trying to use LoRa/Sigfox otherwise you risk damaging the device.
{{< /hint >}}

{{% hint style="info" %}}
The FiPy only supports LoRa on the 868MHz or 915MHz bands. It does not support 433MHz. For this you will require a LoPy4.
{{< /hint >}}

* Firstly you will need to connect the U.FL to SMA pig tail to the FiPy using the U.FL connector on the same side of the FiPy as the LED.

![](/gitbook/assets/lora_sigfox_pigtail_fipy.png)

* If you are using a pycase, you will next need to put the SMA connector through the antenna hole, ensuring you align the flat edge correctly, and screw down the connector using the provided nut.
* Finally you will need to screw on the antenna to the SMA connector.

![](/gitbook/assets/lora_sigfox_pigtail_ant_fipy.png)

### LTE Cat-M1/NB-IoT

{{% hint style="danger" %}}
If you intend on using the LTE CAT-M1 or NB-IoT connectivity of the FiPy you **must** connect a LTE CAT-M1/NB-IoT antenna to your FiPy before trying to use LTE Cat-M1 or NB-IoT otherwise you risk damaging the device.
{{< /hint >}}

* You will need to connect the antenna to the FiPy using the U.FL connector on the under side of the FiPy.

![](/gitbook/assets/lte_ant_fipy.png)

### WiFi/Bluetooth (optional)

All Pycom modules, including the FiPy, come with a on-board WiFi antenna as well as a U.FL connector for an external antenna. The external antenna is optional and only required if you need better performance or are mounting the FiPy in such a way that the WiFi signal is blocked. Switching between the antennas is done via software, instructions for this can be found [here.](/firmwareapi/pycom/network/wlan)

![](/gitbook/assets/wifi_pigtail_ant_fipy.png)

### SIM card <a id="sim-card"></a>

If you intend on using the LTE CAT-M1 or NB-IoT connectivity of the FiPy you will need to insert a SIM card into your FiPy. It should be noted that the FiPy does not support regular LTE connectivity and you may require a special SIM. It is best to contact your local cellular providers for more information on acquiring a LTE CAT-M1/NB-IoT enabled nano SIM.

![](/gitbook/assets/sim_fipy.png)
