# 5.2.2.3 Bluetooth

This class provides a driver for the Bluetooth radio in the module. Currently, only basic BLE functionality is available.

## Quick Usage Example

```python
from network import Bluetooth
import time
bt = Bluetooth()
bt.start_scan(-1)

while True:
  adv = bt.get_adv()
  if adv and bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL) == 'Heart Rate':
      try:
          conn = bt.connect(adv.mac)
          services = conn.services()
          for service in services:
              time.sleep(0.050)
              if type(service.uuid()) == bytes:
                  print('Reading chars from service = {}'.format(service.uuid()))
              else:
                  print('Reading chars from service = %x' % service.uuid())
              chars = service.characteristics()
              for char in chars:
                  if (char.properties() & Bluetooth.PROP_READ):
                      print('char {} value = {}'.format(char.uuid(), char.read()))
          conn.disconnect()
          break
      except:
          print("Error while connecting or reading from the BLE device")
          break
  else:
      time.sleep(0.050)
```

## Bluetooth Low Energy \(BLE\)

Bluetooth low energy \(BLE\) is a subset of classic Bluetooth, designed for easy connecting and communicating between devices \(in particular mobile platforms\). BLE uses a methodology known as Generic Access Profile \(GAP\) to control connections and advertising.

GAP allows for devices to take various roles but generic flow works with devices that are either a Server \(low power, resource constrained, sending small payloads of data\) or a Client device \(commonly a mobile device, PC or Pycom Device with large resources and processing power\). Pycom devices can act as both a Client and a Server.

## Constructors

### class network.Bluetooth\(id=0, ...\)

Create a Bluetooth object, and optionally configure it. See init for params of configuration.

Example:

```python
from network import Bluetooth
bluetooth = Bluetooth()
```

## Methods

### bluetooth.init\(id=0, mode=Bluetooth.BLE, antenna=None\)

* `id` Only one Bluetooth peripheral available so must always be 0
* `mode` currently the only supported mode is `Bluetooth.BLE`
* `antenna` selects between the internal and the external antenna. Can be either

  Bluetooth.INT\_ANT, Bluetooth.EXT\_ANT.

  With our development boards it defaults to using the internal antenna, but in

  the case of an OEM module, the antenna pin \(`P12`\) is not used, so it’s free to be

  used for other things.

Initialises and enables the Bluetooth radio in BLE mode.

### bluetooth.deinit\(\)

Disables the Bluetooth radio.

### bluetooth.start\_scan\(timeout\)

Starts performing a scan listening for BLE devices sending advertisements. This function always returns immediately, the scanning will be performed on the background. The return value is `None`. After starting the scan the function get\_adv\(\) can be used to retrieve the advertisements messages from the FIFO. The internal FIFO has space to cache 16 advertisements.

The arguments are:

* `timeout` specifies the amount of time in seconds to scan for advertisements, cannot be zero. If timeout is &gt; 0, then the BLE radio will listen for advertisements until the specified value in seconds elapses. If timeout &lt; 0, then there’s no timeout at all, and stop\_scan\(\) needs to be called to cancel the scanning process.

Examples:

```python
bluetooth.start_scan(10)        # starts scanning and stop after 10 seconds
bluetooth.start_scan(-1)        # starts scanning indefinitely until bluetooth.stop_scan() is called
```

### bluetooth.stop\_scan\(\)

Stops an ongoing scanning process. Returns `None`.

### bluetooth.isscanning\(\)

Returns `True` if a Bluetooth scan is in progress. `False` otherwise.

### bluetooth.get\_adv\(\)

Gets an named tuple with the advertisement data received during the scanning. The tuple has the following structure: `(mac, addr_type, adv_type, rssi, data)`

* `mac` is the 6-byte ling mac address of the device that sent the advertisement.
* `addr_type` is the address type. See the constants section below for more details.
* `adv_type` is the advertisement type received. See the constants section below fro more details.
* `rssi` is signed integer with the signal strength of the advertisement.
* `data` contains the complete 31 bytes of the advertisement message. In order to parse the data and get the specific types, the method resolve\_adv\_data\(\) can be used.

Example for getting `mac` address of an advertiser:

```python
import ubinascii

bluetooth = Bluetooth()
bluetooth.start_scan(20) # scan for 20 seconds

adv = bluetooth.get_adv() #
ubinascii.hexlify(adv.mac) # convert hexadecimal to ascii
```

### bluetooth.get\_advertisements\(\)

Same as the `get_adv()` method, but this one returns a list with all the advertisements received.

### bluetooth.resolve\_adv\_data\(data, data\_type\)

Parses the advertisement data and returns the requested `data_type` if present. If the data type is not present, the function returns `None`.

Arguments:

* `data` is the bytes object with the complete advertisement data.
* `data_type` is the data type to resolve from from the advertisement data. See constants section below for details.

Example:

```python
import ubinascii
from network import Bluetooth
bluetooth = Bluetooth()

bluetooth.start_scan(20)
while bluetooth.isscanning():
    adv = bluetooth.get_adv()
    if adv:
        # try to get the complete name
        print(bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL))

        mfg_data = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_MANUFACTURER_DATA)

        if mfg_data:
            # try to get the manufacturer data (Apple's iBeacon data is sent here)
            print(ubinascii.hexlify(mfg_data))
```

