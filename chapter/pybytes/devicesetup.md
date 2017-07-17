# Setting up a Device

For this Preview Beta you will have to set your device up manually. This will be automated in first full **v1.0.0** release via a new tool.

### Adding a Device

Please follow these steps to add a device to the Pybytes Platform.

1. Login into Pybytes (https://pybytes.pycom.io)
2. Click on "Devices" in the left menu
3. Click on the "+" (Add Device) button on the top left
4. Select your device type and click next

At this point Pybytes will then guide you through the manual steps required to setup your device.

If you need the instructions for how to upload the Pybytes libraries to your device, please see the instructions below:

1. Download the Pybytes archive (ZIP File)
2. Extract all files contained in the archive to a folder on your computer
3. Replace the placeholders found in main.py with the following:
	3.1 Username: 'your-email-address'
	3.2 Device ID: 'generated-device-id'
4. Replace the placeholders found in boot.py with your routers SSID and Password
5. Upload all files to your device (Please maintain the folder structure, i.e. '/flash/lib' etc.)
