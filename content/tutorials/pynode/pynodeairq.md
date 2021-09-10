---
title: "PyNode+ Air Quality Examples"
aliases:
    - tutorials/pynode/PyNodeAirQ.html
    - tutorials/pynode/pynodeairq.md
    - chapter/tutorials/pynode/PyNodeAirQ
---

You can use the following code to query the PyNode+ AirQ sensor from MicroPython

```python
from network import Bluetooth
import time
import ubinascii
import struct
import math

bt = Bluetooth()
bt.start_scan(-1)

def twoscmp(value):
    if value > 128:
        value = value - 256
    return value

def byte_to_info(uuid):
    gas_res_d = 0
    name = uuid[0:3]
    name_text = ''.join(chr(t) for t in name)
    if name_text == "PyN":
        sensor_id = uuid[7]
        mac = ubinascii.hexlify(uuid[10:16])
        press = ubinascii.hexlify(uuid[8:10])
        press_d = int(press, 16)
        gas_res = ubinascii.hexlify(uuid[3:7])
        gas_res_d = int(gas_res, 16)
        print("{} {} BLE_MAC: {}, Pressure: {} hPa, Gas resistance: {} ohm".format(name_text, sensor_id, mac, press_d, gas_res_d), end=", ")
    return (name_text,gas_res_d)

def air_quality_score(hum, gas_res):
    gas_reference = 250000
    hum_reference = 40
    gas_lower_limit = 5000
    gas_upper_limit = 50000
    if (hum >= 38 and hum <= 42):
        hum_score = 0.25*100
    else:
        if (hum < 38):
            hum_score = 0.25/hum_reference*hum*100
        else:
            hum_score = ((-0.25/(100-hum_reference)*hum)+0.416666)*100
    if (gas_reference > gas_upper_limit):
        gas_reference = gas_upper_limit
    if (gas_reference < gas_lower_limit):
        gas_reference = gas_lower_limit
    gas_score = (0.75/(gas_upper_limit-gas_lower_limit)*gas_reference -(gas_lower_limit*(0.75/(gas_upper_limit-gas_lower_limit))))*100
    air_quality_score = hum_score + gas_score

    print("IAQ score:", air_quality_score)

    print("Air quality is", end=" ")
    air_quality_score = (100-air_quality_score)*5
    if (air_quality_score >= 301):
        print("Hazardous")
    elif (air_quality_score >= 201 and air_quality_score <= 300 ):
        print("Very Unhealthy")
    elif (air_quality_score >= 176 and air_quality_score <= 200 ):
        print("Unhealthy")
    elif (air_quality_score >= 151 and air_quality_score <= 175 ):
        print("Unhealthy for Sensitive Groups")
    elif (air_quality_score >=  51 and air_quality_score <= 150 ):
        print("Moderate")
    elif (air_quality_score >=  00 and air_quality_score <=  50 ):
        print("Good")

while True:
    adv = bt.get_adv()
    if adv: # and adv.rssi>-80:# and ubinascii.hexlify(adv.mac)==b'cd9e13c0f24a':
        read_adv = bt.resolve_adv_data(adv.data, Bluetooth.ADV_MANUFACTURER_DATA)
        if read_adv==None:
            pass
        else:
            manuf = ubinascii.hexlify(read_adv)
            manuf_data = ubinascii.hexlify(read_adv[0:4])
            # print(manuf_data)
            if (manuf_data == b'4c000215') :#or (manuf_data == b'd2000215')):# company id=d2 is Dialog, b'4c000215' is Apple's id and it implies ibeacon
                # print("mac:", ubinascii.hexlify(adv.mac))
                uuid_raw = read_adv[4:20]
                uuid = ubinascii.hexlify(uuid_raw)
                name, air=byte_to_info(uuid_raw)
                if name == "PyN":
                    print("rssi:",adv.rssi)
                    major = ubinascii.hexlify(read_adv[20:22])
                    minor = ubinascii.hexlify(read_adv[22:24])
                    tx_power = ubinascii.hexlify(read_adv[24:25])
                    tx_power_real = twoscmp(int(tx_power, 16))
                    major_int = int(major, 16)
                    major_f = major_int/100 # bme688
                    minor_int = int(minor,16)
                    minor_f = minor_int/100 # bme688, it is divided by 10 initially in the dialog's firmware.
                    print("Temperature: {} C, Humidity: {} %r.H.".format(major_f, minor_f), time.time())
                    air_quality_score(minor_f, air)
                    print("")
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
