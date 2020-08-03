---
title: "Differential OTA Update"
aliases:
    - updatefirmwate/diff_ota.html
    - updatefirmwate/diff_ota.md
    - chapter/updatefirmwate/diff_ota

---
> Note: You can only perform the differential updates if your current firmware version supports this feature. The target can be any version (above 1.20).
In case of a differential update, you download a diff/patch file instead of a complete binary. This can save a considerable amount of bandwidth while downloading the firmware. The exact size of the patch file depends on the source and the target versions and it will usually be minimum when upgrading to successive versions.

To perform a differential firmware update Over The Air (OTA), you will need the following tools and files:
* [bsdiff](/gitbook/assets/DiffCreator.tar.gz)
* Old firmware version archive
* New firmware version archive

> It is also possible to do an OTA differential firmware update using [**OTA Method A**](../ota). 

1. After extracting the contents of the `bsdiff` archive, navigate to the directory with the terminal and type `make` to build the utility. 
2. After building you can run the following command in the terminal to generate the patch file:
    ```bash
    ./diff_creator source.bin target.bin patch.bin
    ```
    * `source.bin` is the current binary of your device, 
    * `target.bin' is the target binary
    * `patch.bin` is the name of the patch file that you want to be generated.
    > Note: replace the `.bin` filenames with the actual filenames.
3. Now, download the `patch.bin` file to the device using [...] . Note that this file is considerably smaller than the `target.bin` file. 

    ```
    Differential Update Image detected. The device will restart to apply the patch.
    ```

4. Afterwards, the device will reset and apply the patch.
    ```
    Patching the binary...
    Patching SUCCESSFUL.
    ```
5. After patching is done, the device will restart again and this time the updated firmware will be loaded.

