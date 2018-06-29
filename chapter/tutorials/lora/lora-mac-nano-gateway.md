# LoRa Nano-Gateway (Raw LoRa)
This example allows a raw LoRa connection between two LoPys (nodes) to a single LoPy acting as a Nano-Gateway.

For more information and discussions about this code, see this forum [post](https://forum.pycom.io/topic/236/lopy-nano-gateway).

### Gateway Code

```python
import socket
import struct
from network import LoRa

# A basic package header, B: 1 byte for the deviceId, B: 1 byte for the pkg size, %ds: Formatted string for string
_LORA_PKG_FORMAT = "!BB%ds"
# A basic ack package, B: 1 byte for the deviceId, B: 1 byte for the pkg size, B: 1 byte for the Ok (200) or error messages
_LORA_PKG_ACK_FORMAT = "BBB"

# Open a LoRa Socket, use rx_iq to avoid listening to our own messages
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORA, rx_iq=True, region=LoRa.EU868)
lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
lora_sock.setblocking(False)

while (True):
    recv_pkg = lora_sock.recv(512)
    if (len(recv_pkg) > 2):
        recv_pkg_len = recv_pkg[1]

        device_id, pkg_len, msg = struct.unpack(_LORA_PKG_FORMAT % recv_pkg_len, recv_pkg)

# If the uart = machine.UART(0, 115200) and os.dupterm(uart) are set in the boot.py this print should appear in the serial port
        print('Device: %d - Pkg:  %s' % (device_id, msg))

        ack_pkg = struct.pack(_LORA_PKG_ACK_FORMAT, device_id, 1, 200)
        lora_sock.send(ack_pkg)
```

The `_LORA_PKG_FORMAT` is used as a method of identifying the different devices within a network. The `_LORA_PKG_ACK_FORMAT` is a simple `ack` package as a response to the nodes package.

### Node

```python
import os
import socket
import time
import struct
from network import LoRa

# A basic package header, B: 1 byte for the deviceId, B: 1 byte for the pkg size
_LORA_PKG_FORMAT = "BB%ds"
_LORA_PKG_ACK_FORMAT = "BBB"
DEVICE_ID = 0x01


# Open a Lora Socket, use tx_iq to avoid listening to our own messages
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORA, tx_iq=True, region=LoRa.EU868)
lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
lora_sock.setblocking(False)

while(True):
    # Package send containing a simple string
    msg = "Device 1 Here"
    pkg = struct.pack(_LORA_PKG_FORMAT % len(msg), DEVICE_ID, len(msg), msg)
    lora_sock.send(pkg)

    # Wait for the response from the gateway. NOTE: For this demo the device does an infinite loop for while waiting the response. Introduce a max_time_waiting for you application
    waiting_ack = True
    while(waiting_ack):
        recv_ack = lora_sock.recv(256)

        if (len(recv_ack) > 0):
            device_id, pkg_len, ack = struct.unpack(_LORA_PKG_ACK_FORMAT, recv_ack)
            if (device_id == DEVICE_ID):
                if (ack == 200):
                    waiting_ack = False
                    # If the uart = machine.UART(0, 115200) and os.dupterm(uart) are set in the boot.py this print should appear in the serial port
                    print("ACK")
                else:
                    waiting_ack = False
                    # If the uart = machine.UART(0, 115200) and os.dupterm(uart) are set in the boot.py this print should appear in the serial port
                    print("Message Failed")

    time.sleep(5)
```

The node is always sending packages and waiting for the `ack` from the gateway.

{% hint style='info' %}
To adapt this code to user specific needs:

- Put a max waiting time for the `ack` to arrive and resend the package or mark it as invalid
- Increase the package size changing the `_LORA_PKG_FORMAT` to `BH%ds`. The `H` will allow the keeping of 2 bytes for size (for more information about [struct format](https://docs.python.org/2/library/struct.html#format-characters))
- Reduce the package size with bitwise manipulation
- Reduce the message size (for this demo, a string) to something more useful for specific development
{% endhint %}
