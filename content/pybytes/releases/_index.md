---
title: "Create New Release"
aliases:
---

In this section, we will explain to you how to create a new release.


## Create release wizard

In Pybytes, go to *Applications* -> *My applications* -> *select target application* -> *Releases* Page:

1. Click on *Create Release*.
![](/gitbook/assets/pybytes/releases/create-release-step-1.png)

2. List of pre-configured application configurations will be listed.
![](/gitbook/assets/pybytes/releases/create-release-step-2.png)

3. Select the target `firmware`, or omit this step.
![](/gitbook/assets/pybytes/releases/create-release-step-3.png)

4. If you want to include code changes in this release you can:
  * *check* _Upload the code_ `checkbox`.
  * `Browse` your target code (should be a `zip` file)
  * The `zip` file size is limited to `4MB`
![](/gitbook/assets/pybytes/releases/create-release-step-7.png)
  * if you need to update files on the device you should have the below structure.
  * `zip` file structure:
      - root
        - flash
          - main.py
          - .....
          - xyz.py

5. *Write* a description for this release.
![](/gitbook/assets/pybytes/releases/create-release-step-8.png)

6. *Review* release details then *Click* Finish.
![](/gitbook/assets/pybytes/releases/create-release-step-9.png)

7. You can see list of created releases under the `Releases` tab.
![](/gitbook/assets/pybytes/releases/create-release-step-10.png)
