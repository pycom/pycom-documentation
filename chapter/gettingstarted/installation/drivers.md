# Drivers

## Linux
You should not need to install any drivers for our devices to be recognised by
linux. You may how ever need to adjust permissions to make sure you have access
to the serial port. On most distributions this can be done by adding your user
to the `dialout` user group. Please check the specific instructions for your
linux distribution for how to do this.

## Mac OS
On Mac OS you shouldn't need to do anything special to get our device to work.

## Windows
Depending on which version of windows, and which products you are using you
maybe be required to install drivers.

 - **Expansion Board 2.0:** This device is based around a FTDI USB to UART chip.
The FTDI drivers can be obtained from [here](http://www.ftdichip.com/Drivers/VCP.htm).

- **Pytrack/Pysense**: The windows drivers, along with instructions on how to
install them can be found in the
[Pytrack/Pysense documentation.](../../pytrackpysense/installation/drivers.md)
When updating the firmware for these boards you will also need to install DFU
drivers, instructions on how to do this can be found
[here.](../../pytrackpysense/installation/firmware.md)
