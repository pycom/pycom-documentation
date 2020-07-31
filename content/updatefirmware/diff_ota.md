---
title: "Differential OTA Update"
aliases:
    - updatefirmwate/diff_ota.html
    - updatefirmwate/diff_ota.md
    - chapter/updatefirmwate/diff_ota

---

It is also possible to do an OTA differential firmware update using [**OTA Method A**](../ota). In case of a differential update, you download a diff/patch file instead of a complete binary. This can save a considerable amount of bandwidth while downloading the firmware. The exact size of the patch file depends on the source and the target versions and it will usually be minimum when upgrading to successive versions.
The diff generation and patching is based on `bsdiff`. You can download the diff generator from [here](/gitbook/assets/DiffCreator.tar.gz).
After extracting the contents, go to the directory and do `make` to build the utility. After building you can run the following command in the terminal to generate the patch file:
```bash
./diff_creator source.bin target.bin patch.bin
```

Here the 'source.bin' is the current binary of your device, 'target.bin' is the target binary and patch.bin is the name of the patch file that you want to be generated.
The generated patch.bin file should now be downloaded to the device instead of target.bin. In the example given in `Method A`, if you are upgrading from firmware_1.0.0 to firmware_1.0.1, the patch file would be renamed as firmware_1.0.1.bin.
After the file has been downloaded, the device identify it as a patch file and you will see the following message in the REPL:
```
Differential Update Image detected. The device will restart to apply the patch.
```
After this, the device will reset and apply the patch.
```
Patching the binary...
Patching SUCCESSFUL.
```
After patching is done, the device will restart again and this time the updated firmware will be loaded.

> Note: You can only perform the differential updates if your current firmware version supports this feature. The target can be any version (above 1.20).