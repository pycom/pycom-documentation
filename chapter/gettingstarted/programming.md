#Programming Your Device

There are multiple ways you can get your micropython onto a Pycom module:

 - [**REPL:**](./programming/repl/README.md) The REPL (Read Evaluate Print Loop)
is an interactive terminal that allows you to type in and test your code
directly on the device, just like interactive python interpreter. It can be
accessed via [UART](./programming/repl/serial.md) or
[Telnet](./programming/repl/telnet.md).

 - [**Pymakr:**](../pymakr/README.md) Using the REPL as a base, our Pymakr
 plug-in for Atom and Visual Studio Code allows you to quickly upload code files
 directly from the text editor to your Pycom modules.

- [**FTP:**](./programming/FTP.md) All Pycom modules start up with a WiFi access
point enabled, and a simple FTP server running on it. Once connected to the
WiFi network, you can use FTP to transfer files over to your device wirelessly.
