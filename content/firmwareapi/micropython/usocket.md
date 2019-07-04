---
title: "usocket"
aliases:
    - firmwareapi/micropython/usocket.html
    - firmwareapi/micropython/usocket.md
    - chapter/firmwareapi/micropython/usocket
---

This module provides access to the BSD socket interface.

See corresponding CPython module for comparison.

## Socket Address Format(s)

Functions below which expect a network address, accept it in the format of `(ipv4_address, port)`, where `ipv4_address` is a string with dot-notation numeric IPv4 address, e.g. `8.8.8.8`, and port is integer port number in the range 1-65535. Note the domain names are not accepted as `ipv4_address`, they should be resolved first using `socket.getaddrinfo()`.

## Methods

#### socket.socket(socket.AF\_INET, socket.SOCK\_STREAM, socket.IPPROTO\_TCP)

Create a new socket using the given address family, socket type and protocol number.

#### socket.getaddrinfo(host, port)

Translate the host/port argument into a sequence of 5-tuples that contain all the necessary arguments for creating a socket connected to that service. The list of 5-tuples has following structure:

`(family, type, proto, canonname, sockaddr)` The following example shows how to connect to a given url:

```python

s = socket.socket()
s.connect(socket.getaddrinfo('www.micropython.org', 80)[0][-1])
```

## Exceptions

`socket.error`, `socket.timeout`

## Constants

* Family types: `socket.AF_INET`, `socket.AF_LORA`, `socket.AF_SIGFOX`
* Socket types: `socket.SOCK_STREAM`, `socket.SOCK_DGRAM`, `socket.SOCK_RAW`
* Socket protocols: `socket.IPPROTO_UDP`, `socket.IPPROTO_TCP`
* Socket options layers: `socket.SOL_SOCKET`, `socket.SOL_LORA`, `socket.SOL_SIGFOX`
* IP socket options: `socket.SO_REUSEADDR`
* LoRa socket options: `socket.SO_CONFIRMED`, `socket.SO_DR`
* Sigfox socket options: `socket.SO_RX`, `socket.SO_TX_REPEAT`, `socket.SO_OOB`, `socket.SO_BIT`

## class Socket

### Methods

#### socket.close()

Mark the socket closed. Once that happens, all future operations on the socket object will fail. The remote end will receive no more data (after queued data is flushed).

Sockets are automatically closed when they are garbage-collected, but it is recommended to `close()` them explicitly, or to use a with statement around them.

#### socket.bind(address)

Bind the `socket` to `address`. The socket must not already be bound. The `address` parameter must be a tuple containing the IP address and the port.

{{% hint style="info" %}}
In the case of LoRa sockets, the address parameter is simply an integer with the port number, for instance: `s.bind(1)`
{{< /hint >}}

#### socket.listen(\[backlog\])

