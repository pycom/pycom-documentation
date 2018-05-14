# Visualise data from your device.

In this section, we will explain to you how to create widgets for data visualisation and set up your device's dashboard on Pybytes.

# Example

## Step 1: Set up your application (main.py)
The first step is to have an application running on your device. The code example presented here has a routine in which device sends a value within a particular time interval.

Here, we're using the function ``pybytes.send_virtual_pin_value(persistent, pin, value))`` to communicate with Pybytes. This function has three arguments: persistent, pin and value.

Persistent denotes information that is infrequently accessed and not likely to be modified. For the moment, you can set this variable as False (e.g. ``persistent = False``).
Pin represents which virtual pin that receives the data (e.g. If ``pin = 1`` and ``value = 5`` this means that from Pybytes you will recognise that the virtual pin number 1 gets the integer 5 as value.).

Insert the following code on your ``main.py``. You will also need Pybytes library.

```python
# # Import what is necessary to create a thread
import _thread
from time import sleep

# # Increment index used to scan each point from vector sensors_data
def inc(index, vector):
    if index < len(vector)-1:
        return index+1
    else:
        return 0

# # Define your thread's behaviour, here it's a loop sending sensors data every 10 seconds
def send_env_data():
    idx = 0
    sensors_data = [0, -0.2, -0.5, -0.7, -0.8, -0.9, -0.9, -0.9, -0.8, -0.6, -0.4, -0.2, 0, 0.3, 0.5, 0.7, 0.8, 0.9, 0.9, 0.9, 0.8, 0.6, 0.4, 0.1]

    while (pybytes):
        pybytes.send_virtual_pin_value(False, 1, sensors_data[idx])
        idx = inc(idx, sensors_data)
        sleep(3)

# # Start your thread
_thread.start_new_thread(send_env_data, ())
```

## Step 2: Is your device already connected to your Pybytes account?
At this point, we assume that you already have your device connected to your account. If you don't have it yet, you should accomplish this action before advancing. Check how to [add your device here](../connect/intro.md). After you complete this, you can go to step 3.


## Step 3: Go to your device's dashboard
On Pybytes' sidebar, click the  ``Devices`` icon.
Select the device that you want to visualise data from the Device's table.
On your device's page click on  ``Data`` tab.

On the card labelled ``Signals``, click the ``Define New Signal`` button.
Once you click on the button, a modal will pop up on your screen.

## Step 4: Define a signal
1. Select a signal number that matches the pin number defined on your application's call of the function ``pybytes.send_virtual_pin_value`` (in our case we defined ``pin = 1``; Hence we select ``1`` for signal);
2. Enter a name for your signal (here we're using the name ``Sinwave``);
3.  Select the data type for your signal (since our data is a floating number, we will select the type ``Float32``);
4. Enter the unit of measurement for your signal. You can leave it blank if you wish (We're adopting ``rad`` as the unit);
5. Click on the button ``Define``.

## Step 5: Set up a widget for your signal's datapoint
On your device's data page, you will find a new card labelled with your signal's name (``Sinwave``).
- Click on this card.

The page will display a table with data points related to that signal.
- Click on the button ``Create a new display``.
- Select how you would like to display your data (e.g. Table, Bar Chart, Line Chart). In this example, we will select ``Line Chart``.

The page will display the selected widget on your screen. On the right side, you will see the ``Settings`` for the widget. You can customise according to your preferences.
- After editing your preferences, click on the button ``Create``.

## Step 6: Add your new widget to your device's dashboard.
 At the signal's page, click on the button ``Edit`` inside the widget.
 - Mark the checkbox ``Display on Dashboard`` and then click on the button ``Save``.
 After that, you can go back to your device's dashboard page, and you will see the widget for you signal displayed there.

## Step 7: Organise your dashboard.
You can reorganise the elements inside your dashboard as you wish. You can resize a widget by clicking on the triangle on the bottom right corner and dragging the pointer. Also, you can reposition each widget by performing drag-and-drop actions on them.
- Click on the button ``Organise``.
Your dashboard's grid will allow you to resize widgets and reposition them.
- After your changes, click on the button ``Save`` to store those modifications.

## Done!
Now you've learned how to set up your device's dashboard to display data visualisation. Also, you can add more displays to other pins of your device.
