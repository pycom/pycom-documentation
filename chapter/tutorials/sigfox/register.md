# Registering with Sigfox
To ensure the device has been provisioned with **Device ID** and **PAC number**, please update to the latest firmware.

In order to send a Sigfox message, the device need to register with the Sigfox Backend. Navigate to https://backend.sigfox.com/activate to find the list of Sigfox enabled development kits.

<p align="center"><img src ="../../../img/sigfox-backend-1.png" width="400"></p>

Select **`Pycom`** to proceed.

Next choose a Sigfox Operator for the country where the device will be activated. Find the specific country and select the operator to continue.

<p align="center"><img src ="../../../img/sigfox-backend-2.png" width="400"></p>

Now need to enter the device's **Device ID** and **PAC number**.

<p align="center"><img src ="../../../img/sigfox-backend-3.png" width="400"></p>

The **Device ID** and **PAC number** are retrievable through a couple of commands via the REPL.

```python
from network import Sigfox
import ubinascii

# initalise Sigfox for RCZ1 (You may need a different RCZ Region)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# print Sigfox Device ID
print(ubinascii.hexlify(sigfox.id()))

# print Sigfox PAC number
print(ubinascii.hexlify(sigfox.pac()))
```

See `Sigfox` for more info about the Sigfox Class and which `RCZ` region to use.

Once the device's Device ID and PAC number have been entered, create an account. Provide the required information including email address and click to continue.

<p align="center"><img src ="../../../img/sigfox-backend-4.png" width="400"></p>

An email confirming the creation of a Sigfox Backend account and the successful registration of the device should arrive at the users inbox.
