---
title: "USB Serial Converter"
aliases:
    - gettingstarted/hardware/usbserial.html
    - gettingstarted/hardware/usbserial.md
    - chapter/gettingstarted/hardware/usbserial
---
When you do not own an expansion board, it is possible to connect to your device using a USB to Serial adapter. Make sure your USB to Serial converter is able to communicate at baudrates of 115200 and 921600. We do not recommend this setup for beginners.

To connect to your device using a USB to Serial adapter, connect the following pins:

![](/gitbook/assets/uart_lopy4.png)
>Note: Please ensure the signal and voltage level of your UART adapter does not exceed 3.3V. When possible, change the settings on your adapter.

* Connect the `RX` and `TX` of your USB converter to the `TX` and `RX` of the device respectively.
* To put the device into bootloader mode to update the firmware, you will need to connect `P2` to `GND`. We recommend to connect a button for this. 

By far the easiest way to access the USB UART REPL is via the our [Pymakr plug-in](../software/) for Atom and Visual Studio Code, though you might want to use one of the options listed below. Note that you can also use these methods when using one of the shields.

## macOS and Linux

To open a serial USB connection from macOS, any serial tool may be used; in this example, the terminal tool `screen` will be used. Open a terminal instance and run the following commands:

```bash
screen /dev/tty.usbmodem* 115200
```

To exit `screen`, press `CTRL-A CTRL-\`.

> On Linux, `picocom` or `minicom` may be used instead of `screen`. The usb serial address might also be listed as `/dev/ttyUSB01` or a higher increment for `ttyUSB`. Additionally, the elevated permissions to access the device (e.g. group uucp/dialout or use `sudo`) may be required.

## Windows

A terminal emulator is needed to open the connection from Windows. Te easiest option is to download the free program, [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).

### COM Port

To use PuTTY the serial port (COM port) in which the Pycom device is connected, must be located. In Windows, this information can be found from the 'Device Manager' program.

1. Open the Windows start menu and search for 'Device Manager'
2. The COM port for the Pycom device will be listed as 'USB Serial Device' or a similar name
3. Copy/Write down the associated COM port (e.g. `COM4`)

### Using Putty

1. With PuTTY open, click on `Session` in the left-hand panel
2. Next click the `Serial` radio button on the right and enter the associated

   COM port (e.g. `COM4`) in the `Serial Line` box and `115200` for the Speed.

3. Finally, click the `Open` button

![](/gitbook/assets/putty.png)
