---
title: "Shields"
aliases:
    - tutorials/expansionboards/introduction.html
    - tutorials/expansionboards/introduction.md
    - chapter/tutorials/expansionboards
disable_breadcrumbs: true
---

>Note: Before using the Pysense, Pytrack and Pyscan boards, check the [GitHub](https://github.com/pycom/pycom-libraries) for the latest version of the libraries.

To use the Pysense, Pytrack or Pyscan, make a folder inside your project folder and call it `lib`. Then, copy the appropiate sensor libraries from the github repository to the folder. Always copy the `pysense.py` or `pytrack.py` and `pycoproc.py` files if you want to use the boards' functions. The `pycoproc.py` library also allows for a special sleep mode. An example for this is provided [here](sleep/)

* [Asset tracking](tracking/)
* [Environment sensing](sensing/)
* [Scanning RFID / NFC Tags](scanning/)
* [Wake on accelerometer](pysleep/)




>Note: Make sure to click `upload to device` to be able to `import` the appropriate libraries in your code!
