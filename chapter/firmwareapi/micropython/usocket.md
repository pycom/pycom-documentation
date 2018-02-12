# usocket – Socket Module
This module provides access to the BSD socket interface.

See corresponding CPython module for comparison.

### Socket Address Format(s)
Functions below which expect a network address, accept it in the format of (ipv4_address, port), where ipv4_address is a string with dot-notation numeric IPv4 address, e.g. "8.8.8.8", and port is integer port number in the range 1-65535. Note the domain names are not accepted as ipv4_address, they should be resolved first using socket.getaddrinfo().

### Functions

#####<function>socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)</function>

Create a new socket using the given address family, socket type and protocol number.

#####<function>socket.getaddrinfo(host, port)</function>

Translate the host/port argument into a sequence of 5-tuples that contain all the necessary arguments for creating a socket connected to that service. The list of 5-tuples has following structure:

(family, type, proto, canonname, sockaddr)
The following example shows how to connect to a given url:

```python
s = socket.socket()
s.connect(socket.getaddrinfo('www.micropython.org', 80)[0][-1])
```

### Exceptions

<constant>socket.error</constant> <constant>socket.timeout</constant>

### Constants

<constant>socket.AF_INET</constant> <constant>socket.AF_LORA</constant>

family types

<constant>socket.SOCK_STREAM</constant> <constant>socket.SOCK_DGRAM</constant> <constant>socket.SOCK_RAW</constant>

socket types

<constant>socket.IPPROTO_UDP</constant> <constant>socket.IPPROTO_TCP</constant>

socket protocols

<constant>socket.SOL_SOCKET</constant> <constant>socket.SOL_LORA</constant> <constant>socket.SOL_SIGFOX</constant>

socket options layers

<constant>socket.SO_REUSEADDR</constant>

IP socket options

<constant>socket.SO_CONFIRMED</constant> <constant>socket.SO_DR</constant>

LoRa socket options

<constant>socket.SO_RX</constant> <constant>socket.SO_TX_REPEAT</constant> <constant>socket.SO_OOB</constant> <constant>socket.SO_BIT</constant>

Sigfox socket options

### class Socket
### Methods

#####<function>socket.close()</function>

Mark the socket closed. Once that happens, all future operations on the socket object will fail. The remote end will receive no more data (after queued data is flushed).

Sockets are automatically closed when they are garbage-collected, but it is recommended to close() them explicitly, or to use a with statement around them.

#####<function>socket.bind(address)</function>

Bind the socket to address. The socket must not already be bound. The address parameter must be a tuple containing the IP address and the port.

{% hint style='info' %}
In the case of LoRa sockets, the address parameter is simply an integer with the port number, for instance: ``s.bind(1)``
{% endhint %}

#####<function>socket.listen([backlog])</function>

Enable a server to accept connections. If backlog is specified, it must be at least 0 (if it’s lower, it will be set to 0); and specifies the number of unaccepted connections that the system will allow before refusing new connections. If not specified, a default reasonable value is chosen.

#####<function>socket.accept()</function>

Accept a connection. The socket must be bound to an address and listening for connections. The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.

#####<function>socket.connect(address)</function>

Connect to a remote socket at address.

socket.send(bytes)
Send data to the socket. The socket must be connected to a remote socket.

#####<function>socket.sendall(bytes)</function>

Alias of socket.send(bytes).

#####<function>socket.recv(bufsize)</function>

Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by bufsize.

#####<function>socket.sendto(bytes, address)</function>

Send data to the socket. The socket should not be connected to a remote socket, since the destination socket is specified by address.

#####<function>socket.recvfrom(bufsize)</function>

Receive data from the socket. The return value is a pair (bytes, address) where bytes is a bytes object representing the data received and address is the address of the socket sending the data.

#####<function>socket.setsockopt(level, optname, value)</function>

Set the value of the given socket option. The needed symbolic constants are defined in the socket module (SO_* etc.). The value can be an integer or a bytes-like object representing a buffer.

#####<function>socket.settimeout(value)</function>

Set a timeout on blocking socket operations. The value argument can be a nonnegative floating point number expressing seconds, or None. If a non-zero value is given, subsequent socket operations will raise a timeout exception if the timeout period value has elapsed before the operation has completed. If zero is given, the socket is put in non-blocking mode. If None is given, the socket is put in blocking mode.

#####<function>socket.setblocking(flag)</function>

Set blocking or non-blocking mode of the socket: if flag is false, the socket is set to non-blocking, else to blocking mode.

This method is a shorthand for certain ``settimeout()`` calls:

```python
sock.setblocking(True) is equivalent to sock.settimeout(None)
sock.setblocking(False) is equivalent to sock.settimeout(0.0)
```

#####<function>socket.makefile(mode='rb')</function>

Return a file object associated with the socket. The exact returned type depends on the arguments given to makefile(). The support is limited to binary modes only (‘rb’ and ‘wb’). CPython’s arguments: ``encoding``, ``errors`` and ``newline`` are not supported.

The socket must be in blocking mode; it can have a timeout, but the file object’s internal buffer may end up in a inconsistent state if a timeout occurs.

{% hint style='info' %}
Difference to CPython

Closing the file object returned by makefile() WILL close the original socket as well.
{% endhint %}

#####<function>socket.read(size)</function>

Read up to size bytes from the socket. Return a bytes object. If ``size`` is not given, it behaves just like <function>socket.readall()</function>, see below.

#####<function>socket.readall()</function>

Read all data available from the socket until EOF. This function will not return until the socket is closed.

#####<function>socket.readinto(buf[, nbytes])</function>

Read bytes into the ``buf``. If ``nbytes`` is specified then read at most that many bytes. Otherwise, read at most ``len(buf)`` bytes.

Return value: number of bytes read and stored into ``buf``.

#####<function>socket.readline()</function>

Read a line, ending in a newline character.

Return value: the line read.

#####<function>socket.write(buf)</function>

Write the buffer of bytes to the socket.

Return value: number of bytes written.
