---
title: "HTTP/S Client"
aliases:
    - firmwareapi/pycom/network/https/client.html
    - firmwareapi/pycom/network/https/client.md
    - chapter/firmwareapi/pycom/network/https/client
---
This module implements a HTTP/S Client.

## Quick Usage Example

```python
from network import WLAN
from network import HTTP_Client

# The callback that handles the responses generated from the requests sent to a HTTP/S Server
def client_callback(status, headers, body):
    print("Status Code: {}".format(status))
    for key, value in headers.items(): 
        print(key, ":", value) 
    print("Body: {}".format(body))

# Connect to the network
wlan = WLAN(mode=WLAN.STA)
wlan.connect('your-ssid', auth=(WLAN.WPA2, 'your-key'))
while not wlan.isconnected():
    pass
print(wlan.ifconfig())

# Initialize HTTP Client
HTTP_Client.init("http://httpbin.org/get", callback=client_callback)
# Send request with GET method
HTTP_Client.send_request(method=HTTP_Client.GET)

# Set HTTPS url
HTTP_Client.url("https://httpbin.org/post")
# Send request with POST method and custom body
HTTP_Client.send_request(method=HTTP_Client.POST, body='post data')

# Optionally deinit Client
HTTP_Client.deinit()
```

## Initialization

#### HTTP_Client.init(url, *, auth=None, callback=None)

Initialize the HTTP_Client module.

The arguments are:

* `url` is the address where the HTTP_Client module handles communication. Based on HTTP or HTTPS Client mode, `url` string must be started with 'http://' or 'https://'.
* `auth` is a tuple with (username, password). `Basic` authentication is supported in case of configured username and password.
* `callback` registers a callback function which will be called when a response received on the Client's request. `callback` must have the following arguments:
  * `status` is the status code issued by a Server in response to a Client's request (e.g. `200` OK or `404` Not Found).
  * `headers` is a dictionary contains all the response headers as key-value pairs. Size of `headers` depends on the number of headers received.
  * `body` is the message body or payload transmitted in response.

## Methods:

#### HTTP_Client.deinit()

Disables and deinitiates HTTP_Client module.

#### HTTP_Client.url(url)

Get or set the `url` for HTTP_Client. 
* Calling method without argument gets the currently set `url` as string. 
* `url` is the address where the HTTP_Client module handles communication. Based on HTTP or HTTPS Client mode, `url` string must be started with 'http://' or 'https://.
This method (re)initiates HTTP_Client.

```python
# Get the url of Client
HTTP_Client.url()

# Set the url for Client
HTTP_Client.url("http://httpbin.org/get")
```

#### HTTP_Client.auth(auth)

Get or set the `auth` for HTTP_Client. 
* Calling method without argument gets the currently set `auth` as tuple. 
* `auth` is a tuple with (username, password). `Basic` authentication is supported in case of configured username and password. Setting empty strings ("") for username and password disables `Basic` authentication.

```python
# Get the auth of Client
HTTP_Client.auth()

# Set the auth for Client
HTTP_Client.auth("user", "pass")

# Disable the auth for Client
HTTP_Client.auth("", "")
```

#### HTTP_Client.callback(callback, *, action=True)

Registeror unregister method for HTTP_Client's response handler.
* `callback` registers/unregisters (based on `action` flag) a callback function which will be called when a response received on the Client's request. `callback` must have the following arguments:
  * `status` is the status code issued by a Server in response to a Client's request (e.g. `200` OK or `404` Not Found).
  * `headers` is a dictionary contains all the response headers as key-value pairs. Size of `headers` depends on the number of headers received.
  * `body` is the message body or payload transmitted in response.
* `action` is a flag which decides if the given `callback` is registered (`action`=True) or unregistered(`action`=False).

```python
# The callback that handles the responses generated from the requests sent to a HTTP/S Server
def client_callback(status, headers, body):
    # Define callback method
    pass

# Register callback for Client
HTTP_Client.callback(client_callback)

# Unregister callback for Client
HTTP_Client.callback(client_callback, action=False)
```

#### HTTP\_Client.send\_request(method=HTTP_Client.GET, body=None, content_type=HTTP_Client.TEXT, accept=None, user_agent='ESP32 HTTP Client/1.0')

* `method` is the method to be sent to the server, can be: `HTTP_Client.GET`, `HTTP_Client.POST`, `HTTP_Client.PUT` or `HTTP_Client.DELETE`.
* `body` is the message body (or content) of the request in string format.
* `content_type` is the Content-Type header of the request, can be: `HTTP_Client.TEXT`, `HTTP_Client.XML`, `HTTP_Client.PLAIN`, `HTTP_Client.JSON`, `HTTP_Client.OCTET` or `HTTP_Client.APP_XML`.
* `accept` is the Accept header of the request in string format.
* `user_agent` is the User-Agent header of the request in string format, which lets server identify the client. The default value is: \'ESP32 HTTP Client/1.0\'.

## Constants
* HTTP_Client methods: `HTTP_Client.GET`, `HTTP_Client.POST`, `HTTP_Client.PUT`, `HTTP_Client.DELETE`
* HTTP_Client media types:

  `HTTP_Client.TEXT`: HyperText Markup Language (HTML): "text/html"

  `HTTP_Client.XML`: XML format: "text/xml"

  `HTTP_Client.PLAIN`: Text format: "text/plain"

  `HTTP_Client.JSON`: Json format: "application/json"

  `HTTP_Client.OCTET`: Binary data: "application/octet-stream"

  `HTTP_Client.APP_XML`: Json format: "application/xml
