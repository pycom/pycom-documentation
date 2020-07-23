---
title: "NTP"
aliases:

---
Using the Network Time Protecol (NTP) we can keep track of the actual time using our device and a wireless connection. The function is built into the `rtc` and `time` libraries. There are several ways to initialise the time in an `rtc` object, which can be used inside the `time` declaration. In this example, we discuss getting the time through WiFi (though you can also use LTE), and reading it out every second. Without our intervention, the time will keep updating.
If everything went correctly, it will print a tuple containing: `(year, month, day, hour, minute, second, weekday, yearday)`
>Note: only weekday counts from 0 (Monday) to 6 (Sunday)
```python
from network import WLAN
import time
import machine

wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid="Pycom", auth=(WLAN.WPA2, "PyE!ndh0ven#")) #for the connection details, check your router.
while not wlan.isconnected():
    machine.idle()
print("connected to WiFi")
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
while not rtc.synced():
    machine.idle()
print("RTC synced with NTP time")
#adjust your local timezone, by default, NTP time will be GMT
time.timezone(2*60**2) #we are located at GMT+2, thus 2*60*60

while True:
    print(time.localtime())
    time.sleep(1)
```
