# Socket

Detailed information about this class can be found in [usocket](../../firmware-and-api-reference/micropython/usocket.md).

## Setting up a server with blocking sockets

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

