# class GATTCService
Services are used to categorise data up into specific chunks of data known as characteristics. A service may have multiple characteristics, and each service has a unique numeric ID called a UUID.

The following class allows control over Client services.

#####<function>service.isprimary()</function>

Returns ``True`` if the service is a primary one. ``False`` otherwise.

#####<function>service.uuid()</function>

Returns the UUID of the service. In the case of 16-bit or 32-bit long UUIDs, the value returned is an integer, but for 128-bit long UUIDs the value returned is a bytes object.

#####<function>service.instance()</function>

Returns the instance ID of the service.

#####<function>service.characteristics()</function>

Performs a get characteristics request on the connected BLE peripheral a returns a list containing objects of the class <class>GATTCCharacteristic</class> if the request succeeds.
