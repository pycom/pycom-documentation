---
title: "MDNS"
aliases:
    - firmwareapi/pycom/network/mdns.html
    - firmwareapi/pycom/network/mdns.md
    - chapter/firmwareapi/pycom/network/mdns
---
This class provides an interface to use the MDNS functionality.

## Quick Usage Example

Example for advertising own services:

```python
import time
from network import MDNS
# As a first step connection to network should be estbalished, e.g. via WLAN

# Initialize the MDNS module
MDNS.init()
# Set the hostname and instance name of this device
MDNS.set_name(hostname = "my_hostname", instance_name = "my_instance")
# Add a TCP service to advertise
MDNS.add_service("_http", MDNS.PROTO_TCP, 80)
# Add an UDP service to advertise
MDNS.add_service("_myservice", MDNS.PROTO_UDP, 1234, txt= (("board","esp32"),("u","user"),("p","password")))

# Wait some time
time.sleep(60)
# Remove a service, it will no longer be advertised
MDNS.remove_service("_http", MDNS.PROTO_TCP)

```

Example for querying:

```python
import time
from network import MDNS
# As a first step connection to network should be estbalished, e.g. via WLAN

# Initialize the MDNS module
MDNS.init()

# Perform a query for 2000 ms
q = MDNS.query(2000, "_http", MDNS.PROTO_TCP)

# Print out the query's result
if q is not None:
    for elem in q:
        print(elem.instance_name())
        print(elem.hostname())
        print(elem.addr())
        print(elem.port())
        print(elem.txt())

```

## Constructor

### class network.MDNS()

Initializes the MDNS module.

## Methods

#### MDNS.deinit()

Deinitializes the MDNS module and removes all registered services.

#### MDNS.set_name(\*, hostname=None, instance_name=None)

Sets the hostname and instance name of this device to be advertised.

The arguments are:

* `hostname` is the hostname to set
* `instance_name` is the instance name to set

#### MDNS.add_service(service_type, proto, port, \*, txt)

Adds a service to the MDNS module which will be advertised.

The arguments are:

* `service_type` is the type of the offered service, e.g.: _http, _ftp or can be custom service
* `proto` is the Layer 4 protocol (TCP or UDP), can be `MDNS.PROTO_TCP` or `MDNS.PROTO_UDP`
* `port` is the port number
* `txt` is the TXT entries to be placed into the advertisement. The TXT entry is a (key, value) tuple and several TXT entries can be included in an advertisement. In that case, 'txt' must be given as a list of tuples.

#### MDNS.remove_service(service_type, proto)

Removes a service from the MDNS module so it will not be advertised anymore.

The arguments are:

* `service_type` is the type of the service, e.g.: _http, _ftp or can be custom service
* `proto` is the Layer 4 protocol (TCP or UDP), can be `MDNS.PROTO_TCP` or `MDNS.PROTO_UDP`

#### MDNS.query(timeout, service_type, proto, \*, instance_name=None)

Performs a query with the given parameters.

The arguments are:

* `timeout` is the timeout value in milliseconds to wait to receive the results
* `service_type` is the type of the service to be queried, e.g.: _http, _ftp or can be custom service
* `proto` is the Layer 4 protocol (TCP or UDP), can be `MDNS.PROTO_TCP` or `MDNS.PROTO_UDP`
* `instance_name` is the instance name of the service to be queried

If the service is found then the function returns with a list of `MDNS_Query` objects.

## MDNS_Query class

The `MDNS_Query` aggregates all of the properties of a successful query session entry:
* `hostname` is the hostname of the host advertising the service
* `instance_name` is the instance_name of the service
* `addr` is the IPv4 address belonging to the service
* `port` is the port number belonging to the service
* `txt` is the TXT entries from the advertisement. The TXT entry is a (key, value) tuple, and several TXT entries can be included in an advertisement.

#### MDNS_Query.hostname()

Returns with the hostname of the queried service.

#### MDNS_Query.instance_name()

Returns with the instance name of the queried service.

#### MDNS_Query.addr()

Returns with the IPv4 address of the queried service.

#### MDNS_Query.port()

Returns with the port of the queried service.

#### MDNS_Query.txt()

Returns with the TXT entries of the queried service.

## Constants

* TCP and UDP protocol types: `MDNS.PROTO_TCP`, `MDNS.PROTO_UDP`


