---
title: "ucrypto"
aliases:
    - firmwareapi/micropython/ucrypto.html
    - firmwareapi/micropython/ucrypto.md
    - chapter/firmwareapi/micropython/ucrypto
---
This module provides native support for cryptographic algorithms. It's loosely based on PyCrypto.

## Classes

* [class AES](/pycom/aes) - Advanced Encryption Standard

## **Methods**

#### crypto.getrandbits(bits)

Returns a bytes object filled with random bits obtained from the hardware random number generator.

According to the **ESP32 Technical Reference Manual**, such bits "... can be used as the basis for cryptographical operations". "These true random numbers are generated based on the noise in the Wi-Fi/BT RF system. When Wi-Fi and BT are disabled, the random number generator will give out pseudo-random numbers."

The parameter `bits` is rounded upwards to the nearest multiple of 32 bits.

{{% hint style="danger" %}}
Cryptography is not a trivial business. Doing things the wrong way could quickly result in decreased or no security. Please document yourself in the subject if you are depending on encryption to secure important information.
{{< /hint >}}

