---
title: 'Frozen'
---
In this section, we discuss the usage of so called `Frozen` code. This is only useful when you build the firmware from source.

What we call `Frozen` code, relates to a principle in MicroPython where you can include specific codeblocks or python module inside the firmware, such that you do not have to manually upload them. This can be very useful if you have a specific section of code you want to include on all your devices, without manually uploading it every time and risk losing it when formatting the file system.

## How To use the Frozen section
1. Download the (latest) source code from our [Github Repository](https://github.com/pycom/pycom-micropython-sigfox) and extract the archive, or use the GitHub desktop tool.
2. Inside the folder `pycom-micropython-sigfox/esp32/frozen` you will find the `frozen` section. We already have frozen some of the python modules into the firmware, such as `sqnsupgrade.py` and `OTA.py`.
3. In here, you can also find `_main.py` and `_boot.py` files under `Base`. These are alternative `main.py` and `boot.py` files you can build into the source code, and they will run like you would expect.
    > Note that if you add anything in the `_boot.py`, it will also run in safeboot mode, and you can only change it by reflashing the firmware.

    > The code already in `_boot.py` is pretty important to make the REPL show up, do not remove that 
    >```python
    >import os
    >from machine import UART
    >os.dupterm(UART(0, 115200))
    >```
4. For example add to the `_main.py`:
    ```python
    # _main.py
    print("Hello from _main.py")
    ```
5. Now rebuild and reflashing the firmware. After reboot, the line will be printed in the REPL
6. You can also add files to the `Custom` folder, in this example, we make a `Block.py` with the following code:
    ```python
    # block.py
    def Block():
        print("My Frozen codeblock")
    ```
7. After rebuilding and reflashing, you are able to:
    ```python
    >>> from block import Block
    >>> Block()
    My Frozen codeblock
    ```