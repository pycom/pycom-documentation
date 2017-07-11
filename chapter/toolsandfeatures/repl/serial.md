# Serial USB REPL (UART)

To use the REPL, a Pycom device must be connected to the host computer with a USB connection either to an expansion board or to serial converter (wired to one of the two UART buses).

In order to connect to the REPL over USB serial, there are multiple methods. Detailed below are the explanations of how to do it in MacOS, Linux and Windows.

### MacOS and Linux

To open a serial USB connection from MacOS, any serial tool may be used; in this example, the terminal tool ``screen`` will be used.

Open a terminal instance and run the following commands:

```bash
$ screen /dev/tty.usbmodem* 115200
```

Upon exiting ``screen``, press CTRL-A CTRL-\. If the keyboard does not support the \-key (i.e. an obscure combination for \ like ALT-SHIFT-7 is required), the key combination can be remapped for the quit command:

- create ~/.screenrc
- add bind ``q`` to the exit command

This will allow screen to exited by pressing CTRL-A Q.

{% hint style='info' %}
On Linux, ``picocom`` or ``minicom`` may be used instead of ``screen``. The usb serial address might also be listed as /dev/ttyUSB01 or a higher increment for ttyUSB. Additionally, the elevated permissions to access the device (eg group uucp/dialout or use sudo) may be required.
{% endhint %}


### Windows

To use the serial USB REPL with Windows, first ensure that the FTDI drivers are installed or install them from [here](). A terminal emulator is needed to open the connection from Windows; the easiest option is to download the free program, [PuTTY]().

##### COM Port

To use PuTTY the serial port (COM port) in which the Pycom device is connected, must be located. In Windows, this information can be found from the 'Device Manager' program.

1. Open the Windows start menu and search for 'Device Manager'
2. The COM port for the Pycom device will be listed as 'USB Serial Device' or a similar name
3. Copy/Write down the associated COM port (e.g. COM4)

##### Using Putty

1. With PuTTY open, click on ``Session`` in the left-hand panel
2. Next click the ``Serial`` radio button on the right and enter the associated COM port (e.g. COM4) in the ``Serial Line`` box
3. Finally, click the ``Open`` button
