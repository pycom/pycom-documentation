---
search:
  keywords:
    - ADC
    - Analog
    - ADCChannel
---

# ADC

## class ADC – Analog to Digital Conversion

### Quick Usage Example

```python
import machine

adc = machine.ADC()             # create an ADC object
apin = adc.channel(pin='P16')   # create an analog pin on P16
val = apin()                    # read an analog value
```

### Constructors

#### class machine.ADC\(id=0\)

Create an ADC object; associate a channel with a pin. For more info check the hardware section.

### Methods

#### adc.init\( \* , bits=12\)

Enable the ADC block. This method is automatically called on object creation.

* `Bits` can take values between 9 and 12 and selects the number of bits of resolution of the ADC block.

#### adc.deinit\(\)

Disable the ADC block.

#### adc.channel\(\* , pin, attn=ADC.ATTN\_0DB\)

Create an analog pin.

* `pin` is a keyword-only string argument. Valid pins are `P13` to `P20`.
* `attn` is the attenuation level. The supported values are: `ADC.ATTN_0DB`, `ADC.ATTN_2_5DB`, `ADC.ATTN_6DB`, `ADC.ATTN_11DB`

Returns an instance of `ADCChannel`. Example:

```python
# enable an ADC channel on P16
apin = adc.channel(pin='P16')
```

#### adc.vref\(vref\)

If called without any arguments, this function returns the current calibrated voltage \(in millivolts\) of the `1.1v` reference. Otherwise it will update the calibrated value \(in millivolts\) of the internal `1.1v` reference.

#### adc.vref\_to\_pin\(pin\)

Connects the internal `1.1v` to external `GPIO`. It can only be connected to `P22`, `P21` or `P6`. It is recommended to only use `P6` on the WiPy, on other modules this pin is connected to the radio.

### Constants

* ADC channel attenuation values: `ADC.ATTN_0DB`, `ADC.ATTN_2_5DB`, `ADC.ATTN_6DB`, `ADC.ATTN_11DB`

## class ADCChannel

Read analog values from internal/external sources. ADC channels can be connected to internal points of the `MCU` or to `GPIO` pins. ADC channels are created using the `ADC.channel` method.

### Methods

#### adcchannel\(\)

Fast method to read the channel value.

#### adcchannel.value\(\)

Read the channel value.

#### adcchannel.init\(\)

\(Re\)init and enable the ADC channel. This method is automatically called on object creation.

#### adcchannel.deinit\(\)

Disable the ADC channel.

#### adcchannel.voltage\(\)

Reads the channels value and converts it into a voltage \(in millivolts\)

#### adcchannel.value\_to\_voltage\(value\)

Converts the provided value into a voltage \(in millivolts\) in the same way voltage does.

{% hint style="danger" %}
ADC pin input range is `0-1.1V`. This maximum value can be increased up to `3.3V` using the highest attenuation of `11dB`. **Do not exceed the maximum of 3.3V**, to avoid damaging the device.
{% endhint %}

