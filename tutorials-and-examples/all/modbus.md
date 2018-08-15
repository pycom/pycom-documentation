# Modbus

Modbus is a messaging protocol that defines the packet structure for transferring data between devices in a master/slave architecture. The protocol is independent of the transmission medium and is usually transmitted over TCP \(MODBUS TCP\) or serial communication \(MODBUS RTU\). Modbus is intended as a request/reply protocol and delivers services specified by function codes. The function code in the request tells the addressed slave what kind of action to perform. The function codes most commonly supported by devices are listed below.

| Function Name | Function Code |
| :--- | :--- |
| Read Coils | 0x01 |
| Read Discrete Inputs | 0x02 |
| Read Holding Registers | 0x03 |
| Read Input Registers | 0x04 |
| Write Single Coil | 0x05 |
| Write Single Register | 0x06 |
| Write Multiple Coils | 0x0F |
| Write Multiple Registers | 0x10 |

For more information on the MODBUS RTU see the following [PDF File](http://www.modbus.org/docs/Modbus_over_serial_line_V1_02.pdf). Information on the MODBUS TCP can be found [here](http://www.modbus.org/docs/Modbus_Messaging_Implementation_Guide_V1_0b.pdf).

## Pycom Modbus Library

Python libraries and sample code that support Modbus TCP and Modbus RTU are available at the following [GitHub Repository](https://github.com/pycom/pycom-modbus). To use this library, connect to the target Pycom device via ftp and upload the uModbus folder to `/flash`. A description of the supported function codes is found below.

### Read Coils

This function code requests the status \(ON/OFF\) of discrete coils on a remote device. The slave device address, the address of the first coil and the number of coils must be specified in the request. The address of the first coil is 0 and a maximum of 2000 contiguous coils can be read. Python sample code is shown below.

```python
slave_addr=0x0A
starting_address=0x00
coil_quantity=100

coil_status = modbus_obj.read_coils(slave_addr, starting_address, coil_quantity)
print('Coil status: ' + ' '.join('{:d}'.format(x) for x in coil_status))
```

### Read Discrete Inputs

This command is used to read the status \(ON/OFF\) of discrete inputs on a remote device. The slave address, the address of the first input, and the quantity of inputs to be read must be specified. The address of the first input is 0 and a maximum of 2000 continuous inputs can be read. The Python sample code is shown below.

```python
slave_addr=0x0A
starting_address=0x0
input_quantity=100

input_status = modbus_obj.read_discrete_inputs(slave_addr, starting_address, input_quantity)
print('Input status: ' + ' '.join('{:d}'.format(x) for x in input_status))
```

### Read Holding Registers

This function code is used to read the contents of analogue output holding registers. The slave address, the starting register address, the number of registers to read and the sign of the data must be specified. Register addresses start at 0 and a maximum of 125 continuous registers can be read.

```python
slave_addr=0x0A
starting_address=0x00
register_quantity=100
signed=True

register_value = modbus_obj.read_holding_registers(slave_addr, starting_address, register_quantity, signed)
print('Holding register value: ' + ' '.join('{:d}'.format(x) for x in register_value))
```

### Read Input Registers

This command is used to read up to 125 continuous input registers on a remote device. The slave address, the starting register address, the number of input registers and the sign of the data must be specified. The address of the first input registers is 0.

```python
slave_addr=0x0A
starting_address=0x00
register_quantity=100
signed=True

register_value = modbus_obj.read_input_registers(slave_addr, starting_address, register_quantity, signed)
print('Input register value: ' + ' '.join('{:d}'.format(x) for x in register_value))
```

### Write Single Coil

This function code is used to write the state of a discrete coil on a remote device. A value of `0xFF00` means the coil should be set to ON, while a value of `0x0000` means the coil should be set to OFF. The Python sample code to set the coil at address `0x00`, to an ON state is shown below.

```python
slave_addr=0x0A
output_address=0x00
output_value=0xFF00

return_flag = modbus_obj.write_single_coil(slave_addr, output_address, output_value)
output_flag = 'Success' if return_flag else 'Failure'
print('Writing single coil status: ' + output_flag)
```

### Write Single Register

This command is used to write the contents of an analog output holding register on a remote device. The slave address, the register address, the register value, and the signature of the data must be specified. As for all the other commands, the register addresses start from 0.

```python
slave_addr=0x0A
register_address=0x01
register_value=-32768
signed=True

return_flag = modbus_obj.write_single_register(slave_addr, register_address, register_value, signed)
output_flag = 'Success' if return_flag else 'Failure'
print('Writing single coil status: ' + output_flag)
```

### Write Multiple Coils

This function code is used to set a continuous sequence of coils, in a remote device, to either ON or OFF. The slave address, the starting address of the coils and an array with the coil states must be specified.

```python
slave_addr=0x0A
starting_address=0x00
output_values=[1,1,1,0,0,1,1,1,0,0,1,1,1]

return_flag = modbus_obj.write_multiple_coils(slave_addr, starting_address, output_values)
output_flag = 'Success' if return_flag else 'Failure'
print('Writing multiple coil status: ' + output_flag)
```

### Write Multiple Registers

This command is used to write the contents of a continuous sequence of analogue registers on a remote device. The slave address, the starting register address, the register values, and the signature of the data must be specified. The address of the first register is 0 and a maximum of 125 register values can be written. The Python sample code is shown below.

```python
slave_addr=0x0A
register_address=0x01
register_values=[2, -4, 6, -256, 1024]
signed=True

return_flag = modbus_obj.write_multiple_registers(slave_addr, register_address, register_values, signed)
output_flag = 'Success' if return_flag else 'Failure'
print('Writing multiple register status: ' + output_flag)
```

