# class DAC – Digital to Analog Conversion

The DAC is used to output analog values (a specific voltage) on pin P22 or pin P21. The voltage will be between 0 and 3.3V.

### Quick Usage Example

```python
import machine

dac = machine.DAC('P22')        # create a DAC object
dac.write(0.5)                  # set output to 50%

dac_tone = machine.DAC('P21')   # create a DAC object
dac_tone.tone(1000, 0)          # set tone output to 1kHz
```

### Constructors

<class><i>class</i> class machine.DAC(pin)</class>

Create a DAC object, that will let you associate a channel with a pin. pin can be a string argument.

### Methods

<function>dac.init()</function>

Enable the DAC block. This method is automatically called on object creation.

<function>dac.deinit()</function>

Disable the DAC block.

<function>dac.write(value)</function>

Set the DC level for a DAC pin. value is a float argument, with values between 0 and 1.

<function>dac.tone(frequency, amplitude)</function>

Sets up tone signal to the specified frequency at amplitude scale. frequency can
be from 125Hz to 20kHz in steps of 122 Hz. amplitude is an integer specifying the tone amplitude to write the DAC pin. Amplitude value represents:
0 is 0dBV (~ 3Vpp at 600 Ohm load), 1 is -6dBV (~1.5 Vpp), 2 is -12dBV (~0.8 Vpp), 3 is -18dBV (~0.4 Vpp). The generated signal is a sine wave with an DC offset of VDD/2.
