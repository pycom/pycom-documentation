---
title: "Sigfox"
aliases:
    - gettingstarted/registration/sigfox.html
    - gettingstarted/registration/sigfox.md
    - chapter/gettingstarted/registration/sigfox
---

Before you start, update your device to the latest firmware. Select _stable_ firmware in Firmware updater. After firmware update is done, _Sigfox ID_ and _Sigfox PAC_ were assigned to your device.

Copy _Sigfox ID_ and _Sigfox PAC_ from the last screen of firmware updater.

![](/gitbook/assets/fwupdater.png)

{{% hint style="danger" %}}
_Sigfox ID_ and _Sigfox Pac_ are assigned to your device just once during the first firmware update process. They will not change after successive firmware updates.
Sigfox Pac is one-time activation code, which will be invalidated after device's registration on Sigfox Backend.
Keep in mind that firmware updater will always display the same (even invalid) Sigfox Pac.
In case of successive registration to a new account (or device type) on Sigfox Backend, you need to get Sigfox Pac from device page on Sigfox Backend.
See [Sigfox documentation](https://support.sigfox.com/docs/device-idpac-couple) for more info.
{{< /hint >}}

After first firmware update you can also get your _Sigfox ID_ and _Sigfox PAC_ through a couple of commands via the REPL.

```python

from network import Sigfox
import binascii

# initalise Sigfox for RCZ1 (You may need a different RCZ Region)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# print Sigfox Device ID
print(binascii.hexlify(sigfox.id()))

# print Sigfox PAC number
print(binascii.hexlify(sigfox.pac()))
```

## Creating account at Sigfox backend

You need to register to the Sigfox Backend. Navigate to [https://backend.sigfox.com/activate](https://backend.sigfox.com/activate)

![](/gitbook/assets/sigfoxactivate%20%281%29.png)

Find the specific country country where the device will be activated. Enter the device's _Sigfox ID_ and _Sigfox PAC_.

You should see green microchip if you entered correct _Sigfox ID_ and _Sigfox PAC_

![](/gitbook/assets/sigfoxidpac.png)

Then provide the required information including email address and complete registration.

{{% hint style="info" %}}
When registering your other devices (not your first device), you already have created Sigfox Account before. Be sure you are login with your Sigfox account. In that way all of your devices will be added to same Sigfox Account.
{{< /hint >}}

![](/gitbook/assets/sigfoxregistrationform.png)

After registration, you will receive confirmation email with _password_ to Sigfox backend [https://backend.sigfox.com/auth/login](https://backend.sigfox.com/auth/login)

Use your email and password to login to Sigfox backend.

![](/gitbook/assets/sigfoxbackend.png)

If you enter correct credentials then you should be able to login to Sigfox backend.

## Transferring your device to new Sigfox account

You may want to transfer your devices to new Sigfox account.

Once you register your device on Sigfox backend, then your Sigfox PAC was used, and is not valid anymore. You need to get new Sigfox PAC. We don't update Sigfox PAC assigned to your device (which can be seen on last page of Firmware updater or read from device).

To get new Sigfox PAC navigate to your device on Sigfox backend. On _device_ click on Sigfox Id of device you want to transfer.

![](/gitbook/assets/sigfoxtableid%20%281%29.png)

Now you can see your new Sigfox PAC.

![](/gitbook/assets/newsigfoxpac%20%281%29.png)

Once you know your new Sigfox PAC go to [https://backend.sigfox.com/activate](https://backend.sigfox.com/activate) and register device with different account.
