---
title: "CoAP"
aliases:
    - firmwareapi/pycom/network/coap.html
    - firmwareapi/pycom/network/coap.md
    - chapter/firmwareapi/pycom/network/coap
---
This module implements a CoAp Server and Client, it operates as both at the same time.

## Usage Example

```python

from network import WLAN
from network import Coap
import uselect
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
def socket_thread(p, coap_socket):
    while True:
        # Wait for any socket to become available
        sockets = p.poll()
        for s in sockets:
            sock = s[0]
            event = s[1]
            if(event & uselect.POLLIN):
                # Check if the socket belongs to Coap module
                if(sock == coap_socket):
                    # Call Coap.read() which parses the incoming Coap message
                    Coap.read()


# Connect to the network
wlan = WLAN(mode=WLAN.STA)
wlan.connect('your-ssid', auth=(WLAN.WPA2, 'your-key'))

# Initialize Coap module
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

# Register the response handler for the requests the module initiates as a Coap Client
Coap.register_response_handler(response_callback)

# Get the UDP socket created for the Coap module
coap_server_socket = Coap.socket()

# Create a new poll object
p = uselect.poll()
# Register the Coap Module's socket to the poll
p.register(coap_server_socket, uselect.POLLIN | uselect.POLLHUP | uselect.POLLERR)

# Start a new thread which will handle the sockets of "p" poll
_thread.start_new_thread(socket_thread, (p, coap_server_socket))

# Send a request to a Coap server
id = Coap.send_request("192.168.0.234", Coap.REQUEST_GET, uri_port=5683, uri_path=".well-known/core", payload="payload", token="token1", include_options=True)
print(id)

```

## Initialization

#### Coap.init(address, *, port=5683, service_discovery=False)

Initialize the Coap module.

Arguments are:

* `address` is the address where Coap Module will handle the communication .
* `port` is the port where Coap Module will listen, if not given it is the default Coap UDP port: 5683.
* `service_discovery` is a boolean argument to enable/disable service discovery. If enabled, the Coap Module will listen on the Coap Multicast address too: 224.0.1.187. By default it is disabled.

## Module's methods

#### Coap.socket()

Returns with the socket assigned to the given `address` and `port` during `Coap.init()` (= assigned to the Coap Module).

#### Coap.add_resource(uri, *, media_type=-1, max_age=-1, value=0, etag=False)

Creates a resource object and adds it to the Coap Module to operate as a server.

* `uri` is the full path of the resource.
* `media_type` is the media type (Coap option: Content-Format) of the resource. If not given, no defined media type is associated with the resource.
* `max_age` is the maximum time in seconds when the value of the resource is considered fresh (Coap option: Max-Age). If not given, no fresh time is associated with the resource.
* `value` is the default value of the resource. If not given it is initialized to decimal 0.
* `etag` is a boolean argument to enable/disable entity tag calculation (Coap option: ETag). By default it is turned off.


{{% hint style="info" %}}
Media type argument should be one of the standard defined value which are available via Coap Module's constants.
{{% /hint %}}

{{% hint style="info" %}}
Entity tag calculation is a simple counter increment between value 1-65535 with overflow but without value 0. Incremented each time the value of the resource is changed.
{{% /hint %}}


#### Coap.remove_resource(uri)

Removes the resource defined by `uri` argument.

* `uri` is the full path of the resource to be removed.

#### Coap.get_resource(uri)

Returns with the resource defined by `uri` argument.

* `uri` is the full path of the resource to be returned.

#### Coap.read()

Must be called when a packet is received on the socket assigned to the Coap Module. This function parses the incoming request, composes and sends out the response if needed.

#### Coap.register_response_handler(callback)

Registers a callback function which will be called when a remote Coap Server responses to our request.

* `callback` is the callback to be registered. It must have the following arguments:
* `code` is the response code from the received message
* `id_param` is the transaction ID of the received message. This can be used to match together requests and the response for it.
* `type_param` is the type flag from the received message
* `token` is the token field from the received message
* `payload` is the payload of the received message

