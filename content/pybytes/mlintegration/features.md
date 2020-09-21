## Model Features

### Data Acquisition

#### Create Sample

In the data acquisition module the samples for training can be collected.

After setting all sample parameters in the form click on **Create Sample** to start.

The sampling occurs when the device led is amber, when the light turns purple, the device is processing and saving the samples.

If the device gets stuck showing the purple light, maybe the sampling should be done again.

#### Data Collection

The data collection shows the collected samples. Click on the sample to see the graph.

* Is recommended to have the same number of samples per label. If you have collected 2 samplings for a waving movement, you should have the same number of sampling for the other movements (labels) as well.

![Data Acquisition](/gitbook/assets/pybytes/ml/data_acquisition_graph.png)

### Signal Processing

Signal processing is used to extract features for the Neural Network module.

There are many ways to extract features. The simplest way is using convolutional layers, but doing this there is no control of what features will be used and also the convolutional layers make the neural network bigger, so more data is needed for training.

Signal processing provides an easy and intuitively way to extract features and also the features can be analyzed using different methods.

The input data consists from accelerations values on three axes (X, Y, Z). To analyze the data, a window of a certain size is moved over the data using a moving step. The Window Size and Window Step are model specific and they are defined in the Model Configuration tab. This window is received by the signal processing block as input.

##### Standardization

First, the window data can be standardized by subtracting the average and dividing it by its standard deviation, thus obtaining a window with zero mean and a variance equal to one.

##### Filter

After the window is standardized, a filter can be applied to the data. The type of the filter (none, low-pass, high-pass), the cutoff frequency and the filter order can be selected by the user.

##### Features

Using Fourier analysis (FFT transform), features are extracted from the data.

Features are calculated for every axis (X, Y, Z), independently of other axes. The next features are available to be selected/used by the user:

-	The root mean square. It is the square root of the arithmetic mean of the squares of the values.
-	FFT peaks. First peaks from FFT values, to be used as features.
-	Spectral Power on intervals. Mean of the squares of the FFT values, on specified frequencies intervals.

##### Select Features

To select the desired features and also to see the filtered data and calculated FFTs, select the data window to be analyzed, fill in the form and click the **Process Signal** button.

![Processing](/gitbook/assets/pybytes/ml/processing.png)

#### Training

The neural network receives its input from the Signal Processing block.

The number of layers and the number of neurons in this layer can be selected by the user. For the moment there are supported only dense layers as hidden layers.  Other parameters that can be selected are: the number of training epochs, the learning rate and the confidence threshold.

To train the model, fill the Neural Network Settings form and click on **START TRAINING** button.

The results can be checked on the Training Performance section.

![Training](/gitbook/assets/pybytes/ml/training.png)

#### Testing

In the module, the samples for testing can be collected.

After setting all sample parameters in the form click on **Create Sample** to start.

#### Data Collection

The data collection shows the testing collected samples. Click on the **Test xxx Samples** to test the module.

![Testing](/gitbook/assets/pybytes/ml/testing.png)

After the testing is performed, the results can be checked below the Data collection form.

![Testing Results](/gitbook/assets/pybytes/ml/testing_results.png)

#### Model Deployment

After all training and testing, the model can be deployed into the devices.

Select the devices and click on the **DEPLOY MODEL** button.

![Model Deployment](/gitbook/assets/pybytes/ml/deploy.png)

* Once the model is deployed on the device, it can be called from python code to classify new gestures using the data collected from the accelerometer sensor. 

* The path to the deployed model is: `/flash/model_definition.json`. This file is going to be used by the device firmware, and once generated it should not be changed by the user. Any changes can cause features to malfunction.

* The pycom module provides two functions for model interaction: `pycom.ml_new_model()` and `pycom.ml_run_model()`. Below is a very simple example:

