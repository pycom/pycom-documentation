# Custom contract

For building Sigfox application on Pybytes we recommend to [buy Sigfox contract](https://buy.sigfox.com/).

With Sigfox custom contract you can use Pybytes to register Sigfox devices on Sigfox backend automatically \(Pybytes talk to Sigfox backend API to register Sigfox devices automatically\).

You can select Sigfox _device type_ associated with your Sigfox _custom contract_.

Newly created devices will be added to selected device type completely by Pybytes.

## Adding devices using Sigfox custom contract

Go to: Settings \(in sidebar\) → Sigfox API → Settings

and select Sigfox device type which is associated with Sigfox custom contract.

![](../../../.gitbook/assets/selectdevicetypecustomcontract.png)

### Add your Sigfox device to Pybytes

1. Create Sigfox device \(Lopy4, SiPy, FiPy\) in Pybytes and copy its device token to clipboard.
2. Connect your device to your computer and update it with Pycom firmware updater.
   1. Select Pybytes firmware
   2. Paste your device token to firmware updater

{% hint style="info" %}
Detailed steps which are same for all devices are [**described here**](../quick.md).
{% endhint %}

After your device was flashed with Pybytes firmware in automatically start adding itself to Sigfox backend.

![](../../../.gitbook/assets/sigfoxcustomcontractstatus%20%281%29.png)

## Troubleshooting

[Disengage Sigfox sequence number](../../../tutorials/sigfox.md#disengage-sequence-number)

