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


<!-- ![](/gitbook/assets/getting_started%20%281%29.png) -->

## Step 1: Setting up the hardware

Congratulations on your Pycom module! In the first part of this getting started guide, we will take you through setting up your device. Firstly we will cover how to connect the module to your computer via USB.

#### Connect your board to your computer through USB

This step works the same for all our development boards and expansion boards. Insert your development board (Lopy, Wipy, etc.) into the expansion board (Pytrack, Pysense, etc.) with the reset button and RGB LED above the USB connector like shown below. Connect an USB cable to the USB port and your computer. Now, you can talk to your device through USB, but we still need some software to upload your first program!

![](/gitbook/assets/expansion_board_3_lopy4.png)

>Note: If you do not have an expansion board, you are able to use a [USB-Serial converter](/gettinstarted/programming/usbserial/) or [WiFi](/gettingstarted/programming/ftp/) to connect.

# Step 2: Setting up your computer

Now that your module is successfully connected, you will need to install some software on your computer to interface with it. For this, we use Pymakr, a plugin for both Visual Studio Code or Atom IDE. Through one of the environments, we can connect to the board and talk python! Follow the link below for the installation instructions:

- [Atom](/gettingstarted/software/atom/)

- [VS Code](/gettingstarted/software/vscode/)

Once you have installed and opened the IDE, the board should automatically show up in the terminal. If not, check if any of your other plugins are in conflict.

If everything is correct, the terminal will show `>>>`.

# Step 3: Programming your module

Now that you have a connected module and all the required software installed it is time to begin programming your device!

In this first example, we will make the on-board RGB LED flash different colors.
### Creating a project in Pymakr

1. Firstly you will need to create a new, empty, directory on your computer. For this example we will create one called `RGB-Blink`.

2. Next you will need to open either Atom or Visual Studio Code depending on which you setup previously.

3. Once the text editor has loaded you will need to click `File` &gt; `Open`, and open the directory you created in step 1

If you are using Atom, it is important to check at this point that Atom has successfully identified the project. The name of the directory you created in step 1 (`RGB-Blink` in this case) should be shown in the Pymakr pane like so:

![](/gitbook/assets/atom_project.png)

>If this is not the case you can press `alt-ctrl-r` on Windows/Linux or `ctrl-alt-cmd-l` on macOS, in order to reload Atom and fix the issue.


4. Now that you have created a poject, we need to add some files. A standard MicroPython project will have a `lib` folder for additional libraries, and two python files: `main.py` and `boot.py`.

    * `main.py` This script runs directly after `boot.py` and should contain the main code you wish to run on your device.

    * `boot.py` This is the first script that runs on your module when it turns on. This is often used to connect a module to a network without cluttering up the `main.py` file. As a beginner you generally do not need to use a `boot.py`.

    * It is often a good idea to split out re-usable code into libraries. If you want to create or use libraries created by others, you will need to create a `lib` directory and put the library files in this. It is important that you put `.py` files directly into `lib` rather than creating a directory tree. By default MicroPython will not detect any libraries within sub-directories.

Your file structure should look something like this:
![]()

### Controlling the on-board RGB LED

Now that you have setup and configured your project, we can move on to programming your module. The first thing we will need to do is import some libraries in order to interact with the on-board LED. The Pycom firmware comes with a large amount of libraries for standard functionality built-in. You can find out more about these in the [API documentation](/firmwareapi/introduction). For this example you will need to open the `main.py` file and add the following code:

```python
import pycom
import time
```

This will import two libraries, `Pycom` which is responsible for Pycom specific features, such as the on-board LED and `time` which is a standard library used timing and delays.

You may have noticed that when you power up your Pycom module, the on-board LED blinks blue on a regular basis. This "heartbeat" is used as a way of know that your module has powered up and started correctly. Before we can change the colour of this LED we need to disable this heart beat. Below your imports you will need to add the following:


```python
pycom.heartbeat(False)
```


Now it's time to test your code. On the Pymakr pane/bottom of the window you will see a `run` button. (If you haven't connected to your device yet, you will need to do that first). When you click the run button, the code in the currently open file will be executed on the device, but it won't copy it to the device. After running this code, you should see that that on-board LED stops blinking blue.

Now that we can confirm the device is connected and Pymakr is able to run code on it, we can complete our script to blink the LED like so:

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

Once you run the above script, it will run forever. You will notice this prevents you from accessing the interactive REPL on the device (You cannot see the `>>>` prompt). In order to stop the script, click onto the Pymakr terminal, and press `ctrl-c` on your keyboard. This should stop the script running and return you to the interactive REPL.

Great work, the RGB-LED on your device should now blink in red, green and blue

### Uploading to your module

In the previous section we got code running on on your Pycom module using the `run` feature of Pymakr. This is useful for quick testing but has a couple of drawbacks. Firstly the code does not remain on the device permanently. If you reboot the device, it will no longer be running your code. Secondly, it will only work if you are using libraries built into the firmware. If you need any extra libraries, these need to be copied to the device first. This is where the `upload` feature comes in. If instead of `run` you click `upload`, Pymakr will upload all the files in the project (so long as their type is in the `sync_file_types` setting for your project). These then persist on your device even between reboots, and allows you to use libraries from the `lib` folder in your project.


If you need to remove files from your device you can use the following commands:

```python
import os
os.fsformat('/flash')
```

## Getting started with
From here on, you can continue to use the additional features of your expansionboard:

|[ Pygate](/tutorials/expansionboards/pysense/)| [Pysense](/tutorials/expansionboards/pysense/) | [Pysense 2.0 X](/tutorials/expansionboards/pysense/)| [Pytrack](/tutorials/expansionboards/pysense/)| [Pytrack 2.0 X](/tutorials/expansionboards/pysense/)| [PyScan ](/tutorials/expansionboards/pysense/)|
|:---|:---|:---|:---|:---|:---|
| ![](/gitbook/assets/expansion_board_3_lopy4.png)|![](/gitbook/assets/pysense_icon.png) | ![](/gitbook/assets/pytrack_icon.png)| ![](/gitbook/assets/pytrack_icon.png)| ![](/gitbook/assets/pytrack_icon.png)| ![](/gitbook/assets/pytrack_icon.png) |


# Step 4: Further reading
Now that we got the basic example running, you can continue with the links below.

* [More examples](/tutorials/)

* [Documentation](/firmwareapi/)

* [Get started using the FTP and Telnet Server](/gettingstarted/programming/ftp/)

* [Connect using Pybytes](/pybytes/getstarted/)

* [Registering with a network](/gettingstarted/registration/)

* [Updating the firmware of your device](/updatefirmware/)


<!--## Step 4: (Optional) Connect through WiFi (Telnet & FTP)

On boot, your device will initialize an Access Point (AP), together with a FTP and telnet server, to which you can communicate over WiFi. This feature can be very useful if you do not have physical access to your device. Look in your WiFi connections for the SSID: `xxpy-wlan-####`. Connect to it using the default password: ` `. -->
