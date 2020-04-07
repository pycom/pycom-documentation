---
title: "Add Sigfox device"
aliases:
---

{{% hint style="danger" %}}
Before you start you need to create Sigfox account. You need Pycom device with Sigfox to get your Sigfox account. [**Follow these instructions**](/gettingstarted/registration/sigfox).
{{% /hint %}}

## Create Sigfox API credentials

Once you have you account setup and are logged in Sigfox backend, you need to create API credentials for Pybytes.

Click on GROUP → &lt;your\_company\_name&gt; → API ACCESS → New

![](/gitbook/assets/pybytes/sigfox/apiaccess.png)

In the form chose arbitrary _name_, select `LIMITED_ADMIN` and Profile and click on Ok.

![](/gitbook/assets/pybytes/sigfox/apiaccessscope.png)

Copy _Login_ and _Password_ to the clipboard.

![](/gitbook/assets/pybytes/sigfox/apiaccesskeys.png)

In Pybytes go to Settings → Sigfox API or [follow this link](https://pybytes.pycom.io/settings/sigfox-credentials) then paste in the form.

![](/gitbook/assets/pybytes/sigfox/pybytessigfoxcredentials.png)

## Sigfox contract types

### Sigfox DevKit contracts

Read more how to use Sigfox with [devKit contract](devkit).

### Sigfox custom contracts

Read more how to use Sigfox with [Custom contract](devkit).
