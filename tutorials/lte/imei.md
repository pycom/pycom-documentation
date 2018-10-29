# Module IMEI

In order to retrieve the IMEI of your cellular enabled Pycom module you will firstly need to make sure you are on firmware version `1.17.0.b1` or higher. You can check your firmware version by running the following code on you device via the interactive REPL.

```python
>>> import os
>>> os.uname()
(sysname='GPy', nodename='GPy', release='1.17.0.b1', version='v1.8.6-849-d0dc708 on 2018-02-27', machine='GPy with ESP32')
```

Once you have a compatible firmware, you can run the following code to get your modules IMEI number:

```python
from network import LTE
lte = LTE()
lte.send_at_cmd('AT+CGSN=1')
```

You’ll get a return string like this `\r\n+CGSN: "354347xxxxxxxxx"\r\n\r\nOK`. The value between the double quotes is your IMEI.

