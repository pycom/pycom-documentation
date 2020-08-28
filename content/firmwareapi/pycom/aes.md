---
title: "AES"
aliases:
    - firmwareapi/pycom/aes.html
    - firmwareapi/pycom/aes.md
    - chapter/firmwareapi/pycom/aes
---

AES (Advanced Encryption Standard) is a symmetric block cipher standardised by NIST. It has a fixed data block size of 16 bytes. Its keys can be 128, 192, or 256 bits long.

>AES is implemented using the ESP32 hardware module.


## Quick Usage Example

```python
from crypto import AES
import crypto
key = b'notsuchsecretkey' # 128 bit (16 bytes) key
iv = crypto.getrandbits(128) # hardware generated random IV (never reuse it)

cipher = AES(key, AES.MODE_CFB, iv)
msg = iv + cipher.encrypt(b'Attack at dawn')

# ... after properly sent the encrypted message somewhere ...

cipher = AES(key, AES.MODE_CFB, msg[:16]) # on the decryption side
original = cipher.decrypt(msg[16:])
print(original)
```

## Constructors

### class ucrypto.AES(key, [mode=AES.MODE_ECB, IV, counter, segment_size])

Create an AES object that will let you encrypt and decrypt messages.

The arguments are:

* `key` (byte string) is the secret key to use. It must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) bytes long.
* `mode` is the chaining mode to use for encryption and decryption. Can be the following values:
    * `AES.MODE_ECB`: Electronic Code Book. Simplest encryption mode.
    * `AES.MODE_CBC`: Cipher-Block Chaining. An Initialisation Vector (IV) is required.
    * `AES.MODE_CFB`: Cipher feedback. `plaintext` and `ciphertext` are processed in segments of `segment_size` bits. Works a stream cipher.
    * `AES.MODE_CTR`:  Counter mode. Each message block is associated to a counter which must be unique across all messages that get encrypted with the same key.
* `IV` (byte string) initialisation vector. Should be 16 bytes long. It is ignored in modes `AES.MODE_ECB` and `AES.MODE_CRT`.
> To avoid security issues, IV should always be a random number and should never be reused to encrypt two different messages. The same applies to the counter in CTR mode. You can use `crypto.getrandbits()` for this purpose.
* `counter` (byte string) used only for `AES.MODE_CTR`. Should be 16 bytes long. Should not be reused.
* `segment_size` is the number of bits `plaintext` and `ciphertext` are segmented in. Is only used in `AES.MODE_CFB`. Supported values are:
    * `AES.SEGMENT_8`
    * `AES.SEGMENT_128`



## Methods

### ucrypto.encrypt()

Encrypt data with the key and the parameters set at initialisation.

### ucrypto.decrypt()

Decrypt data with the key and the parameters set at initialisation.

## Constants

* `AES.MODE_ECB`, `AES.MODE_CBC`, `AES.MODE_CFB`, `AES.MODE_CTR`
* `AES.SEGMENT_8`, `AES.SEGMENT_128`


