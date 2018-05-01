# Command Line Update Utility

### Windows
After installing the [windows version](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=win32&redirect=true)
of the updater tool, the CLI tool can be
found here:

32-Bit Windows: ``C:\Program Files\Pycom\Pycom Firmware Update\pycom-fwtool-cli.exe``

64-Bit Windows: ``C:\Program Files (x86)\Pycom\Pycom Firmware Update\pycom-fwtool-cli.exe``

### Mac
In order to get access to the CLI tool on mac you will need to right click on
the [mac version](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=macos&redirect=true)
of the updater tool and click `Show Package Contents`, then navigate to
`contents/resources`, here you will find the `pycom-fwtool-cli`.

### Linux
The [linux version](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=unix&redirect=true)
of the updater tool does not come with a precompiled `pycom-fwtool-cli` binary,
but rather raw the python script. This can be found in `bin/updater.py`

## Usage

```
usage: pycom-fwtool-cli [-h] [-v] [-q] [-p PORT] [-s SPEED] [-c] [-x] [--ftdi]
                        [--pic]
                        {list,chip_id,wmac,smac,sigfox,exit,flash,write,write_remote,cb,nvs,ota,lpwan,erase_fs,erase_all}
                        ...

Update your Pycom device with the specified firmware image file

positional arguments:
  {list,chip_id,wmac,smac,sigfox,exit,flash,write,write_remote,cb,nvs,ota,lpwan,erase_fs,erase_all}
    list                Get list of available COM ports
    chip_id             Show ESP32 chip_id
    wmac                Show WiFi MAC
    smac                Show LPWAN MAC
    sigfox              Show sigfox details
    exit                Exit firmware update mode
    flash               Write firmware image to flash
    write               Write to flash memory
    write_remote        Write remote config to flash memory
    cb                  Read/Write config block
    nvs                 Read/Write non volatile storage
    ota                 Read/Write ota block
    lpwan               Get/Set LPWAN parameters
    erase_fs            Erase flash file system area
    erase_all           Erase entire flash!

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         show verbose output from esptool
  -q, --quiet           suppress success messages
  -p PORT, --port PORT  the serial port to use
  -s SPEED, --speed SPEED    baudrate
  -c, --continuation    continue previous connection
  -x, --noexit          do not exit firmware update mode (Pysense/Pytrack only)
  --ftdi                force running in ftdi mode
  --pic                 force running in pic mode (Pysense/Pytrack)

```



## Modes
###  list                
Get list of available serial ports ports.
```
usage: pycom-fwtool-cli  list [-h]

optional arguments:
  -h, --help  show this help message and exit
```

**Example:**
```
$pycom-fwtool-cli  list
/dev/cu.usbmodemPy343431  [Pytrack] [USB VID:PID=04D8:F013 SER=Py343434 LOCATION=20-2]
/dev/cu.Bluetooth-Incoming-Port  [n/a] [n/a]
```
or on windows
```
COM6  [Pytrack] [USB VID:PID=04D8:F013 SER=Py343434 LOCATION=20-2]
```

{% hint style='info' %}
If you are using an expansion board 1.0 or 2.0, you will need to have a jumper
connected between `P2` and `GND` to use any of the commands below. You will also
need to press the reset button before running each command.
{% endhint %}


###  chip_id             
Shows the unique ID of the ESP32 on the connected module.
```
usage: pycom-fwtool-cli  -p PORT exit [-h]

optional arguments:
  -h, --help  show this help message and exit
```

###  wmac                
Shows the WiFi MAC of the connected module.

```
usage: pycom-fwtool-cli  -p PORT wmac [-h]

optional arguments:
  -h, --help  show this help message and exit
```

###  smac                
Shows the LPWAN MAC of the connected module.

```
usage: pycom-fwtool-cli  -p PORT smac [-h]

optional arguments:
  -h, --help  show this help message and exit
```

###  sigfox              
Show sigfox details

```
usage: pycom-fwtool-cli  -p PORT sigfox [-h]

optional arguments:
  -h, --help  show this help message and exit
```

