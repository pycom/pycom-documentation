# Your first Pymakr project

This guide will take you through how to setup your first project with Pymakr and make the on-board RGB LED flash various colours.

## Creating a project in Pymakr

1. Firstly you will need to create a new, empty, directory on your computer.

   For this example we will create one called `RGB-Blink`.

2. Next you will need to open either Atom or Visual Studio Code depending on

   which you setup previously.

3. Once the text editor has loaded you will need to click `File` &gt; `Open`, and open the directory you created in step 1

{% hint style="info" %}
If you are using Atom, it is important to check at this point that Atom has successfully identified the project. The name of the directory you created in step 1 \(`RGB-Blink` in this case\) should be shown in the Pymakr pane like so:

![](../../.gitbook/assets/atom_project.png)

If this is not the case you can press `alt-ctrl-r` on Windows/Linux or `ctrl-alt-cmd-l` on macOS, in order to reload Atom and fix the issue.
{% endhint %}

4. Now that you have a project created, we need to add some files to it. A standard MicroPython project has the following structure:

```text
RGB-Blink
|-lib
|  |- some_library.py
|-boot.py
|-main.py
```

* `boot.py` This is the first script that runs on your module when it

  turns on. This is often used to connect a module to a WiFi network so that

  Telnet and FTP can be used without connecting to the WiFi AP created by the

  module and not cluttering up the `main.py` file. As a beginner you do not

  need to use a `boot.py`.

* `main.py` This script runs directly after `boot.py` and should contain

  the main code you wish to run on your device.

* `lib` It is often a good idea to split out re-usable code into libraries.

  If you want to create or use libraries created by others, you will need to

  create a `lib` directory and put the library files in this. It is important

  that you put `.py` files directly into `lib` rather than creating a directory

  tree. By default MicroPython will not detect any libraries within

  sub-directories.

For this example, you will just need to create a `main.py` file.

Now that the project structure is setup, you may wish to configure project specific settings for Pymakr e.g. Which serial port to use. On Atom you need to click the `^` button on the Pymakr pane, then click `Project Settings`. On Visual Studio Code you need to click the `All commands` button on the bottom of the windows, then click `Pymakr > Project Settings`. This creates a file called `pymakr.conf` inside your project and populates it with default settings copied over from your global settings. A detailed explanation of these settings can be found [here](../../pymakr/settings.md).

## Controlling the on-board LED

Now that you have setup and configured your project, we can move on to programming your module. The first thing we will need to do is import some libraries in order to interact with the on-board LED. The Pycom firmware comes with a large amount of libraries for standard functionality built-in. You can find out more about these in the [API documentation](../../firmwareapi/introduction.md). For this example you will need to open the `main.py` file and add the following code:

```python
import pycom
import time
```

This will import two libraries, `Pycom` which is responsible for Pycom specific features, such as the on-board LED and `time` which is a standard library used timing and delays.

You may have noticed that when you power up your Pycom module, the on-board LED blinks blue on a regular basis. This "heartbeat" is used as a way of know that your module has powered up and started correctly. Before we can change the colour of this LED we need to disable this heart beat. Below your imports you will need to add the following:

```python
pycom.heartbeat(False)
```

Now it's time to test your code. On the Pymakr pane/bottom of the window you will see a `run` button. \(If you haven't connected to your device yet, you will need to do that first\). When you click the run button, the code in the currently open file will be executed on the device, but it won't copy it to the device. After running this code, you should see that that on-board LED stops blinking blue.

Now that we can confirm the device is connected and Pymakr is able to run code on it, we can complete our script to blink the LED like so:

```python
import pycom
import time

pycom.heartbeat(False)

while True:
    pycom.rgbled(0xFF0000)  # Red
    time.sleep(1)
    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)
    pycom.rgbled(0x0000FF)  # Blue
    time.sleep(1)
```

Once you run the above script, it will run forever. You will notice this prevents you from accessing the interactive REPL on the device \(You cannot see the `>>>` prompt\). In order to stop the script, click onto the Pymakr terminal, and press `ctrl-c` on your keyboard. This should stop the script running and return you to the interactive REPL.

## Uploading to your module

In the previous section we got code running on on your Pycom module using the `run` feature of Pymakr. This is useful for quick testing but has a couple of drawbacks. Firstly the code does not remain on the device permanently. If you reboot the device, it will no longer be running your code. Secondly, it will only work if you are using libraries built into the firmware. If you need any extra libraries, these need to be copied to the device first. This is where the `upload` feature comes in. If instead of `run` you click `upload`, Pymakr will upload all the files in the project \(so long as their type is in the `sync_file_types` setting for your project\). These then persist on your device even between reboots, and allows you to use libraries from the `lib` folder in your project.

If you need to remove files from your device you have two options, either connect via FTP and manage your files that way or format the device's internal flash like so:

```python
import os
os.mkfs('/flash')
```