#### Coap.send_request(uri_host, method, *, uri_port=5683, uri_path, content_format, payload, token, include_options=true)

Creates and sends a request to a Coap server.

* `uri_host` is the IP address of the server, included in the message as an "URI-HOST" option
* `method` is the method to be sent to the server, can be: `Coap.REQUEST_GET`, `Coap.REQUEST_PUT`, `Coap.REQUEST_POST`, `Coap.REQUEST_DELETE`
* `uri_port` is the port of the server, included in the message as an "URI-PORT" option, by default it is 5683
* `uri_path` is the full path of the resource in the server, included in the message as an "URI-PATH" option. If nothing is given the request will not have URI-PATH option.
* `content_format` is the Content-Format option of the request, can be: `Coap.MEDIATYPE_TEXT_PLAIN`, `Coap.MEDIATYPE_APP_LINK_FORMAT`, `Coap.MEDIATYPE_APP_XML`, `Coap.MEDIATYPE_APP_OCTET_STREAM`, `Coap.MEDIATYPE_APP_RDF_XML`, `Coap.MEDIATYPE_APP_EXI`, `Coap.MEDIATYPE_APP_JSON`, `Coap.MEDIATYPE_APP_CBOR`. If nothing is given the request will not have Content-Format option.
* `payload` is the payload of the request. If nothing is given the request will not have payload.
* `token` is the token field of the request. If nothing is given the request will not have token field.
* `include_options` decides whether put any options (including the ones above) into the message or not. It can be used to send special requests to servers accepting Coap formed requests without options, e.g. to a Dish Telemetry server. By default the options are included.

## Class resource

The resource class represents a resource in the scope of the Coap Module when acting as a server. A new resource can be only created with the `Coap.add_resource` function.

#### Class methods

The following methods are defined in the scope of the `resource` class.

#### resource.add_attribute(name, value)

Adds a new attribute to the resource. Attributes are used to explain the resource during service discovery.

* `name` is the name of the resource.
* `value` is the value of the resource.

{{% hint style="info" %}}
During service discovery, GET request to ".well-know/core", the attributes are returned with the belonging values.
E.g. using the "libcoap's" command line coap-client to fetch the resource from our server:

coap-client -m get coap://<Coap-Server's address>/.well-known/core

< /resource2>,< /resource1>;ct=0;title=resource1

{{% /hint %}}

#### resource.value(value)

Updates or fetches the value of the resource.

* `value` is the value to update the current value with.
If the method is called without parameter the current value is returned.

#### resource.callback(operation, enable)
To enable or disable a specific operation (GET, PUT, POST, DELETE) on the resource.

* `operation` is the operation to enable/disable, can be ORED of the followings: `Coap.REQUEST_GET`, `Coap.REQUEST_PUT`, `Coap.REQUEST_POST`, `Coap.REQUEST_DELETE`
* `enable` is boolean parameter to enable/disable the operations specified by `operation`


{{% hint style="info" %}}
During a GET request, only the first occurance of an ETAG or Accept option is parsed and interpreted, the others of the same type are dropped (if any).
{{% /hint %}}

{{% hint style="info" %}}
During a PUT request, only the first occurance of an If-Match option is parsed and interpreted, the others of the same type are dropped (if any).
{{% /hint %}}

{{% hint style="danger" %}}
Due to limitations of the underlying ESP-IDF/libcoap library, new resources cannot be added via PUT or POST requests.
{{% /hint %}}

## Constants

* Define the media type: `Coap.MEDIATYPE_TEXT_PLAIN`, `Coap.MEDIATYPE_APP_LINK_FORMAT`, `Coap.MEDIATYPE_APP_XML`, `Coap.MEDIATYPE_APP_OCTET_STREAM`, `Coap.MEDIATYPE_APP_RDF_XML`, `Coap.MEDIATYPE_APP_EXI`, `Coap.MEDIATYPE_APP_JSON`, `Coap.MEDIATYPE_APP_CBOR`
* Define the operation: `Coap.REQUEST_GET`, `Coap.REQUEST_PUT`, `Coap.REQUEST_POST`, `Coap.REQUEST_DELETE`
