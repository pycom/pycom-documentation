---
title: "Pyscan Examples"
aliases:
    - tutorials/pyscan.html
    - tutorials/pyscan.md
    - chapter/tutorials/pyscan
---

This basic example shows how to read an NFC card and authenticate it using a pre-defined access list.

```python

from pyscan import Pyscan
from MFRC630 import MFRC630
import time
import pycom
import _thread

VALID_CARDS = [[0x43, 0x95, 0xDD, 0xF8],
               [0x43, 0x95, 0xDD, 0xF9]]

py = Pyscan()
nfc = MFRC630(py)

RGB_BRIGHTNESS = 0x8

RGB_RED = (RGB_BRIGHTNESS << 16)
RGB_GREEN = (RGB_BRIGHTNESS << 8)
RGB_BLUE = (RGB_BRIGHTNESS)

# Make sure heartbeat is disabled before setting RGB LED
pycom.heartbeat(False)

# Initialise the MFRC630 with some settings
nfc.mfrc630_cmd_init()

def check_uid(uid, len):
    return VALID_CARDS.count(uid[:len])

def discovery_loop(nfc, id):
    while True:
        # Send REQA for ISO14443A card type
        atqa = nfc.mfrc630_iso14443a_WUPA_REQA(nfc.MFRC630_ISO14443_CMD_REQA)
        if (atqa != 0):
            # A card has been detected, read UID
            uid = bytearray(10)
            uid_len = nfc.mfrc630_iso14443a_select(uid)
            if (uid_len > 0):
                if (check_uid(list(uid), uid_len)) > 0:
                    pycom.rgbled(RGB_GREEN)
                else:
                    pycom.rgbled(RGB_RED)
        else:
            # No card detected
            pycom.rgbled(RGB_BLUE)
        nfc.mfrc630_cmd_reset()
        time.sleep(.5)
        nfc.mfrc630_cmd_init()

# This is the start of our main execution... start the thread
_thread.start_new_thread(discovery_loop, (nfc, 0))
```

You can find this, and all the other examples in our [pycom-libraries GitHub repository](https://github.com/pycom/pycom-libraries)

