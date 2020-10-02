---
title: "Getting Started"
aliases:
    - gettingstarted/introduction.html
    - gettingstarted/introduction.md
    - chapter/gettingstarted
    - getting-started
    - gettingstarted/gettingstarted
    - chapter/gettingstarted/introduction
disable_breadcrumbs: true
---

Welcome to the getting started guide for your device!
In the following guide, we will explain the basic process to get started using your Pycom products.

1. [Setting up the hardware](#step-1-setting-up-the-hardware)
2. [Setting up your computer](#step-2-setting-up-your-computer)
3. [Programming the module](#step-3-programming-your-module)
4. [Using your Expansionboard](#step-4-using-your-expansionboard)

<!-- ![](/gitbook/assets/getting_started%20%281%29.png) -->

## Step 1: Setting up the hardware

In the first part of this getting started guide, we will take you through setting up your device. Firstly we will cover how to connect the module to your computer via USB.

### Connect your board to your computer through USB

This step works the same for all our development boards and expansion boards. Insert your development board (Lopy, Wipy, etc.) into the expansion board (Pytrack, Pysense, Expansion board etc.) with the reset button and RGB LED above the USB connector like shown below. Connect an USB cable to the USB port and your computer. Now, you can talk to your device through USB, but we still need some software to upload your first program!

![](/gitbook/assets/expansion_board_3_lopy4.png)

>Note: If you do not have an expansion board, you are able to use a [USB-Serial converter](/gettinstarted/programming/usbserial/) or [WiFi](/gettingstarted/programming/ftp/) to connect.


## Step 2: Setting up your computer

Now that your module is successfully connected, you will need to install some software on your computer to interface with it. For this, we use Pymakr, a plugin for both Visual Studio Code and Atom IDE. Through either one of the environments, we can connect to the board and talk Python!

Follow the link below for the installation instructions:

- [Atom](/gettingstarted/software/atom/)

- [VS Code](/gettingstarted/software/vscode/)

Once you have installed and opened the IDE, the board should automatically show up in the terminal. If not, check if any of your other plugins are in conflict. If everything is correct, the REPL (Read Evaluate Print Loop) terminal will show the classic Python `>>>`.

>Note: If your device does not get recognized the first time on Windows, check if you need [additional drivers](/gettingstarted/software/drivers/)

## Step 3: Programming your module

Now that you have connected your device and installed Pymakr, it is time to begin programming your device!

### Running your first code
If you have any experience with python, you know that the `>>>` means we can start typing commands! Type the following commands in the REPL terminal:
```python
>>> import pycom
>>> pycom.heartbeat(False)
>>> pycom.rgbled(0x330033)
```
This will turn the RGB LED on your device purple! Notice that the REPL does not give any feedback. Only when we make a mistake, or ask it to return something will it give us a response.

### Creating a project in Pymakr
In this first project, we will make the on-board RGB LED flash different colors.

1. Firstly you will need to create a new, empty, directory on your computer. For this example we will create one called `RGB-Blink`.
2. Open the project folder you have created in your IDE.
3. Now, we will need to add some files. A standard MicroPython project will have a `lib` folder for additional libraries, and two python files: `main.py` and `boot.py`.
    * `main.py` This script runs directly after `boot.py` and should contain the main code you wish to run on your device.
    * `boot.py` This is the first script that runs on your module when it turns on. This is often used to connect a module to a network without cluttering up the `main.py` file. As a beginner you generally do not need to use a `boot.py`.
    * It is often a good idea to split out re-usable code into libraries. If you want to create or use libraries created by others, you will need to create a `lib` directory and put the library files in this. It is important that you put `.py` files directly into `lib` rather than creating a directory tree. For example, the extra sensor libraries for the Pytrack, Pysense and Pyscan are put in this folder. In this example, we will not use it.


#### Controlling the on-board RGB LED

Now that you have setup and configured your project, we can move on to programming your module. The first thing we will need to do is import some libraries in order to interact with the on-board LED. The Pycom firmware comes with a large amount of built-in modules. You can find out more about these in the [API documentation](/firmwareapi/introduction). For this example you will need to open the `main.py` file and add the following code:

```python
import pycom
import time
```

This will import two libraries, `pycom` which is responsible for Pycom specific features, such as the on-board LED and `time` which is a standard library used for timing and delays.

>You may have noticed that when you power up your Pycom module, the on-board LED blinks blue on a regular basis. This "heartbeat" is used as a way of know that your module has powered up and started correctly.

Before we can change the colour of this LED we need to disable this heart beat. Below your imports you will need to add the following:


```python
pycom.heartbeat(False)
```


Now it's time to test your code. On the Pymakr pane, you will see a `run` button, but als an `upload (to device)` button. For now, we will use `run`.

After running the example code above, you should see that that on-board LED stops blinking blue. Now, we can complete our script to blink the LED like so:

```python
import pycom
import time

pycom.heartbeat(False)

while True:
    #colors in hexadecimal (0xRRGGBB)
    pycom.rgbled(0xFF0000)  # Red
    time.sleep(1)
    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)
    pycom.rgbled(0x0000FF)  # Blue
    time.sleep(1)
```

Once you run the above script, it will run forever (due to the infinite `While`-loop). In order to stop the script, click onto the Pymakr terminal, and press `ctrl-c` on your keyboard. This stops the script and returns to the interactive REPL.

Great work, the RGB-LED on your device should now blink in red, green and blue

### Uploading to your module

In the previous section we got code running on on your Pycom module using the `run` feature of Pymakr. This is useful for quick testing but has a couple of drawbacks. Firstly the code does not remain on the device permanently. If you reboot the device, it will no longer be running your code. Secondly, it will only work if you are using libraries built into the firmware. If you need any extra libraries, these need to be copied to the device first. This is where the `upload` feature comes in. If instead of `run` you click `upload`, Pymakr will upload all the files in the project. These then persist on your device even between reboots, and allows you to use libraries from the `lib` folder in your project.

If you need to remove files from your device you can use the following commands:

```python
>>> import os
>>> os.fsformat('/flash')
```

## Step 4: Using your expansionboard
From here on, you can continue to use the additional features of your expansionboard:
>Note The Expansionboard requires no additional libraries and all functions work out of the box!

|[ Pygate](/tutorials/expansionboards/pygate/)| [Pysense](/tutorials/expansionboards/pysense/) | [Pysense 2.0 X](/tutorials/expansionboards/pysense2/)| [Pytrack](/tutorials/expansionboards/pytrack/)| [Pytrack 2.0 X](/tutorials/expansionboards/pytrack2/)| [PyScan ](/tutorials/expansionboards/pyscan/)|
|:---|:---|:---|:---|:---|:---|
| ![](/gitbook/assets/expansion_board_3_lopy4.png)|![](/gitbook/assets/pysense_icon.png) | ![](/gitbook/assets/pytrack_icon.png)| ![](/gitbook/assets/pytrack_icon.png)| ![](/gitbook/assets/pytrack_icon.png)| ![](/gitbook/assets/pytrack_icon.png) |

## Step 5: Connecting to a network

|[WiFi](/tutorials/networks/wlan/) | [LoRa](/tutorials/networks/lora/) | [SigFox](/tutorials/networks/sigfox/) | [BLE](/tutorials/networks/ble/) | [LTE](/tutorials.networks/lte/) | Ethernet |
|:---|:---|:---|:---|:---|:---|
## Further references
Now that we got the basic example running, you can continue with the links below.


* [More examples](/tutorials/)

* [Documentation](/firmwareapi/)

* [Get started using the FTP and Telnet Server](/gettingstarted/programming/ftp/)

* [Connect using Pybytes](/pybytes/getstarted/)

* [Registering with a network](/gettingstarted/registration/)

* [Updating the firmware of your device](/updatefirmware/)


<!--## Step 4: (Optional) Connect through WiFi (Telnet & FTP)

On boot, your device will initialize an Access Point (AP), together with a FTP and telnet server, to which you can communicate over WiFi. This feature can be very useful if you do not have physical access to your device. Look in your WiFi connections for the SSID: `xxpy-wlan-####`. Connect to it using the default password: ` `. -->
