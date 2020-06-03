---
title: "CoAP"
aliases:
    - firmwareapi/pycom/network/coap.html
    - firmwareapi/pycom/network/coap.md
    - chapter/firmwareapi/pycom/network/coap
---
This module implements a CoAp Server and Client, operating as both at the same time.

## Usage Example of CoAp Server

```python

from network import WLAN
from network import Coap
import _thread

# Thread handling the CoAp Server
def coap_thread():
    while True:
        # Call Coap.read() without specyfing timeout value, in this way it handled all requests sent to the CoAp Server silently
        Coap.read()


# Connect to the network
wlan = WLAN(mode=WLAN.STA)
wlan.connect('your-ssid', auth=(WLAN.WPA2, 'your-key'))

# Initialize Coap module as CoAp Server
Coap.init(str(wlan.ifconfig()[0]), service_discovery=True)

# Add a resource with default value and plain text content format
r = Coap.add_resource("resource1", media_type=Coap.MEDIATYPE_TEXT_PLAIN, value="default_value")
# Add an attribute to the resource
r.add_attribute("title", "resource1")
# Add an attribute to the resource
r.add_attribute("ct", str(Coap.MEDIATYPE_TEXT_PLAIN))
# Configure the possible operations on the resource
r.callback(Coap.REQUEST_GET | Coap.REQUEST_POST | Coap.REQUEST_PUT, True)

# Add a resource without default value, XML content format and E-Tag enabled
r = Coap.add_resource("resource2", media_type=Coap.MEDIATYPE_APP_XML, etag=True)
# Configure the possible operations on the resource
r.callback(Coap.REQUEST_GET | Coap.REQUEST_POST | Coap.REQUEST_PUT | Coap.REQUEST_DELETE, True)

# Start a new thread which handles the CoAp Server
_thread.start_new_thread(coap_thread, ())

```

## Usage Example of CoAp Client in blocking mode

```python

from network import WLAN
from network import Coap
import _thread

# Callback handling the responses to the requests sent to a Coap Server
def response_callback(code, id_param, type_param, token, payload):
    print("Code: {}".format(code))
    # The ID can be used to pair the requests with the responses
    print("ID: {}".format(id_param))
    print("Type: {}".format(type_param))
    print("Token: {}".format(token))
    print("Payload: {}".format(payload))

# Thread handling the sockets
def coap_thread():
    while True:
        # Using Coap.read() without timeout value means that if no new packet arrives to any of the client sessions registered before this is called, then this function will never return
        Coap.read()


# Connect to the network
wlan = WLAN(mode=WLAN.STA)
wlan.connect('your-ssid', auth=(WLAN.WPA2, 'your-key'))

# Initialize Coap module
Coap.init(str(wlan.ifconfig()[0]), service_discovery=True)

# Register the response handler for the requests the module initiates as a Coap Client
Coap.register_response_handler(response_callback)

# As the Coap.read() will be called in a form that it blocks until no new data arrives to the socket, it is only safe
# to create new client sessions before Coap.read() is called
session = Coap.new_client_session("192.168.0.234", 5683)

# Start a new thread which calls Coap.read() which will block until no new packet arrives to the socket
_thread.start_new_thread(coap_thread, ())

# After this point it is not safe to create new Coap Client Session as they might not be handled by Coap.read()

# Request to a normal CoAp Server
id = session.send_request(Coap.REQUEST_GET, uri_path=".well-known/core", payload="payload", token="token1", include_options=True)
print(id)
# Request to a normal CoAp Server
id = session.send_request(Coap.REQUEST_GET, uri_path="time", payload="payload", token="token2", include_options=True)
print(id)
# Request to a normal CoAp Server
id = session.send_request(Coap.REQUEST_PUT, uri_path="time",content_format=Coap.MEDIATYPE_TEXT_PLAIN, payload="ABCD", token="token3", include_options=True)
print(id)
# Request to a Dish Telemetry server, payload is the AMQP message, token is maximum 8 bytes containing the IMEI or IMSI id, no options should be present
imei = int('359738090028145').to_bytes(8, 'big')
id = session.send_request(Coap.REQUEST_GET, payload="amqp://artemis:5672/dish.app1.FjhBV78.telemetry", token=imei, include_options=False)
print(id)

```

## Usage Example of CoAp Client in non-blocking mode

