---
title: "ucrypto"
aliases:
    - firmwareapi/micropython/ucrypto.html
    - firmwareapi/micropython/ucrypto.md
    - chapter/firmwareapi/micropython/ucrypto
---

This module provides native support for cryptographic algorithms. It's loosely based on PyCrypto.

## Classes

* [class AES](/firmwareapi/pycom/aes) - Advanced Encryption Standard

## **Methods**

#### crypto.getrandbits(bits)

Returns a bytes object filled with random bits obtained from the hardware random number generator.

According to the **ESP32 Technical Reference Manual**, such bits "... can be used as the basis for cryptographical operations". "These true random numbers are generated based on the noise in the Wi-Fi/BT RF system. When Wi-Fi and BT are disabled, the random number generator will give out pseudo-random numbers."

The parameter `bits` is rounded upwards to the nearest multiple of 32 bits.

{{% hint style="danger" %}}
Cryptography is not a trivial business. Doing things the wrong way could quickly result in decreased or no security. Please document yourself in the subject if you are depending on encryption to secure important information.
{{< /hint >}}

#### crypto.generate\_rsa\_signature(message, private_key, \*, pers="esp32-tls")

Generates signature for `message` based on `private_key` using RS256 algorithm.
The `message` is expected as a string.
The `private_key` is the content of the private key and not the path of it. The private key must be in PKCS8 format!
The `pers` is the personalization string used for random number generation.
Returns with a Bytes object containing the generated signature.

```python

import crypto

# Example of a JWT header + payload
header_payload = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFtcGxlLmNvbS9pc19yb290Ijp0cnVlfQ"
# Private key MUST BE in PKCS8 format !!!
f = open("cert/private_key_pkcs8.pem")
pk = f.read()
# Generate the signature
signature = crypto.generate_rsa_signature(header_payload, pk, pers="my_pers_string")
```
