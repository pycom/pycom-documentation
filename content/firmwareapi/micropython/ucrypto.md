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

{{% hint style="danger" %}}Cryptography is not a trivial business. Doing things the wrong way could quickly result in decreased or no security. Please document yourself in the subject if you are depending on encryption to secure important information. {{% /hint %}}

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

#### crypto.rsa_encrypt\(message, public_key)

Encrypts the `message` with the `public_key` of the recipient, so it will be decrypted only by the real destination.

The `message` is Bytes object.

The `public_key` is RSA 2048bits, it is the content of the key file (not the path to it) and it needs to be in PKCS8 format. An `openssl` example of how this key was generated is bellow.

Returns the Bytes object containing the encrypted message.

The usage example is at the method `crypto.rsa_decrypt()`.

#### crypto.rsa_decrypt\(message, private_key)

Decrypts the `message` with the `private_key`.

The `message` is Bytes object.

The `private_key` is RSA 2048bits, it is the content of the key file (not the path to it) and it needs to be in PKCS8 format. An `openssl` example of how this key was generated is bellow.

Returns the Bytes object containing the decrypted message.

```python
# generating the public-private keys pair in a single PEM file
$ openssl genrsa -des3 -out private.pem 2048
# export the RSA public key to a file
$ openssl rsa -in private.pem -outform PEM -pubout -out public.pem
# export the RSA private key to a file
$ openssl rsa -in private.pem -out private_unencrypted.pem -outform PEM

# Example of message
message = "this is a secret message, it needs to be encrypted"

# read the key from file
f = open("cert/public.pem")
pk = f.read()
f.close()

# Encrypt the message
message_encrypted = crypto.rsa_encrypt(payload, pk)

# adding a SHA checksum (`uhashlib.sha()`) is encouraged,
# so when message is decrypted consistency can be checked

# ... next send the message_encrypted on the network (LoRa, Wifi, BLE, Cellular)

# on the receiver try to decrypt

# read the key from file
f = open("cert/private_unencrypted.pem")
pub = f.read()
f.close()

message_decrypted = crypto.rsa_decrypt(message_encrypted, pub)
# additionally, the consistency should be checked (usage of `uhashlib.sha()``)
# as the message could have been altered (attacker, network issues)
```
