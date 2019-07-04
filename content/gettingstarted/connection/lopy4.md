---
title: "LoPy 4"
aliases:
    - gettingstarted/connection/lopy4.html
    - gettingstarted/connection/lopy4.md
    - chapter/gettingstarted/connection/lopy4
    - gettingstarted/lopy4.html
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
          <li> Before connecting your module to an Expansion Board 3.0, you should update the firmware on the Expansion Board 3.0. Instructions on how to do this
          <a href="/pytrackpysense/installation/firmware">can be found here</a>
        </li>
        <li> Look for the reset button on the module (located at a corner of the board, next to the LED).
        </li>
        <li> Locate the USB connector on the expansion board.</li>
        <li> Insert the LoPy4 module on the Expansion Board with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.
        </li>
        </ul>
        <img src="/gitbook/assets/expansion_board_3_lopy4.png">
      </v-tab-item>
      <!-- Tab 2 -->
      <v-tab-item key="2">
      <ul>
      <li> Look for the reset button on the module (located at a corner of the board, next to the LED).</li>
      <li> Locate the USB connector on the expansion board.</li>
      <li> Insert the LoPy4 module on the the expansion board with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.</li>
      </ul>
      <img src="/gitbook/assets/expansion_board_2_lopy4.png">
      </v-tab-item>
      <!-- Tab 3 -->
      <v-tab-item key="3">
      <ul>
      <li> Before connecting your module to a Pysense/Pytrack/Pyscan board, you should update the firmware on the Pysense/Pytrack/Pyscan. Instructions on how to do this  
      <a href="/pytrackpysense/installation/firmware">can be found here</a>.</li>
      <li> Look for the reset button on the LoPy4 module (located at a corner of the board, next to the LED).</li>
      <li> Locate the USB connector on the Pysense/Pytrack/Pyscan.</li>
      <li> Insert the module on the Pysense/Pytrack/Pyscan with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.</li>
      </ul>

      <img src="/gitbook/assets/assets-2f-lifiulge6_ztmmvcuea-2f-lkmxk1kqvbgjpw04i3u-2f-liqbk7blltxqntvqzh_-2fpysense_lopy4.png">
      <img src="/gitbook/assets/assets-2f-lifiulge6_ztmmvcuea-2f-lkmxk1kqvbgjpw04i3u-2f-liqbluw130dl1amaklt-2fpytrack_lopy4.png">


      </v-tab-item>
      <!-- Tab 4 -->
      <v-tab-item key="4">
      <ul>
      <li> Firstly you will need to connect power to your LoPy4. You will need to supply <code>3.5v</code>-<code>5.5v</code> to the <code>Vin</code> pin.

      Do **not** feed <code>3.3v</code> directly to the <code>3.3v</code>
      supply pin, this will damage the regulator.</li>


      <li>  The connect the <code>RX</code> and <code>TX</code> of your USB UART to the
      <code>TX</code> and <code>RX</code> of the LoPy4 respectively.

      Please ensure you have the signal level of the UART adapter set to
      <code>3.3v</code> before connecting it.</li>

      <li>  In order to put the LoPy4 into bootloader mode to update the device firmware you will need to connect <code>P2</code> to <code>GND</code>. We recommend you connect a button between the two to make this simpler.
      </li>
      </ul>

      <img src="/gitbook/assets/uart_lopy4.png">


      </v-tab-item>
      <!-- Tab 5 -->
      <v-tab-item key="5">

      <b>Note:</b> This method of connection is not recommended for first time users. It is possible to lock yourself out of the device, requiring a USB connection.
      <ul>
      <li> In order to access the LoPy4 via WiFi you only need to provide
      <code>3.5v</code> - <code>5.5v</code> on the <code>Vin</code> pin of the LoPy4:

      <ing src="/gitbook/assets/bare_lopy4.png">
      </li>
      <li> By default, when the LoPy4 boots, it will create a WiFi access point with the following credentials:
      <ul>
        <li> SSID: <code>lopy4-wlan</code>
        <li> password: <code>www.pycom.io</code>
      </ul>
      </li>
      <li> Once connected to this network you will be able to access the telnet and FTP servers running on the LoPy4. For both of these the login details are:
      <ul>
        <li> username: <code>micro</code>
        <li>  password: <code>python</code>
        </ul>
      </li>
      </ul>
      </v-tab-item>
 </v-tabs-items>
  </v-tabs>
</div>

## Antennas

### Lora/Sigfox

{{% hint style="danger" %}}
If you intend on using the LoRa/Sigfox connectivity of the LoPy4 you **must** connect a LoRa/Sigfox antenna to your LoPy4 before trying to use LoRa/Sigfox otherwise you risk damaging the device.
{{< /hint >}}

* Firstly you will need to connect the U.FL to SMA pig tail to the LoPy4 using one of the two the U.FL connectors on the same side of the LoPy4 as the LED. The one on the left hand side is for 433MHz (LoRa only), the one of the right hand side is for 868MHz/915MHz (LoRa & Sigfox). **Note:** This is different from the LoPy.

![](/gitbook/assets/lora_sigfox_pigtail_lopy4.png)

* If you are using a pycase, you will next need to put the SMA connector through the antenna hole, ensuring you align the flat edge correctly, and screw down the connector using the provided nut.
* Finally you will need to screw on the antenna to the SMA connector.

![](/gitbook/assets/lora_sigfox_pigtail_ant_lopy4.png)

{{% hint style="danger" %}}
Since the LoRa chip only runs on one frequency band at a time you only need to connect an antenna to the appropriate U.FL connecor. You should be supplied with a the antenna that suits the band you intend using.
{{< /hint >}}

### WiFi/Bluetooth (optional)

All Pycom modules, including the LoPy4, come with a on-board WiFi antenna as well as a U.FL connector for an external antenna. The external antenna is optional and only required if you need better performance or are mounting the LoPy4 in such a way that the WiFi signal is blocked. Switching between the antennas is done via software, instructions for this can be found [here.](/firmwareapi/pycom/network/wlan)

![](/gitbook/assets/wifi_pigtail_ant_lopy4.png)
