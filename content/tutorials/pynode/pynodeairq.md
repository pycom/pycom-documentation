---
title: "PyNode+ Air Quality Examples"
aliases:
    - tutorials/pynode/PyNodeAirQ.html
    - tutorials/pynode/pynodeairq.md
    - chapter/tutorials/pynode/PyNodeAirQ
---

You can use the following code to query the PyNode+ Air Quality sensor from MicroPython

```python
from network import Bluetooth
import time
import ubinascii


def score_air_quality(hum, gas_res):
    """
    calculate air quality using humidity and gas resistance
    """
    gas_reference = 250000
    hum_reference = 40
    gas_lower_limit = 5000
    gas_upper_limit = 50000
    if hum >= 38 and hum <= 42:
        hum_score = 0.25 * 100
    else:
        if hum < 38:
            hum_score = 0.25 / hum_reference * hum * 100
        else:
            hum_score = (
                (-0.25 / (100 - hum_reference) * hum) + 0.416666
            ) * 100
    if gas_reference > gas_upper_limit:
        gas_reference = gas_upper_limit
    if gas_reference < gas_lower_limit:
        gas_reference = gas_lower_limit
    gas_score = (
        0.75 / (gas_upper_limit - gas_lower_limit) * gas_reference
        - (gas_lower_limit * (0.75 / (gas_upper_limit - gas_lower_limit)))
    ) * 100
    air_quality_score = hum_score + gas_score

    air_quality_score = (100 - air_quality_score) * 5
    air_quality_info = ""
    if air_quality_score >= 301:
        air_quality_info = "Hazardous"
    elif air_quality_score >= 201 and air_quality_score <= 300:
        air_quality_info = "Very Unhealthy"
    elif air_quality_score >= 176 and air_quality_score <= 200:
        air_quality_info = "Unhealthy"
    elif air_quality_score >= 151 and air_quality_score <= 175:
        air_quality_info = "Unhealthy for Sensitive Groups"
    elif air_quality_score >= 51 and air_quality_score <= 150:
        air_quality_info = "Moderate"
    elif air_quality_score >= 00 and air_quality_score <= 50:
        air_quality_info = "Good"
    return air_quality_score, air_quality_info


def get_pynode_airq_data(uuid):
    """
    returns a dict containing values sent by a Pynode airQ sensor
    """
    humidity = int(ubinascii.hexlify(uuid[18:20]), 16) / 100
    gas_resistance = int(ubinascii.hexlify(uuid[3:7]), 16)
    air_quality_score, air_quality_info = score_air_quality(
        humidity, gas_resistance
    )
    return {
        "sensor_id": uuid[7],
        "ble_mac": ubinascii.hexlify(uuid[10:16]),
        "pressure": int(ubinascii.hexlify(uuid[8:10]), 16),
        "gas_resistance": gas_resistance,
        "temperature": int(ubinascii.hexlify(uuid[16:18]), 16) / 100,
        "humidity": humidity,
        "air_quality_score": air_quality_score,
        "air_quality_info": air_quality_info,
    }


def is_pynode_airq(uuid):
    """
    returns True if message is sent by a Pynode airQ sensor
    """
    return "".join(chr(t) for t in uuid[0:3]) == "PyN" and uuid[7] == 2


print("running pynode airq sensor")
bt = Bluetooth()
bt.start_scan(-1)

while True:
    adv = bt.get_adv()
    if adv:
        read_adv = bt.resolve_adv_data(
            adv.data, Bluetooth.ADV_MANUFACTURER_DATA
        )
        if read_adv:
            # check if this is a pycom device
            if ubinascii.hexlify(read_adv[0:4]) == b"4c000215":
                uuid = read_adv[4:24]
                if is_pynode_airq(uuid):
                    data = get_pynode_airq_data(uuid)
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
         '100ms': b'\x01', # 100ms
         '200ms': b'\x02', # 200ms
         '500ms': b'\x05', # 500ms
        '1000ms': b'\x10' # 1000ms
    }
    return time_msec.get(arg, b'\x00') # default is 1000ms

def get_adv_dur(time_value, scale):
    calc_time = bytes([0])
    if scale == 'ms':
        if time_value >= 100 and time_value < 1000:
            calc_time = bytes([(int(time_value/100))])
    elif scale == 'sec':
        if time_value >= 1 and time_value < 10:
            calc_time = bytes([(int(time_value) | 0x10)])
    elif scale == 'sec':
        if time_value >= 10 and time_value < 60:
            calc_time = bytes([(int(time_value/10) | 0x20)])
    return calc_time

def get_sleep_dur(time_value, scale):
    calc_time = bytes([0])
    if scale == 'ms':
        if time_value >= 100 and time_value < 1000:
            calc_time = bytes([(int(time_value/100))])
    elif scale == 'sec':
        if time_value >= 1 and time_value < 10:
            calc_time = bytes([(int(time_value) | 0x10)])
    elif scale == 'sec':
        if time_value >= 10 and time_value < 60:
            calc_time = bytes([(int(time_value/10) | 0x20)])
    elif scale == 'min':
        if time_value >= 1 and time_value < 6:
            calc_time = bytes([(int(time_value) | 0xA0)])
    elif scale == 'min':
        if time_value >= 10 and time_value < 60:
            calc_time = bytes([(int(time_value/10) | 0xB0)])
    elif scale == 'hour':
        if time_value >= 1 and time_value < 12:
            calc_time = bytes([(time_value | 0xC0)])
    return calc_time

def measurement_count(arg):
    count = bytes([arg])
    return count

def twoscmp(value):
    if value > 128:
        value = value - 256
    return value

def change_adv(adv_int, adv_dur, sleep_dur, meas_count):
    from network import Bluetooth
    bt = Bluetooth()
    bt.start_scan(-1)
    last_time = time.time()
    print("scanning |", end="")
    while (time.time()-last_time)<20:
        print("\b\\", end="")
        time.sleep(0.010)
        print("\b-", end="")
        time.sleep(0.010)
        print("\b|", end="")
        time.sleep(0.010)
        print("\b/", end="")
        time.sleep(0.010)
        adv = bt.get_adv()
        if adv and bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL) == 'PyNode+ Air Quality':
            print("Found!")
            try:
                print(adv.mac)
                conn = bt.connect(adv.mac)
                print(adv.mac)
                services = conn.services()
                for service in services:
                    u = service.uuid()
                    time.sleep(1)
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
                                    print("is changed to:", sleep_dur[0],sleep_dur[1])
                                    value = get_sleep_dur(sleep_dur[0], sleep_dur[1])
                                    char.write(value)
                                elif c_hex == b'25ee8d0ce1f04a0cb325dc536a68862d': # advertising duration
                                    print("is changed to:", adv_dur[0], adv_dur[1])
                                    value = get_adv_dur(adv_dur[0], adv_dur[1])
                                    char.write(value)
                                elif c_hex == b'22ee8d0ce1f04a0cb325dc536a68862d': # advertising interval
                                    print("is changed to:", adv_int)
                                    value = get_adv_int(adv_int)
                                    char.write(value)
                                elif c_hex == b'27ee8d0ce1f04a0cb325dc536a68862d': # measurement count
                                    print("is changed to:", (meas_count*5))
                                    value = measurement_count(meas_count)
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

# try 5 secs sleep
# change_adv("100ms",[1,"sec"],[1,"min"], 1)


change_adv("100ms",[200,"ms"],[100,"ms"], 255) # 01, 02, 01, 255
```
