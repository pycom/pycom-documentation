# class Bluetooth

This class provides a driver for the Bluetooth radio in the module. Currently, only basic BLE functionality is available.

### Quick Usage Example

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

### Bluetooth Low Energy (BLE)

Bluetooth low energy (BLE) is a subset of classic Bluetooth, designed for easy connecting and communicating between devices (in particular mobile platforms). BLE uses a methodology known as Generic Access Profile (GAP) to control connections and advertising.

GAP allows for devices to take various roles but generic flow works with devices that are either a Server (low power, resource constrained, sending small payloads of data) or a Client device (commonly a mobile device, PC or Pycom Device with large resources and processing power). Pycom devices can act as both a Client and a Server.

### Constructors

<class><i>class</i> network.Bluetooth(id=0, ...)</class>

Create a Bluetooth object, and optionally configure it. See init for params of configuration.

Example:

```python
from network import Bluetooth
bluetooth = Bluetooth()
```

### Methods
<function>bluetooth.init()</function>

Initialises and enables the Bluetooth radio in BLE mode.

<function>bluetooth.deinit()</function>

Disables the Bluetooth radio.

<function>bluetooth.start_scan(timeout)</function>

Starts performing a scan listening for BLE devices sending advertisements. This function always returns immediately, the scanning will be performed on the background. The return value is ``None``. After starting the scan the function <function>get_adv()</function> can be used to retrieve the advertisements messages from the FIFO. The internal FIFO has space to cache 8 advertisements.

The arguments are:

- ``timeout`` specifies the amount of time in seconds to scan for advertisements, cannot be zero. If timeout is > 0, then the BLE radio will listen for advertisements until the specified value in seconds elapses. If timeout < 0, then there’s no timeout at all, and <function>stop_scan()</function> needs to be called to cancel the scanning process.

Examples:

```python
bluetooth.start_scan(10)        # starts scanning and stop after 10 seconds
bluetooth.start_scan(-1)        # starts scanning indefenitely until bluetooth.stop_scan() is called
```

<function>bluetooth.stop_scan()</function>

Stops an ongoing scanning process. Returns ``None``.

<function>bluetooth.isscanning()</function>

Returns ``True`` if a Bluetooth scan is in progress. ``False`` otherwise.

<function>bluetooth.get_adv()</function>

Gets an named tuple with the advertisement data received during the scanning. The tuple has the following structure: (``mac``, ``addr_type``, ``adv_type``, ``rssi``, ``data``)

- ``mac`` is the 6-byte ling mac address of the device that sent the advertisement.
- ``addr_type`` is the address type. See the constants section below for more details.
- ``adv_type`` is the advertisement type received. See the constants section below fro more details.
- ``rssi`` is signed integer with the signal strength of the advertisement.
- ``data`` contains the complete 31 bytes of the advertisement message. In order to parse the data and get the specific types, the method <function>resolve_adv_data()</function> can be used.

Example for getting ``mac`` address of an advertiser:

```python
import binascii

bluetooth = Bluetooth()
bluetooth.start_scan(20) # scan for 20 seconds

adv = bluetooth.get_adv() #
binascii.hexlify(adv.mac) # convert hexidecimal to ascii
```

<function>bluetooth.resolve_adv_data(data, data_type)</function>

Parses the advertisement data and returns the requested data_type if present. If the data type is not present, the function returns None.

Arguments:

- ``data`` is the bytes object with the complete advertisement data.
- ``data_type`` is the data type to resolve from from the advertisement data. See constants section below for details.

Example:

```python
import binascii
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
            print(binascii.hexlify(mfg_data))
```

<function>bluetooth.connect(mac_addr)</function>

Opens a BLE connection with the device specified by the ``mac_addr`` argument. This function blocks until the connection succeeds or fails. If the connections succeeds it returns a object of type ``GATTCConnection``.

```python
bluetooth.connect('112233eeddff') # mac address is accepted as a string
```

<function>bluetooth.callback(trigger=None, handler=None, arg=None)</function>

Creates a callback that will be executed when any of the triggers occurs. The arguments are:

- ``trigger`` can be either <constant>Bluetooth.NEW_ADV_EVENT</constant>, <constant>Bluetooth.CLIENT_CONNECTED</constant> or <constant>Bluetooth.CLIENT_DISCONNECTED</constant>
- ``handler`` is the function that will be executed when the callback is triggered.
- ``arg`` is the argument that gets passed to the callback. If nothing is given the bluetooth object itself is used.

