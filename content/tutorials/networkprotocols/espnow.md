---
title: ""
aliases:
    - tutorials/all/ESP-NOW.html
    - tutorials/all/espnow.md
---

Detailed information about this class can be found in [espnow](/firmwareapi/pycom/network/espnow).

### Sending and receiving messages to/from 2 remote devices: Peer 1 and Peer 2

The following example sets up a device which communicates with 2 remote Peers. Message exchange with Peer 1 is encrypted while with Peer 2 it is not.

```python

from network import WLAN
from network import ESPNOW
import binascii
import time

# Modify this variable to change the PMK to be used
# Note: This must match with the value of ESPNOW_PMK from the next example.
ESPNOW_PMK = "0123456789abcdef"
# Modify this variable to change the MAC address of the remote Peer 1
# Note: This must match with the MAC address of the Peer 1 from the next example.
ESPNOW_PEER_1_MAC = "112233445566"
# Modify this variable to change the LMK to be used when communicating with remote Peer 1
# Note: This must match with the value of ESPNOW_PEER_LMK from the next example.
ESPNOW_PEER_1_LMK = "0123456789123456"
# Modify this variable to change the MAC address of the remote Peer 2
# Note: This must match with the MAC address of the Peer 2 from the next example.
ESPNOW_PEER_2_MAC = "AABBCCDDEEFF"


# The callback to be registered when a message has been sent to a Peer
def espnow_tx(result):
    # "result" is the parameter in form of 2 element long tuple
    # "peer" is the Peer which the message has been sent to
    # "sent" is a boolean showing whether the message could be sent
	peer, sent = result
	mac = peer.addr()
	if(sent == False):
		print("Sending message to %s failed!" % binascii.hexlify(mac))
	else:
		print("Message sent to: %s" % (binascii.hexlify(mac)))

# The callback to be registered when a message has been received
def espnow_rx(result):
	# "result" is the parameter in form of 3 element long tuple
	# "mac" is the MAC address of the sender
	# "peer" is the Peer which the message has been received from. If message has been received from a not registered Peer this parameter is None
	# "msg" is the payload from the received message
	mac, peer, msg = result
	# Accept and handle messages only from the registered Peers
	if(peer is not None):
		# Do something with the received message
		print("Message received from %s with content: %s" % (binascii.hexlify(mac), msg))

# The ESPNOW module needs that WLAN is initialized
w = WLAN()
# Initialize the ESPNOW module
ESPNOW.init()
print("ESP-NOW version: %s" % ESPNOW.version())

# Register the callback which will be called on TX
ESPNOW.on_send(espnow_tx)
# Register the callback which will be called on RX
ESPNOW.on_recv(espnow_rx)
# Configure the Primary Master Key which is used to encrypt the Local Master Key
ESPNOW.pmk(ESPNOW_PMK)

# Add Peer 1
p1 = ESPNOW.add_peer(ESPNOW_PEER_1_MAC)
# Add Peer 2
p2 = ESPNOW.add_peer(ESPNOW_PEER_2_MAC)
# Set the Local Master Key of Peer p1
p1.lmk(ESPNOW_PEER_1_LMK)
# Do not set LMK for Peer 2, traffic is not encrypted

# Get the number of registered Peers and how many is encrypted
count = ESPNOW.peer_count()
print("Number of Peers: %s, encrypted: %s" % (count[0], count[1]))

# Sending some messages to the Peers individually
i = 0
while i < 10:
    # The Peer 1 will only receive this message if the same PMK and LMK is configured for the Peer object created for this device on the other device also. Check the next examples.
    p1.send("%s" % (i))
    # Message to Peer 2 is not encrypted, on the Peer 2 device encryption for this current device's Peer object should not be configured. Check the next examples.
    p2.send("%s" % (i))
    i = i + 1
    time.sleep(1)

# Sending 1 message to all Peers which are registered
ESPNOW.send(None, "Hello all Peers!")

# Remove Peer 1
ESPNOW.del_peer(p1)

# Deinit the module
ESPNOW.deinit()

```

### Example code for Peer 1
This example code implements Peer 1 device from the previous example.

```python
from network import WLAN
from network import ESPNOW
import binascii
import time

# Modify this variable to change the PMK to be used
# Note: This must match with the value of ESPNOW_PMK from the first example.
ESPNOW_PMK = "0123456789abcdef"
# Modify this variable to change the MAC address of the remote Peer.
# Note: This must match with the MAC address of the Peer from the first example.
ESPNOW_PEER_MAC = "665544332211"
# Modify this variable to change the LMK to be used when communicating with the remote Peer
# Note: This must match with the value of ESPNOW_PEER_1_LMK from the first example.
ESPNOW_PEER_LMK = "0123456789123456"

def tx(result):
	peer, sent = result
	mac = peer.addr()
	print("Sending to: %s - %r" % (binascii.hexlify(mac),sent))

def rx(result):
	print("Message received:")
	mac, peer, msg = result
    # Accept messages only from the registered Peer
	if(peer is not None):
		print("Received: %s - %s" % (binascii.hexlify(mac),msg))
		# Send back a response
		peer.send("Message received: %s" % msg)

w = WLAN()
ESPNOW.init()
ESPNOW.on_send(tx)
ESPNOW.on_recv(rx)
ESPNOW.pmk(ESPNOW_PMK)

# Add the Peer
p = ESPNOW.add_peer(ESPNOW_PEER_MAC)
# Configure the LMK to be used during communication.
p.lmk(ESPNOW_PEER_LMK)

```

### Example code for Peer 2
This example code implements Peer 2 device from the first example.

```python
from network import WLAN
from network import ESPNOW
import binascii
import time

# Modify this variable to change the MAC address of the remote Peer.
# Note: This must match with the MAC address of the Peer from the first example.
ESPNOW_PEER_MAC = "665544332211"

def tx(result):
	peer, sent = result
	mac = peer.addr()
	print("Sending to: %s - %r" % (binascii.hexlify(mac),sent))

def rx(result):
	print("Message received:")
	mac, peer, msg = result
    # Accept messages only from the registered Peer
	if(peer is not None):
		print("Received: %s - %s" % (binascii.hexlify(mac),msg))
		# Send back a response
		peer.send("Message received: %s" % msg)

w = WLAN()
# Init ESP-NOW, no PMK is configured.
ESPNOW.init()
ESPNOW.on_send(tx)
ESPNOW.on_recv(rx)

# Add the Peer. No LMK will be configured for it.
p = ESPNOW.add_peer(ESPNOW_PEER_MAC)

```

### Example snippet for RX callback
This example snippet shows how it may be handled when the device receives a message from a previously not registered Peer.

```python

# The callback to be registered when a message has been received
def espnow_rx(result):
	# "result" is the parameter in form of 3 element long tuple
    # "mac" is the MAC address of the sender
    # "peer" is the Peer which the message has been received from. If message has been received from a not registered Peer this parameter is None
    # "msg" is the payload from the received message
    mac, peer, msg = result
	if(peer is None):
		print("Message received from an unknown Peer, registering...")
		peer = ESPNOW.add_peer(mac)
	print("Message received from %s with content: %s" % (binascii.hexlify(mac), msg))
	peer.send("Sending back an answer...")

```