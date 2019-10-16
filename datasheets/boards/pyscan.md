# Pyscan

![](../../.gitbook/assets/pyscan-new%20%281%29.png)

## Pyscan Libraries

* Pyscan libraries to use the RFID/NFC reader are located [here](https://github.com/pycom/pycom-libraries/tree/master/pyscan)
* The accelerometer library is [here](https://github.com/pycom/pycom-libraries/blob/master/pytrack/lib/LIS2HH12.py)

{% hint style="info" %}
For the time being, we recommend uploading the `MFRC630.mpy` file via FTP due to current Pymakr limitations that will be fixed shortly.
{% endhint %}

Libraries for the rest of the components will be added soon.

## Pyscan components:

* **Accelerometer**: ST LIS2HH12
* **Ambient light sensor**: Lite-on LTR-329ALS-01
* **RFID/NFC reader**: NXP MFRC63002HN, 151

## Driver

The Windows 7 driver for Pyscan is located [here](../../pytrackpysense/installation/firmware.md).

For other Operating Systems, no driver is required. 

## Pinout

The pinout of the Pyscan is available as a PDF File

{% file src="../../.gitbook/assets/pyscan-pinout.pdf" caption="Pyscan Pinout" %}

![](../../.gitbook/assets/pyscan-pinout-1.png)

## Battery Charger

The board features a single cell Li-Ion/Li-Po charger. When the board is being powered via the micro USB connector, it will charge the battery \(if connected\).

## Specsheets

The specsheet of the Pyscan is available as a PDF File.

{% file src="../../.gitbook/assets/pyscan-specsheet.pdf" caption="Pyscan Datasheet" %}
