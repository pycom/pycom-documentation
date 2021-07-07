---
title: "Current Consumption"
---
On this page we cover the current consumption of several operation modes of the development modules in combination with several shields. All measurements were done with no hardware modifications or additions, and on the latest firmware at the time of writing. The values are indicative, but by no means a guarentee and your mileage may vary, depending on the operation settings like duty cycle and tx power settings. The examples used for various measurements are listed at the bottom. 

> Firmware **Pybytes 1.20.2.r4**
```python
insert the 'on-boot' settings
```
## Measurement results

### Expansionboard 3.1
All tests were done using a Fipy v1.2 on an Expansionboard 3.1 with all jumpers removed 

|  Mode  | Current consumption | 
| ------ | ------------ |
|  Idle  |  32 mA         |
|  WiFi  |              |
|  LoRa  |              |
|  LTE   |              |
| Sleep  |              |
| Deepsleep |    22 uA     |
| No module |    |

### Pytrack 2.0 X

|  Mode  | Current consumption | 
| ------ | ------------ |
|  Idle  |               |
|  disable sensor power  |              |
|  pysleep accelerometer wake  |              |
|  pysleep timer wake |     |
| No module |       |

### Pysense 2.0 X


|  Mode  | Current consumption | 
| ------ | ------------ |
|  Idle  |               |
|  disable sensor power  |              |
|  pysleep accelerometer wake  |              |
|  pysleep timer wake |     |
| No module |    |

## Examples used for measurements:
* [WiFi](/link/to/example)