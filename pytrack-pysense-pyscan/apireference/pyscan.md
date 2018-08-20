# Pyscan

This chapter describes the various libraries which are designed for the Pyscan board. This includes details about the various methods and classes available for each of the Pyscan’s sensors.

## 3-Axis Accelerometer \(LIS2HH12\)

Pysense has a 3-Axis Accelerometer that provides outputs for acceleration as well as roll, pitch and yaw.

### Constructors

#### class LIS2HH12\(pysense = None, sda = 'P22', scl = 'P21'\)

Creates a `LIS2HH12` object, that will return values for acceleration, roll, pitch and yaw. Constructor must be passed a Pysense or I2C object to successfully construct.

### Methods

#### LIS2HH12.acceleration\(\)

Read the acceleration from the `LIS2HH12`. Returns a **tuple** with the 3 values of acceleration \(G\).

#### LIS2HH12.roll\(\)

Read the current roll from the `LIS2HH12`. Returns a **float** in degrees in the range -180 to 180.

#### LIS2HH12.pitch\(\)

Read the current pitch from the `LIS2HH12`. Returns a **float** in degrees in the range -90 to 90. Once the board tilts beyond this range the values will repeat. This is due to a lack of yaw measurement, making it not possible to know the exact orientation of the board.

## Digital Ambient Light Sensor \(LTR-329ALS-01\)

Pysense has a dual light sensor that provides outputs for external light levels in lux. See the datasheet for more information about the wavelengths of the two sensors.

### Constructors

#### class LTR329ALS01\(pysense = None, sda = 'P22', scl = 'P21', gain = ALS\_GAIN\_1X, integration = ALS\_INT\_100, rate = ALS\_RATE\_500\)

Creates a `LTR329ALS01` object, that will return values for light in lux. Constructor must be passed a Pysense or I2C object to successfully construct.

### Methods

#### LTR329ALS01.light\(\)

Read the light levels of both `LTR329ALS01` sensors. Returns a **tuple** with two values for light levels in lux.

### Arguments

The following arguments may be passed into the constructor.

* gain: `ALS_GAIN_1X`,`ALS_GAIN_2X`, `ALS_GAIN_4X`, `ALS_GAIN_8X`, `ALS_GAIN_48X`, `ALS_GAIN_96X`
* integration: `ALS_INT_50`, `ALS_INT_100`, `ALS_INT_150`, `ALS_INT_200`, `ALS_INT_250`, `ALS_INT_300`, `ALS_INT_350`, `ALS_INT_400`
* rate: `ALS_RATE_50`, `ALS_RATE_100`, `ALS_RATE_200`, `ALS_RATE_500`, `ALS_RATE_1000`, `ALS_RATE_2000`

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

{% hint style="info" %}
Please note that more functionality is being added weekly to these libraries. If a required feature is not available, feel free to contribute with a pull request at the [Libraries GitHub repository](https://github.com/pycom/pycom-libraries)
{% endhint %}

