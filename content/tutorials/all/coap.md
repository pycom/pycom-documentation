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
import _thread

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

# Thread handling the CoAp Server
def coap_thread():
    while True:
        # Call Coap.read() without specyfing timeout value, in this way it handles all requests sent to the CoAp Server silently
        Coap.read()

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

# Start a new thread which handles the CoAp Server
_thread.start_new_thread(coap_thread, ())

```

### Example of CoAp Client in blocking mode
This example implements a CoAp Client session in blocking mode which means the relevant thread ("coap_thread") handling the Coap related activities will only be awake if there is an incoming CoAp message to process.
Blocking fashion has its advantage that the thread "coap_thread" is only executed when there is Coap message to process. In this case it may happen the new Client Sessions created after the "coap_thread" is started will not be handled.


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
session = Coap.new_client_session(COAP_SERVER_ADDRESS, COAP_SERVER_PORT)

# Start a new thread which calls Coap.read() which will block until no new packet arrives to the socket
_thread.start_new_thread(coap_thread, ())

# After this point it is not safe to create new Coap Client Session as they might not be handled by Coap.read()

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

### Example of CoAp Client in non-blocking mode
This example implements a CoAp Client session in non-blocking mode which means the relevant thread ("coap_thread") handling the Coap related activities will awake from time to time and not just when there is an incoming CoAp message to process.
Non-blocking fashion has its advantage that new Client Sessions created after the thread "coap_thread" is fired will still be processed.

```python
from network import WLAN
from network import Coap
import _thread

# Address of the CoAp Server 1 which this Client Session wants to connect 
COAP_SERVER_ADDRESS_1 = "192.168.0.101"
# Address of the CoAp Server 2 which this Client Session wants to connect 
COAP_SERVER_ADDRESS_2 = "192.168.0.102"
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

# Create a new client session to connect to CoAp Server 1
session1 = Coap.new_client_session(COAP_SERVER_ADDRESS_1, COAP_SERVER_PORT)

# Send a GET Request to the CoAp Server 1 asking for all resources via URI ".well-known/core"
id = session1.send_request(Coap.REQUEST_GET, uri_path=".well-known/core", token="session1")
print(id)
# Send a GET Request to the CoAp Server asking for resource with URI "time"
id = session1.send_request(Coap.REQUEST_GET, uri_path="time", token="session1")
print(id)

# Create a new client session to connect to CoAp Server 2
session2 = Coap.new_client_session(COAP_SERVER_ADDRESS_2, COAP_SERVER_PORT)

# Send a GET Request to the CoAp Server 2 asking for all resources via URI ".well-known/core"
id = session2.send_request(Coap.REQUEST_GET, uri_path=".well-known/core")
print(id)
# Send a GET Request to the CoAp Server 2 asking for resource with URI "resource1"
id = session2.send_request(Coap.REQUEST_GET, uri_path="resource1")
print(id)
# Send a PUT request to the CoAp Server 2 updating the resource with URI "resource1" to new value "new_value"
id = session2.send_request(Coap.REQUEST_POST, uri_path="resource1", payload="new_value")
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