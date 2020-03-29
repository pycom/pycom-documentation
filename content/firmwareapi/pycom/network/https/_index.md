---
title: "HTTP/S"
aliases:
    - chapter/firmwareapi/pycom/network/https
---

This module implements an HTTP and HTTPS Server and Client, operating as both at the same time.

## Quick Usage Example
Below is an example demonstrating the usage of `HTTP_Server` and `HTTP_Client` at the same time:

```python
from network import WLAN
from network import HTTP_Server
from network import HTTP_Client

# The callback that handles the responses generated from the requests sent to a HTTP/S Server
def server_callback(uri, method, headers, body, new_uri, status):
    print("Request URI: {}".format(uri))
    print("Request Method: {}".format(method))
    for key, value in headers.items(): 
        print("Request headers:", (key, value)) 
    print("Request Body: {}".format(body))
    print("Request New URI: {}".format(new_uri))
    print("Request Status: {}".format(status))

# The callback that handles the responses generated from the requests sent to a HTTP/S Server
def client_callback(status, headers, body):
    print("Response Status: {}".format(status))
    for key, value in headers.items(): 
        print("Response headers:", (key, value))
    print("Response Body: {}".format(body))

# Connect to the network
wlan = WLAN(mode=WLAN.STA)
wlan.connect('your-ssid', auth=(WLAN.WPA2, 'your-key'))
while not wlan.isconnected():
    pass
print(wlan.ifconfig())

# Initilise an HTTP Server
HTTP_Server.init()

# Add new resource to Server
res = HTTP_Server.add_resource('/resource', value = "Hello Client!")
# Register resource request handler
res.register_request_handler(HTTP_Server.GET, callback=server_callback)

# Initialize an HTTP Client
HTTP_Client.init('http://' + str(wlan.ifconfig()[0] + '/resource'), callback=client_callback)
# Send request with body
HTTP_Client.send_request(body='Hello Server!')
```
To implement HTTPS Server and Client, only the two init methods need to be changed:

```python
# HTTP Server init
HTTP_Server.init()

# HTTP Client init
HTTP_Client.init('http://' + str(wlan.ifconfig()[0] + '/resource'), callback=client_callback)
```

```python
# HTTPS Server init
HTTP_Server.init(port=443, keyfile='/flash/cert/prvtkey.pem', certfile='/flash/cert/cacert.pem')

# HTTPS Client init
HTTP_Client.init('https://' + str(wlan.ifconfig()[0] + '/resource'), callback=client_callback)
```
