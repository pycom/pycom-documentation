---
title: "USB Serial Converter"
aliases:
    - gettingstarted/hardware/usbserial.html
    - gettingstarted/hardware/usbserial.md
    - chapter/gettingstarted/hardware/usbserial
---
When you do not own an expansion board, it is possible to connect to your device using a USB to Serial adapter. 
> Note: We do not recommend this setup for beginners.

To connect to your device using a USB to Serial adapter, connect the following pins:

![](/gitbook/assets/uart_lopy4.png)
>Note: Please ensure the signal and voltage level of your UART adapter does not exceed 3.3V. When possible, change the settings on your adapter.

* Connect the `RX` and `TX` of your USB converter to the `TX` and `RX` of the device respectively.
* To put the device into bootloader mode to update the firmware, you will need to connect `P2` to `GND`. We recommend to connect a button for this. 
