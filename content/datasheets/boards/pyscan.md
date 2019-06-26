---
title: "Pyscan"
aliases:
    - datasheets/boards/pyscan.html
    - datasheets/boards/pyscan.md
    - product-info/boards/pyscan
    - chapter/datasheets/boards/pyscan
---

![](/gitbook/assets/assets-lil0igdl11z7jos_jpx-lkn7scqkkkb6tqb3uyo-lkn83hfia61dsuyojco-pyscan-new.png)

## Datasheet

The datasheet of the Pyscan is available as a PDF File.

<a href="/gitbook/assets/pyscan-specsheet.pdf" target="_blank"> Pyscan Datasheet </a>

## Pyscan Libraries

* Pyscan libraries to use the RFID/NFC reader are located [here](https://github.com/pycom/pycom-libraries/tree/master/pyscan)
* The accelerometer library is [here](https://github.com/pycom/pycom-libraries/blob/master/pytrack/lib/LIS2HH12.py)

{{% hint style="info" %}}
For the time being, we recommend to upload the `MFRC630.mpy` file via FTP due to current limitations of Pymakr that will be fixed shortly.
{{< /hint >}}

Libraries for the rest of the components will be added soon.

## Pyscan components:

* **Accelerometer**: ST LIS2HH12
* **Ambient light sensor**: Lite-on LTR-329ALS-01
* **RFID/NFC reader**: NXP MFRC63002HN, 151

## Driver

The Windows 7 driver for Pyscan is located [here](/pytrackpysense/installation/firmware).

For other Operating Systems there's no driver required.

## Pinout

The pinout of the Pyscan is available as a PDF File

<a href="/gitbook/assets/pyscan-pinout.pdf" target="_blank"> Pyscan Pinout </a>

![](/gitbook/assets/pyscan-pinout-1.png)

## Battery Charger

The board features a single cell Li-Ion/Li-Po charger. When the board is being powered via the micro USB connector, it will charge the battery (if connected).




## Mechanical Dimensionsde
![](/gitbook/assets/pyscan_V0.7_20180416_MecahnicalDimensions.png)

## 3D model for case design

* Please see the <a href="/gitbook/assets/PyScan_v0.7.step" target="_blank"> 3D model </a> (step format)
