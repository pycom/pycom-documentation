# 1.1.1 LoPy

* Look for the reset button on the module \(located at a corner of the board, next to the LED\).
* Locate the USB connector on the expansion board.
* Insert the LoPy module on the the expansion board with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.

\[Picture here\]

* Before connecting your module to an Expansion Board 3.0, you should update the firmware on the Expansion Board 3.0. Instructions on how to do this can be found [here](../../3.-pytrack-pysense-pyscan/installation/firmware.md).
* Look for the reset button on the module \(located at a corner of the board, next to the LED\).
* Locate the USB connector on the expansion board.
* Insert the LoPy module on the Expansion Board with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.

\[Picture here\]

* Before connecting your module to a Pysense/Pytrack/Pyscan board, you should update the firmware on the Pysense/Pytrack/Pyscan. Instructions on how to do this can be found [here](../../3.-pytrack-pysense-pyscan/installation/firmware.md).
* Look for the reset button on the LoPy module \(located at a corner of the board, next to the LED\).
* Locate the USB connector on the Pysense/Pytrack/Pyscan.
* Insert the module on the Pysense/Pytrack/Pyscan with the reset button pointing towards the USB connector. It should firmly click into place and the pins should now no longer be visible.

\[Picture here\]

Once you have completed the above steps successfully you should see the on-board LED blinking blue. This indicates the device is powered up and running.

* Firstly you will need to connect power to your LoPy. You will need to supply `3.5v`-`5.5v` to the `Vin` pin. **Note:** Do _not_ feed `3.3v` directly to the `3.3v` supply pin, this will damage the regulator.
* The connect the `RX` and `TX` of your USB UART to the `TX` and `RX` of the LoPy respectively. **Note:** Please ensure you have the signal level of the UART adapter set to `3.3v` before connecting it.
* In order to put the LoPy into bootloader mode to update the device

  firmware you will need to connect `P2` to `GND`. We recommend you connect a button between the two to make this simpler.

\[Picture here\]

**Note:** This method of connection is not recommended for first time users. It is possible to lock yourself out of the device, requiring a USB connection.

* In order to access the LoPy via WiFi you only need to provide `3.5v` - `5.5v` on the `Vin` pin of the LoPy:

\[Picture here\]

* By default, when the LoPy boots, it will create a WiFi access point with the following credentials:
  * SSID: `lopy-wlan`
  * password: `www.pycom.io`
* Once connected to this network you will be able to access the telnet and FTP servers running on the LoPy. For both of these the login details are:
  * username: `micro`
  * password: `python`

