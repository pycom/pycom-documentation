---
title: "CLI Updater"
aliases:
    - advance/cli.html
    - advance/cli.md
    - chapter/advance/cli
---

## Command Line Update Utility

#### Windows

After installing the [Windows version](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=win32&redirect=true) of the updater tool, the CLI tool `pycom-fwtool-cli.exe` can be found here:

* 32-Bit Windows: `C:\Program Files\Pycom\Pycom Firmware Update\`
* 64-Bit Windows: `C:\Program Files (x86)\Pycom\Pycom Firmware Update\`

#### macOS

In order to get access to the CLI tool on macOS, you will need to right click on the [Mac version](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=macos&redirect=true) of the updater tool and click `Show Package Contents`, then navigate to `Contents/Resources`, here you will find the `pycom-fwtool-cli`.

#### Linux

In the [Ubuntu 14.04 LTS](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=unix&redirect=true) (and newer) version of the updater tool, `pycom-fwtool-cli` is installed in `/usr/local/bin`. In the [Generic Linux](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=unix&redirect=true) package, the tool is extracted into folder `./pyupgrade`

### Usage

```text
usage: pycom-fwtool-cli [-h] [-v] [-d] [-q] [-p PORT] [-s SPEED] [-c] [-x]
                        [--ftdi] [--pic] [-r]
                        {list,chip_id,wmac,smac,sigfox,exit,flash,copy,write,write_remote,wifi,pybytes,cb,nvs,ota,lpwan,erase_fs,erase_all}
                        ...

Update your Pycom device with the specified firmware image file For more
details please see https://docs.pycom.io/chapter/advance/cli.html

positional arguments:
  {list,chip_id,wmac,smac,sigfox,exit,flash,copy,write,write_remote,wifi,pybytes,cb,nvs,ota,lpwan,erase_fs,erase_all}
    list                Get list of available COM ports
    chip_id             Show ESP32 chip_id
    wmac                Show WiFi MAC
    smac                Show LPWAN MAC
    sigfox              Show sigfox details
    exit                Exit firmware update mode
    flash               Write firmware image to flash
    copy                Read/Write flash memory partition
    write               Write to flash memory
    wifi                Get/Set default WIFI parameters
    pybytes             Read/Write pybytes configuration
    cb                  Read/Write config block
    nvs                 Read/Write non volatile storage
    ota                 Read/Write ota block
    lpwan               Get/Set LPWAN parameters [ EU868 US915 AS923 AU915]
    erase_fs            Erase flash file system area
    erase_all           Erase entire flash!

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         show verbose output from esptool
  -d, --debug           show debuggin output from fwtool
  -q, --quiet           suppress success messages
  -p PORT, --port PORT  the serial port to use
  -s SPEED, --speed SPEED
                        baudrate
  -c, --continuation    continue previous connection
  -x, --noexit          do not exit firmware update mode
  --ftdi                force running in ftdi mode
  --pic                 force running in pic mode
  -r, --reset           use Espressif reset mode
