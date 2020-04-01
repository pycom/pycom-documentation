---
title: "HTTP/S Server"
aliases:
    - firmwareapi/pycom/network/https/server.html
    - firmwareapi/pycom/network/https/server.md
    - chapter/firmwareapi/pycom/network/https/server
---

This module implements HTTP/S Server.

## Quick Usage Example

```python
from network import WLAN
from network import HTTP_Server

# The callback that handles the responses generated from the requests sent to a HTTP/S Server
def server_callback(uri, method, headers, body, new_uri, status):
    print("Request URI: {}".format(uri))
    print("Request Method: {}".format(method))
    for key, value in headers.items(): 
        print("Request headers:", (key, value)) 
    print("Request Body: {}".format(body))
    print("Request New URI: {}".format(new_uri))
    print("Request Status: {}".format(status))

# Connect to the network
wlan = WLAN(mode=WLAN.STA)
wlan.connect('your-ssid', auth=(WLAN.WPA2, 'your-key'))
while not wlan.isconnected():
    pass
print(wlan.ifconfig())

# Initilise an HTTP Server
HTTP_Server.init()

# Add resources to Server
res1 = HTTP_Server.add_resource('/resource1', value = "Hello Client!")
res2 = HTTP_Server.add_resource('/resource2')

# Register resource request handlers
res1.register_request_handler(HTTP_Server.GET)
res2.register_request_handler(HTTP_Server.GET | HTTP_Server.POST | HTTP_Server.PUT | HTTP_Server.DELETE, callback=server_callback)

```

## Initialization

#### HTTP_Server.init(port=80, max_uri=100, keyfile=None, certfile=None)

Initialize the HTTP_Server module.
The arguments are:
* `port` is the port where the HTTP_Server module listens. If not set, the default port is 80. HTTPS (HTTP Secure or HTTP over TLS/SSL) mode is activated in case of 443 port setting. In this case, `keyfile` and `certfile` must be placed into `/flash/cert/` folder on the device.
* `max_uri` is the maximum allowed resources on the Server.
* `keyfile` is the Private Key path for SSL Certificate.
* `certfile` is the Certification File path for SSL Certificate.

For example you can create an HTTP Server:
```python
# Init HTTP Server
HTTP_Server.init()
```
or an HTTPS:
```python
# Init HTTPS Server
HTTP_Server.init(port=443, keyfile='/flash/cert/prvtkey.pem', certfile='/flash/cert/cacert.pem')
```
_Note: Self-signed Certificate can be gemerated by using OpenSSL command line tool:_
```
openssl req -newkey rsa:2048 -nodes -keyout prvtkey.pem -x509 -days 365 -out cacert.pem -subj "/CN=Pycom HTTPS Server"
```

## Methods:

#### HTTP_Server.deinit()

Disables and deinitiates HTTP_Server module.

#### HTTP_Server.add_resource(uri, *, content_type=HTTP_Server.TEXT, value=0)

Creates a `HTTP_Resource` object, which can be defined with its `uri`, and can be registered with different request handlers.

* `uri` is the unique identifier path to the resource, `uri` string must be started with '/'.
* `content_type` is the representation type of the resource.
* `value` is the default value of the resource. If not given, it is initialised to decimal 0.

#### HTTP_Server.get_resource(uri, *)

Returns with the `HTTP_Resource` object defined by `uri` argument.

* `uri` is the full path of the resource to be returned.

#### HTTP_Server.list_resource(uri_start=None)

Returns with the list of uri starts with `uri_start` strings, registered on the Server.

* `uri_start` is start string of uri to be returned. If not set, all the existing resources are returned.

#### HTTP_Server.remove_resource(uri, *)

Removes the `HTTP_Resource` defined by the `uri` argument, and unregister its handler.

* `uri` is the full path of the resource to be removed.

## Class resource

The resource class represents a resource in the scope of the HTTP\_Server module. A new resource can be created with the `HTTP_Server.add_resource` function or with a POST Client request.

#### Class methods

The following methods are defined in the scope of the `HTTP_Resource` class.

#### resource.value(value)
Get or set the `value` for resource. 

* Calling method without argument gets the currently set `value` as string.
* `value` is the new value to update the current value with.

#### resource.register_request_handler(method, *, callback)

Registers the servers operation on the given resource.
* `method` is the indication of the desired action to be performed for a given resource. It can be `HTTP_Server.GET`, `HTTP_Server.POST`, `HTTP_Server.PUT`, `HTTP_Server.DELETE`, or any combination at the same time. Calling method again with different method, unregisters recent settings, and resets the new one(s).
* `callback` can be assigned to the resource, it contains information about Client's request:
   * `uri` is the full path of the resource to be requested.
   * `method` indicates the request method.
   * `headers` is a dictionary contains all the request headers as key-value pairs. Size of `headers` depends on the number of headers received.
   * `body` is the message body or payload transmitted in request.
   * `new_uri` is the full path of newly created `uri`. It is empty except in case of successful Post request.
   * `status` is the status code sent back by the Server in the response.

```python
# The callback that handles the requests of the Server
def server_callback(uri, method, headers, body, new_uri, status):
    # Define callback method
    pass

# Create a resource
res = HTTP_Server.add_resource('/res')

# Register a GET request handler for resource
res.register_request_handler(HTTP_Server.GET)

# Register GET and POST request handler for resource with a callback
res.register_request_handler(HTTP_Server.GET | HTTP_Server.POST, callback=server_callback)
```
---
_Note: Registering a request handler means that `HTTP_Server` automatically handles basic HTTP requests. Currently four methods are supported:_
* _GET: Server serves the requested resources value. Successful GET: `200 OK`._
* _PUT: Server updates the value of the requested resource (creating resource with PUT request is not supported). Successful PUT: `204 No Content`. `Content-Location` header in response contains the updated reource's URI._
* _POST: Server creates a new resource. New resource will be the subresource of the requested one, and a 5 digit ID is generated by the Server, and the value of the resource will be the payload of the request. Successful POST: `201 Created`. `Location` header in response contains the created reource's URI._ 
* _DELETE: Server deletes the requested resource. Successful DELETE: `204 No Content`._

_Currently handled status codes by Server: `200`, `201`, `204`, `404`, `405`, `406`, `408`, `413`, `415`, `500` and `507`_ 


---

## Constants
* HTTP_Server methods: `HTTP_Serveer.GET`, `HTTP_Server.POST`, `HTTP_Server.PUT`, `HTTP_Server.DELETE`
* HTTP_Server media types:

  `HTTP_Server.TEXT`: HyperText Markup Language (HTML): "text/html"

  `HTTP_Server.XML`: XML format: "text/xml"

  `HTTP_Server.PLAIN`: Text format: "text/plain"

  `HTTP_Server.JSON`: Json format: "application/json"

  `HTTP_Server.OCTET`: Binary data: "application/octet-stream"

  `HTTP_Server.APP_XML`: Json format: "application/xml
