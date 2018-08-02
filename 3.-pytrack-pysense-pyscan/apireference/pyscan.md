# 3.3.4 Pyscan

This chapter describes the various libraries which are designed for the Pyscan board. This includes details about the various methods and classes available for each of the Pyscan’s sensors.

## Pyscan NFC library \(MFRC6300\)

### Constructors

#### class MFRC630\(pyscan=None, sda='P22', scl='P21', timeout=None, debug=False\)

Creates a `MFRC630` object. Constructor must be passed a Pyscan or I2C object to successfully construct.

### Methods

#### MFRC630.mfrc630\_cmd\_init\(\)

Initialise the `MFRC630` with some settings

#### MFRC630.mfrc630\_cmd\_reset\(\)

Reset the device. Stops the currently active command and resets device.

#### MFRC630.mfrc630\_cmd\_idle\(\)

Set the device into idle mode. Stops the currently active command and return to idle mode.

#### MFRC630.mfrc630\_cmd\_load\_key\(key\)

Loads the provided key into the key buffer.

* `key` Array which holds the MIFARE key, **it is always 6 bytes long**

#### MFRC630.mfrc630\_MF\_read\_block\(block\_address, dest\)

Reads a block of memory from an authenticated card. Try to read a block of memory from the card with the appropriate timeouts and error checking.

* `block_address` The block to read
* `dest` The array in which to write the 16 bytes read from the card

Returns `0` for failure, otherwise the number of bytes received.

#### MFRC630.mfrc630\_MF\_auth\(uid, key\_type, block\)

Perform a MIFARE authentication procedure. This function is a higher-level wrapper around the MF authenticate command. The result of the authentication is checked to identify whether it appears to have succeeded. The key must be loaded into the key buffer with `MFRC630.mfrc630_cmd_load_key(key)`.

Once authenticated, the authentication MUST be stopped manually by calling the `mfrc630_MF_deauth()` function or otherwise disabling the `Crypto1 ON` bit in the status register.

* `key_type` The MIFARE key A or B \(`MFRC630_MF_AUTH_KEY_A` or `MFRC630_MF_AUTH_KEY_B`\) to use
* `block` The block to authenticate
* `uid` The authentication procedure required the first four bytes of the card's UID to authenticate

Returns `0` in case of failure, nonzero in case of success.

#### MFRC630.mfrc630\_MF\_deauth\(\)

Disables MIFARE authentication. Disable the `Crypto1` bit from the status register to disable encryption.

#### MFRC630.mfrc630\_iso14443a\_WUPA\_REQA\(instruction\)

Send `WUPA` and `REQA`. Returns the response byte, the answer to request `A` byte \(`ATQA`\), or `0` in case of no answer.

* instruction: `MFRC630_ISO14443_CMD_WUPA`, `MFRC630_ISO14443_CMD_REQA`

#### MFRC630.mfrc630\_iso14443a\_select\(uid\)

Performs the `SELECT` procedure to discover a card's UID. This performs the `SELECT` procedure as explained in _ISO14443A_, this determines the UID of the card, if multiple cards are present, a collision will occur, which is handled according to the norm.

* `uid`: The UID of the card will be stored into this array.

Returns the length of the UID in bytes \(`4, 7, 10`\), or `0` in case of failure.

#### MFRC630.print\_debug\(msg\)

Prints debug statements if `DEBUG` is enabled.

#### MFRC630.format\_block\(block, length\)

Prints `block` with `length`.

#### MFRC630.mfrc630\_format\_block\(data, len\)

Converts `data` to hexadecimal format.

* `data` The array to be formatted
* `len` The number of bytes to format

#### MFRC630.mfrc630\_print\_block\(data, len\)

Prints the bytes in `data` array in hexadecimal format, separated by spaces using the `mfrc630_format_block` method.

* `data` The array to be printed
* `len` The number of bytes to print

