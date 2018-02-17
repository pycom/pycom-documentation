# RMT
Detailed information about this class can be found in [``RMT``]().

The following example creates an RMT object on channel 4, configures it for transmission and sends some data in various forms

```py
from machine import RMT
rmt = machine.RMT(channel=4, gpio="P21", tx_idle_level=RMT.LOW)
data_1 = (1,0,1,0,1,0,1,0,1,0)                                  
duration_1 = 10000                                              
rmt.send_pulses(data_1, duration_1)   

data_2 = 165
duration_2 = (8,11,8,11,6,13,6,13) 
rmt.send_pulses(data_2, duration_2, bit_num=8) 

data_3 = (1,0,1,0,1)
duration_3 = (400,200,400,200,400) 
rmt.send_pulses(data_3, duration_3)
```

The following example creates an RMT object on channel 5, configures it for receiving, filters out pulses width width < 20*100 nano seconds, then wait for 100 pulses

```py
from machine import RMT
rmt = machine.RMT(channel=5)
rmt.init(gpio="P21", rx_idle_threshold=1000, rx_filter_threshold=20)

data = rmt.recv_pulses(100)
```

The following example creates an RMT object on channel 4, configures it for transmission with carrier modulation
```py
from machine import RMT
rmt = machine.RMT(channel=4, gpio="P21", tx_idle_level=RMT.LOW, tx_carrier = (100, 70, RMT.HIGH))
data = (1,0,1,0,1,0,1,0,1,0)                                  
duration = 10000                                              
rmt.send_pulses(data, duration)   
```