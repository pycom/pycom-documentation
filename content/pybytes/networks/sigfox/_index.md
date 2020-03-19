---
title: "Add Sigfox device"
aliases:
---

{{% hint style="danger" %}}
Before you start you need to create Sigfox account. You need Pycom device with Sigfox to get your Sigfox account. [**Follow these instructions**](/gettingstarted/registration/sigfox).
{{% /hint %}}

## Create Sigfox API credentials

Once you have your account set up and are logged into [Sigfox backend](https://backend.sigfox.com), you need to create API credentials for Pybytes.

Click on GROUP → &lt;your\_company\_name&gt; → API ACCESS → New

![](/gitbook/assets/pybytes/sigfox/apiaccess.png)

In the form chose a _Name_, e.g., _pybytes_. Then select the _Profile_ `LIMITED_ADMIN` and click on Ok.

![](/gitbook/assets/pybytes/sigfox/apiaccessscope.png)

From here you copy _Login_ and _Password_ 

![](/gitbook/assets/pybytes/sigfox/apiaccesskeys.png)

and paste them in Pybytes Settings → [Sigfox API](https://pybytes.pycom.io/settings/sigfox-credentials).

![](/gitbook/assets/pybytes/sigfox/pybytessigfoxcredentials.png)

Now Pybytes will confirm that the Sigfox integration has been activated.

## Sigfox contract types

### Sigfox DevKit contracts

Read more how to use Sigfox with [devKit contract](devkit).

### Sigfox custom contracts

Read more how to use Sigfox with [Custom contract](custom).
