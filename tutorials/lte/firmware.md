---
description: Sequans LTE modem upgrade steps
---

# Modem Firmware Update

There are 2 ways to upgrade the firmware on the LTE modem: via an SD card or via UART serial interface \(Windows, Linux, or macOS\)

{% hint style="info" %}
This article is only related to [GPy](../../datasheets/development/gpy.md), [FiPy](../../datasheets/development/fipy.md), and [G01](../../datasheets/oem/g01.md) boards
{% endhint %}

Before going into details of this method, please do the following:

1. [Upgrade Pycom Firmware Updater tool to the latest version](../../gettingstarted/installation/firmwaretool.md)
2. [Upgrade firmware](../../gettingstarted/installation/firmwaretool.md#updating-device-firmware) to latest `stable` version \(`v1.18.1`\)

## Via SD card

First, you need to get the firmware image files downloaded onto your FAT32 formatted SD card. You can find the different versions of the firmware here: [https://github.com/pycom/sqnsupgrade/tree/master/fw](https://github.com/pycom/sqnsupgrade/tree/master/fw)

You will find 2 types of files for firmware: `.dup` and `updater.elf`. You will need the `updater.elf` file only for the first time you do this upgrade.

Once you've downloaded the firmware files onto the SD card, insert it in your board and run the following commands:

```python
import sqnsupgrade
sqnsupgrade.run('<Path_to_dup_file_on_SD>','<Path_to_dot_elf_on_SD')
```

Once the update is finished successfully, you will have a summary of the new updated versions, something like this:

```text
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

## Via UART Serial Interface

If you don't want to use an SD card to hold the firmware images, you can directly use the existing UART interface you have with the board to load these firmware files from your computer.

In that case, you need to **run upgrade scripts from both your board and your computer**.

### **Commands to be run on the board**

```python
import sqnsupgrade
sqnsupgrade.uart(True)
```

After this command is executed a message will be displayed asking you to close the port

```text
Going into MIRROR mode... please close this terminal to resume the upgrade via UART
```

You should close the terminal and run the following commands from your computer:

### **Commands to be run on your** computer

Please note that you need to do these steps **before running the script on your computer:**

* Have [Python 3](https://docs.python-guide.org/starting/installation/) installed on your computer
* Install [`Pyserial`](https://github.com/pyserial/pyserial#installation) package for Python 3 using [pip](https://pip.pypa.io/en/stable/installing/)

Now, you have to download the Sequans upgrade scripts from GitHub: [https://github.com/pycom/sqnsupgrade](https://github.com/pycom/sqnsupgrade.git)

Go to the directory and run the following commands in terminal:

```python
$ python3
Python 3.6.5 (default, Apr 25 2018, 14:23:58)
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import sqnsupgrade
>>> sqnsupgrade.run('Serial_Port', './fw/<file>.dup', './fw/updater.elf')
```

Once the update is finished successfully, you will have a summary of the new updated versions, something like this:

```text
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

## **Retrying process**

In case of any failure or interruption to the process of LTE modem upgrade, you can repeat the same steps **after doing a hard reset to the board \(i.e. disconnecting power and connect again\), normal reset is not enough.**

In case of upgrade via UART, there is a change to the command that you should run on the board. Instead of `sqnsupgrade.uart(True)`, you should use `sqnsupgrade.uart(True, retry=True)`

