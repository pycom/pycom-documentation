---
title: "Modem Firmware Update"
aliases:
    - tutorials/lte/firmware.html
    - tutorials/lte/firmware.md
    - chapter/tutorials/lte/firmware
---

**This article is only related to GPy, FiPy, and G01 boards**

>Note: The LTE modem updater is integrated in the latest stable **pybytes-firmware** release, make sure you update your device firmware first [here](/updatefirmware/device/)

Before updating the modem firmware, check the current modem firmware version using:
```python
>>> import sqnsupgrade
>>> sqnsupgrade.info()
```
The bottom two lines explain the LTE firmware edition:

* LR5.xx is for CAT-M1
* LR6.xx is for NB-IoT

The firmwares for CAT-M1 and NB-IoT are fundamentally different and cannot be used interchangable. For security reasons, the modem firmware files are password protected. In order to download them, head to https://forum.pycom.io and become a member (if you aren't already) and go [here](https://forum.pycom.io/topic/4020/firmware-files-for-sequans-lte-modem-now-are-secured) for the credentials. (On the forum: Announcements & News &rarr; Announcements for members only &rarr; the Firmware Files)
You can find the firmwares listed [here](https://software.pycom.io/downloads/sequans2.html).

Our newest products ship with the modem firmware version CAT-M1 5.4.1.0-50523. At the moment it is not possible to update the modem to that version.

There are several different ways to update the firmware of the LTE modem:
1. [Flash](#flash) (slow)
1. [SD card](#sd-card) (fastest)
1. [USB](#usb) (medium)
1. [Wireless](#wireless) (slowest)

>In case of any failure or interruption to the process of LTE modem upgrade you can repeat the same steps after **power cycling to the board (i.e disconnecting and reconnecting power)**. Just pressing the reset button is not enough.



## Note on Updating to CAT-M1 5.2-48829

This update has to be done in two steps and is a full upgrade, meaning you can only use the steps for 'SD Card' or 'USB'.
1. update with `CATM1-5.2-48829-1.dup`
    
    For the first update you have to also specify `load_fff=False`. Using the SD cad method, it would be like this:

    ```
    sqnsupgrade.run('/sd/CATM1-5.2-48829-2.dup', load_fff=False)
    ```


    wait until the LTE modem resets and prints out something similar to this:

    ```
    Resetting............
    Your modem has been successfully updated.
    Here is the current firmware version:
    UE5.0.0.0d
    LR5.1.1.0-39529
    IMEI: xyz
    ```
2. update with `CATM1-5.2-48829-2.dup`

    ```
    sqnsupgrade.run('/sd/CATM1-5.2-48829-2.dup')
    ```
    At the end reset the board.

## Flash

>Note: For Flash updates, we currently only support the use of upgdiff- files. If there is no upgdiff- file for your version available, try to use another method. 

1. Copy the firmware update file you want to use in your project folder and click `upload to device` in the Pymakr plugin. Make sure the first 5 numbers match the current version of your modem firmware. Uploading might take a while because of the large filesize.
    > Note: If the firmware does not sync to your device, open the Pymakr settings &rarr; project settings and add `"dup"` to the entry `"sync_file_types"`. This will create a `pymakr.conf` file in your project and allow you to sync `.dup` files to the device using pymakr.
2. After uploading the file, you can run the following commands
    ```python
    import sqnsupgrade
    sqnsupgrade.run('upgdiff_old-to-new.dup')
    ```
3. The update takes about 5 minutes. Note that the update may seem to 'stall' around 7-10% and again at 99%. This is completely normal. 
    >Note: **Do not disconnect power to the module during the updating process**
4. The updater will show the new `SYSTEM VERSION` when it is done, and return control to REPL.

## SD Card

1. Format the SD card using your computer, or the following commands:
    ```python
    from machine import SD
    import os

    sd = SD()
    os.mount(sd, '/sd')     # mount it
    os.fsformat('/sd')    # format SD card
    fs = os.mkfat(sd)
    print(os.listdir('/sd'))     # list its content
    ```
    The last command should return an empty list.

2. Copy all the files from the `.zip` archive to the SD card. You can either use the [FTP server](gettingstarted/programming/ftp/) or insert the SD card in your computer and copy the files through there. 
    >Note: Do not forget to mount the SD card when re-inserting it.

3. Once the files are on the SD card, you can flash the LTE modem using one of the following commands:
    ```python
    import sqnsupgrade
    sqnsupgrade.run('/sd/upgdiff_old-to-new.dup')
    # if no upgdiff is available, run the following instead
    # sqnsupgrade.run('/sd/name.dup')
    # WARNING! If you are updating from version 33080, use the updater.elf file as well, this is not needed for the upgdiff file.
    # sqnsupgrade.run('/sd/name.dup', '/sd/updater.elf')

    ```
    >Note: Replace `name.dup` or `upgdiff_old-to-new.dup` with the actual filename. There are different versions for `CAT-M1`  and `NB-IoT`

4. The command will now make sure the firmware is updated. This takes about 5 minutes. Note that the update may seem to 'stall' around 7-10% and again at 99%. This is completely normal. 
    >Note: **Do not disconnect power to the module during the updating process**
5. The updater will show the new `SYSTEM VERSION` when it is done, and return control to REPL.


## USB
If you do not have an SD card available, you can update the firmware over USB. For this you will need to install 

* [Python 3](https://www.python.org/downloads)
* [PySerial](https://pythonhosted.org/pyserial/pyserial.html#installation)
* [sqnsupgrade python script](https://github.com/pycom/pycom-libraries/tree/master/lib/sqnsupgrade)

1. On the Pycom module run the following command to allow direct UART communication to the LTE modem:
    ```python
    import sqnsupgrade
    sqnsupgrade.uart(True)
    ```
1. You will see a response similar to this:
    ```python
    <<< Welcome to the SQN3330 firmware updater [1.2.6] >>>
    >>> GPy with firmware version 1.20.3.b2
    Preparing modem for upgrade...
    FFH mode is not necessary... ignoring!
    Do not specify updater.elf when updating!
    Attempting AT wakeup...
    Going into MIRROR mode... please close this terminal to resume the upgrade via UART
    ```
1. Take note of the Serial port used and close the REPL.

1. On the computer go to the directory where you saved the `sqnsupgrade` script and run the following commands in the command line / terminal
    ```python
    $ python3
    >>> import sqnsupgrade
    >>> sqnsupgrade.run('Serial_Port', '/path/to/upgdiff_old-to-new.dup')
    # If no upgdiff file is available, use the following
    # >>> sqnsupgrade.run('Serial_Port', '/path/to/name.dup')
    # WARNING! If you are updating from version 33080, use the updater.elf file as well, this is not needed for the upgdiff file
    # >>> sqnsupgrade.run('Serial_Port', '/path/to/name.dup', '/path/to/updater.elf')
    ```
    >Note: Replace the paths and `name.dup` with the actual files. There are different versions for `CAT-M1`  and `NB-IoT`

1. The update is now running. Note that the update may seem to 'stall' around 7-10% and again at 99%. This is completely normal. 
    >Note: **Do not disconnect power to the module during the updating process**
1.  The updater will show `SYSTEM VERSION` when it is done, and return control to REPL.


## Wireless

To update the modem firmware wirelessly, you can follow the [Flash](/updatefirmware/ltemodem/#flash) guide. Upload the files through the [FTP Server and communicate throught Telnet](/gettingstarted/programming/ftp/), or use [Pybytes Pymakr](https://pybytes.pycom.io/pymakr)


<!--
# Old content


Please also use the file upgdiff_33080-to-39529.dup (1.2M) from the archive.

    ```python
    import sqnsupgrade
    sqnsupgrade.run('upgdiff_33080-to-39529.dup', 'updater.elf')
    ```

We are using `CATM1-39529.zip` and `NB1-37781.zip` as examples in this tutorial.

After unpacking the zip archive, you will find each firmware packages contains two files, one being the firmware file (e.g. `CATM1-39529.dup` or `NB1-37781.dup`) and the `updater.elf` file, which is required when using the "recovery" firmware update method or if a previous upgrade failed and the modem is in recovery mode.

Please note that the `updater.elf` file is only around 300K so you can also store it inside the flash file system of the module. The firmware dup files will NOT fit into the available `/flash` file system on the module, so you either need to use an SD card or upload it directly from your computer.

>To upgrade from the previous CAT-M1 firmware 38638 you can simply upload the upgdiff_38638-to-39529.dup file (452K) from the CATM1-39529.zip archive into the /flash directory on your module and run:
```python
import sqnsupgrade
sqnsupgrade.run('upgdiff_38638-to-39529.dup')
```
If you are updating the Sequans firmware on your module for the first time, please use instead the file upgdiff_33080-to-39529.dup (1.2M) from the same archive.
Similar upgrade packages are available for the NB-IoT firmwares.


## Via SD card

To transfer the firmware files onto the SD card you have two options:

1. Format your SD card as with the FAT file system and then copy the files onto the card using your computer
2. Make sure your SD card has an MBR and a single primary partition, the format it directly on the module, mount it and transfer the firmware files onto the SD card using FTP. Please ensure the transfer is successful and that each file on the module has the same size as the original file on your PC.

```python

from machine import SD

sd = SD()
os.fsformat('/sd')    # format SD card
from machine import SD
sd = SD()
fs = os.mkfat(sd)
os.mount(fs, '/sd')     # mount it
os.listdir('/sd')      # list its content
```

Once you copied/uploaded the firmware files on to the SD card you can flash the LTE modem using the following command:

To flash the CAT-M1 firmware onto your device using the recovery method:

```python

import sqnsupgrade
sqnsupgrade.run('/sd/CATM1-39529.dup', '/sd/updater.elf')
```

To flash the NB-IoT firmware onto your device using the recovery method:

```python

import sqnsupgrade
sqnsupgrade.run('/sd/NB1-37781.dup', '/sd/updater.elf')
```

Please note you can directly flash the desired firmware onto your module, it is not necessary to upgrade to the latest CAT-M1 firmware before switching to NB-IoT.

If you have already mounted the SD card, please use the path you used when mounting it. Otherwise, if an absolute path other than `/flash` is specified, the script will automatically mount the SD card using the path specified.

Once update is finished successfully you will have a summary of new updated versions. The full output from the upgrade will looks similar to this:

```text
<<< Welcome to the SQN3330 firmware updater >>>
Attempting AT wakeup...
Starting STP (DO NOT DISCONNECT POWER!!!)
Session opened: version 1, max transfer 8192 bytes
Sending 54854 bytes: [########################################] 100%
Bootrom updated successfully, switching to upgrade mode
Attempting AT auto-negotiation...
Session opened: version 1, max transfer 2048 bytes
Sending 306076 bytes: [########################################] 100%
Attempting AT wakeup...
Upgrader loaded successfully, modem is in upgrade mode
Attempting AT wakeup...
Starting STP ON_THE_FLY
Session opened: version 1, max transfer 8192 bytes
Sending 5996938 bytes: [########################################] 100%
Code download done, returning to user mode
Resetting (DO NOT DISCONNECT POWER!!!)................
Upgrade completed!
Here's the current firmware version:

SYSTEM VERSION
==============
  FIRMWARE VERSION
    Bootloader0  : 5.1.1.0 [33080]
    Bootloader1  : 5.1.1.0 [38638]
    Bootloader2* : 5.1.1.0 [38638]
    NV Info      : 1.1,0,0
    Software     : 5.1.1.0 [38638] by robot-soft at 2018-08-20 09:51:46
    UE           : 5.0.0.0d
  COMPONENTS
    ZSP0         : 1.0.99-13604
    ZSP1         : 1.0.99-12341
```

{{% hint style="info" %}}
Please note that the firmware update may seem to "stall" around 7-10% and again at 99%. This is not an indication of a failure but the fact that the modem has to do some tasks during and the updater will wait for these tasks to be completed. Unless the upgrade process is hanging for more than 5 minutes, **do not interrupt the process** as you will have to start again if you don't finish it. It may also take several minutes for the updater to load before responding to the AT wakeup command.
{{% /hint %}}

After you have updated your modem once using the recovery method, you can now flash your modem again using just the `CATM1-38638.dup` or `NB1-37781.dup` file without specifying the `updater.elf` file. However, should the upgrade fail, your modem may end up in recovery mode and you will need the `updater.elf` file again. The updater will check for this and prompt you if using the `updater.elf` file is necessary.

Example output using just the firmware file:

```text
<<< Welcome to the SQN3330 firmware updater >>>
Attempting AT wakeup...

Starting STP ON_THE_FLY
Session opened: version 1, max transfer 8192 bytes
Sending 5996938 bytes: [########################################] 100%
Code download done, returning to user mode
Resetting (DO NOT DISCONNECT POWER!!!)............................................................................
Upgrade completed!
Here's the current firmware version:

SYSTEM VERSION
==============
  FIRMWARE VERSION
    Bootloader0  : 5.1.1.0 [33080]
    Bootloader1* : 5.1.1.0 [38638]
    Bootloader2  : 5.1.1.0 [38638]
    NV Info      : 1.1,0,0
    Software     : 5.1.1.0 [38638] by robot-soft at 2018-08-20 09:51:46
    UE           : 5.0.0.0d
  COMPONENTS
    ZSP0         : 1.0.99-13604
    ZSP1         : 1.0.99-12341
```

## Via UART Serial Interface

If you can't use an SD card to hold the firmware images, you can use the existing UART interface you have with the board to load these firmware files from your Computer.

You will need the following software installed on your computer:

1. [Python 3](https://www.python.org/downloads), if it's not directly available through your OS distributor
2. [PySerial](https://pythonhosted.org/pyserial/pyserial.html#installation)

You will also need to download the following Python scripts: [https://github.com/pycom/pycom-libraries/tree/master/lib/sqnsupgrade](https://github.com/pycom/pycom-libraries/tree/master/lib/sqnsupgrade)

**Important**: When upgrading your modem for the first time, even if you have updated it in the past with the old firmware update method, you **MUST** use the "recovery" upgrade method described below. Otherwise, you will risk breaking your module.

You can upload the `updater.elf` file to the module's flash file system rather than uploading it via UART directly to the modem, which will slightly increase the speed of the upgrade.

First, you need to prepare your modem for upgrade mode by using the following commands.

### **Commands to run on the Pycom module**

To use the recovery method:

```python

import sqnsupgrade
sqnsupgrade.uart(True)
```

To use the recovery method using the `updater.elf` file on the module**:**

```python

 import sqnsupgrade
 sqnsupgrade.uart(True,'/flash/updater.elf')
```

To use the normal method:

```python

 import sqnsupgrade
 sqnsupgrade.uart()
```

After this command is executed a message will be displayed asking you to close the port.

```text
Going into MIRROR mode... please close this terminal to resume the upgrade via UART
```

### **Commands to be run on your computer**

You must close the terminal/Atom or Visual Studio Code console to run the following commands from your computer:

Go to the directory where you saved the `sqnsupgrade` scripts and run the following commands in terminal:

When using the recovery method:

```python

$ python3
Python 3.6.5 (default, Apr 25 2018, 14:23:58)
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import sqnsupgrade
>>> sqnsupgrade.run('Serial_Port', '/path/to/CATM1-39529.dup', '/path/to/updater.elf')
```

When using the standard method (or if the `updater.elf` was loaded on the module):

```python

 $ python3
 Python 3.6.5 (default, Apr 25 2018, 14:23:58)
 [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)] on darwin
 Type "help", "copyright", "credits" or "license" for more information.
 >>>
 >>> import sqnsupgrade
 >>> sqnsupgrade.run('Serial_Port', '/path/to/CATM1-39529.dup')
```

Please note that the firmware update may seem to "stall" around 7-10% and again at 99%. This is not an indication of a failure but the fact that the modem has to do some tasks during and the updater will wait for these tasks to be completed. Unless the upgrade process is hanging for more than 5 minutes, **do not interrupt the process** as you will have to start again if you don't finish it. It may also take several minutes for the updater to load before responding to the AT wakeup command.

## Retrying process

In case of any failure or interruption to the process of LTE modem upgrade you can repeat the same steps **after doing a hard reset to the board (i.e disconnecting and reconnecting power), pressing the reset button is not enough.**

## Sqnsupgrade class

The latest version of the `sqnsupgrade` class has a few additional features that help with debugging or modem update.


#### sqnsupgrade.info()
     If the modem is in application mode, the current firmware version is displayed. This behaviour replaces the version() command which now is only available in uart() mode. Optional parameters are sqnsupgrade.info(verbose=False, debug=False)

#### sqnsupgrade.run(load_fff=True)
There is an optional command line load_fff for the sqnsupgrade.run() command. This is designed to be an internal flag. IMPORTANT: This should only be used when advised by Pycom Support.
-->
