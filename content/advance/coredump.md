---
title: "Troubleshooting Coredumps"

---


It is never nice when a project coredumps. With this tool. you might be able to figure out why it coredumps and what you can do about it.

>Note that some coredumps are not caused by the Python or C code, but by instability of the microcontroller. For example, supplying not enough power or ... will also generate a coredump. 

1. Install the ESP-IDF toolchain. You can find instructions [here](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html#get-started-get-esp-idf). If you already built our firmware from source once, you do not need to install the idf again.
2. This will provide us with a tool called `addr2line`, which converts the stacktrace addresses to a line number in C sourcecode. From here, we might be able to determine the root cause of the coredump. You can find the tool in `../xtensa-esp32-elf/bin/xtensa-esp32-elf-addr2line`. 
    >Note: This is a command line tool only. 
3. Grab the .elf for your firmware version and board type [here](https://github.com/pycom/pycom-micropython-sigfox/releases). From here on, we will call it `application.elf`
    > If you do not know your current firmware version, you can check it using:
    > ```python
    > >>> import os
    > >>> os.uname()
    > ```

4. Wait for your running code to coredump. I attached an example here. We are only interested in the top section. 
    ```
    Guru Meditation Error: Core  0 panic'ed (StoreProhibited). Exception was unhandled.
    Core 0 register dump:
    PC      : 0x40195846  PS      : 0x00060530  A0      : 0x801952fb  A1      : 0x3ffbaef0  
    A2      : 0x00000000  A3      : 0x00000000  A4      : 0x00000005  A5      : 0xffffffff  
    A6      : 0x0000336d  A7      : 0x3ffba1c4  A8      : 0x80194d84  A9      : 0x3ffbaeb0  
    A10     : 0x00000028  A11     : 0x00000000  A12     : 0x3ffb9f28  A13     : 0x00000000  
    A14     : 0x3ffb9f38  A15     : 0x00000001  SAR     : 0x00000000  EXCCAUSE: 0x0000001d  
    EXCVADDR: 0x0000002d  LBEG    : 0x40093718  LEND    : 0x40093746  LCOUNT  : 0xffffffff  

    ELF file SHA256: 0000000000000000000000000000000000000000000000000000000000000000

    Backtrace: 0x40195846:0x3ffbaef0 0x401952f8:0x3ffbaf10 0x40184fe8:0x3ffbaf30

    ================= CORE DUMP START =================
    hDEAAAEAAAAOAAAAbAEAAA==
    tJ/7PzCu+z/Er/s/
    0K37P2Cv+z/MMwAAEMj8PxDI/D+0n/s/CMj8PwcAAAAIn/s/CJ/7P7Sf+z8AAAAA
    EgAAAMih+z90aVQA6MX8P7x9+z/EffsAAAAAAMSv+z8AAAAAIAcGABIAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAADUZPs/PGX7P6Rl+z8AAAAAAAAAAAEAAAAAAAAA
    OsRAPwAAAAAoUAlAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    ...
    ```

5. Navigate terminal to the folder where your `application.elf` file is located. From there, use the following command. replace `[backtrace]` with the numbers following the `Backtrace:` in the coredump. 
    ```python
    xtensa-esp32-elf-addr2line -fe [application.elf] [backtrace]
    ```
    > In this case, the backtrace is `0x40195846:0x3ffbaef0 0x401952f8:0x3ffbaf10 0x40184fe8:0x3ffbaf30`

6. The output of this command will give you the files and line numbers of the last ran commands (`stack trace`), where the last command will have caused the error. 

> More Advanced \
> You can also use the `xtensa-esp32-elf-gdb` tool in the command line, which will return where in the code the processor crashed. You can use: 
> * `info symbol [PC]` (where `[PC]` is the program counter found in the coredump) to get the section of the line that causes the coredump 
> * `disassemble [PC]` to get the instructions of the specified line in assemble format.

## Common errors and solutions

