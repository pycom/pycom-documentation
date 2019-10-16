---
title: ""
aliases:
    - tutorials/all/Socket.html
    - tutorials/all/Socket.md
---

Detailed information about this class can be found in [usocket]().

### Setting up a server with blocking sockets

The following example sets up a server which can accept 5 connections in parallel, create a new thread for each connected client, receives and sends back data then close the socket.

```python

import usocket
import _thread
import time

# Thread for handling a client
def client_thread(clientsocket,n):
    # Receive maxium of 12 bytes from the client
    r = clientsocket.recv(12)

    # If recv() returns with 0 the other end closed the connection
    if len(r) == 0:
        clientsocket.close()
        return
    else:
        # Do something wth the received data...
        print("Received: {}".format(str(r)))

    # Sends back some data
    clientsocket.send(str(n))

    # Close the socket and terminate the thread
    clientsocket.close()

# Set up server socket
serversocket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
serversocket.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
serversocket.bind(("192.168.0.249", 6543))

# Accept maximum of 5 connections at the same time
serversocket.listen(5)

# Unique data to send back
c = 0
while True:
    # Accept the connection of the clients
    (clientsocket, address) = serversocket.accept()
    # Start a new thread to handle the client
    _thread.start_new_thread(client_thread, (clientsocket, c))
    c = c+1
```

### Using a client with non-blocking sockets

The following example sets up a client which can connect to a server with 2 non-blocking sockets, create a new thread to handle the non-blocking sockets.

```python

import socket
import _thread
import time
import uerrno
import uselect

def socket_thread(p):

    while True:
        # Wait for any action to happen infinitely
        l = p.poll()

        # Start processing the actions happened
        for t in l:
            # First element of the returned tuple is the socket itself
            sock = t[0]
            # Second element of the returned tuple is the events happened
            event = t[1]

            # If any error or connection drop happened close the socket
            if(event & uselect.POLLERR or event & uselect.POLLHUP):
                sock.close()
                continue

            # If the socket is writable then send some data
            # The socket becomes writable if the connect() was successfull
            if(event & uselect.POLLOUT):
                # If any error occurs during sending here, do "nothing", poll() will return with error event, close the socket there
                try:
                    sock.send("Data to send")
                    # We only want to send one message on this socket, in the future wait only for new incoming messages
                    p.modify(sock, uselect.POLLIN | uselect.POLLHUP | uselect.POLLERR)
                except:
                    pass


            # If any new data is received then get it
            if(event & uselect.POLLIN):
                # If any error occurs during receiving here, do "nothing", poll() will return with error event, close the socket there
                try:
                    r = sock.recv(1)
                    # If recv() returns with 0 the other end closed the connection
                    if len(r) == 0:
                        sock.close()
                        continue
                    else:
                        # Do something with the received data...
                        print("Data received: " + str(r))
                except:
                    pass


# List for storing our sockets
socket_list = []

# Set up the first socket in non-blocking mode
s1 = socket.socket()
s1.setblocking(False)
socket_list.append(s1)
# Set up the second socket in non-blocking mode
s2 = socket.socket()
s2.setblocking(False)
socket_list.append(s2)

# Create a new poll object
p = uselect.poll()
# Register the sockets into the poll object, wait for all kind of events
p.register(s1, uselect.POLLIN | uselect.POLLOUT | uselect.POLLHUP | uselect.POLLERR)
p.register(s2, uselect.POLLIN | uselect.POLLOUT | uselect.POLLHUP | uselect.POLLERR)

# Try to connect to the server with each sockets
for s in socket_list:
    try:
        s.connect(socket.getaddrinfo("192.168.0.234", 6543)[0][-1])
    except OSError as e:
        # In case of non-blocking socket the connect() raises eception of EINPROGRESS what is expected
        if e.args[0] != uerrno.EINPROGRESS:
            # Raise all other errors
            raise

# Start the thread which takes care of the non-blocking sockets through the created poll object
_thread.start_new_thread(socket_thread, (p,))
```

### Connecting to a server with non-blocking SSL wrapped socket

```python


import socket
import ssl
import _thread
import time
import uerrno
import uselect

# Helper function for doing the handshake
def handshake_helper(sock):

    while True:
        time.sleep_ms(1)
        try:
            # Perform the handshake
            sock.do_handshake()
            return
        except ssl.SSLError as e:
            # For now raise any other errors then TIMEOUT...
            if e.args[0] != ssl.SSL_TIMEOUT:
                raise

def socket_thread(p):

    while True:
        # Wait for any action to happen infinitely
        l = p.poll()

        # Start processing the actions happened
        for t in l:
            # First element of the returned tuple is the socket itself
            sock = t[0]
            # Second element of the returned tuple is the events happened
            event = t[1]

            # If any error or connection drop happened close the socket
            if(event & uselect.POLLERR or event & uselect.POLLHUP):
                p.unregister(sock)
                sock.close()

            # If any new data is received then get it
            elif(event & uselect.POLLIN):
                # If any error occurs during receiving here, do "nothing", poll() will return with error event, close the socket there
                try:
                    r = sock.recv(1)
                    # If recv() returns with 0 the other end closed the connection
                    if len(r) == 0:
                        p.unregister(sock)
                        sock.close()
                    else:
                        # Do something with the received data...
                        print("Data received: " + str(r))
                except:
                    pass

            # If the socket is writable then we may expect it is connected, do handshake and send some data
            elif(event & uselect.POLLOUT):

                try:
                    # Performing the SSL handshake
                    handshake_helper(sock)
                except:
                    # An error happened, close the socket, unregister it from poll
                    p.unregister(sock)
                    sock.close()

                # If any error occurs during sending here, do "nothing", poll() will return with error event, close the socket there
                try:
                    sock.send("Data to send")
                    # We only want to send one message on this socket, in the future wait only for new incoming messages
                    p.modify(sock, uselect.POLLIN | uselect.POLLHUP | uselect.POLLERR)
                except:
                    pass


# Create and wrap the socket
s = socket.socket()
ssl_socket = ssl.wrap_socket(s, keyfile="/flash/cert/my_private_key.pem",
                                certfile="/flash/cert/my_public_key.pem",
                                server_side=False,
                                cert_reqs=ssl.CERT_REQUIRED,
                                ca_certs="/flash/cert/my_CA_cert.pem"
                            )
# Set the wrapped socket to non-blocking
ssl_socket.setblocking(False)
# Create a new poll object
p = uselect.poll()
# Register the wrapped socket into the poll object, wait only for write and error events
p.register(ssl_socket, uselect.POLLOUT | uselect.POLLHUP | uselect.POLLERR)

 # Try to connect to the server
try:
    ssl_socket.connect(socket.getaddrinfo("192.168.0.234", 6543)[0][-1])
except OSError as e:
    # In case of non-blocking socket the connect() raises eception of EINPROGRESS what is expected
    if e.args[0] != uerrno.EINPROGRESS:
        # Raise all other errors
        raise

# Start the thread which takes care of the non-blocking socket through the created poll object
_thread.start_new_thread(socket_thread, (p))

```