---
title: ""
aliases:
    - tutorials/all/coap.html
    - tutorials/all/coap.md
---

Detailed information about this class can be found in [coap](/firmwareapi/pycom/network/coap).

### Example of CoAp Server

The following example sets up a Coap Server.

```python

from network import WLAN
from network import Coap

# Callback to be called when a new resource has been added via PUT
def new_resource_callback(new_resource):
    details = new_resource.get_details()
    print("New resource has been created!")
    print("URI: {}".format(details[0]))
    print("Mediatype: {}".format(details[1]))
    print("Max Age: {}".format(details[2]))
    print("ETAG: {}".format(details[3]))
    print("ETAG value: {}".format(details[4]))
    print("Value: {}".format(new_resource.value()))
    # Configure the properties of the new resource
	# Mediatype, max_age and etag depends on the use-case, for this example set them randomly
    new_resource.set_details(mediatype=Coap.MEDIATYPE_TEXT_PLAIN, max_age=100, etag=True)

# Connect to the network
wlan = WLAN(mode=WLAN.STA)
wlan.connect('your-ssid', auth=(WLAN.WPA2, 'your-key'))

# Initialize Coap module as CoAp Server, enable service discovery and new resources to be added via PUT 
Coap.init(str(wlan.ifconfig()[0]), service_discovery=True, dynamic_resources=True)
# Register callback which will be called when new resource is added via PUT
Coap.register_new_resource_handler(new_resource_callback)

# Add an example resource with default value and plain text content format
r = Coap.add_resource("resource1", media_type=Coap.MEDIATYPE_TEXT_PLAIN, value="default_value")
# Add an attribute to the resource
r.add_attribute("title", "resource1")
# Add an attribute to the resource
r.add_attribute("ct", str(Coap.MEDIATYPE_TEXT_PLAIN))
# Configure the possible operations on the resource
r.callback(Coap.REQUEST_GET | Coap.REQUEST_POST | Coap.REQUEST_PUT, True)

# Add another example resource without default value, XML content format and E-Tag enabled
r = Coap.add_resource("resource2", media_type=Coap.MEDIATYPE_APP_XML, etag=True)
# Configure the possible operations on the resource
r.callback(Coap.REQUEST_GET | Coap.REQUEST_POST | Coap.REQUEST_PUT | Coap.REQUEST_DELETE, True)

```

### Example of CoAp Client
This example shows how to use the CoAp Client session.


```python
from network import WLAN
from network import Coap
import _thread

# Address of the CoAp Server which this Client Session wants to connect 
COAP_SERVER_ADDRESS = "192.168.0.234"
# Port of the CoAp Server which this Client Session wants to connect 
COAP_SERVER_PORT = 5683

# Callback handling the responses to the requests sent to a Coap Server
def response_callback(code, id_param, type_param, token, payload):
    print("Code: {}".format(code))
    # The ID can be used to pair the requests with the responses
    print("ID: {}".format(id_param))
    print("Type: {}".format(type_param))
    print("Token: {}".format(token))
    print("Payload: {}".format(payload))

# Connect to the network
wlan = WLAN(mode=WLAN.STA)
wlan.connect('your-ssid', auth=(WLAN.WPA2, 'your-key'))

# Initialize Coap module
Coap.init(str(wlan.ifconfig()[0]), service_discovery=True)

# Register the response handler for the requests the module initiates as a Coap Client
Coap.register_response_handler(response_callback)

# Create a new Client Session
session = Coap.new_client_session(COAP_SERVER_ADDRESS, COAP_SERVER_PORT)

# Send a GET Request to the CoAp Server asking for all resources via URI ".well-known/core"
id = session.send_request(Coap.REQUEST_GET, uri_path=".well-known/core", payload="payload", token="token1", include_options=True)
# The id can be used to match the request with the response in the response_callback
print(id)
# Send a GET Request to the CoAp Server asking for resource with URI "time"
id = session.send_request(Coap.REQUEST_GET, uri_path="time", payload="payload", token="token2", include_options=True)
print(id)
# Send a PUT request to the CoAp Server updating the resource with URI "time" to new value "ABCD"
id = session.send_request(Coap.REQUEST_PUT, uri_path="time",content_format=Coap.MEDIATYPE_TEXT_PLAIN, payload="ABCD", token="token3", include_options=True)
print(id)

```
### Example snippet for sending message without options
This example snippet shows how to send messages to servers which accept CoAp messages without any options.
In this case the URI should be placed in the "payload".

```python

# Token can be 8 bytes maximum
TOKEN = 12345678
# Payload must include the full URI (Host, Port, Path etc.)
FULL_URI_PATH = "abcd://server:1234/mypath.data"
# Disable normal CoAp options via include_options=False
id = session.send_request(Coap.REQUEST_GET, payload=FULL_URI_PATH, token=TOKEN, include_options=False)

```