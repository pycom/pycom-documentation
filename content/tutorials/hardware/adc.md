---
title: "ADC"
aliases:
    - tutorials/all/adc.html
    - tutorials/all/adc.md
    - chapter/tutorials/all/adc
---

This example is a simple ADC sample. For more information please see [`ADC`](/firmwareapi/pycom/machine/adc).

```python
from machine import ADC
adc = ADC(0)
adc_c = adc.channel(pin='P13')
adc_c()
adc_c.value()
```

## Calibration

Currently the ESP32's ADC is not calibrated from the factory. This means it must be calibrated each time you wish to use it. To do this you must firstly measure the internal voltage reference. The following code will connect the 1.1v reference to `P22`

```python
from machine import ADC
adc = ADC()

# Output Vref of P22
adc.vref_to_pin('P22')
```

Now that the voltage reference is externally accessible you should measure it with the most accurate voltmeter you have access to. Note down the reading in millivolts, e.g. `1120`. To disconnect the 1.1v reference from `P22` please reset your module. You can now calibrate the ADC by telling it the true value of the internal reference. You should then check your calibration by connecting the ADC to a known voltage source.

```python
# Set calibration - see note above
adc.vref(1100)

# Check calibration by reading a known voltage
adc_c = adc.channel(pin='P16', attn=ADC.ATTN_11DB)
print(adc_c.voltage())
```

