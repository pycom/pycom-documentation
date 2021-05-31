---
title: "Visual Studio Code"
aliases:
    - pymakr/installation/vscode.html
    - pymakr/installation/vscode.md
    - chapter/pymakr/installation/vscode
---

Pycom supports Microsoft's Visual Studio Code IDE platform with the Pymakr Plugin. 

1. First [download and install Visual Studio Code](https://code.visualstudio.com/). 

2. You will also need NodeJS installed on your PC. Please download the latest LTS version available [from the NodeJS website.](https://nodejs.org/)

Please follow these steps to install the [Pymakr VSCode Extension](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr):

3. Ensure that you have the latest VSCode installed and open.

![](/gitbook/assets/vsc_setup_step_1-1.png)

4. Navigate to the Extensions page, using the 5th button in the left navigation

![](/gitbook/assets/vsc_setup_step_2-1.png)

5. Search for `Pymakr` and click the install button next to it.

![](/gitbook/assets/vsc_setup_step_3.png)

6. Within a few minutes, a reload button should appear. Press it to reload VSCode.

![](/gitbook/assets/vsc_setup_step_4.png)

7. That's it! You've installed the Pymakr Extension for VSCode

![](/gitbook/assets/vsc_setup_step_5.png)

## Connecting via Serial USB

After installing the Pymakr Plugin, you need to take a few seconds to configure it for first time use. Please follow these steps:

1. Connect your Pycom device to your computer via USB. 

2. Open Visual Studio Code and ensure that the Pymakr Plugin has correctly installed.

![](/gitbook/assets/vsc_config_step_1-1.png)

3. Generally, your device will be auto-detected. If this does not work, click `All commands` on the bottom of the Visual Studio Code window

![](/gitbook/assets/vsc_config_step_2-1.png)

4. In the list that appears, click `Pymakr > Extra > List Serial Ports`

![](/gitbook/assets/vsc_config_step_3-1.png)

5. This will list the available serial ports. If Pymakr is able to auto-detect which to use, this will be copied to your clipboard. If not please manually copy the correct serial port.

![](/gitbook/assets/vsc_config_step_4.png)