###  exit                
If a Pysense/Pytrack has previously been left in firmware update mode by using
the `-x` option, this command can be used to exit the firmware update mode.

```
usage: pycom-fwtool-cli  -p PORT exit [-h]

optional arguments:
  -h, --help  show this help message and exit
```

###  flash               
Writes firmware image to flash, must be as a tar(.gz) file as provided by Pycom.
These files can be found on [GitHub](https://github.com/pycom/pycom-micropython-sigfox/releases).
```
usage: pycom-fwtool-cli  -p PORT flash [-h] [-t TAR]

optional arguments:
  -h, --help         show this help message and exit
  -t TAR, --tar TAR  perform the upgrade from a tar[.gz] file
```

###  write               
Write to a specific location in flash memory.

```
usage: pycom-fwtool-cli  -p PORT write [-h] [-a ADDRESS] [--contents CONTENTS]

optional arguments:
  -h, --help            show this help message and exit
  -a ADDRESS, --address ADDRESS
                        address to write to
  --contents CONTENTS   contents of the memory to write (base64)
 ```

### write_remote
This is an internal function used by the GUI update tool. This is not intended
to be used by end users.

###  cb                  
Read/Write config block (LPMAC, Sigfox PAC & ID, etc.). You can find the
structure of this block [here.](https://github.com/pycom/pycom-micropython-sigfox/blob/master/esp32/pycom_config.h#L24)
```
usage: pycom-fwtool-cli  -p PORT cb [-h] [-f FILE] [-b] [-r]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  name of the backup file
  -b, --backup          backup cb partition to file
  -r, --restore         restore cb partition from file
```

To backup your config block:
``$pycom-fwtool-cli  -p PORT cb``

If neither `-b` or `-r` is provided, the command will default to backup. If no
file name is provided, `<WMAC>.cb` is used.

To restore your config block:
``$pycom-fwtool-cli  -p PORT cb -r -f backup.cb``

###  nvs                 
Read/Write non-volatile storage.
```
usage: pycom-fwtool-cli  -p PORT nvs [-h] [-f FILE] [-b] [-r]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  name of the backup file
  -b, --backup          backup cb partition to file
  -r, --restore         restore cb partition from file
```

To backup your NVS:
``$pycom-fwtool-cli  -p PORT nvs``

If neither `-b` or `-r` is provided, the command will default to backup. If no
file name is provided, `<WMAC>.nvs` is used.

To restore your NVS:
``$pycom-fwtool-cli  -p PORT nvs -r -f backup.nvs``


###  ota    
Read/Write ota block, this contains data relating to OTA updates such as the
hash of the OTA firmware.
```
usage: pycom-fwtool-cli  ota [-h] [-f FILE] [-b] [-r]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  name of the backup file
  -b, --backup          backup cb partition to file
  -r, --restore         restore cb partition from file
```

To backup your OTA block:
``$pycom-fwtool-cli  -p PORT ota``

If neither `-b` or `-r` is provided, the command will default to backup. If no
file name is provided, `<WMAC>.ota` is used.

To restore your OTA block:
``$pycom-fwtool-cli  -p PORT ota -r -f backup.ota``

###  lpwan               
Get/Set LPWAN parameters saved to non-volatile storage. Please see
[here](../firmwareapi/pycom/network/lora.md##loranvramsave) for more details.

```
usage: pycom-fwtool-cli  -p PORT lpwan [-h] [--region REGION]

optional arguments:
  -h, --help       show this help message and exit
  --region REGION  Set default LORA region
  --erase_region   Erase default LORA region
  --lora_region    Output only LORA region
```

###  erase_fs            
Erase flash file system area. This is useful if some code running on the device
is reventing access to the REPL.
```
usage: pycom-fwtool-cli  -p PORT erase_fs [-h]

optional arguments:
  -h, --help  show this help message and exit
```

###  erase_all           
Erase entire flash, only use this if you are sure you know what you are doing.
This will remove your devices lpwan mac addresses etc.

```
usage: pycom-fwtool-cli erase_all [-h]

optional arguments:
  -h, --help  show this help message and exit
```
