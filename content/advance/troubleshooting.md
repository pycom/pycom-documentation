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

Once the USB device shows up and gets assigned a COM port (in Windows), the Pymakr plugin will try to connect to it, however, there is no py- module to connect to yet. If this is not the case, 

Insert your py- module with the button / RGB LED towards the USB connector, like shown here: (This works the same for all modules)

![](/gitbook/assets/expansion_board_3_lopy4.png)

> Note: For the expansion board, make sure that at least the jumpers for TX RX LED and RTS are inserted correctly. 

* The module should flash the RGB LED blue every 4 seconds (unless you disabled the hearbeat last time). This indicates the module is operational. 
---
* If it does not flash, the module might be constantly crashing or in programming mode. You can check this by viewing the Pymakr REPL terminal in VSCode or Atom. The text will be similar to ..
    ```
    Connecting to /dev/tty.usbmodemPy37219b1...
    ets Jun  8 2016 00:22:57

    rst:0x1 (POWERON_RESET),boot:0x6 (DOWNLOAD_BOOT(UART0/UART1/SDIO_REI_FEO_V2))
    waiting for download
    ```
This means GPIO0, (P2) of the py module is pulled LOW and the module keeps itself in programming mode. This problem can be caused by the expansion board, in which case you should update the firmware, described here: https://docs.pycom.io/pytrackpysense/installation/firmware/. If your expansion board fails to update, check this link: https://forum.pycom.io/topic/4911/expansion-board-3-1-issues?_=1593093156432. 

Note: The expansion board firmware updater has some issues in MacOS, causing the dfu-util: set alt interfaces zero error, any other operating system works fine

If it does not give that, try the safe boot procedure described here: https://docs.pycom.io/gettingstarted/programming/safeboot/. 

Okay, when you got this far, it means that 

Your expansion board is operational

Your -py module is operational

If you still cannot get the device to show up in your computer, please check that your USB cable has a data connection. 


Showing up in Pymakr, but no response / keeps coredumping
You should now receive something similar to this in the REPL terminal of Pymakr, after you press the reset button:

>>> ets Jun  8 2016 00:22:57

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
If this is not the case, you should use the Firmware updater tool: https://docs.pycom.io/gettingstarted/installation/firmwaretool/ to update your module to the latest firmware. A firmware update might also solve some of the Guru-Meditation errors, in that case, also make sure the NVM is formatted using the advanced option:



If the firmware upgrade tool returns:

“Failed to connect to ESP32: Timed out waiting for packet header”
And you followed all previous steps (no blinking heartbeat LED, no orange LED on the expansionboard 3.0, etc.) The probability that your board is dead is quite high. It is quite unusual for both an expansion board and a -py module to die simultaneously, without user error. Generally, this is caused by reversing the polarity on the battery charger, thus breaking both modules. 


Intermittent problems
Intermittent problems are generally caused by

Unstable power supply

Changing jumper placement

Atom 

Loose connections (for example, a loose USB connector)

Old firmware

Running machine.deepsleep()or py.go_to_sleep() will also stop USB connection. 