```

## How to use the Parameters

{{% hint style="info" %}}
The CLI tool uses a combination of global and command specific parameters. The **order of parameters** is **important** to avoid ambiguity.

`pycom-fwtool-cli [global parameters] [command] [command parameters]`

While `pycom-fwtool-cli -h` shows help for global parameters and a list of available commands, command specific parameters can be viewed using `pycom-fwtool-cli [command] -h`

The parameter `-r, --reset` has been added as a courtesy for users of 3rd party ESP32 products. This functionality is **not supported** by the Expansion Board 2.0 and may cause this tool to crash or hang in certain circumstances.
{{< /hint >}}

### Global Parameters

```text
`-h / --help`    : shows above help (you can also get detailed help for each sub-command
`-v / --verbose` : show verbose output from esptool.
`-d / --debug`   : show debug output from fwtool.
`-q / --quiet`   : suppress most output, used for scripting
`-p / --port`    : specifies the serial port to be used. Can also be set via **environment variable ESPPORT**
`-s / --speed`   : specifies the serial speed to be used. Can also be set via **environment variable ESPBAUD**
`-c / --continuation` : continue previous connection in FTDI mode. This allows running multiple commands sequentially without having to reset the module. This option is ignored in PIC mode as the module can be reset via the serial connection.
`-x / --noexit`  : This will prevent the PIC from leaving firmware update mode.
`--ftdi`         : This will force the CLI updater to run in FTDI mode.
`--pic`          : This will force the CLI updater to run in PIC mode.
`-r, --reset`    : This will force the CLI updater to use Espressif's workaround to switch into Firmware update mode. This reset method is intended for 3rd party hardware only and is not supported by the Expansion Board 2.0
```

### Commands

#### list

Get list of available serial ports ports.

```bash
usage: pycom-fwtool-cli list [-h]

optional arguments:
  -h, --help  show this help message and exit
```

**Example:** On macOS:

```bash
$ pycom-fwtool-cli  list
/dev/cu.usbmodemPy343431  [Pytrack] [USB VID:PID=04D8:F013 SER=Py343434 LOCATION=20-2]
/dev/cu.Bluetooth-Incoming-Port  [n/a] [n/a]
```

On Windows:

```text
COM6  [Pytrack] [USB VID:PID=04D8:F013 SER=Py343434 LOCATION=20-2]
```

{{% hint style="info" %}}
This is the only command that does not require any additional parameters.

All other commands require that **the serial port is specified either through the** `-p` **/** `--port` **option or through environment variable** `ESPPORT` You can optionally specify the speed either through `-s` / `--speed` or via environment variable `ESPBAUD`. The default speed is `921600`. The maximum speed for read operations on PIC based expansion boards & shields is `230400`. The speed will be reduced automatically if necessary.

#### Special note for Expansion Board 2.0

You will need to have a **jumper wire** connected between `G23` and `GND` to use any of the commands below. You will also need to **press the reset button** either before running each command or at least before running the first command. To avoid having to press the reset button again after each command, you can use the `-c` / `--continuation` option. The first command connecting to the device **MUST NOT** use the `-c` / `--continuation` option. This is to make sure a program called `_stub_` is uploaded onto the device. This `_stub_` cannot be uploaded more than once, so you need to tell the cli tool that the `_stub_` is already running, which is done through using the `-c` / `--continuation` option.
{{< /hint >}}

#### chip\_id

Shows the unique ID of the ESP32 on the connected module.

```text
usage: pycom-fwtool-cli  -p PORT exit [-h]

optional arguments:
  -h, --help  show this help message and exit
```

#### wmac

Shows the WiFi MAC of the connected module.

```text
usage: pycom-fwtool-cli  -p PORT wmac [-h]

optional arguments:
  -h, --help  show this help message and exit
```

#### smac

Shows the LPWAN MAC of the connected module.

```text
usage: pycom-fwtool-cli  -p PORT smac [-h]

optional arguments:
  -h, --help  show this help message and exit
```

#### sigfox

Show sigfox details

```text
usage: pycom-fwtool-cli  -p PORT sigfox [-h]

optional arguments:
  -h, --help  show this help message and exit
```

#### exit

If a Pysense/Pytrack/Expansion 3 has previously been left in firmware update mode by using the `-x` option, this command can be used to exit the firmware update mode.

```text
usage: pycom-fwtool-cli  -p PORT exit [-h]

optional arguments:
  -h, --help  show this help message and exit
```

#### flash

Writes firmware image to flash, must be as a `.tar(.gz)` file as provided by Pycom. These files can be found on [GitHub](https://github.com/pycom/pycom-micropython-sigfox/releases).

```text
usage: pycom-fwtool-cli  -p PORT flash [-h] [-t TAR]

optional arguments:
  -h, --help         show this help message and exit
  -t TAR, --tar TAR  perform the upgrade from a tar[.gz] file
```

#### copy

Read/Write flash memory partition from/to local file

```text
usage: pycom-fwtool-cli  -p PORT [-h] [-p PARTITION] [-f FILE] [-r] [-b]

optional arguments:
  -h, --help            show this help message and exit
  -p PARTITION, --partition PARTITION
                        The partition to read/write (all, fs, nvs, factory,
                        secureboot, bootloader, partitions, otadata, fs1,
                        ota_0, config)
  -f FILE, --file FILE  name of the binary file (default: <wmac>-<part>.bin)
  -r, --restore         restore partition from binary file
  -b, --backup          backup partition to binary file (default)
```

#### write

Write to a specific location in flash memory.

```text
usage: pycom-fwtool-cli  -p PORT write [-h] [-a ADDRESS] [--contents CONTENTS]

optional arguments:
  -h, --help            show this help message and exit
  -a ADDRESS, --address ADDRESS
                        address to write to
  --contents CONTENTS   contents of the memory to write (base64)
```

#### wifi

Get/Set default WiFi parameters.

```text
usage: pycom-fwtool-cli wifi [-h] [--ssid SSID] [--pwd PWD] [--wob [WOB]]

optional arguments:
  -h, --help   show this help message and exit
  --ssid SSID  Set Wifi SSID
  --pwd PWD    Set Wifi PWD
  --wob [WOB]  Set Wifi on boot
```

#### pybytes

Read/Write pybytes configuration.

```text
usage: pycom-fwtool-cli pybytes [-h] [--token TOKEN] [--mqtt MQTT] [--uid UID]
                                [--nwprefs NWPREFS] [--extraprefs EXTRAPREFS]

optional arguments:
  -h, --help            show this help message and exit
  --token TOKEN         Set Device Token
  --mqtt MQTT           Set mqttServiceAddress
  --uid UID             Set userId
  --nwprefs NWPREFS     Set network preferences
  --extraprefs EXTRAPREFS
                        Set extra preferences
```

{{% hint style="info" %}}
Note: The local `pybytes_config.json` file is overwritten when making any modifications using this command (requires Pybytes firmware `1.17.5.b6` or higher and Firmware updater `1.14.3`).
{{< /hint >}}

#### cb

Read/Write config block (LPMAC, Sigfox PAC & ID, etc.). You can find the structure of this block [here.](https://github.com/pycom/pycom-micropython-sigfox/blob/master/esp32/pycom_config.h#L24)

```text
usage: pycom-fwtool-cli  -p PORT cb [-h] [-f FILE] [-b] [-r]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  name of the backup file
  -b, --backup          backup cb partition to file
  -r, --restore         restore cb partition from file
```

If neither `-b` or `-r` is provided, the command will default to backup. If no file name is provided, `<WMAC>.cb` is used.

To backup your config block: `$pycom-fwtool-cli -p PORT cb`

To restore your config block: `$pycom-fwtool-cli -p PORT cb -r -f backup.cb`

#### nvs

Read/Write non-volatile storage.

```text
usage: pycom-fwtool-cli  -p PORT nvs [-h] [-f FILE] [-b] [-r]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  name of the backup file
  -b, --backup          backup cb partition to file
  -r, --restore         restore cb partition from file
```

If neither `-b` or `-r` is provided, the command will default to backup. If no file name is provided, `<WMAC>.nvs` is used.

To backup your NVS: `$ pycom-fwtool-cli -p PORT nvs`

To restore your NVS: `$ pycom-fwtool-cli -p PORT nvs -r -f backup.nvs`

#### ota

Read/Write ota block, this contains data relating to OTA updates such as the hash of the OTA firmware.

```text
usage: pycom-fwtool-cli  ota [-h] [-f FILE] [-b] [-r]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  name of the backup file
  -b, --backup          backup cb partition to file
  -r, --restore         restore cb partition from file
```

If neither `-b` nor `-r` is provided, the command will default to backup. If no file name is provided, `<WMAC>.ota` is used.

To backup your OTA block: `$pycom-fwtool-cli -p PORT ota`

To restore your OTA block: `$pycom-fwtool-cli -p PORT ota -r -f backup.ota`

#### lpwan

Get/Set LPWAN parameters saved to non-volatile storage. Please see [here](/firmwareapi/pycom/network/lora#loranvramsave) for more details.

```text
usage: pycom-fwtool-cli  -p PORT lpwan [-h] [--region REGION]

optional arguments:
  -h, --help       show this help message and exit
  --region REGION  Set default LORA region
  --erase_region   Erase default LORA region
  --lora_region    Output only LORA region
```

#### erase\_fs

Erase flash file system area. This is useful if some code running on the device is preventing access to the REPL.

```text
usage: pycom-fwtool-cli  -p PORT erase_fs [-h]

optional arguments:
  -h, --help  show this help message and exit
```

#### erase\_all

Erase entire flash, only use this if you are sure you know what you are doing. This will remove your devices lpwan mac addresses etc.

```text
usage: pycom-fwtool-cli erase_all [-h]

optional arguments:
  -h, --help  show this help message and exit
```