Enable a server to accept connections. If backlog is specified, it must be at least 0 (if it's lower, it will be set to 0); and specifies the number of unaccepted connections that the system will allow before refusing new connections. If not specified, a default reasonable value is chosen.

#### socket.accept()

Accept a connection. The socket must be bound to an address and listening for connections. The return value is a pair `(conn, address)` where `conn` is a new socket object usable to send and receive data on the connection, and `address` is the address bound to the socket on the other end of the connection.

#### socket.connect(address)

Connect to a remote socket at `address`.

#### socket.send(bytes)

Send data to the socket. The socket must be connected to a remote socket.

#### socket.sendall(bytes)

Alias of `socket.send(bytes)`.

#### socket.recv(bufsize)

Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by `bufsize`.

#### socket.sendto(bytes, address)

Send data to the socket. The socket should not be connected to a remote socket, since the destination socket is specified by address.

#### socket.recvfrom(bufsize)

Receive data from the socket. The return value is a pair `(bytes, address)` where `bytes` is a bytes object representing the data received and `address` is the address of the socket sending the data.

#### socket.setsockopt(level, optname, value)

Set the value of the given socket option. The needed symbolic constants are defined in the socket module (`SO_*` etc.). The value can be an integer or a bytes-like object representing a buffer.

#### socket.settimeout(value)

Set a timeout on blocking socket operations. The value argument can be a nonnegative floating point number expressing seconds, or `None`. If a non-zero value is given, subsequent socket operations will raise a timeout exception if the timeout period value has elapsed before the operation has completed. If zero is given, the socket is put in non-blocking mode. If None is given, the socket is put in blocking mode.

#### socket.setblocking(flag)

Set blocking or non-blocking mode of the socket: if flag is false, the socket is set to non-blocking, else to blocking mode.

This method is a shorthand for certain `settimeout()` calls:

```python

sock.setblocking(True) is equivalent to sock.settimeout(None)
sock.setblocking(False) is equivalent to sock.settimeout(0.0)
```

#### socket.makefile(mode='rb')

Return a file object associated with the socket. The exact returned type depends on the arguments given to makefile(). The support is limited to binary modes only (`rb` and `wb`). CPython's arguments: `encoding`, `errors`, and `newline` are not supported.

The socket must be in blocking mode; it can have a timeout, but the file object's internal buffer may end up in a inconsistent state if a timeout occurs.

{{% hint style="info" %}}
**Difference to CPython**

Closing the file object returned by `makefile()` **WILL** close the original socket as well.
{{< /hint >}}

#### socket.read(size)

Read up to size bytes from the socket. Return a bytes object. If `size` is not given, it behaves just like [`socket.readall()`](../usocket.md#socket-readall), see below.

#### socket.readall()

Read all data available from the socket until EOF. This function will not return until the socket is closed.

#### socket.readinto(buf\[, nbytes\])

Read bytes into the `buf`. If `nbytes` is specified then read at most that many bytes. Otherwise, read at most `len(buf)` bytes.

Return value: number of bytes read and stored into `buf`.

#### socket.readline()

Read a line, ending in a newline character.

Return value: the line read.

#### socket.write(buf)

Write the buffer of bytes to the socket.

Return value: number of bytes written.

#### socket.do_handshake()

Perform the SSL handshake on the previously "wrapped" socket with ssl.wrap_socket().
could be used when the socket is non-blocking and the SSL handshake is not performed during connect().

Example:

```
from network import WLAN
import time
import socket
import ssl
import uselect as select

wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid='<AP_SSID>', auth=(WLAN.WPA2, '<PASS>'))
while not wlan.isconnected():
    time.sleep(1)
    print("Wifi .. Connecting")

print ("Wifi Connected")

a = socket.getaddrinfo('www.postman-echo.com', 443)[0][-1]
s= socket.socket()
s.setblocking(False)
s = ssl.wrap_socket(s)
try:
    s.connect(a)
except OSError as e:
    if str(e) == '119': # For non-Blocking sockets 119 is EINPROGRESS
        print("In Progress")
    else:
        raise e
poller = select.poll()
poller.register(s, select.POLLOUT | select.POLLIN)
while True:
    res = poller.poll(1000)
    if res:
        if res[0][1] & select.POLLOUT:
            print("Doing Handshake")
            s.do_handshake()
            print("Handshake Done")
            s.send(b"GET / HTTP/1.0\r\n\r\n")
            poller.modify(s,select.POLLIN)
            continue
        if res[0][1] & select.POLLIN:
            print(s.recv(4092))
            break
    break
```

#### socket.dnsserver(*, dnsIndex, ip_addr)

When no arguments are passed this function returns the configured DNS servers Primary (Index=0) and backup (Index = 1)
to set primary and Backup DNS servers specify the Index and Ip Address.

Example:

```
>>> socket.dnsserver()
('10.0.0.1', '8.8.8.8')
```
Setting DNS servers:

```
>>> socket.dnsserver(1, '0.0.0.0')
>>> socket.dnsserver()
('10.0.0.1', '0.0.0.0')
```