An example of how this may be used can be seen in the <function>bluetooth.events()<function> method.

<function>bluetooth.events()</function>

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

<function>bluetooth.set_advertisement(* , name=None, manufacturer_data=None, service_data=None, service_uuid=None)</function>

Configure the data to be sent while advertising. If left with the default of None the data won’t be part of the advertisement message.

The arguments are:

- ``name`` is the string name to be shown on advertisements.
- ``manufacturer_data`` manufacturer data to be advertised (hint: use it for iBeacons).
- ``service_data`` service data to be advertised.
- ``service_uuid`` uuid of the service to be advertised.

Example:

```python
bluetooth.set_advertisement(name="advert", manufacturer_data="lopy_v1")
```

<function>bluetooth.advertise([Enable])</function>
Start or stop sending advertisements. The <function>set_advertisement()</function> method must have been called prior to this one.

<function>bluetooth.service(uuid, * , isprimary=True, nbr_chars=1, start=True)</function>

Create a new service on the internal GATT server. Returns a object of type ``BluetoothServerService``.

The arguments are:

- ``uuid`` is the UUID of the service. Can take an integer or a 16 byte long string or bytes object.
- ``isprimary`` selects if the service is a primary one. Takes a bool value.
- ``nbr_chars`` specifies the number of characteristics that the service will contain.
- ``start`` if ``True`` the service is started immediately.

```python
bluetooth.service('abc123')
```

<function>bluetooth.disconnect_client()<function>

Closes the BLE connection with the client.

### Constants
<constant>Bluetooth.CONN_ADV</constant> <constant>Bluetooth.CONN_DIR_ADV</constant> <constant>Bluetooth.DISC_ADV</constant> <constant>Bluetooth.NON_CONN_ADV</constant> <constant>Bluetooth.SCAN_RSP</constant>

Advertisement type

<constant>Bluetooth.PUBLIC_ADDR</constant> <constant>Bluetooth.RANDOM_ADDR</constant> <constant>Bluetooth.PUBLIC_RPA_ADDR</constant> <constant>Bluetooth.RANDOM_RPA_ADDR</constant>

Address type

<constant>Bluetooth.ADV_FLAG</constant> <constant>Bluetooth.ADV_16SRV_PART</constant> <constant>Bluetooth.ADV_T16SRV_CMPL</constant> <constant>Bluetooth.ADV_32SRV_PART</constant> <constant>Bluetooth.ADV_32SRV_CMPL</constant> <constant>Bluetooth.ADV_128SRV_PART</constant> <constant>Bluetooth.ADV_128SRV_CMPL</constant> <constant>Bluetooth.ADV_NAME_SHORT</constant> <constant>Bluetooth.ADV_NAME_CMPL</constant> <constant>Bluetooth.ADV_TX_PWR</constant> <constant>Bluetooth.ADV_DEV_CLASS</constant> <constant>Bluetooth.ADV_SERVICE_DATA</constant> <constant>Bluetooth.ADV_APPEARANCE</constant> <constant>Bluetooth.ADV_ADV_INT</constant> <constant>Bluetooth.ADV_32SERVICE_DATA</constant> <constant>Bluetooth.ADV_128SERVICE_DATA</constant> <constant>Bluetooth.ADV_MANUFACTURER_DATA</constant>

Advertisement data type

<constant>Bluetooth.PROP_BROADCAST</constant> <constant>Bluetooth.PROP_READ</constant> <constant>Bluetooth.PROP_WRITE_NR</constant> <constant>Bluetooth.PROP_WRITE</constant> <constant>Bluetooth.PROP_NOTIFY</constant> <constant>Bluetooth.PROP_INDICATE</constant> <constant>Bluetooth.PROP_AUTH</constant> <constant>Bluetooth.PROP_EXT_PROP</constant>

Characteristic properties (bit values that can be combined)

<constant>Bluetooth.CHAR_READ_EVENT</constant> <constant>Bluetooth.CHAR_WRITE_EVENT</constant> <constant>Bluetooth.NEW_ADV_EVENT</constant> <constant>Bluetooth.CLIENT_CONNECTED</constant> <constant>Bluetooth.CLIENT_DISCONNECTED</constant> <constant>Bluetooth.CHAR_NOTIFY_EVENT</constant>

Characteristic callback events
