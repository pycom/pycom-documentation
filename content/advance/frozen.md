---
title: 'Frozen'
---
In this section, we discuss the usage of so called `Frozen` code. This is only useful when you build the firmware from source.

What we call `Frozen` code, relates to a principle in MicroPython where you can include specific codeblocks or python module inside the firmware, such that you do not have to manually upload them. This can be very useful if you have a specific section of code you want to include on all your devices, without manually uploading it every time and risk losing it when formatting the file system.
>It is only possible to include python files in the frozen section. Other filetypes (like `.json` or `.cert`) will not be added in the final binaries

## How To use the Frozen section
1. Download the (latest) source code from our [Github Repository](https://github.com/pycom/pycom-micropython-sigfox) and extract the archive, or use the GitHub desktop tool. If you have never build firmware from the sourcecode before, you can find the setup guide on GitHub as well. 

2. Inside the folder `pycom-micropython-sigfox/esp32/frozen` you will find the `frozen` section. We already have frozen some of the python modules into the firmware, such as `sqnsupgrade.py` and `OTA.py`.
3. You can find the `_main.py` and `_boot.py` files in the `frozen/Base/` folder. These are similar to `main.py` and `boot.py` files you can build into the source code, with the exception that `_boot.py` will also run in safeboot mode. Moreover can only change the behaviour by rebuilding and reflashing the firmware. 
    > If you plan to make changes in the `_boot.py`, keep the code already in the file, as that enables the output to REPL.

4. For example, add to the `_main.py`:
    ```python
    # _main.py
    print("Hello from _main.py")
    ```
    > When building firmware with `VARIANT=PYBYTES`, you need to use the `_main.py` and `_boot.py` files in the `frozen/Pybytes` folder. The files in `frozen/Base` will **NOT** be used.
    > Moreover, if you then enable the `pybytes_on_boot(True)`, the `_pybytes_main.py` will be used instead of the `_main.py`, as that contains the pybytes activation code.
5. Now rebuild and reflash the firmware. After reboot, the line will be printed in the REPL.
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
This works similar to `import machine` and the other built-in modules. 
This concludes the section about Frozen code. You should now be able to include Frozen python code inside the firmware. 