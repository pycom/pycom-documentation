---
title: "Server"
aliases:
    - firmwareapi/pycom/network/server.html
    - firmwareapi/pycom/network/server.md
    - chapter/firmwareapi/pycom/network/server
---

The `Server` class controls the behaviour and the configuration of the FTP and telnet services running on the Pycom device. Any changes performed using this class' methods will affect both.

Example:

```python

import network
server = network.Server()
server.deinit() # disable the server
# enable the server again with new settings
server.init(login=('user', 'password'), timeout=600)
```

## Quick Usage Example

```python

from network import Server

# init with new user, password and seconds timeout
server = Server(login=('user', 'password'), timeout=60)
server.timeout(300) # change the timeout
server.timeout() # get the timeout
server.isrunning() # check whether the server is running or not
```

## Constructors

#### class network.Server(id, ...)

Create a server instance, see `init` for parameters of initialisation.

## Methods

#### server.init(\* , login=('micro', 'python'), timeout=300)

Init (and effectively start the server). Optionally a new `user`, `password` and `timeout` (in seconds) can be passed.

#### server.deinit()

Stop the server.

#### server.timeout(\[timeout\_in\_seconds\])

Get or set the server timeout.

#### server.isrunning()

Returns `True` if the server is running (connected or accepting connections), `False` otherwise.