```python
import json
import pycom

# A window which contains a gesture. Should be a list with 126 * 3 = 378 entries. This is because, in model_definition.json, the window_size_ms = 2000, sampling_frequency=62.5, so: 62.5*2 + 1 = 126 samples in a window. 
# The data is in the next format: acc_x, acc_y, acc_z, acc_x, ...
# This is just an example. In a real application, this data should be collected from the accelerometer.
data_l = []  

# Read deployed model.
with open('/flash/model_definition.json') as file:
    model_str = file.read()
    model_dict = json.loads(model_str)

# Read labels.
for block in model_dict['model']['blocks']:
    if block['block_type'] == 'nn_block':
        output_labels =  block['trained_nn_model']['label_to_id']

def new_model():
    """Instantiate deployed model."""
    ret = pycom.ml_new_model(model_str)
    print('new_model status = {}'.format(ret))

def run_model():
    """Run model to classify data."""
    result = pycom.ml_run_model(data_l)['NN']
    # Map probabilities to labels and print the result.
    for (label, index) in output_labels.items():
        print('{}: {:.2}%'.format(label, result[index] * 100))

new_model()
run_model()
```

* And an example in which data is real-time collected from the accelerometer:

```python
import pycom
import time
import json
from pysense import Pysense
from LIS2HH12 import *
import _thread

GRAVITATIONAL_ACC = 9.80665

with open('/flash/model_definition.json') as file:
    model_str = file.read()

done_acq = False
data = []
done_sig = False

py = Pysense()

li = LIS2HH12(py)
li.set_odr(ODR_400_HZ)

def new_model():

    print('Create new model.')

    ret = pycom.ml_new_model(model_str)

    print('ret = {}'.format(ret))

def run_model(data_l):

    print('Run model.')

    t0 = time.ticks_us()
    ret = pycom.ml_run_model(data_l)
    delta = time.ticks_us() - t0

    print("time duration = {} ms".format(delta/1000))

    return ret

def data_acq(window_size_ms, sampling_frequency, window_step_ms):
    global done_acq, data, done_sig

    delta_t_us = int(1000000.0 / sampling_frequency)
    samples_num = 3 * int(window_size_ms * sampling_frequency / 1000)
    step_samples = 3 * int(window_step_ms * sampling_frequency / 1000)

    print("Start acquisition data for %d msec, freq %d Hz, samples_num %d"%(window_size_ms, sampling_frequency, samples_num))

    data_local = []
    index = 0
    done_acq = False

    next_ts = time.ticks_us()
    while True:
        if done_sig:
            _thread.exit()
            # while next_ts - time.ticks_us() > 0:
        while time.ticks_diff(next_ts, time.ticks_us()) > 0:
            pass
        acc = li.acceleration()
        ts = next_ts
        data_local.append(acc[0] * GRAVITATIONAL_ACC)
        data_local.append(acc[1] * GRAVITATIONAL_ACC)
        data_local.append(acc[2] * GRAVITATIONAL_ACC)
        next_ts = ts + delta_t_us
        index += 3
        if index >= samples_num:
            # signal the main thread that we have a new window of data
            done_acq = True
            data  = data_local[-samples_num:]
            # delete the first samples, that are not useful anymore
            index -= step_samples
            del data_local[:step_samples]

# parse the mode to obtain window sise and sampling frecquncy
try:
    model_dict = json.loads(model_str)
    window_size_ms = float(model_dict['model']['blocks'][0]['window_size_ms'])
    sampling_frequency = float(model_dict['model']['blocks'][0]['sampling_frequency'])
    window_step_ms = float(model_dict['model']['blocks'][0]['window_step_ms'])
    output_labels =  model_dict['model']['blocks'][2]['trained_nn_model']['label_to_id']
    minimum_confidence_rating =  model_dict['model']['blocks'][2]['trained_nn_model']['minimum_confidence_rating']
except:
    print("Model parsing failed")
    import sys
    sys.exit(0)

new_model()

_thread.start_new_thread(data_acq, (window_size_ms, sampling_frequency, window_step_ms))

print("Result labels: ", output_labels)

while True:

    # wait for buffer of acceleration to be filled in the Thread
    while not done_acq:
        time.sleep(.2)
    done_acq = False
    # print("\nNew data:", len(data), data[:10])
    result = run_model(data)['NN']
    # print("Inference result:", result)
    activity = "None"
    activity_idx = -1
    if max(result) >= minimum_confidence_rating:
        activity_idx = result.index(max(result))

    for (label, index) in output_labels.items():
        print('{}: {:.2}%'.format(label, result[index] * 100))
        # print('{}: {}'.format(label, index))
        if activity_idx == index:
            activity = label

    print("Result activity: {}".format(activity))
    print("--------------------------------------------------")

done_sig = True
time.sleep(1)
print("Done")

```

[**Machine Learning Integration**](/pybytes/mlintegration)
