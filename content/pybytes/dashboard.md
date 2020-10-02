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
            pybytes.send_signal(math.sin(i*math.pi))
            print('sent signal {}'.format(i))
            time.sleep(10)
    ```

2. Press *Upload* button to upload the code into your device.

>Note that if you have a Pytrack or Pysense expansion board, you could also sent sensor data instead!


## Step 2: Add a signal from your device

1. Go to the [Pybytes device](https://pybytes.pycom.io/devices) page select your device.

2. Then go to `Signals` tab and click on *define new signal*

![](/gitbook/assets/pybytes/add-device/define-signal.png)

## Step 3: Add a widget for the signal

1. Click on the *signal card* of the selected device.

![](/gitbook/assets/pybytes/add-device/send-signal.png)

2. Click on the *Create a new display* button.

![](/gitbook/assets/pybytes/dashboard/create-new-display.png)

3. Select the type of visualisation (e.g. bar chart or line graph).   

4. You can adjust the parameters of your widget at `Settings`. After, click on the button `Create`.

![](/gitbook/assets/pybytes/dashboard/confirm-graph-creation.png)

Your widget was created. Now, add your widget to your device's dashboard. Click on the button `Edit` on your widget, and mark the checkbox `Display on Dashboard` at `Settings`. Finally, click on the button `Save`.

Click on the `Dashboard` tab. Your widget was successfully added there!

![](/gitbook/assets/pybytes/dashboard/sinwave-dashboard-widget.png)

## Done!

Now you've learned how to set up your device's dashboard to display data. Also, you can add more widgets to your device's other signals.
