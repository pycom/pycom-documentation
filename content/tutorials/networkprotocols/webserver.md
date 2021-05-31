---
title: "HTTP Webserver Example"
aliases:
    - tutorials/networks/webserver.html
    - tutorials/networks/webserver.md
    - chapter/tutorials/networks/webserver
---

Using the WiFi connection, we can create a HTTP simple webserver on the module with the socket library.

```python
import usocket
import _thread
import time
from network import WLAN
import pycom

availablecolor = 0x001100
connectioncolor = 0x110000

# Thread for handling a client
def client_thread(clientsocket,n):
    # Receive maxium of 12 bytes from the client
    r = clientsocket.recv(4096)

    # If recv() returns with 0 the other end closed the connection
    if len(r) == 0:
        clientsocket.close()
        return
    else:
        # Do something wth the received data...
        print("Received: {}".format(str(r))) #uncomment this line to view the HTTP request

    http = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection:close \r\n\r\n" #HTTP response
    
    if "GET / " in str(r):
        #this is a get response for the page   
        # Sends back some data
        clientsocket.send(http + "<html><body><h1> You are connection "+ str(n) + "</h1><br> Your browser will send multiple requests <br> <a href='/hello'> hello!</a><br><a href='/color'>change led color!</a></body></html>")
    elif "GET /hello "in str(r):
        
        clientsocket.send(http + "<html><body><h1> Hello to you too! </h1><br> <a href='/'> go back </a></body></html>")
    elif "GET /color" in str(r):
        pycom.rgbled(0xFFFFFF)
        clientsocket.send(http + "<html><body><h1> You are connection "+ str(n) + "</h1><br> Your browser will send multiple requests <br> <a href='/hello'> hello!</a><br><a href='/color'>change led color!</a></body></html>")

    # Close the socket and terminate the thread

    clientsocket.close()
    pycom.rgbled(connectioncolor)
    time.sleep_ms(500)
    pycom.rgbled(availablecolor)  

time.sleep(1)
wifi = WLAN()
wifi.init(mode=WLAN.AP, ssid="hello", auth=None, channel=1)
print("WiFi is up!")
time.sleep(1)
pycom.heartbeat(False)
pycom.rgbled(availablecolor)

# Set up server socket
serversocket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
serversocket.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
serversocket.bind(("192.168.4.1", 80))

# Accept maximum of 5 connections at the same time
serversocket.listen(5)

# Unique data to send back
c = 1
while True:
    # Accept the connection of the clients
    (clientsocket, address) = serversocket.accept()
    # Start a new thread to handle the client
    _thread.start_new_thread(client_thread, (clientsocket, c))
    c = c+1
serversocket.close()
```





