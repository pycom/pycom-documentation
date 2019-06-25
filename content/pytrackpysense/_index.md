---
title: ""
aliases:
---

In addition to the Expansion Board, Pycom also offers three additional sensor boards, which are ideal for quickly building a fully functioning IoT solution! Whether the application is environment sensing or asset tracking, these additional boards support a variety of sensors.

## Pytrack

Pytrack is a location enabled version of the Expansion Board, intended for use in GPS applications such as asset tracking or monitoring.

![](/gitbook/assets/pytrack%20%281%29.png)

### Features & Hardware

The Pytrack is has a number of features including GPS, 3-Axis Accelerometer and Battery Charger. See the list below for detailed specifics about each sensor, including datasheets.

* Serial USB
* 3-Axis Accelerometer ([LIS2HH12](apireference/pytrack.md#3-axis-accelerometer-lis-2-hh-12))
* Battery Charger (BQ24040 with JST connector)
* GPS and GLONASS ([L76-L](apireference/pytrack.md#gps-with-glonass-quectel-l-76-l-gnss))
* MicroSD Card Reader

All of the included sensors are connected to the Pycom device via the I2C interface. These pins are located at `P22` (SDA) and `P21` (SCL).

You can find the datasheet and more info here:

{{% refname "../datasheets/boards/pytrack.md" %}}

## Pysense

Pysense is a sensor packed version of the Expansion Board, intended for use in environment sensing applications such as temperature, humidity monitoring, and light sensing.

![](/gitbook/assets/pysense%20%281%29.png)

### Features & Hardware

The Pysense is packed with a number of sensors and hardware, see the list below for detailed specifics about each sensor, including datasheets.

* Serial USB
* 3-Axis Accelerometer ([LIS2HH12](apireference/pysense.md#3-axis-accelerometer-lis-2-hh-12))
* Battery Charger (BQ24040 with JST connector)
* Digital Ambient Light Sensor ([LTR-329ALS-01](apireference/pysense.md#digital-ambient-light-sensor-ltr-329-als-01))
* Humidity and Temperature Sensor ([SI7006-A20](apireference/pysense.md#humidity-and-temperature-sensor-si-7006-a20))
* Barometric Pressure Sensor with Altimeter ([MPL3115A2](apireference/pysense.md#barometric-pressure-sensor-with-altimeter-mpl-3115-a2))
* MicroSD Card Reader

All of the included sensors are connected to the Pycom device via the I2C interface. These pins are located at `GPI09` (SDA) and `GPI08` (SCL).

You can find the datasheet and more info here:

{{% refname "../datasheets/boards/pysense.md" %}}

## Pyscan

Pyscan is a RFID-NFC enabled version of the Expansion Board, intended for use in scanning applications, such as RFID/NFC readers.

![](/gitbook/assets/pyscan-new%20%281%29.png)

### Features & Hardware

The Pyscan is packed with a number of sensors and hardware, see the list below for detailed specifics about each sensor, including datasheets.

* 3-Axis Accelerometer ([LIS2HH12](apireference/pyscan.md#3-axis-accelerometer-lis-2-hh-12))
* Digital Ambient Light Sensor ([LTR-329ALS-01](apireference/pyscan.md#digital-ambient-light-sensor-ltr-329-als-01))
* RFID-NFC Chip ([MFRC63002HN](apireference/pyscan.md#pyscan-nfc-library-mfrc-6300))
* Serial USB
* Battery Charger (BQ24040 with JST connector)
* MicroSD Card Reader
* Ultra low power operation (~1uA in deep sleep)

All of the included sensors are connected to the Pycom device via the I2C interface. These pins are located at `P22` (SDA) and `P21` (SCL).

You can find the datasheet and more info here:

{{% refname "../datasheets/boards/pyscan.md" %}}

