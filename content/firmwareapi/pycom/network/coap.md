---
title: "CoAP"
aliases:
    - firmwareapi/pycom/network/coap.html
    - firmwareapi/pycom/network/coap.md
    - chapter/firmwareapi/pycom/network/coap
---
This module implements a CoAp Server and Client.

## Usage Example of CoAp Server

```python

from network import WLAN
from network import Coap
import _thread

# Thread handling the CoAp Server
def coap_thread():
    while True:
        Coap.read()

# Connect to the network
wlan = WLAN(mode=WLAN.STA)
wlan.connect('your-ssid', auth=(WLAN.WPA2, 'your-key'))

# Initialize Coap module as CoAp Server, enable new resources to be added via PUT 
Coap.init(str(wlan.ifconfig()[0]), service_discovery=True, dynamic_resources=True)

# Add an example resource with URI "resource1" and value "default_value" and content format "plain text" 
r = Coap.add_resource("resource1", media_type=Coap.MEDIATYPE_TEXT_PLAIN, value="default_value")
# Configure the possible operations on the resource
r.callback(Coap.REQUEST_GET | Coap.REQUEST_POST | Coap.REQUEST_PUT, True)

# Start a new thread which handles the CoAp Server
_thread.start_new_thread(coap_thread, ())

```

## Usage Example of CoAp Client

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
        Coap.read()

# Connect to the network
wlan = WLAN(mode=WLAN.STA)
wlan.connect('your-ssid', auth=(WLAN.WPA2, 'your-key'))

# Initialize Coap module
Coap.init(str(wlan.ifconfig()[0]))

# Register the response handler for the requests the module initiates as a Coap Client
Coap.register_response_handler(response_callback)
# Create a new Client Session to use to communicate with the CoAp Server
session = Coap.new_client_session("server-ip-address")

# Start a new thread which calls Coap.read() to handle incoming requests
_thread.start_new_thread(coap_thread, ())

# Send a GET Request to the CoAp Server asking for all resources via URI ".well-known/core"
id = session.send_request(Coap.REQUEST_GET, uri_path=".well-known/core")
print(id)