### bluetooth.connect\(mac\_addr\)

Opens a BLE connection with the device specified by the `mac_addr` argument. This function blocks until the connection succeeds or fails. If the connections succeeds it returns a object of type `GATTCConnection`.

```python
bluetooth.connect('112233eeddff') # mac address is accepted as a string
```

### bluetooth.callback\(trigger=None, handler=None, arg=None\)

Creates a callback that will be executed when any of the triggers occurs. The arguments are:

* `trigger` can be either Bluetooth.NEW\_ADV\_EVENT, Bluetooth.CLIENT\_CONNECTED or Bluetooth.CLIENT\_DISCONNECTED
* `handler` is the function that will be executed when the callback is triggered.
* `arg` is the argument that gets passed to the callback. If nothing is given the bluetooth object itself is used.

An example of how this may be used can be seen in the bluetooth.events\(\) method.

### bluetooth.events\(\)

Returns a value with bit flags identifying the events that have occurred since the last call. Calling this function clears the events.

Example of usage:

```python
from network import Bluetooth

bluetooth = Bluetooth()
bluetooth.set_advertisement(name='LoPy', service_uuid=b'1234567890123456')

def conn_cb (bt_o):
    events = bt_o.events()   # this method returns the flags and clears the internal registry
    if events & Bluetooth.CLIENT_CONNECTED:
        print("Client connected")
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print("Client disconnected")

bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)

bluetooth.advertise(True)
```

### bluetooth.set\_advertisement\(\* , name=None, manufacturer\_data=None, service\_data=None, service\_uuid=None\)

Configure the data to be sent while advertising. If left with the default of `None` the data won’t be part of the advertisement message.

The arguments are:

* `name` is the string name to be shown on advertisements.
* `manufacturer_data` manufacturer data to be advertised \(hint: use it for iBeacons\).
* `service_data` service data to be advertised.
* `service_uuid` uuid of the service to be advertised.

Example:

```python
bluetooth.set_advertisement(name="advert", manufacturer_data="lopy_v1")
```

### bluetooth.advertise\(\[Enable\]\)

Start or stop sending advertisements. The set\_advertisement\(\) method must have been called prior to this one.

### bluetooth.service\(uuid, \* , isprimary=True, nbr\_chars=1, start=True\)

Create a new service on the internal GATT server. Returns a object of type `BluetoothServerService`.

The arguments are:

* `uuid` is the UUID of the service. Can take an integer or a 16 byte long string or bytes object.
* `isprimary` selects if the service is a primary one. Takes a `bool` value.
* `nbr_chars` specifies the number of characteristics that the service will contain.
* `start` if `True` the service is started immediately.

```python
bluetooth.service('abc123')
```

### bluetooth.disconnect\_client\(\)

Closes the BLE connection with the client.

## Constants

### Bluetooth mode

Bluetooth.BLE

### Advertisement type

Bluetooth.CONN\_ADVBluetooth.CONN\_DIR\_ADVBluetooth.DISC\_ADVBluetooth.NON\_CONN\_ADVBluetooth.SCAN\_RSP

### Address type

Bluetooth.PUBLIC\_ADDRBluetooth.RANDOM\_ADDRBluetooth.PUBLIC\_RPA\_ADDRBluetooth.RANDOM\_RPA\_ADDR

### Advertisement data type

Bluetooth.ADV\_FLAGBluetooth.ADV\_16SRV\_PARTBluetooth.ADV\_T16SRV\_CMPLBluetooth.ADV\_32SRV\_PARTBluetooth.ADV\_32SRV\_CMPLBluetooth.ADV\_128SRV\_PARTBluetooth.ADV\_128SRV\_CMPLBluetooth.ADV\_NAME\_SHORTBluetooth.ADV\_NAME\_CMPLBluetooth.ADV\_TX\_PWRBluetooth.ADV\_DEV\_CLASSBluetooth.ADV\_SERVICE\_DATABluetooth.ADV\_APPEARANCEBluetooth.ADV\_ADV\_INTBluetooth.ADV\_32SERVICE\_DATABluetooth.ADV\_128SERVICE\_DATABluetooth.ADV\_MANUFACTURER\_DATA

### Characteristic properties \(bit values that can be combined\)

Bluetooth.PROP\_BROADCASTBluetooth.PROP\_READBluetooth.PROP\_WRITE\_NRBluetooth.PROP\_WRITEBluetooth.PROP\_NOTIFYBluetooth.PROP\_INDICATEBluetooth.PROP\_AUTHBluetooth.PROP\_EXT\_PROP

### Characteristic callback events

Bluetooth.CHAR\_READ\_EVENTBluetooth.CHAR\_WRITE\_EVENTBluetooth.NEW\_ADV\_EVENTBluetooth.CLIENT\_CONNECTEDBluetooth.CLIENT\_DISCONNECTEDBluetooth.CHAR\_NOTIFY\_EVENT

### Antenna type

Bluetooth.INT\_ANTBluetooth.EXT\_ANT

