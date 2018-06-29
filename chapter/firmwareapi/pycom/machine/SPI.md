# class SPI – Serial Peripheral Interface

SPI is a serial protocol that is driven by a master. At the physical level there are 3 lines: SCK, MOSI, MISO.

See usage model of I2C; SPI is very similar. Main difference is parameters to init the SPI bus:

```python
from machine import SPI
spi = SPI(0, mode=SPI.MASTER, baudrate=1000000, polarity=0, phase=0, firstbit=SPI.MSB)
```

Only required parameter is mode, must be <constant>SPI.MASTER</constant>. Polarity can be 0 or 1, and is the level the idle clock line sits at. Phase can be 0 or 1 to sample data on the first or second clock edge respectively.

### Quick Usage Example

```python
from machine import SPI

# configure the SPI master @ 2MHz
# this uses the SPI default pins for CLK, MOSI and MISO (``P10``, ``P11`` and ``P14``)
spi = SPI(0, mode=SPI.MASTER, baudrate=2000000, polarity=0, phase=0)
spi.write(bytes([0x01, 0x02, 0x03, 0x04, 0x05])) # send 5 bytes on the bus
spi.read(5) # receive 5 bytes on the bus
rbuf = bytearray(5)
spi.write_readinto(bytes([0x01, 0x02, 0x03, 0x04, 0x05]), rbuf) # send a receive 5 bytes
```

### Quick Usage Example using non-default pins

```python
from machine import SPI

# configure the SPI master @ 2MHz
# this uses the SPI non-default pins for CLK, MOSI and MISO (``P19``, ``P20`` and ``P21``)
spi = SPI(0, mode=SPI.MASTER, baudrate=2000000, polarity=0, phase=0, pins=('P19','P20','P21'))
spi.write(bytes([0x01, 0x02, 0x03, 0x04, 0x05])) # send 5 bytes on the bus
spi.read(5) # receive 5 bytes on the bus
rbuf = bytearray(5)
spi.write_readinto(bytes([0x01, 0x02, 0x03, 0x04, 0x05]), rbuf) # send a receive 5 bytes
```

### Constructors

#####<class><i>class</i> machine.SPI(id, ...)</class>

Construct an SPI object on the given bus. `id` can be only 0. With no additional parameters, the SPI object is created but not initialised (it has the settings from the last initialisation of the bus, if any). If extra arguments are given, the bus is initialised. See init for parameters of initialisation.

### Methods

#####<function>spi.init(mode, baudrate=1000000, * , polarity=0, phase=0, bits=8, firstbit=SPI.MSB, pins=(CLK, MOSI, MISO))</function>

Initialise the SPI bus with the given parameters:

- `mode` must be <constant>SPI.MASTER</constant>.
- `baudrate` is the SCK clock rate.
- `polarity` can be 0 or 1, and is the level the idle clock line sits at.
- `phase` can be 0 or 1 to sample data on the first or second clock edge respectively.
- `bits` is the width of each transfer, accepted values are 8, 16 and 32.
- `firstbit` can be <constant>SPI.MSB</constant> or <constant>SPI.LSB</constant>.
- `pins` is an optional tuple with the pins to assign to the SPI bus. If the pins argument is not given the default pins will be selected (`P10` as CLK,`P11` as MOSI and `P14` as MISO). If pins is passed as None then no pin assignment will be made.

#####<function>spi.deinit()</function>

Turn off the SPI bus.

#####<function>spi.write(buf)</function>

Write the data contained in `buf`. Returns the number of bytes written.

#####<function>spi.read(nbytes, * , write=0x00)</function>

Read the `nbytes` while writing the data specified by `write`. Return the number of bytes read.

#####<function>spi.readinto(buf, * , write=0x00)</function>

Read into the buffer specified by `buf` while writing the data specified by `write`. Return the number of bytes read.

#####<function>spi.write_readinto(write_buf, read_buf)</function>

Write from `write_buf` and read into `read_buf`. Both buffers must have the same length. Returns the number of bytes written

### Constants

<constant>SPI.MASTER</constant>

For initialising the SPI bus to master

<constant>SPI.MSB</constant>

Set the first bit to be the most significant bit

<constant>SPI.LSB</constant>

Set the first bit to be the least significant bit
