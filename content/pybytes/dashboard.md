---
title: "Visualise data from your device"
aliases:
    - pybytes/dashboard.html
    - pybytes/dashboard.md
    - chapter/pybytes/dashboard/intro
---

In this section, we will explain to you how to create widgets for data visualisation and set up your device's dashboard on Pybytes.

{{% hint style="info" %}}
We assume that you already have your device connected to Pybytes. In case you haven't, check how to [add your device here](../connect/). After your done with that, you can proceed to the next example.
{{< /hint >}}

## Step 1: Set up your python application

The first step is to have your python application uploaded and running on your Pycom device.

1. Install the [Pymakr](https://atom.io/packages/pymakr) plugin.

    (We highly recommend using Pymakr with Atom, but you can also use Pymakr with [VS Code](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr)). Learn more about Pymakr [here](/pymakr).
2. In Atom create a project folder `my-first-wipy` (any other name will work as well).
4. In your project folder create the `main.py` file
3. Copy and paste the following code into your `main.py`

{{% hint style="info" %}}
Scroll a bit down to see the picture of the project structure in Atom.
{{< /hint >}}

This python application will send data from the array every 5 seconds to Pybytes.

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
        idx = inc(idx, sensors_data)
        sleep(5)

# Start your thread
_thread.start_new_thread(send_env_data, ())
```

{{% hint style="info" %}}
In this code, we're calling the function `pybytes.send_signal(signalNumber, value))` to send data to Pybytes. This function is part of the Pybytes library, and it has two arguments: `signalNumber` and `value`.

* `signalNumber` represents which signal is receiving data:

    **255** different values: **0 ... 254** (signalNumber 255 is reserved for the Pybytes terminal)
* `value` is the value being attributed to that particular signal number
{{< /hint >}}

Your example project in Atom (with Pymakr) should look like this.
Press *Upload* button to upload the code into your device.

![](/gitbook/assets/pybytes/dashboard/pymakr-with-example-code.png)

By default, Pymakr will upload all files like `*.py` from your project folder (`my-first-wipy` in this case).
File `main.py` will be uploaded to `/flash` folder on your device.

After the upload is done, the device will reboot and start sending data to Pybytes.
In the Pymakr terminal, you should see messages send to Pybytes.

![](/gitbook/assets/pybytes/dashboard/device-sending-messsages.png)

Every line stands for one message sent every 5 seconds. Line `1 [-0.7]` means signal `1` sent value `-0.7`.

## Step 2: Add a signal from your device

Go to Pybytes and on *Devices* page select your device;

![](/gitbook/assets/pybytes/dashboard/device-table.png)

Then go to `Data` tab and click on the row in the *Undefined signals* table (recommended). Alternatively, you can click on *Define new signal* button.
{{% hint style="info" %}}
If you don't see your undefined signal in *Undefined signals* table, please reload your browser.
{{< /hint >}}

![](/gitbook/assets/pybytes/dashboard/undefined-signals-table.png)

Define new signal by entering a signal name, and optionally a unit (If you clicked on "undefined signal row" your signal number `1` will be already pre-filled).

![](/gitbook/assets/pybytes/dashboard/define-new-signal.png)

Your signal was defined!

![](/gitbook/assets/pybytes/dashboard/signal-was-added.png)

{{% hint style="info" %}}
The name and unit are labels used to identify your signal inside Pybytes (In this example we defined `Sinwave` as the name of the signal and `Rad` as the unit).

The signal number has to match the signal number that you defined on `pybytes.send_signal` function call, inside your `main.py` code (In this example we defined `signalNumber = 1`);
{{< /hint >}}

## Step 3: Add a widget for the signal

Click on the *"signal card"*.

![](/gitbook/assets/pybytes/dashboard/signal-card.png)

Click on the *Create a new display* button.

![](/gitbook/assets/pybytes/dashboard/create-new-display.png)

Select the type of visualisation (e.g. *Bar chart* or *Line chart*). Let's select the *Line chart*.   

![](/gitbook/assets/pybytes/dashboard/line-chart.png)

You can adjust the parameters of your widget at `Settings`. After, click on the button `Create`.

![](/gitbook/assets/pybytes/dashboard/confirm-graph-creation.png)

Your widget was created. Now, add your widget to your device's dashboard. Click on the button `Edit` on your widget.

![](/gitbook/assets/pybytes/dashboard/graph-settings-button.png)

Mark the checkbox `Display on Dashboard` at `Settings`. Finally, click on the button `Save`.

![](/gitbook/assets/pybytes/dashboard/display-on-dashboard-checkbox.png)

Click on the `Dashboard` tab. Your widget was successfully added there!

![](/gitbook/assets/pybytes/dashboard/sinwave-dashboard-widget.png)

## Done!

Now you've learned how to set up your device's dashboard to display data. Also, you can add more widgets to other signals of your device.
