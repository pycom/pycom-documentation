# class SD – Secure digital Memory Card
The SD card class allows to configure and enable the memory card module of your Pycom module and automatically mount it as `/sd` as part of the file system. There is a single pin combination that can be used for the SD card, and the current implementation only works in 1-bit mode. The pin connections are as follows:

`P8: DAT0`, `P23: SCLK` and `P4: CMD` (no external pull-up resistors are needed)

If you have one of the Pycom expansion boards, then simply insert the card into the micro SD socket and run your script.

{% hint style='info' %}
Make sure your SD card is formatted either as FAT16 or FAT32.
{% endhint %}

### Quick Example Usage:

```python
from machine import SD
import os

sd = SD()
os.mount(sd, '/sd')

# check the content
os.listdir('/sd')

# try some standard file operations
f = open('/sd/test.txt', 'w')
f.write('Testing SD card write operations')
f.close()
f = open('/sd/test.txt', 'r')
f.readall()
f.close()
```

### Constructors

#####<class><i>class</i> machine.SD(id, ...)</class>

Create a SD card object. See <function>sd.init()</function> for parameters if initialisation.

###Methods

#####<function>sd.init(id=0)</function>

Enable the SD card.

#####<function>sd.deinit()</function>

Disable the SD card.

{% hint style='info' %}
Please note that the SD card library currently supports FAT16/32 formatted SD cards up to 32 GB. Future firmware updates will increase compatibility with additional formats and sizes.
{% endhint %}
