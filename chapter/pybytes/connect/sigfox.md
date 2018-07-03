# Add Sigfox device

{% hint style='danger' %}
Before you start you need to register your Sigfox account at **[Sigfox backend](../../gettingstarted/registration/sigfox.md)**.
You need Pycom device with Sigfox connectivity to get your Sigfox account.
{% endhint %}

## Create Sigfox API credentials

Once you have you account setup and are logged in Sigfox backend, you need to create API credentials for Pybytes.

Click on GROUP &rarr; `<YOUR COMPANY NAME>` &rarr; API ACCESS &rarr; New

<p align="center"><img src ="../../../img/pybytes/sigfox/apiAccess.png"></p>

In the form chose arbitrary *name*, select Profiles `DEVICE MANAGER [R]` and `DEVICE MANAGER [W]`.
Then click on Ok.

<p align="center"><img src ="../../../img/pybytes/sigfox/apiAccessScope.png"></p>

Copy *Login* and *Password* to the clipboard.

<p align="center"><img src ="../../../img/pybytes/sigfox/apiAccessKeys.png"></p>

Paste *Login* and *Password* to the Pybytes Sigfox credentials page.

<p align="center"><img src ="../../../img/pybytes/sigfox/pybytesSigfoxCredentials.png"></p>

## Add Sigfox device in Pybytes

1. Create Sigfox device (Lopy4, SiPy, FiPy) in Pybytes
2. Activate device with the firmware updater.

{% hint style='info' %}
Detailed steps which are same for all devices are described **[here](./quick.md)**.
{% endhint %}