```python

from network import WLAN
from network import Coap
import _thread

# Callback handling the responses to the requests sent to a Coap Server
def response_callback(code, id_param, type_param, token, payload):
    print("Code: {}".format(code))
    # The ID can be used to pair the requests with the responses
    print("ID: {}".format(id_param))
    print("Type: {}".format(type_param))
    print("Token: {}".format(token))
    print("Payload: {}".format(payload))

# Thread handling the sockets
def coap_thread():
    while True:
        # Wait only 3 seconds for new packets then return back
        # In the next call it will also handle any new CoAp Client Sessions created during the previous call
        Coap.read(3000)


# Connect to the network
wlan = WLAN(mode=WLAN.STA)
wlan.connect('your-ssid', auth=(WLAN.WPA2, 'your-key'))

# Initialize Coap module, to be used only as a CoAp Client
Coap.init()

# Start a new thread which handles the CoAp, it is safe to start as soon as possible as the Coap.read() has timeout specified
# After this point it is safe to create new CoAp Client Sessions, it will be processed by the coap_thread correctly as Coap.read() is used with timeout value
_thread.start_new_thread(coap_thread, ())

# Register the response handler for the requests the module initiates as a Coap Client
Coap.register_response_handler(response_callback)

# Create a new client session on demand
session1 = Coap.new_client_session("192.168.0.234", 5683)

# Request to a normal CoAp Server via CoAp Client Session: session1
id = session1.send_request(Coap.REQUEST_GET, uri_path=".well-known/core", token="session1")
print(id)
# Request to a normal CoAp Server via CoAp Client Session: session1
id = session1.send_request(Coap.REQUEST_GET, uri_path="time", token="session1")
print(id)

# Create again a new CoAp Client Session on demand, without restriction
session2 = Coap.new_client_session("192.168.0.236", 5683)

# Request to a normal CoAp server via CoAp Client Session: session2
id = session2.send_request(Coap.REQUEST_GET, uri_path=".well-known/core")
print(id)
# Request to a normal CoAp server via CoAp Client Session: session2
id = session2.send_request(Coap.REQUEST_GET, uri_path="resource1")
print(id)
# Request to a normal CoAp server via CoAp Client Session: session2
id = session2.send_request(Coap.REQUEST_POST, uri_path="resource1", payload="new_value")
print(id)

```


## Initialization

#### Coap.init(address, *, port=5683, service_discovery=False)

Initialize the CoAp module.

The arguments are:

* `address` is the address where the CoAp module handles communication when it is a Server. If not set, the module can be used as a CoAp Client only.
* `port` is the port where the CoAp Server listens. If not set, the default CoAp UDP port is 5683.
* `service_discovery` is a Boolean argument that enables/disables service discovery. If enabled, the CoAp Server will listen on the CoAp multicast address: 224.0.1.187. This is disabled by default.

## Methods:

#### Coap.add_resource(uri, *, media_type=-1, max_age=-1, value=0, etag=False)

Creates a resource object and adds it to the CoAp Server.

* `uri` is the full path of the resource.
* `media_type` is the media type (CoAp option: Content-Format) of the resource. If not given, no defined media type is associated with the resource.
* `max_age` is the maximum time in seconds that the value of the resource is considered fresh (CoAp option: Max-Age). If not given, no fresh time is associated with the resource.
* `value` is the default value of the resource. If not given, it is initialised to decimal 0.
* `etag` is a Boolean argument that enables/disables entity tag calculation (CoAp option: ETag). By default it is turned off.


{{% hint style="info" %}}
Media-type argument is one of the standard defined values that is available via CoAp module's constants.
{{% /hint %}}

{{% hint style="info" %}}
Entity tag calculation is a simple counter increment between value 1-65535 with overflow, it doesn't include the value 0. It is incremented each time and the value of the resource is changed.
{{% /hint %}}


#### Coap.remove_resource(uri)

Removes the resource defined by the `uri` argument.

* `uri` is the full path of the resource to be removed.

#### Coap.get_resource(uri)

Returns with the resource defined by `uri` argument.

* `uri` is the full path of the resource to be returned.

#### Coap.read(timeout=0)

Must be called peridically to process any incoming CoAp packets.

* `timeout` is a timeout value in milliseconds. If not set or value 0 is passed the call will be blocked forever or until a new CoAp packet arrives on the CoAp Server (if any) or on the already registered CoAp Client Sessions (if any). If the value is given it returns after the defined timeout or when a new CoAp packet arrives to the CoAp Server (if any) or to the already registered CoAp Client Sessions (if any).

{{% hint style="info" %}}
Coap.read() is only aware of the CoAp Client Sessions created before the actual Coap.read() is called. If the `timeout` is not specified or 0, it is not safe to create additional CoAp Client Sessions after the first call to Coap.read() as it may happen that no CoAp packets arrives to the CoAp Server or to the already created CoAp Client Sessions thus the newly created CoAp Client Session will not be served as the current Coap.read() will never return.
{{% /hint %}}

#### Coap.register_response_handler(callback)

Registers a callback function which will be called when a remote CoAp Server responses to the local CoAp client's request.

* `callback` is the callback to be registered. It must have the following arguments:
* `code` is the response code from the received message
* `id_param` is the transaction ID of the received message. This can be used to match together requests and the response for it.
* `type_param` is the type flag from the received message
* `token` is the token field from the received message
* `payload` is the payload of the received message

#### Coap.new_client_session(destination, port=5683, protocol=UDP)

Creates a new CoAp Client Session which can be used to communicate with an external CoAp Server.

* `destination` is the IPv4 Address of the CoAp Server to join.
* `port` is the port of the CoAp Server to join. If not set, the default CoAp UDP port 5683 is used.
* `protocol` is the protocol to use to communicate with the CoAp Server. If not set the protocol UDP is used. Currently no other protocols than UDP is supported.


