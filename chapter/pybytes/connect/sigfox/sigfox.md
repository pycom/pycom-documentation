# Add Sigfox device

{% hint style='danger' %}
Before you start you need to create Sigfox account.
You need Pycom device with Sigfox to get your Sigfox account. **[Follow these instructions](../../../gettingstarted/registration/sigfox.md)**.
{% endhint %}

## Create Sigfox API credentials

Once you have you account setup and are logged in Sigfox backend, you need to create API credentials for Pybytes.

Click on GROUP &rarr; &lt;your_company_name&gt; &rarr; API ACCESS &rarr; New

<p align="center"><img src ="../../../../img/pybytes/sigfox/apiAccess.png"></p>

In the form chose arbitrary *name*, select Profiles `DEVICE MANAGER [R]` and `DEVICE MANAGER [W]`.
Then click on Ok.

<p align="center"><img src ="../../../../img/pybytes/sigfox/apiAccessScope.png"></p>

Copy *Login* and *Password* to the clipboard.

<p align="center"><img src ="../../../../img/pybytes/sigfox/apiAccessKeys.png"></p>

In Pybytes go to Settings &rarr; Sigfox API or [follow this link](https://pybytes.pycom.io/settings/sigfox-credentials) then paste in the form.

<p align="center"><img src ="../../../../img/pybytes/sigfox/pybytesSigfoxCredentials.png"></p>

## Sigfox contract types

### Sigfox DevKit contracts

Read more how to use Sigfox with [devKit contract](./sigfoxDevKit.md).

### Sigfox custom contracts

Read more how to use Sigfox with [Custom contract](./sigfoxDevKit.md).
