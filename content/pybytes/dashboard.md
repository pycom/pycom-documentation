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

1. Create a project in Pymakr called `Pybytes_signals`, and add the following code to `main.py`. This python application will send data from the array every 5 seconds to Pybytes.

    ```python
    # Import what is necessary to create a thread
    import _thread
    from time import sleep

    # Increment index used to scan each point from vector sensors_data
    def inc(index, vector):
        if index < len(vector)-1:
            return index+1
        else:
            return 0

    # Define your thread's behaviour, here it's a loop sending sensors data every 5 seconds
    def send_env_data():
        idx = 0
        sensors_data = [0, -0.2, -0.5, -0.7, -0.8, -0.9, -0.9, -0.9, -0.8, -0.6, -0.4, -0.2, 0, 0.3, 0.5, 0.7, 0.8, 0.9, 0.9, 0.9, 0.8, 0.6, 0.4, 0.1]

        while True:
            # send one element from array `sensors_data` as signal 1
            pybytes.send_signal(1, sensors_data[idx])
            print('sent {} to Pybytes'.format(sensors_data[idx]))
            idx = inc(idx, sensors_data)
            sleep(5)

    # Start your thread
    _thread.start_new_thread(send_env_data, ())
    ```

2. Press *Upload* button to upload the code into your device.

3. After the upload is done, the device will reboot and start sending data to Pybytes. In the Pymakr terminal, you should see messages send to Pybytes.
![](/gitbook/assets/pybytes/dashboard/device-send-messages.png)

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
