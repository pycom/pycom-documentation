# class Server
The Server class controls the behaviour and the configuration of the FTP and telnet services running on the Pycom Device. Any changes performed using this class’ methods will affect both.

Example:

```python
import network
server = network.Server()
server.deinit() # disable the server
# enable the server again with new settings
server.init(login=('user', 'password'), timeout=600)
```

### Quick Usage Example

```python
from network import Server

# init with new user, password and seconds timeout
server = Server(login=('user', 'password'), timeout=60)
server.timeout(300) # change the timeout
server.timeout() # get the timeout
server.isrunning() # check whether the server is running or not
```

### Constructors

<class><i>class</i> network.Server(id, ...)</class>

Create a server instance, see ``init`` for parameters of initialisation.

### Methods
<function>server.init(* , login=('micro', 'python'), timeout=300)</function>

Init (and effectively start the server). Optionally a new ``user``, ``password`` and ``timeout`` (in seconds) can be passed.

<function>server.deinit()</function>

Stop the server.

<function>server.timeout([timeout_in_seconds])</function>

Get or set the server timeout.

<function>server.isrunning()</function>

Returns ``True`` if the server is running (connected or accepting connections), ``False`` otherwise.
