# ADC

This example is a simple ADC sample. For more information please see [``ADC``](../../firmwareapi/pycom/machine/ADC.md).

```python
from machine import ADC
adc = ADC(0)
adc_c = adc.channel(pin='P13')
adc_c()
adc_c.value()
```
