---
title: "Updating Expansion Board Firmware "
aliases:
    - updatefirmware/expansionboard.html
    - updatefirmware/expansionboard.md
    - chapter/updatefirmware/expansionboard
---

## Not showing up in Pymakr

### Step 1
First check if the expansion board (Expansionboard, Pytrack, Pysense, etc.) **Without the py module** shows up in Device Manager under Windows, or `lsusb` under MacOS or Linux. The device should show up with a COM port as shown here:

or in the terminal as shown here: (Example is an Expansion board 3.1 on MacOS)

![](/gitbook/assets/usb-terminal.png)

>Note: the USB vendor ID is always 0x04d8, for the device ID, check [here](/updatefirmware/expansionboard/), Table 1

* If it does show up, the expansion module is connected and recognised. This also means the USB cable and board are connected correctly. Contintue to [step 5](#step-5)

* If it shows up with the Device ID in DFU update mode, check [here](/updatefirmware/expansionboard/).

* If it does not show up, continue to [step 2](#step-2)
    
### Step 2
If the expansion board is not showing up on your computer, try to use a different USB cable or USB port. On Windows, check if device manager updates when plugging in the board, and, to what driver it gets assigned. Use the guide [here](/gettingstarted/software/drivers) to set the correct driver. 
* If this solved the problem, continue to [step 5](#step-5)
* If this did not solve the problem, go to [step 3](#step-3)
> some USB cables only support charging and have no conductors for the communication lines. This also holds for some USB-C to USB micro adapters

> Note: The green LED next to the `USB` marking on the Expansionboard 2.0 / 3.0 implies the board is operational. If this is not the case, check [step 3](#step-3)

### Step 3
In this case, the board is still not showing up on your computer and you have tried all different USB cables and combinations. Now, we are going to use a multimeter to check the voltage. Check the datasheet of your expansion board [here](/datasheets/expansionboards/) for the correct pinouts. Connect the expansion board (again, without -py module) to your computer, and measure the voltages:
Re evaluate this part for naming!
* Between `Vin` and `GND`
    * Any value between 4.5 and 5.5 V is fine. 
    * If this is below 4 V, and the board is not getting extremely hot, re-evaluate your USB setup.
    
    
* Between `3V3Sensors` or 
Check if no power to the board
getting hot 
etc

### Step 4
* If you cannot get the expansion board to show up on your computer, you can still test the functionality of the py device with another board, or a [USB UART adapter](/gettingstarted/programming/usbserial/).

* If you suspect the USB is not going to work and have no UART adapter, you can try uploading over [WiFi](/gettingstarted/programming/ftp) (if you did not disable this).

### Step 5
If you reached this step, the expansion board's USB connection is fully operational. 

Once the expansion board shows up and gets assigned a COM port in Windows, or a `/dev/tty-` address in MacOS or Linux, the Pymakr plugin will try to connect to it. However, there is no py- module to connect to yet, so it will wait forever. 

Now is the time to insert your py- module. Always place the button / RGB LED towards the USB connector, like shown here: (This works the same for all modules and expansion board variants)

![](/gitbook/assets/expansion_board_3_lopy4.png)

> Note: For the Expansion board, make sure that at least the jumpers for TX RX LED and RTS are inserted correctly. 

> Note: all (new) -py modules give a flashing blue led every 4 seconds. This is the heartbeat. Once you see this, the module is guarenteed to work. It is also possible to disable this.

> In some instances you will have to restart your IDE or computer to pick up the connection again. 

If you inserted the module and:
* The green LED on the Expansion board turned off
* The module gets hot
* The expansionboard is now disconnected 
Go to [step 8](#step-8)

If, on the other hand, the module now shows connected in Pymakr, but keeps coredumping or does not return anything, go to the next step

### Step 6
First, try to press the reset button on the device. The output should look similar to this:
```
ets Jun  8 2016 00:22:57

rst:0x1 (POWERON_RESET),boot:0x17 (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
mode:DIO, clock div:1
load:0x3fff8020,len:8
load:0x3fff8028,len:2140
ho 0 tail 12 room 4
load:0x4009fa00,len:19760
entry 0x400a05bc

Pycom MicroPython 1.20.2.rc9 [v1.11-1a257d8] on 2020-06-10; LoPy4 with ESP32
Type "help()" for more information.
>>> 
```
This means the module is in working condition and you are done! On the other hand, if it does not do this, but continues to crash or return nothing, try to do a `safe-boot` like described [here](/gettingstarted/programming/safeboot/). That should bring the device in a mode where the python code is disabled, or the previous firmware is loaded. 

If your output looks like this:
```
ets Jun  8 2016 00:22:57

rst:0x1 (POWERON_RESET),boot:0x6 (DOWNLOAD_BOOT(UART0/UART1/SDIO_REI_FEO_V2))
waiting for download
```
Pin `P2` is stuck pulled `LOW`, causing the controller to expect a new firmware upload. This can be caused by ... updating expansion board?

If your expansion board fails to update, check this [Forum post](https://forum.pycom.io/topic/4911/expansion-board-3-1-issues?_=1593093156432) 

> Note: The expansion board firmware updater has some issues in MacOS, causing the dfu-util: set alt interfaces zero error, any other operating system works fine

If that does not help, try to use the [Firmware Updater tool](/updatefirmware/device/). make a more exhaustive guide here.

> After updating the firmware, the heartbeat will be re-enabled. 

### Step 7
Your expansion board is operational

Your -py module is operational

## Step 8

Measure voltages. 
If you end up here, your module's hardware is most probably broken. Either the voltage regulator died, or the micrcontroller inside is not responding to any inputs anymore. 

## Notes
If the firmware upgrade tool returns:

“Failed to connect to ESP32: Timed out waiting for packet header”
And you followed all previous steps (no blinking heartbeat LED, no orange LED on the expansionboard 3.0, etc.) The probability that your board is dead is quite high. It is quite unusual for both an expansion board and a -py module to die simultaneously, without user error. Generally, this is caused by reversing the polarity on the battery charger, thus breaking both modules. 


# Intermittent problems
Intermittent problems are generally caused by

Unstable power supply

Changing jumper placement

Atom 

Loose connections (for example, a loose USB connector)

Old firmware

Running machine.deepsleep()or py.go_to_sleep() will also stop USB connection. 