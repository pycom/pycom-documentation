---
title: "Pymakr Online"
aliases:
  - pymakr-online/introduction
---

On this page, we discuss the functionality of Pymakr Online. 

## What is Pymakr Online?

Pymakr Online is an online IDE for your MicroPython projects. We brought our Pymakr Plugin for Atom and Visual Studio code into Pybytes as an IDE, so you won't necessarily need to have those code editors installed anymore in order to work with your Pycom devices.

## What does Pymakr Online offer you?

* Everything you would expect from a code editor: syntax highlighting, auto complete, multi tabs, file tree, search box etc.
* REPL terminal
* Import from multiple sources (blank/device/project/Github repository), export to a zip file/device/project
* Device activity indicator: track what's going between Pymakr Online and your device.

## Let's get started!

There are two ways in which you can use Pymakr online. 
1. Go to [your device](https://pybytes.pycom.io/devices) and select the `Pymakr Online` tab. This method allows you to make quick changes to the Python code on your device and upload it.

![](/gitbook/assets/pybytes/pymakr-online/opening-pymakr-device.png)

2. Start a new project on the [Pymakr](https://pybytes.pycom.io/pymakr) tab in Pybytes. There are several different types you can choose from, including a link to your Github repository! Later, we can link the project to a release. 

![](/gitbook/assets/pybytes/pymakr-online/opening-pymakr-project.png)

## Using Pymakr Online

1. When you open Pymakr Online, you will see the following

![](/gitbook/assets/pybytes/pymakr-online/initial.png)


  * On the left we see the files. Depending on where you started, the online environment will first load with the files you last used. If the device is online, it will automatically try to `Refresh Hierarcy` and synchronise the content. You can click the `Refresh Hierarcy` icon next to your device name to manually update the online filestructure. The online editor will automatically try to connect.
  * In the top right, the connection status is displayed. Every so often, you will see a ping being sent out to the device to check if it is still connected. 
  * And finally, on the bottom, the REPL is displayed, this works exactly the same as the REPL you are used to in VSCode or Atom. Everything you type in there will be duplicated to the REPL over USB. 

2. Open the `main.py` file, or, when not available, create one by right clicking on the device name to `Create File`. Here, we can write our own python code in the main editor. You can use the example we added below to try it out. 

![](/gitbook/assets/pybytes/pymakr-online/open-file.png)

  ```python
  import pycom
  import time
  pycom.heartbeat(False)
  while(True):
    pycom.rgbled(0xAA0000)
    time.sleep(0.5)
    pycom.rgbled(0xAA00AA)
    time.sleep(0.5)
    pycom.rgbled(0x00AA00)
    time.sleep(0.5)
  ```
3. After adding the code, a `Save and Upload` button will appear, allowing you to upload code to the device. Clicking this will upload and reboot the device. The device will restart and go offline for a second. Then come back online and show the RGB LED blinking in three different colors.

![](/gitbook/assets/pybytes/pymakr-online/upload.png)

>Note that if you make a syntax error, the device will come back online but not throw any error in the REPL.

4. Now that you know how to use the Pymakr Online environment, we can creat a project.

## The differences between the two ways of opening Pymakr online

### From the device page

![](/gitbook/assets/pymakr-online/pymakr-linked.jpg)

If you have opened Pymakr Online from a device page, you may notice: 

1. Device activity indicator. To track what's going on between the Pymakr Online and the linked device.
2. REPL terminal.
3. Save and upload current file. That will save that file on the cloud and upload it to your device.
4. Refresh hierarchy. That will request the device its hierarchy, in case the files structure has been changed. 
5. Download file. That will request the file from the device, forcing the download of it. Warning: that will override your changes in case you haven't uploaded the file to the device. 

### From the Pymakr initial page

![](/gitbook/assets/pymakr-online/pymakr-no-device.jpg)

1. Save/export button. 

Since there's no device linked in this way of opening Pymakr Online, there are no device related actions here (download file, device activity indicator etc). Instead, you decide what you are going to do with your code:

![](/gitbook/assets/pymakr-online/pymakr-export-modal.png)

*Modal opened after clicking on Save/Export button*
