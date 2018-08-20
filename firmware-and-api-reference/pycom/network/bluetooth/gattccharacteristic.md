# GATTCCharacteristic

The smallest concept in GATT is the Characteristic, which encapsulates a single data point \(though it may contain an array of related data, such as X/Y/Z values from a 3-axis accelerometer, longitude and latitude from a GPS, etc.\).

The following class allows you to manage characteristics from a Client.

## Methods

#### characteristic.uuid\(\)

Returns the UUID of the service. In the case of 16-bit or 32-bit long UUIDs, the value returned is an integer, but for 128-bit long UUIDs the value returned is a bytes object.

#### characteristic.instance\(\)

Returns the instance ID of the service.

#### characteristic.properties\(\)

Returns an integer indicating the properties of the characteristic. Properties are represented by bit values that can be OR-ed together. See the constants section for more details.

#### characteristic.read\(\)

Read the value of the characteristic, sending a request to the GATT server. Returns a bytes object representing the characteristic value.

#### characteristic.value\(\)

Returns the locally stored value of the characteristic without sending a read request to the GATT server. If the characteristic value hasn't been read from the GATT server yet, the value returned will be 0.

#### characteristic.write\(value\)

Writes the given value on the characteristic. For now it only accepts bytes object representing the value to be written.

```python
characteristic.write(b'x0f')
```

#### characteristic.callback\(trigger=None, handler=None, arg=None\)

This method allows to register for notifications on the characteristic.

* `trigger` can must be `Bluetooth.CHAR_NOTIFY_EVENT`.
* `handler` is the function that will be executed when the callback is triggered.
* `arg` is the argument that gets passed to the callback. If nothing is given, the characteristic object that owns the callback will be used.

