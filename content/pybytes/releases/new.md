---
title: "Create New Release"
aliases:
---

In this section, we will explain how to create a new release.


## Create release wizard

In Pybytes, go to *Applications* -> *My applications* -> *select target application* -> *Releases* Page:

1. Click on *Create Release*.
![](/gitbook/assets/pybytes/releases/create-release-step-1.png)

2. A list of pre-configured application configurations will be shown.
![](/gitbook/assets/pybytes/releases/create-release-step-2.png)

3. Select the target `firmware`, or omit this step.
![](/gitbook/assets/pybytes/releases/create-release-step-3.png)

4. If you want to include code changes in this release you can:
  * *check* _Upload the code_ `checkbox`.
  * `Browse` your target code (should be a `zip` file)
  * The `zip` file size is limited to `4MB`
![](/gitbook/assets/pybytes/releases/create-release-step-7.png)
  * Download and extend example release zip archive **[my-release.zip](/gitbook/assets/pybytes/releases/code-example/my-code.zip)** 
  * Or create a zip file with the following structure:
    ```
      my_release.zip
      ├── flash <-- updates files on the /flash partition
      │   └── main.py
      │   └── my_awesome_module.py
      │   └── ...
      └── sd <-- updates files on the MicroSD card
          └── my_another_awesome_module.py
          └── ...
    ```

5. *Write* a description for this release.
![](/gitbook/assets/pybytes/releases/create-release-step-8.png)

6. *Review* release details then *Click* Finish.
![](/gitbook/assets/pybytes/releases/create-release-step-9.png)

7. You can see a list of created releases under the `Releases` tab.
![](/gitbook/assets/pybytes/releases/create-release-step-10.png)
