# GATTSService

The GATT Server allows the device to act as a peripheral and hold its own ATT lookup data, server & characteristic definitions. In this mode, the device acts as a slave and a master must initiate a request.

Services are used to categorise data up into specific chunks of data known as characteristics. A service may have multiple characteristics, and each service has a unique numeric ID called a UUID.

The following class allows control over Server services.

## Methods

#### service.start\(\)

Starts the service if not already started.

#### service.stop\(\)

Stops the service if previously started.

#### service.characteristic\(uuid, \* , permissions, properties, value\)

Creates a new characteristic on the service. Returns an object of the class `GATTSCharacteristic`. The arguments are:

* `uuid` is the UUID of the service. Can take an integer or a 16 byte long string or bytes object.
* `permissions` configures the permissions of the characteristic. Takes an integer with a combination of the flags.
* `properties` sets the properties. Takes an integer with an OR-ed combination of the flags.
* `value` sets the initial value. Can take an integer, a string or a bytes object.

```python
service.characteristic('temp', value=25)
```

