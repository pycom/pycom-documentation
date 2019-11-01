---
title: "Pymesh Library CLI"
aliases:
  - pymesh/simple-example
---

## Licensing process

In order to receive access to the Pymesh firmware releases (for Lopy4, Fipy, L01 or L04), the next process should be followed:

1. Complete the <a href="/gitbook/assets/pymesh/Pymesh_Licence_Copyright_Notice.pdf" target="\_blank"> the Pymesh LICENCE PDF document </a>, sign it and send us by [this email](mailto:catalin@pycom.io?subject=[Pymesh_LICENCE]).
1. You will receive by email an archive containing the images for all boards.
1. Extract the corresponding image, for example Lopy4.tar.gz, and upload the firmware to your board, using the [Pycom Firmware Update Tool](https://pycom.io/downloads/), similar in the following image:
<img src="/gitbook/assets/pymesh/pymesh_firmware_update.png" alt="Pymesh Firmware Update" width="500"/>

## Test Pymesh firmware loading

### Method 1

The simplest way to check if the Pymesh class has been successfully installed is to try the following code, directly in REPL:

```python
>>> from network import LoRa
>>> lora = LoRa(mode=LoRa.LORA)
>>> mesh = lora.Mesh()
```

### Method 2

Upload the `main.py` from the [Simple Example](/pymesh/simple-example).

## FAQ

Q: **I've received an error, such as `(LoadProhibited). Exception was unhandled.`, what should I do?**

A: In some cases, the NVM partition needs to be formatted. For this a format of whole Flash Memory should be performed.

This can be done using the cli version of the `Firmware Update Tool`, so please navigate where the app was installed (search for pycom-fwtool-cli executable) and execute:
```
pycom-fwtool-cli -p <PORT> erase_all
```

`<PORT>` should be replaced with the actual USB COM port, for example:

* on Windows `COM10`
* on Linux `/dev/ttyACM0`
* on MacOS `/dev/tty.usbmodemPy8eaa911`
