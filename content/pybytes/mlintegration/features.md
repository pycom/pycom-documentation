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

* Once you have the model deployed on the devices, it can be used for furthers applications like movement detection and so on.

* This file is going to be used by the device firmware, and once generated it should not be changed by the user. Any changes can cause features to malfunction.


[**Machine Learning Integration**](/pybytes/mlintegration)
