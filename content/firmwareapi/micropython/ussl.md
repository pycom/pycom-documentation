---
title: "ussl"
aliases:
    - firmwareapi/micropython/ussl.html
    - firmwareapi/micropython/ussl.md
    - chapter/firmwareapi/micropython/ussl
---

This module provides access to Transport Layer Security (often known as "Secure Sockets Layer") encryption and peer authentication facilities for network sockets, both client-side and server-side.

## Methods

#### ssl.wrap\_socket(sock, keyfile=None, certfile=None, server\_side=False, cert\_reqs=CERT\_NONE, ssl\_version=0, ca\_certs=None, server\_hostname=None, saved_session=None, timeout=10sec)

Takes an instance `sock` of `socket.socket`, and returns an instance of `ssl.SSLSocket`, a subtype of `socket.socket`, which wraps the underlying socket in an SSL context. Example:

```python

import socket
import ssl
s = socket.socket()
ss = ssl.wrap_socket(s)
ss.connect(socket.getaddrinfo('www.google.com', 443)[0][-1])
```

Certificates must be used in order to validate the other side of the connection, and also to authenticate ourselves with the other end. Such certificates must be stored as files using the FTP server, and they must be placed in specific paths with specific names.

For instance, to connect to the Blynk servers using certificates, take the file `ca.pem` located in the `blynk` examples folder and put it in `/flash/cert/`. Then do:

```python

import socket
import ssl
s = socket.socket()
ss = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='/flash/cert/ca.pem')
ss.connect(socket.getaddrinfo('cloud.blynk.cc', 8441)[0][-1])
```

SSL sockets inherit all methods and from the standard sockets, see the `usocket` module.

`saved_session` : Takes a saved session instance of `ssl.SSLSocket`, and retrieve an already established TLS connection.

`timeout` : specify a Timeout in Seconds for the SSL handshake operation between client and server, default is 10 seconds

#### ssl.save\_session(ssl_sock)

Takes an instance `ssl_sock` of `ssl.SSLSocket`, and returns an instance of `ssl.SSLSession`. Saved session can be resumed later, thereby reducing mobile data and time required. Example:

```python

import socket
import ssl
s = socket.socket()
ss = ssl.wrap_socket(s)
ss.connect(socket.getaddrinfo('www.google.com', 443)[0][-1])
ses = ssl.save_session(ss)
ss.close()
ss = ssl.wrap_socket(s, saved_session=ses)
ss.connect(socket.getaddrinfo('www.google.com', 443)[0][-1])
```

## Exceptions

* `ssl.SSLError`

## Constants

* `ssl.CERT_NONE`, `ssl.CERT_OPTIONAL`, `ssl.CERT_REQUIRED`: Supported values in `cert_reqs`