#### Coap.remove_client_session(destination, port=5683, protocol=UDP)

Removes the specified CoAp Client Session.

* `destination` is the IPv4 Address of the CoAp Server where this CoAp Client Session has joined.
* `port` is the port of the CoAp Server where this CoAp Client Session has joined. If not set, the default CoAp UDP port 5683 is used.
* `protocol` is the protocol to use to communicate with the CoAp Server where this CoAp Client Session has joined. If not set the protocol UDP is used. Currently no other protocols than UDP is supported.

#### Coap.get_client_sessions()

Returns with all the registered CoAp Client Sessions.

## Class Client Session

The CoAp Client Session class represents a Client Session in the scope of the CoAp module which can be used to communicate with an external CoAp Server. A new CoAp Client Session can only be created with the `Coap.new_client_session` function.

#### CoapClientSession.send_request(method, *, uri_path, content_format, payload, token, include_options=true)

Creates and sends a request to the external CoAp Server defined by the `destination` and `port` parameters when this CoAp Client Session was created.

* `method` is the method to be sent to the server, can be: `Coap.REQUEST_GET`, `Coap.REQUEST_PUT`, `Coap.REQUEST_POST`, `Coap.REQUEST_DELETE`
* `uri_path` is the full path of the resource in the server, included in the message as an "URI-PATH" option. If nothing is given the request will not have URI-PATH option.
* `content_format` is the Content-Format option of the request, can be: `Coap.MEDIATYPE_TEXT_PLAIN`, `Coap.MEDIATYPE_APP_LINK_FORMAT`, `Coap.MEDIATYPE_APP_XML`, `Coap.MEDIATYPE_APP_OCTET_STREAM`, `Coap.MEDIATYPE_APP_RDF_XML`, `Coap.MEDIATYPE_APP_EXI`, `Coap.MEDIATYPE_APP_JSON`, `Coap.MEDIATYPE_APP_CBOR`. If nothing is given the request will not have Content-Format option.
* `payload` is the payload of the request. If nothing is given the request will not have payload.
* `token` is the token field of the request. If nothing is given the request will not have token field.
* `include_options` decides whether put any options (including the ones above) into the message or not. It can be used to send special requests to servers accepting CoAp formed requests without options, e.g. to a Dish Telemetry server. By default, the options are included.

#### CoapClientSession.get_details()

Returns with a list of elements showing internal information about this CoAP Client Session:

* `destination` is the IPv4 Address of the CoAp Server where this CoAp Client Session has joined.
* `port` is the port of the CoAp Server where this CoAp Client Session has joined.

## Class CoapResource

The CoapResource class represents a resource in the scope of the CoAp module when acting as a server. A new resource can only be created with the `Coap.add_resource` function.

#### Class methods

The following methods are defined in the scope of the `resource` class.

#### CoapResource.add_attribute(name, value)

Adds a new attribute to the resource. Attributes are used to explain the resource during service discovery.

* `name` is the name of the resource.
* `value` is the value of the resource.

{{% hint style="info" %}}
During service discovery, GET request to ".well-know/core", the attributes are returned with the relevant values.
E.g. using the "libcoap's" command line coap-client to fetch the resource from our server:

coap-client -m get coap://<Coap-Server's address>/.well-known/core

< /resource2>,< /resource1>;ct=0;title=resource1

{{% /hint %}}

#### CoapResource.value(value)

Updates or fetches the value of the resource.

* `value` is the new value to update the current value with.
If the method is called without a parameter, the current value is returned.

#### CoapResource.callback(operation, enable)
To enable or disable a specific operation (GET, PUT, POST, DELETE) on the resource.

* `operation` is the operation to enable/disable, can be ORED of the followings: `Coap.REQUEST_GET`, `Coap.REQUEST_PUT`, `Coap.REQUEST_POST`, `Coap.REQUEST_DELETE`
* `enable` is Boolean parameter that enables/disables the operations specified by `operation`


{{% hint style="info" %}}
During a GET request, only the first occurrence of an ETAG or Accept option is passed on and interpreted; others of the same type are dropped (if any).
{{% /hint %}}

{{% hint style="info" %}}
During a PUT request, only the first occurrence of an If-Match option is passed on and interpreted; others of the same type are dropped (if any).
{{% /hint %}}

{{% hint style="danger" %}}
Due to limitations of the underlying ESP-IDF/libcoap library, new resources cannot be added via PUT or POST requests.
{{% /hint %}}

## Constants

* Define the media type: `Coap.MEDIATYPE_TEXT_PLAIN`, `Coap.MEDIATYPE_APP_LINK_FORMAT`, `Coap.MEDIATYPE_APP_XML`, `Coap.MEDIATYPE_APP_OCTET_STREAM`, `Coap.MEDIATYPE_APP_RDF_XML`, `Coap.MEDIATYPE_APP_EXI`, `Coap.MEDIATYPE_APP_JSON`, `Coap.MEDIATYPE_APP_CBOR`
* Define the operation: `Coap.REQUEST_GET`, `Coap.REQUEST_PUT`, `Coap.REQUEST_POST`, `Coap.REQUEST_DELETE`
