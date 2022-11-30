---
title: "PyNode+ Air Examples"
aliases:
    - tutorials/pynode/PyNodeAir.html
    - tutorials/pynode/pynodeair.md
    - chapter/tutorials/pynode/PyNodeAir
---

You can use the following code to query the PyNode+ Air sensor from MicroPython

```python
from network import Bluetooth
import time
import ubinascii

bt = Bluetooth()
bt.start_scan(-1)


def is_pynode_air(read_adv):
    uuid = ubinascii.hexlify(read_adv[4:20])
    return uuid.decode().startswith("50794e6f646553315631")


def get_pynode_data(read_adv):
    return {
        "temperature": float(
            -45 + 175 * int(ubinascii.hexlify(read_adv[20:22]), 16) / 65536
        ),
        "humidity": float(
            100 * int(ubinascii.hexlify(read_adv[22:24]), 16) / 65536
        ),
    }


print("Starting pynode air sensor")
while True:
    adv = bt.get_adv()
    if adv:
        read_adv = bt.resolve_adv_data(
            adv.data, Bluetooth.ADV_MANUFACTURER_DATA
        )
        if read_adv:
            manuf_data = ubinascii.hexlify(read_adv[0:4])
            if manuf_data == b"4c000215":  # ibeacon
                if is_pynode_air(read_adv):
                    data = get_pynode_data(read_adv)
                    print(data)
                    time.sleep(10)
    else:
        time.sleep(0.050)

```


The below code can be used to modify the sleep duration.

```python
import time
import ubinascii
import struct

def get_adv_int(arg):
    time_msec = {
         100: b'\x01', # 100ms
         200: b'\x02', # 200ms
         500: b'\x05', # 500ms
        1000: b'\x10' # 1000ms
    }
    return time_msec.get(arg, b'\x00') # default is 1000ms

def get_adv_dur(arg):
    time_sec = {
         1: b'\x01', # 1 hour
         2: b'\x02', # 3 hours
         3: b'\x03', # 6 hours
         4: b'\x04', # 11 hours (max)
         5: b'\x05' # 10 secs
    }
    return time_sec.get(arg, b'\x00') # default is 10 secs

def get_sleep_dur(arg):
    time_sec = {
        10: b'\xFF', # 10 secs
         3: b'\x03', # 3 secs
        20: b'\x20', # 20 secs
        30: b'\x30', # 30 secs
        11: b'\x11', # 1 hour
        33: b'\x33', # 3 hours
        66: b'\x66', # 6 hours
        1111: b'\xBB' # 11 hours (max)
    }
    return time_sec.get(arg, b'\x00') # default is 5 secs

def change_adv(adv_int, adv_dur, sleep_dur):
    from network import Bluetooth
    bt = Bluetooth()
    bt.start_scan(10)
    last_time = time.time()
    print("scanning |", end="")
    while (time.time()-last_time)<10:
        print("\b\\", end="")
        time.sleep(0.050)
        print("\b-", end="")
        time.sleep(0.050)
        print("\b|", end="")
        time.sleep(0.050)
        print("\b/", end="")
        time.sleep(0.050)
        adv = bt.get_adv()
        if adv and bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL) == 'PyNode Air':
            try:
                conn = bt.connect(adv.mac)
                services = conn.services()
                for service in services:
                    u = service.uuid()
                    time.sleep(0.50)
                    if isinstance(u, int):
                        pass
                    else:
                        if ubinascii.hexlify(u) == b'595a08e4862a9e8fe911bc7c7c464218':
                            chars = service.characteristics()
                            for char in chars:
                                c_uuid = char.uuid()
                                descriptor = char.read_descriptor(0x2901)
                                print("")
                                print(descriptor.decode('utf-8'),end=" ")
                                c_hex = ubinascii.hexlify(c_uuid)
                                if c_hex == b'23ee8d0ce1f04a0cb325dc536a68862d': # sleep duration
                                    print("is changed to:", sleep_dur,"sec")
                                    value = get_sleep_dur(sleep_dur)
                                    char.write(value)
                                elif c_hex == b'25ee8d0ce1f04a0cb325dc536a68862d': # advertising duration
                                    print("is changed to:", adv_dur,"sec")
                                    value = get_adv_dur(adv_dur)
                                    char.write(value)
                                elif c_hex == b'22ee8d0ce1f04a0cb325dc536a68862d': # advertising interval
                                    print("is changed to:", adv_int,"ms")
                                    value = get_adv_int(adv_int)
                                    char.write(value)
                                else:
                                    print(" ")
                conn.disconnect()
                break
            except Exception as e:
                print(e)
                if conn:
                    conn.disconnect()
                bt.deinit()
                print("Error while connecting or reading from the BLE device")
                break
        else:
            time.sleep(0.050)
```
