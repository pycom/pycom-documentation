# class LTE
The LTE class provides access to the LTE-M/NB-IoT modem on the GPy and FiPy. LTE-M/NB-IoT are new categories of cellular protocols developed by the [3GPP](http://www.3gpp.org) and optimized for long battery life power and longer range. These are new protocols currently in the process of being deployed by mobile networks across the world. 

The GPy and FiPy support both new LTE-M protocols: 

* **Cat-M1**: also known as **LTE-M** defines a 1.4 MHz radio channel size and about 375 kbps of throughput. It is optimized for coverage and long battery life, outperforming 2G/GPRS, while being similar to previous LTE standards. 

* **Cat-NB1** also known as **NB-IoT**, defines a 200 kHz radio channel size and around 60 kbps of uplink speed. It's optimized for ultra low throughput and specifically designed for IoT devices with a very long battery life. NB-IoT shares some features with LTE such as operating in licensed spectrum, but it's a very different protocol. 

**Please note: The GPy and FiPy only support the two protocols above and are not compatible with older LTE standards.**



* [LTE Cat M1](/chapter/firmwareapi/pycom/network/lte/cat-m1.md)