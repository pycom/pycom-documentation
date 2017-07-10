# class AES - Advanced Encryption Standard
AES (Advanced Encryption Standard) is a symmetric block cipher standardised by NIST. It has a fixed data block size of 16 bytes. Its keys can be 128, 192, or 256 bits long.

{% hint style='danger' %}
AES is implemented using the ESP32 hardware module.
{% endhint %}

### Quick Usage Example

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

### Constructors
<class><i>class</i> ucrypto.AES(key, mode, IV, * , counter, segment_size)</class>

Create an AES object that will let you encrypt and decrypt messages.

The arguments are:

- ``key`` (byte string) is the secret key to use. It must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) bytes long.
- ``mode`` is the chaining mode to use for encryption and decryption. Default is <constant>AES.MODE_ECB</constant>.
- ``IV`` (byte string) initialisation vector. Should be 16 bytes long. It is ignored in modes <constant>AES.MODE_ECB</constant> and <constant>AES.MODE_CRT</constant>.
- ``counter`` (byte string) used only for <constant>AES.MODE_CTR</constant>. Should be 16 bytes long. Should not be reused.
- ``segment_size`` is the number of bits ``plaintext`` and ``ciphertext`` are segmented in. Is only used in <constant>AES.MODE_CFB</constant>. Supported values are <constant>AES.SEGMENT_8</constant> and <constant>AES.SEGMENT_128</constant>.

### Methods

<function>ucrypto.encrypt()</function>

Encrypt data with the key and the parameters set at initialisation.

<function>ucrypto.decrypt()</function>

Decrypt data with the key and the parameters set at initialisation.

### Constants

<constant>AES.MODE_ECB</constant>

Electronic Code Book. Simplest encryption mode. It does not hide data patterns well (see this article for more info).

<constant>AES.MODE_CBC</constant>

Cipher-Block Chaining. An Initialisation Vector (IV) is required.

<constant>AES.MODE_CFB</constant>

Cipher feedback. ``plaintext`` and ``ciphertext`` are processed in segments of segment_size bits. Works a stream cipher.

<constant>AES.MODE_CTR</constant>

Counter mode. Each message block is associated to a counter which must be unique across all messages that get encrypted with the same key.

<constant>AES.SEGMENT_8</constant> <constant>AES.SEGMENT_128</constant>

Length of the segment for <constant>AES.MODE_CFB</constant>.

{% hint style='danger' %}
To avoid security issues, IV should always be a random number and should never be reused to encrypt two different messages. The same applies to the counter in CTR mode. You can use <function>crypto.getrandbits()</function> for this purpose.
{% endhint %}
