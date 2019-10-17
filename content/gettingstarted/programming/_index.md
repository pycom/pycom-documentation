---
title: "Programming the modules"
aliases:
---

Now that you have connected and updated your pycom module and installed all the required software on your computer, we can begin programming your Pycom module.

If this is your first time using a Pycom module we highly recommend you read through the following pages:

* [**Introduction to MicroPython:**](micropython) This page will explain what Micropython is and its relation to Python.
* [**MicroPython Examples:**](examples) We also recommend you browse these short MicroPython examples to familiarise yourself with its syntax. This is not meant as a comprehensive guide to MicroPython programming but rather a reference to those who already know programming. If you are new to python, or programming all together, we highly recommend searching the internet for Python tutorials. There are many very good tutorials available for free and the skills you learn will be easily transferable to our platform.
* [**Your first Pymakr project:**](first-project) Once you understand what MicroPython is, this guide will take you through setting up your first Pymakr project to blink the on-board RGB LED. This guide will explain the structure of a MicroPython project as well as how to upload it to your module.

Once you are familiar with MicroPython and Pymakr, the recommended way of uploading code to your module, you can explore the pages below. These will discuss in greater detail the various mechanisms for running code on your device as well as how to recover it if something goes wrong.

* [**REPL:**](repl/) The REPL (Read Evaluate Print Loop) is an interactive terminal that allows you to type in and test your code directly on the device, just like interactive python interpreter. It can be accessed via [UART](repl/serial) or [Telnet](repl/telnet). This is accessed easiest by using Pymakr but if you wish to use other tools, this page will explain how.
* [**FTP:**](ftp) All Pycom modules start up with a WiFi access point enabled, and a simple FTP server running on it. Once connected to the WiFi network, you can use FTP to transfer files over to your device wirelessly. This can be very useful if you do not have physical access to your device.
* [**Safe Boot:**](safeboot) It is possible that some code you upload to your module will prevent you accessing the REPL or FTP server, preventing you from updating your scripts. This guide will detail how to safe boot your module and how to remove the offending scripts from it.

