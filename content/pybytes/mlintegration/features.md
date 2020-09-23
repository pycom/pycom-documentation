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

* The path to the deployed model is: `flash/model_definition.json`. This file is going to be used by the device firmware, and once generated it should not be changed by the user. Any changes can cause features to malfunction.

* The pycom module provides two functions for model interaction: `pycom.ml_new_model()` and `pycom.ml_run_model()`. Below is a very simple example:

```python
import json
import pycom

# This is just an example. In a real application, the input 
# data should be collected from the accelerometer.

# In order for this model to run with the data_l defined here, in 
# the model_definition.json, we must have: window_size_ms = 2000 
# and sampling_frequency=62.5! If the model used has other 
# settings please update the data_l list accordingly. The data_l 
# list should contain only one window of data, on three axes!

# A window which contains a gesture. It is a list with 126 * 3 = 378 
# entries. This is because in the model_definition.json the 
# window_size_ms = 2000 and sampling_frequency = 62.5, so there are 
# 62.5*2 + 1 = 126 samples in a window. The data is in the next 
# format: acc_x, acc_y, acc_z, acc_x, ...
data_l = [-0.9337, 0.0575, 11.8405, -0.7422, -0.1006, 10.6195, -0.1532, 0.6129, 10.0353, -0.4357, 0.7135, 7.6938, -0.4357, 0.7135, 7.6938, -0.4405, 0.5315, 6.3434, -0.2346, 0.4788, 4.5191, 0.1772, 0.6177, 3.705, 0.4597, 0.5219, 4.7202, 0.8619, 1.2258, 6.1711, 1.1013, 2.2936, 6.1567, 0.9002, 2.2362, 4.0642, 0.9002, 2.2362, 4.0642, 0.2921, 1.7573, 1.5407, 0.656, 1.4748, -0.1448, 0.8523, 1.3408, -0.3938, 1.2067, 1.3551, 0.9373, 1.403, 1.9106, 2.7809, 1.0056, 1.9776, 3.4081, 1.0056, 1.9776, 3.4081, 1.1396, 1.5419, 2.8766, 1.0439, 1.1684, 3.1831, 1.1971, 1.3743, 3.5853, 0.9816, 1.6616, 3.6332, 0.249, 1.8387, 3.5949, 0.4884, 1.8675, 4.203, 0.5698, 1.7382, 5.2948, 0.3543, 1.901, 5.8646, 0.3687, 1.9249, 5.7928, 0.3687, 1.9249, 5.7928, 0.5459, 1.4078, 5.357, 0.4741, 0.4549, 5.3762, 0.5842, 0.723, 6.8414, 0.3639, 1.1444, 7.6363, 0.3639, 1.2019, 8.8334, 0.4884, 0.565, 9.341, 0.723, 0.6033, 10.088, 0.407, 0.6752, 10.1359, -0.431, 0.7374, 10.1023, -0.3112, 0.68, 11.9459, 0.249, 0.5842, 13.4494, 0.0479, 0.7183, 13.21, -0.972, 0.8763, 12.5396, -0.814, 0.6656, 13.8181, -0.6321, 0.7039, 15.451, -1.221, 0.565, 15.2259, -1.4317, 0.5028, 15.1972, -1.7526, 0.8811, 16.356, -2.2553, 0.9242, 17.5339, -2.3559, 1.5802, 18.7646, -2.5331, 1.5371, 19.2099, -2.7054, 1.6616, 19.5882, -2.7916, 1.6185, 19.8084, -2.7916, 1.6185, 19.8084, -2.5762, 1.5993, 20.0383, -2.5762, 1.5993, 20.0383, -2.1117, 0.9529, 18.9321, -1.81, 0.4645, 17.4765, -1.6137, 0.2873, 17.1365, -1.2402, 0.1053, 16.3895, -1.0439, 0.0479, 15.4414, -0.7087, -0.1006, 14.613, -0.5124, -0.1101, 14.273, -0.6752, 0.5028, 13.5787, -0.4741, 0.6943, 12.9036, -0.3926, 0.7422, 11.8453, -0.3926, 0.7422, 11.8453, -0.1006, 0.5219, 10.4088, 0.3926, 0.5459, 11.9459, 0.5555, 0.7422, 11.491, 0.4693, 1.2402, 8.5317, -0.2921, 0.8188, 4.9979, -0.2921, 0.8188, 4.9979, 0.1006, 0.7757, 5.0985, 0.8523, 1.0918, 7.9332, 0.8236, 2.4086, 9.1447, 0.2921, 2.5953, 7.2532, 0.431, 2.2122, 5.9891, 1.1109, 1.2258, 3.8439, 1.1109, 1.2258, 3.8439, 0.838, 0.431, 1.5838, 1.2929, 0.5986, 1.1432, 1.3503, 0.838, 1.7178, 1.336, 1.7813, 3.0969, 0.9194, 2.4229, 3.8678, 0.7901, 2.4852, 4.2365, 0.7087, 2.3894, 4.2653, 0.8763, 1.6999, 4.045, 0.9912, 1.4413, 3.7816, 0.8092, 1.5993, 4.1312, 0.7757, 1.8531, 4.8638, 0.7374, 1.8004, 5.2086, 0.6512, 1.8244, 5.1415, 0.6177, 2.2362, 5.6204, 0.2203, 2.2745, 5.5869, -0.2346, 1.7382, 5.0218, 0.1724, 1.5083, 5.1846, 0.7949, 1.5802, 6.7935, 0.2251, 2.5091, 7.8326, -0.2346, 2.4038, 7.7129, -0.2729, 1.8196, 7.4974, 0.2921, 1.5802, 8.0385, -0.2586, 1.6712, 8.6706, -0.3065, 1.7382, 9.0633, -0.3065, 1.7382, 9.0633, -0.0144, 1.6233, 10.1885, -0.182, 1.0056, 10.8302, -0.3017, 0.9337, 10.5285, -0.5267, 0.9194, 10.337, -0.6656, 0.7805, 11.2803, -0.1389, 0.1484, 12.5588, -0.067, 0.2586, 12.9658, -0.0527, 0.4214, 13.6601, -0.7901, 0.8332, 13.3824, -0.5507, 0.3735, 12.2236, -0.7278, 0.1053, 13.8947, -0.5602, 0.0718, 14.5125, -0.9816, 0.5938, 15.0344, -1.3791, 0.407, 15.2403, -1.3503, 0.3112, 16.2746, -1.494, 0.407, 16.6146, -1.494, 0.407, 16.6146, -1.992, 0.6512, 17.2466, -2.3367, 1.3216, 18.4725, -2.1883, 1.5897, 18.9178, -2.4229, 1.6712, 18.5634]  

# Read deployed model.
with open('flash/model_definition.json') as file:
    model_str = file.read()
    model_dict = json.loads(model_str)

# Read labels.
for block in model_dict['model']['blocks']:
    if block['block_type'] == 'nn_block':
        output_labels =  block['trained_nn_model']['label_to_id']

def new_model():
    """Instantiate deployed model."""
    return pycom.ml_new_model(model_str)
    

def run_model():
    """Run model to classify data."""
    result = pycom.ml_run_model(data_l)['NN']
    # Map probabilities to labels and print the result.
    for (label, index) in output_labels.items():
        print('{}: {:.2}%'.format(label, result[index] * 100))

if new_model():
    print('Model succesfully created')
    run_model()

```

* And an example in which data is real-time collected from the accelerometer:
```python
# TODO: Add example.
```

[**Machine Learning Integration**](/pybytes/mlintegration)
