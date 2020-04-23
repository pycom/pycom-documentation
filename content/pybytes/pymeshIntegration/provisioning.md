## Pymesh Provisioning

In the flow below, a single device is being used to illustrate the provisioning, but the user can use as many devices is necessary.

The Pymesh is created under a project, the project interface was extended with the new Pymesh features.

In the screen below there are 2 previously set up projects. Let's go first with the Pymesh Provisioning were we can see the lopy4, that is running the v1.20 firmware version.

![Project interface extended with the Pymesh feature](/gitbook/assets/pybytes/pymesh/project_ui.png)


Is possible to create one Pymesh per project.

Once clicking on Create Pymesh button, we are going to be guided through a wizard, where we are going to set up the new Pymesh in 4 steps.

![Create Pymesh](/gitbook/assets/pybytes/pymesh/pymesh_provisioning_create_pymesh.png)

### Pymesh Wizard

#### The first step is the license agreement.

After the reading, if the user agrees with the terms, the user should tick the checkmark and click on Next button.

![Pymesh license agreement](/gitbook/assets/pybytes/pymesh/pymesh_license.png)

#### The second step is the device selection.

All devices eligible to be part of a Pymesh, will be under this list. The user should select the devices and click on the Next button.

![Pymesh device selection](/gitbook/assets/pybytes/pymesh/pymesh_select_devices.png)

#### The third step is the Pymesh Settings.

All parameters are filled with default values, if you need to change it, it's possible.

If all the parameters are ok, the user should generate the join-key, and go ahead.

The join-key is what makes the Pymesh unique, In the generate join-key box the user can have more information about the use of the join-key.

If the user wants extra information about each field, hover the mouse over the question mark, and the information will appear.

![Pymesh settings](/gitbook/assets/pybytes/pymesh/pymesh_settings_form.png)

#### The last step is the Pymesh settings summary.

Here the user can check if all information is correct. If everything is fine, the user can go ahead and save the Pymesh settings.

![Pymesh settings summary](/gitbook/assets/pybytes/pymesh/pymesh_summary.png)

### And here is the Pymesh.

On this interface, the user can add or remove devices from the Pymesh, we also can go to configuration, and change the Pymesh settings if it is necessary.

To deploy the Pymesh Settings and Pymesh Firmware into the devices, let's click on the **Deploy Pymesh** button.

![Pymesh](/gitbook/assets/pybytes/pymesh/pymesh_monitoring_struct.png)

Once clicking, the user has a warning message, the update takes up a minute and then there are the confirmation message.

![Pymesh deployment warning message](/gitbook/assets/pybytes/pymesh/pymesh_warning_message.png)

Now the device is properly configured with the Pymesh settings and Pymesh firmware.

All the user needs to do is implement their own script on the well-know **main.py** file.

To illustrate the Pymesh behavior, check [**Pymesh Monitoring**](/pybytes/pymesh/monitoring)
