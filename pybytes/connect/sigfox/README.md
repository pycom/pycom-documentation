# Add Sigfox device

{% hint style="danger" %}
Before you start you need to create Sigfox account. You need Pycom device with Sigfox to get your Sigfox account. [**Follow these instructions**](../../../gettingstarted/registration/sigfox.md).
{% endhint %}

## Create Sigfox API credentials

Once you have you account setup and are logged in Sigfox backend, you need to create API credentials for Pybytes.

Click on GROUP → &lt;your\_company\_name&gt; → API ACCESS → New

![](../../../.gitbook/assets/apiaccess%20%281%29.png)

In the form chose arbitrary _name_, select Profiles `DEVICE MANAGER [R]` and `DEVICE MANAGER [W]`. Then click on Ok.

![](../../../.gitbook/assets/apiaccessscope.png)

Copy _Login_ and _Password_ to the clipboard.

![](../../../.gitbook/assets/apiaccesskeys.png)

In Pybytes go to Settings → Sigfox API or [follow this link](https://pybytes.pycom.io/settings/sigfox-credentials) then paste in the form.

![](../../../.gitbook/assets/pybytessigfoxcredentials.png)

## Sigfox contract types

### Sigfox DevKit contracts

Read more how to use Sigfox with [devKit contract](devkit.md).

{% page-ref page="devkit.md" %}

### Sigfox custom contracts

Read more how to use Sigfox with [Custom contract](devkit.md).

{% page-ref page="custom.md" %}

