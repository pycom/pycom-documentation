## Model Features

### Data Acquisition

#### Create Sample

In the data acquisition module the samples for training can be collected.

After setting all sample parameters in the form click on **Create Sample** to start.

The sampling occurs when the device led is amber, when the light turns purple, the device is processing and saving the samples.

If the device gets stuck showing the purple light, maybe the sampling should be done again.

#### Data Collection

The data collection shows the collected samples. Click on the sample to see the graph.

![Data Acquisition](/gitbook/assets/pybytes/ml/data_acquisition_graph.png)

### Processing

#### Raw Data

In the processing tab, the Windows Size and Windows Step should be filled. Select the data range on the graph to fill the Windows step.

#### Spectral Analysis

After selecting the data range to be analyzed. Fill the form and click in the button **Process Signal**

![Processing](/gitbook/assets/pybytes/ml/processing.png)

#### Training

Fill the Neural Network Settings form and click on **START TRAINING** to train the model.

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

[**Machine Learning Integration**](/pybytes/mlintegration)
