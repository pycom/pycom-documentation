# HTTPS

Basic connection using `ssl.wrap_socket()`.

```python
import socket
import ssl

s = socket.socket()
ss = ssl.wrap_socket(s)
ss.connect(socket.getaddrinfo('www.google.com', 443)[0][-1])
```

Below is an example using certificates with the blynk cloud.

Certificate was downloaded from the blynk examples [folder](https://github.com/wipy/wipy/tree/master/examples/blynk) and placed in `/flash/cert/` on the device.

```python
import socket
import ssl

s = socket.socket()
ss = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='/flash/cert/ca.pem')
ss.connect(socket.getaddrinfo('cloud.blynk.cc', 8441)[0][-1])
```

For more info, check the [`ssl`](../../firmwareapi/micropython/ussl.md) module in the API reference.

