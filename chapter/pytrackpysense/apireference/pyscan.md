# Pyscan API

This chapter describes the various libraries which are designed for the Pyscan board. This includes details about the various methods and classes available for each of the Pyscan’s sensors.

### Pyscan NFC library (MFRC6300)

#### Constructors

##### <class><i>class</i> MFRC630(pyscan=None, sda='P22', scl='P21', timeout=None, debug=False)</class>

Creates a `MFRC630` object. Constructor must be passed a Pyscan or I2C object to successfully construct.

#### Methods
##### <function>MFRC630.mfrc630_cmd_init()</function>
Initialise the `MFRC630` with some settings

##### <function>MFRC630.mfrc630_cmd_reset()</function>
Reset the device. Stops the currently active command and resets device.

##### <function>MFRC630.mfrc630_cmd_idle()</function>
Set the device into idle mode. Stops the currently active command and return to idle mode.

##### <function>MFRC630.mfrc630_cmd_load_key(key)</function>
Loads the provided key into the key buffer.

- `key` Array which holds the MIFARE key, **it is always 6 bytes long**

##### <function>MFRC630.mfrc630_MF_read_block(block_address, dest)</function>
Reads a block of memory from an authenticated card. Try to read a block of memory from the card with the appropriate timeouts and error checking.

- `block_address` The block to read
- `dest` The array in which to write the 16 bytes read from the card

Returns `0` for failure, otherwise the number of bytes received.

##### <function>MFRC630.mfrc630_MF_auth(uid, key_type, block)</function>
Perform a MIFARE authentication procedure. This function is a higher-level wrapper around the MF authenticate command. The result of the authentication is checked to identify whether it appears to have succeeded. The key must be loaded into the key buffer with <function>MFRC630.mfrc630_cmd_load_key(key)</function>.

Once authenticated, the authentication MUST be stopped manually by calling the <function>mfrc630_MF_deauth()</function> function or otherwise disabling the `Crypto1 ON` bit in the status register.

- `key_type` The MIFARE key A or B (<constant>MFRC630_MF_AUTH_KEY_A</constant> or <constant>MFRC630_MF_AUTH_KEY_B</constant>) to use
- `block` The block to authenticate
- `uid` The authentication procedure required the first four bytes of the card's UID to authenticate

Returns `0` in case of failure, nonzero in case of success.

##### <function>MFRC630.mfrc630_MF_deauth()</function>
Disables MIFARE authentication. Disable the `Crypto1` bit from the status register to disable encryption.

##### <function>MFRC630.mfrc630_iso14443a_WUPA_REQA(instruction)</function>
Send `WUPA` and `REQA`. Returns the response byte, the answer to request `A` byte (`ATQA`), or `0` in case of no answer.

**`instruction`**

<constant>MFRC630_ISO14443_CMD_WUPA</constant> <constant>MFRC630_ISO14443_CMD_REQA</constant>

##### <function>MFRC630.mfrc630_iso14443a_select(uid)</function>
Performs the `SELECT` procedure to discover a card's UID. This performs the `SELECT` procedure as explained in *ISO14443A*, this determines the UID of the card, if multiple cards are present, a collision will occur, which is handled according to the norm.

- `uid`: The UID of the card will be stored into this array.

Returns the length of the UID in bytes (`4, 7, 10`), or `0` in case of failure.

##### <function>MFRC630.print_debug(msg)</function>
Prints debug statements if `DEBUG` is enabled.

##### <function>MFRC630.format_block(block, length)</function>
Prints `block` with `length`.

##### <function>MFRC630.mfrc630_format_block(data, len)</function>
Converts `data` to hexadecimal format.

- `data` The array to be formatted
- `len` The number of bytes to format

##### <function>MFRC630.mfrc630_print_block(data, len)</function>
Prints the bytes in `data` array in hexadecimal format, separated by spaces using the `mfrc630_format_block` method.

- `data` The array to be printed
- `len` The number of bytes to print
