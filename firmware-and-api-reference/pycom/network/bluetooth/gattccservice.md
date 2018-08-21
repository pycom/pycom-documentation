# GATTCService

Services are used to categorise data up into specific chunks of data known as characteristics. A service may have multiple characteristics, and each service has a unique numeric ID called a UUID.

The following class allows control over Client services.

## Methods

#### service.isprimary\(\)

Returns `True` if the service is a primary one. `False` otherwise.

#### service.uuid\(\)

Returns the UUID of the service. In the case of 16-bit or 32-bit long UUIDs, the value returned is an integer, but for 128-bit long UUIDs the value returned is a bytes object.

#### service.instance\(\)

Returns the instance ID of the service.

#### service.characteristics\(\)

Performs a get characteristics request on the connected BLE peripheral a returns a list containing objects of the class GATTCCharacteristic if the request succeeds.

