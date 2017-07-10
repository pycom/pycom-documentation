# ussl – ssl module
This module provides access to Transport Layer Security (often known as “Secure Sockets Layer”) encryption and peer authentication facilities for network sockets, both client-side and server-side.

### Functions
<function>ssl.wrap_socket(sock, keyfile=None, certfile=None, server_side=False, cert_reqs=CERT_NONE, ca_certs=None)</function>

Takes an instance sock of socket.socket, and returns an instance of <constant>ssl.SSLSocket</constant>, a subtype of socket.socket, which wraps the underlying socket in an SSL context. Example:

```python
import socket
import ssl
s = socket.socket()
ss = ssl.wrap_socket(s)
ss.connect(socket.getaddrinfo('www.google.com', 443)[0][-1])
```

Certificates must be used in order to validate the other side of the connection, and also to authenticate ourselves with the other end. Such certificates must be stored as files using the FTP server, and they must be placed in specific paths with specific names.

For instance to connect to the Blynk servers using certificates, take the file ``ca.pem`` located in the blynk examples folder and put it in ``/flash/cert/``. Then do:

```python
import socket
import ssl
s = socket.socket()
ss = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='/flash/cert/ca.pem')
ss.connect(socket.getaddrinfo('cloud.blynk.cc', 8441)[0][-1])
```

SSL sockets inherit all methods and from the standard sockets, see the ``usocket`` module.

### Exceptions

<constant>ssl.SSLError</constant>

### Constants

<constant>ssl.CERT_NONE</constant> <constant>ssl.CERT_OPTIONAL</constant> <constant>ssl.CERT_REQUIRED</constant>

supported values in cert_reqs