```

## Initialization

#### Coap.init(address, *, port=5683, service_discovery=False, dynamic_resources=False, psk=None, hint=None)

Initialize the CoAp module.

The arguments are:

* `address` is the address where the CoAp module handles communication when it is a Server. If not set, the module can be used as a CoAp Client only.
* `port` is the port where the CoAp Server listens. If not set, the default CoAp UDP port 5683 is used if no PSK is given otherwise the default CoAp DTLS port 5684 is used.
* `service_discovery` is a Boolean argument that enables/disables service discovery. If enabled, the CoAp Server will listen on the CoAp multicast address: 224.0.1.187. This is disabled by default.
* `dynamic_resources` is a Boolean argument that enables/disables new resource creation via PUT operations. This is disabled by default.
* `psk` is a String representing the Pre-Shared Key to be used for the DTLS connection. 
* `hint` is a String representing the hint value to be used for the DTLS connection.

When `dynamic_resources` is TRUE new resources can be created via PUT reqeusts, if the resource with the given URI does not already exist.
The new resource is created with default properties (no mediatype, no Max-Age and no ETAG is enabled) and with default value received in the PUT request. On the new resource by default all operations (GET, PUT, POST and DELETE) are enabled.

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

#### Coap.register_new_resource_handler(callback)

Registers a callback function which will be called when a new resource has been created via PUT operation.

* `callback` is the callback to be registered. The callback must have 1 argument:
    * `resource` is the new resource which has been created

#### Coap.new_client_session(address, *, port=5683, psk=None, identity=None)

Creates a new CoAp Client Session which can be used to communicate with an external CoAp Server.

* `address` is the IPv4 Address of the CoAp Server to join.
* `port` is the port of the CoAp Server to join. If not set, the default CoAp UDP port 5683 is used if no PSK is given otherwise the default CoAp DTLS port 5684 is used.
* `psk` is a String representing the Pre-Shared Key to be used for the DTLS connection. 
* `identity` is a String representing the identity value to be used for the DTLS connection.


#### Coap.remove_client_session(destination, port=5683, protocol=UDP)

Removes the specified CoAp Client Session.

* `destination` is the IPv4 Address of the CoAp Server where this CoAp Client Session has joined.
* `port` is the port of the CoAp Server where this CoAp Client Session has joined. If not set, the default CoAp UDP port 5683 is used.
* `protocol` is the protocol to be used to communicate with the CoAp Server where this CoAp Client Session has joined. This value can be: `Coap.PROTOCOL_UDP`,`Coap.PROTOCOL_DTLS`, if not set the protocol UDP is used.

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

* `Item 0:` is the IPv4 Address of the CoAp Server where this CoAp Client Session has joined.
* `Item 1:` is the port of the CoAp Server where this CoAp Client Session has joined.

## Class CoapResource

The CoapResource class represents a resource in the scope of the CoAp module when acting as a server.

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

#### CoapResource.get_details()

Returns with the main details of this resource in a form of list:
* `Item 0:` is the URI of the resource.
* `Item 1:` is the mediatype (content format) configured for this resource. -1 means no mediatype is configured.
* `Item 2:` is the Max-Age configured for this resource. -1 means no Max-Age is configured.
* `Item 3:` is a boolean showing whether ETAG is enabled on this resource.
* `Item 4:` is the current ETAG value.

#### CoapResource.set_details(*, mediatype, max_age, etag)

Configures the main details of this resource:
* `mediatype` is the mediatype (content format) os the resource. Value -1 means no mediatype is defined for this resource.
* `max_age` is max-age value to be used on the resource. Value -1 means no Max-Age is defined for this resource.
* `etag` is a Boolean which enables or disables ETAG on the resource.

This function leaves untouched any property of the resource not given as a parameter.


#### CoapResource.value(value)

Updates or fetches the value of the resource.

* `value` is the new value to update the current value with.
If the method is called without a parameter, the current value is returned.

#### CoapResource.callback(operation, enable)
To enable or disable a specific operation (GET, PUT, POST, DELETE) on the resource.

* `operation` is the operation to enable/disable, can be ORED of the followings: `Coap.REQUEST_GET`, `Coap.REQUEST_PUT`, `Coap.REQUEST_POST`, `Coap.REQUEST_DELETE`
* `enable` is Boolean parameter that enables/disables the operations specified by `operation`


{{% hint style="info" %}}
During a GET request, only the first occurrence of an ETAG or Accept option is interpreted; others of the same type are dropped (if any).
{{% /hint %}}

{{% hint style="info" %}}
During a PUT request, only the first occurrence of an If-Match and If-None-Match option is interpreted; others of the same type are dropped (if any).
{{% /hint %}}

{{% hint style="danger" %}}
Due to limitations of the underlying ESP-IDF/libcoap library, new resources cannot be added via POST request.
{{% /hint %}}

## Constants

* Define the media type: `Coap.MEDIATYPE_TEXT_PLAIN`, `Coap.MEDIATYPE_APP_LINK_FORMAT`, `Coap.MEDIATYPE_APP_XML`, `Coap.MEDIATYPE_APP_OCTET_STREAM`, `Coap.MEDIATYPE_APP_RDF_XML`, `Coap.MEDIATYPE_APP_EXI`, `Coap.MEDIATYPE_APP_JSON`, `Coap.MEDIATYPE_APP_CBOR`
* Define the operation: `Coap.REQUEST_GET`, `Coap.REQUEST_PUT`, `Coap.REQUEST_POST`, `Coap.REQUEST_DELETE`
* Define the protocol:  `Coap.PROTOCOL_UDP`,`Coap.PROTOCOL_DTLS`