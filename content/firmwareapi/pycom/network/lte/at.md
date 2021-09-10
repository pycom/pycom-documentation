---
title: "AT Commands"
---

Next to using the [LTE Module](../), it is also possible to manually send AT commands to the LTE modem. Below we specify some of them in more detail

Note that you can only use AT commands when _not_ in PPP mode

```
import time
from network import LTE
lte=LTE(debug=True)
time.sleep(1)
```

### LTE modem verbosity
AT+CEREG

### Find nearby cell towers
Scan the local area for cell towers and their ID's. As the LTE modem does a live scan, we need the timeout to be large in order to get full details. 
Use argument `0` for a full scan, and `1` for a fast scan. 
```python

lte.send_at_cmd('AT+SQNINS=1', timeout=50000)
```
A proper response will be of the following format: (missing information will not be displayed)
```
<action>,<rb>,<ratINS>,<cell_Id>,<tac>,<plmn>,<earfcn>,<pci>,<bandwidth Download>, <rsrp>, <rsrq>
```

### Find the currently used band 
> Only works when the LTE modem is attached to the network

```python
band_to_earfcn = [
#   ( low, mid,high)  # band
    (-1,-1,-1), # dummy entry for index 0
    (   0, 300, 599), # 1
    ( 600, 900,1199), # 2
    (1200,1575,1949), # 3
    (1950,2175,2399), # 4
    (2400,2525,2649), # 5
    (2650,2700,2749), # 6
    (2750,3100,3449), # 7
    (3450,3625,3799), # 8
    (3800,3975,4149), # 9
    (4150,4450,4749), # 10
    (4750,4850,4949), # 11
    (5010,5090,5179), # 12
    (5180,5230,5279), # 13
    (5280,5330,5379), # 14
    (-2,-2,-2), # 15
    (-3,-3,-3), # 16
    (5730,5790,5849), # 17
    (5850,5925,5999), # 18
    (6000,6075,6149), # 19
    (6150,6300,6449), # 20
    (6450,7125,6599), # 21
]

earfcn_to_band = {}
for band in range(1, len(band_to_earfcn)):
    earfcn_to_band[band_to_earfcn[band]] = band


def find_band(earfcn, verbose=False):
    if isinstance(earfcn, str):
        earfcn = int(earfcn)
    for b in range(len(band_to_earfcn)):
        x = band_to_earfcn[b]
        if x[0] <= earfcn and x[2] >= earfcn:
            if verbose:
                print("EARFCN", earfcn, "is in range", x, "which is band", b)
            return b
    return None

def band():
    try:
        mn = lte.send_at_cmd('AT+SQNMONI=9')
        print(mn)
        # +SQNMONI: 20416 Cc:204 Nc:16 RSRP:-80.20 CINR:0.00 RSRQ:-12.90 TAC:31 Id:222 EARFCN:3700 PWR:-59.52 PAGING:64
        # +SQNMONI: NL KPN Cc:204 Nc:08 RSRP:-90.00 CINR:18.00 RSRQ:-7.70 TAC:64503 Id:176 EARFCN:6400 PWR:-74.52 PAGING:64
        # +SQNMONI: Amarisoft Network Cc:001 Nc:01 RSRP:-88.20 CINR:-1.30 RSRQ:-13.30 TAC:2 Id:1 EARFCN:6309 PWR:-67.12 PAGING:128
        return find_band(int(mn.split(':')[9].split(' ')[0]), verbose=True)
    except Exception as e:
        print(e)
```