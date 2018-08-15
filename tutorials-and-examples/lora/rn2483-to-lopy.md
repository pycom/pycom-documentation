# RN2483 to LoPy

This example shows how to send data between a Microchip RN2483 and a LoPy via raw LoRa.

## RN2483

```text
mac pause
radio set freq 868000000

radio set mod lora
radio set bw 250
radio set sf sf7
radio set cr 4/5
radio set bw 125
radio set sync 12
radio set prlen 8

# Transmit via radio tx:
radio tx 48656c6C6F  #(should send ‘Hello’)
```

## LoPy

```python
from network import LoRa
import socket

lora = LoRa(mode=LoRa.LORA, frequency= 868000000, bandwidth=LoRa.BW_125KHZ, sf=7, preamble=8,
    coding_rate=LoRa.CODING_4_5, power_mode=LoRa.ALWAYS_ON,
    tx_iq=False, rx_iq=False, public=False)

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# This keeps listening for data "forever".
while(True):
    s.recv(64)
```

