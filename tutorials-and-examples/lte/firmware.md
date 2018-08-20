# Modem Firmware Update

## Description

The Sequans Monarch SQN3330 cellular radio found on the Pycom FiPy, GPy and GO1 modules requires a different firmware to operate in CAT-M1 or NB-IoT mode.

This page will explain the process to upgrade the firmware of the cellular radio The process involves streaming the firmware file from the ESP32 to the SQN3330. Currently, the file has to be stored in a micro SD card first so that the ESP32 can access it easily. We are current working to add support for streaming the file via the updater tool as well.

## Requirements

Before proceeding you will need:

* Pycom cellular enabled module \(GPy, FiPy, G01\)
* FAT32 formatted microSD card \(with at least 6MB of free space\)
* A Pycom Expansion Board or shield \(or a microSD card socket breakout board\)

## Usage

{% hint style="danger" %}
If your module is running the factory LTE chip firmware, you **MUST** first perform an update to the latest CAT-M1 firmware before trying to upgrade to the NB-IoT firmware. Skipping this step will cause your radio to become unresponsive and it will require access to the test points in order to re-flash the firmware.
{% endhint %}

Firstly, you will need to download the required library files from [here](https://github.com/pycom/pycom-libraries/tree/master/lib/sqnsupgrade). You will need to place these in a directory called "lib" just like any other libraries. This can be done using either [FTP](../../getting-started/programming/ftp.md) or [Pymakr](../../pymakr-plugin/installation/)

Next you need to download the firmware file from [here](https://software.pycom.io/downloads/sequans.html). You will need to place the firmware on a FAT32 formatted microSD card, then insert the SD card into a Expansion Board, Pytrack, Pysense or Pyscan. Power-up the system and connect to the interactive REPL and run the following code:

```python
import sqnsupgrade
sqnsupgrade.run(path_to_firmware, 921600)   # path_to_firmware example: '/sd/FIPY_NB1_35351.dup'
```

The whole process can take between 2 and 3 minutes and at some points it will seem to stall, this is normal, just be patience. You should see an output like this:

```text
<<< Welcome to the SQN3330 firmware updater >>>
Entering recovery mode
Resetting.

Starting STP (DO NOT DISCONNECT POWER!!!)
STP started
Session opened: version 1, max transfer 8192 bytes
Sending 4560505 bytes: [########################################] 100%
Code download done, returning to user mode
Resetting (DO NOT DISCONNECT POWER!!!).
.........
Deploying the upgrade (DO NOT DISCONNECT POWER!!!)...
Resetting (DO NOT DISCONNECT POWER!!!)..
...
Upgrade completed!
Here is the current firmware version:
UE6.0.0.0-ER7
LR6.0.0.0-35351
OK
```

{% hint style="danger" %}
**DO NOT DISCONNECT** power while the upgrade process is taking place, wait for it to finish!
{% endhint %}

If the module get's stuck in here for more than 1 minute while upgrading to the NB-IoT firmware, you can cycle power and retry. In this case it is safe.

```text
Sending 4560505 bytes: [##                                      ]   6%
```

