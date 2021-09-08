---
title: "Reading Battery Voltage"
---

Each shield allows you to read the battery voltage, though in a slightly different way. Below we explain how to measure the battery voltage for each shield.
## Expansionboard 2
```python
from machine import ADC
adc = ADC()
bat_voltage = adc.channel(attn=ADC.ATTN_11DB, pin='P16')
vbat = bat_voltage.voltage()
# note that the expansionboard 2.0 has a voltage divider of 115K / 56K to account for

# 115K / 56K, ratio =~ 1:3
print('battery voltage:', vbat*3, 'mV')
```

## Expansionboard 3.0 / 3.1

The Expansionboard has an on-board voltage monitor connected through a voltage divider to an ADC pin, allowing you to read the voltage. You can use the example below. Note that, depending on the revision of expansionboard you own, the dividing ratio of the voltag divider varies. Note that the battery voltage will be close to 5V when you ahve a USB cable connected.

```python
from machine import ADC
adc = ADC()
bat_voltage = adc.channel(attn=ADC.ATTN_11DB, pin='P16')
vbat = bat_voltage.voltage()
# note that the expansionboard 3 has a voltage divider of 1M / 1M to account for
# 1M / 1M, ratio = 1:2
print('battery voltage:', vbat*2, 'mV')
```

## Pysense / Pytrack / Pyscan

The first and second generation of Pysense, Pytrack and Pyscan shields do not directly connect the battery voltage to the module. Instead, they use the ADC of the coprocessor to read the battery voltage, saving an additional IO pin. You can use the following example. Note that the battery voltage will be close to 5V when you have a USB cable connected.
```python

# first generation
# from pycoproc_1 import Pycoproc
# py = Pycoproc(Pycoproc.PYSENSE)

# second generation
from pycoproc_2 import Pycoproc
py = Pycoproc()

print(py.read_battery_voltage())
```

## Pygate

The Pygate has a voltage divider of 100K / 100K on board, with the battery connected to P13. Note that the battery voltage will be close to 5V when you have a USB cable connected.

```python
from machine import ADC
adc = ADC()
bat_voltage = adc.channel(attn=ADC.ATTN_11DB, pin='P13')
vbat = bat_voltage.voltage()
# note that the Pygate has a voltage divider of 100K / 100K to account for
# 100K / 100K ratio = 1:2
print('battery voltage:', vbat*2, 'mV')
```
