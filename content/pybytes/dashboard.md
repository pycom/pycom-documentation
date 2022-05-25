---
title: "Visualise data from your device"
aliases:
    - pybytes/dashboard.html
    - pybytes/dashboard.md
    - chapter/pybytes/dashboard/intro
---

In this section, we will explain how to create widgets for data visualisation and how to set up your device's dashboard on Pybytes.

> We're assuming that you have already connected your device to Pybytes. In case you haven't, check how to [add your device here](../connect/). After you're done with that, you can proceed to the next example.

## Step 1: Setup a Pymakr Project

1. Create a project in Pymakr called `Pybytes_signals`, and add the following code to `main.py`. This python application will send data every 5 seconds to Pybytes.

    ```python
    # Import what is necessary to create a thread
    import time
    import math

    # Send data continuously to Pybytes
    while True:
        for i in range(0,20):
            pybytes.send_signal(1, math.sin(i/10*math.pi))
            print('sent signal {}'.format(i))
            time.sleep(10)
    ```

2. Press the *Upload* button to upload the code into your device.
Once the code has run, you should be able to see the signal in the `Signals` tab of your device

![](/gitbook/assets/pybytes/dashboard/signal-test.png)

>Note that if you have a Pytrack or Pysense expansion board, you could also send sensor data instead!


## Step 2: Add a widget for the signal

1. Go to the device dashboard and click `Add Widget`

![](/gitbook/assets/pybytes/dashboard/add-widget.png)

2. Choose a data representation widget, for example `Line chart`

![](/gitbook/assets/pybytes/dashboard/choose-linechart.png)

3. Select the `Pin` and `Chart type` and click `Add Widget`

![](/gitbook/assets/pybytes/dashboard/widget-settings.png)

4. A new widget has been added to your Dashboard

![](/gitbook/assets/pybytes/dashboard/widget-result.png)

>Click on the `Edit` button on your widget to change the settings

## Done!

Now you've learned how to set up your device's dashboard to display data. Also, you can add more widgets to your device's other signals.
