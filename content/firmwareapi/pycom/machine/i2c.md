---
title: "I2C"
aliases:
    - firmwareapi/pycom/machine/i2c.html
    - firmwareapi/pycom/machine/i2c.md
    - chapter/firmwareapi/pycom/machine/i2c
---

I2C is a two-wire protocol for communicating between devices. At the physical level it consists of 2 wires: SCL and SDA, the clock and data lines respectively.

I2C objects are created attached to a specific bus. They can be initialised when created, or initialised later on.

## Example using default Pins

```python

from machine import I2C

i2c = I2C(0)                         # create on bus 0
i2c = I2C(0, I2C.MASTER)             # create and init as a master
i2c = I2C(0, pins=('P10','P11'))     # create and use non-default PIN assignments (P10=SDA, P11=SCL)
i2c.init(I2C.MASTER, baudrate=20000) # init as a master
i2c.deinit()                         # turn off the peripheral
```

## Example using non-default Pins

```python

from machine import I2C

i2c = I2C(0, pins=('P10','P11'))     # create and use non-default PIN assignments (P10=SDA, P11=SCL)
i2c.init(I2C.MASTER, baudrate=20000) # init as a master
i2c.deinit()                         # turn off the peripheral
```

Printing the `i2c` object gives you information about its configuration.

A master must specify the recipient's address:

```python

i2c.init(I2C.MASTER)
i2c.writeto(0x42, '123')        # send 3 bytes to slave with address 0x42
i2c.writeto(addr=0x42, b'456')  # keyword for address
```

Master also has other methods:

```python

i2c.scan()                          # scan for slaves on the bus, returning
                                    #   a list of valid addresses
i2c.readfrom_mem(0x42, 2, 3)        # read 3 bytes from memory of slave 0x42,
                                    #   starting at address 2 in the slave
i2c.writeto_mem(0x42, 2, 'abc')     # write 'abc' (3 bytes) to memory of slave 0x42
                                    # starting at address 2 in the slave, timeout after 1 second
```

## Quick Usage Example

```python

from machine import I2C
# configure the I2C bus
i2c = I2C(0, I2C.MASTER, baudrate=100000)
i2c.scan() # returns list of slave addresses
i2c.writeto(0x42, 'hello') # send 5 bytes to slave with address 0x42
i2c.readfrom(0x42, 5) # receive 5 bytes from slave
i2c.readfrom_mem(0x42, 0x10, 2) # read 2 bytes from slave 0x42, slave memory 0x10
i2c.writeto_mem(0x42, 0x10, 'xy') # write 2 bytes to slave 0x42, slave memory 0x10
```

## Constructors

#### class machine.I2C(bus, ...)

Construct an I2C object on the given `bus`. `bus` can only be `0, 1, 2`. If the `bus` is not given, the default one will be selected (`0`). Buses `0` and `1` use the ESP32 I2C hardware peripheral while bus `2` is implemented with a bit-banged software driver.

## Methods

### General Methods

#### i2c.init(mode, \* , baudrate=100000, pins=(SDA, SCL))

Initialise the I2C bus with the given parameters:

* `mode` must be I2C.MASTER
* `baudrate` is the SCL clock rate
* pins is an optional tuple with the pins to assign to the I2C bus. The default I2C pins are `P9` (SDA) and `P10` (SCL)

#### i2c.scan()

Scan all I2C addresses between `0x08` and `0x77` inclusive and return a list of those that respond. A device responds if it pulls the SDA line low after its address (including a read bit) is sent on the bus.

### Standard Bus Operations

The following methods implement the standard I2C master read and write operations that target a given slave device.

#### i2c.readfrom(addr, nbytes)

Read `nbytes` from the slave specified by `addr`. Returns a bytes object with the data read.

#### i2c.readfrom\_into(addr, buf)

Read into `buf` from the slave specified by `addr`. The number of bytes read will be the length of `buf`.

Return value is the number of bytes read.

#### i2c.writeto(addr, buf, \* , stop=True)

Write the bytes from `buf` to the slave specified by `addr`. The argument `buf` can also be an integer which will be treated as a single byte. If `stop` is set to `False` then the stop condition won't be sent and the I2C operation may be continued (typically with a read transaction).

Return value is the number of bytes written.

### Memory Operations

Some I2C devices act as a memory device (or set of registers) that can be read from and written to. In this case there are two addresses associated with an I2C transaction: the slave address and the memory address. The following methods are convenience functions to communicate with such devices.

#### i2c.readfrom\_mem(addr, memaddr, nbytes, \*, addrsize=8)

Read `nbytes` from the slave specified by `addr` starting from the memory address specified by `memaddr`. The `addrsize` argument is specified in bits and it can only take 8 or 16.

#### i2c.readfrom\_mem\_into(addr, memaddr, buf, \*, addrsize=8)

Read into `buf` from the slave specified by `addr` starting from the memory address specified by `memaddr`. The number of bytes read is the length of `buf`. The `addrsize` argument is specified in bits and it can only take 8 or 16.

The return value is the number of bytes read.

#### i2c.writeto\_mem(addr, memaddr, buf \*, addrsize=8)

Write `buf` to the slave specified by `addr` starting from the memory address specified by `memaddr`. The argument `buf` can also be an integer which will be treated as a single byte. The `addrsize` argument is specified in bits and it can only take 8 or 16.

The return value is the number of bytes written.

## Constants

* `I2C.MASTER`: Used to initialise the bus to master mode.

