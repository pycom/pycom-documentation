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

<iframe width="560" height="315" src="https://www.youtube.com/embed/qydlJKRDzFs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Pymakr Git Demo

<iframe width="560" height="315" src="https://www.youtube.com/embed/-yIdZmY6N3g" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Let's get started!

There are two ways in which you can use Pymakr online.
1. Go to [your device](https://pybytes.pycom.io/devices) and select the `Pymakr Online` tab. This method allows you to make quick changes to the Python code on your device and upload it. This is the method we use below.

![](/gitbook/assets/pybytes/pymakr-online/opening-pymakr-device.png)

2. Start a new project on the [Pymakr](https://pybytes.pycom.io/pymakr) tab in Pybytes. There are several different types you can choose from, including a link to your Github repository! Later, we can link the project to a release.

![](/gitbook/assets/pybytes/pymakr-online/opening-pymakr-project.png)

## Using Pymakr Online

1. When you open Pymakr Online, you will see the following

![](/gitbook/assets/pybytes/pymakr-online/initial.png)


  * On the left we see the files. Depending on where you started, the online environment will first load with the files you last used. If the device is online, it will automatically try to `Refresh Hierarcy` and synchronise the content. You can click the `Refresh Hierarcy` icon next to your device name to manually update the online filestructure. The online editor will automatically try to connect.
  * In the top right, the connection status is displayed. Every so often, you will see a ping being sent out to the device to check if it is still connected. If you started pymakr from a project, you will also see the `Save/Export` button here as well.
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
3. After adding the code, a `Save and Upload` button will appear (or you can use the `Save/Export` button already present), allowing you to upload code to the device. Clicking this will upload and reboot the device. The device will restart and go offline for a second. Then come back online and show the RGB LED blinking in three different colors.

![](/gitbook/assets/pybytes/pymakr-online/upload.png)

>Note that if you make a syntax error, the device will come back online but not throw any error in the REPL.

## Creating a Project

1. Now that you know how to use the Pymakr Online environment, we can create a project (if you have not already). If you just followed the example above, go to the [Pymakr](https://pybytes.pycom.io/pymakr#) tab and click on `Import from Existing Device`.

![](/gitbook/assets/pybytes/pymakr-online/starting-project.png)

2. Select your device and either `Retrieve from Cloud` or `Request from device`, depending on where the latest version of your code is. This will load the hierarchy and bring up the Pymakr Online interface.

3. Make your changes and then click the `Save/Export` button, this offers three options. This time, we use `Include in Release`. It will ask us to create a new project, or add to an already existing project.

![](/gitbook/assets/pybytes/pymakr-online/new-project.png)


4. Assuming you have not create a project yet, creat a new one, and name it `My first project` and click next.

![](/gitbook/assets/pybytes/pymakr-online/new-project1.png)

5. Here, it asks for the networks we want to use. For now, lets select WiFi.

![](/gitbook/assets/pybytes/pymakr-online/new-project1.png)

6. In the next screen, it asks for the WiFi network you want to use, select the one that is most convenient for you.

7. Now that we have successfully create a project. Using projects, you can add unlimited devices and keep them all up-to-date Over The Air (OTA) with new Pybytes configuration files, Python code or update the firmware.
