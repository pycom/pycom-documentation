# Amazon Web Services

The AWS IoT platform enables devices to connect to the Amazon cloud and lets applications in the cloud interact with Internet-connected things. Common IoT applications either collect and process telemetry from devices or enable users to control a device remotely. Things report their state by publishing messages, in JSON format, on MQTT topics. 

For more information see this [PDF File](http://docs.aws.amazon.com/iot/latest/developerguide/iot-dg.pdf).

## Getting Started with AWS IoT

### Creating the message broker (Amazon website):

- Sign in to the [AWS Management Console](https://aws.amazon.com/console/)
- Navigate to the IoT Console by clicking on the <a href="../../../img/awd-1.png" target="_blank">AWS IoT link</a>
- In the left navigation pane, choose [Register/Manage](../../../img/aws-2.png)
- Click on the create button, give your [device a name and press create](../../../img/aws-3.png)
- Click on the device that has been created
- On the Details page, in the left navigation pane, choose [Security](../../../img/aws-4.png)
- On the Certificates page, choose Create certificate
- Download the device certificate, public key, private key, and the root CA for AWS IoT [Security](../../../img/aws-5.png)

### Setting up the device (Pycom device):

- Download the lastest AWS SDK and sample code from the Pycom [GitHub Repository](https://github.com/pycom/pycom-libraries/tree/master/examples/aws).
- Connect to the device via ftp and put the AWSIoTPythonSDK folder in the device flash
- Put the downloaded certificates in the certs directory
- Use Atom or visual studio blocks to create the desired MQTT communication. Sample code of publishing, shadow updater and delta listener are given below.

### Configuration (config.py):

This file contains the wifi, certificate paths and application specific settings that need to be updated by the user.

```python
# wifi configuration
WIFI_SSID = 'my wifi ssid'
WIFI_PASS = 'my wifi password'

# AWS general configuration
AWS_PORT = 8883
AWS_HOST = 'aws host'
AWS_ROOT_CA = '/flash/cert/aws root CA'
AWS_PUBLIC_KEY = '/flash/cert/aws public key'
AWS_PRIVATE_KEY = '/flash/cert/aws private key'

# Subscribe / Publish client 
CLIENT_ID = 'PycomPublishClient'
TOPIC = 'PublishTopic'
OFFLINE_QUEUE_SIZE = -1
DRAINING_FREQ = 2
CONN_DISCONN_TIMEOUT = 10
MQTT_OPER_TIMEOUT = 5
LAST_WILL_TOPIC = 'PublishTopic'
LAST_WILL_MSG = 'To All: Last will message'

# Shadow updater
#THING_NAME = "my thing name"
#CLIENT_ID = "ShadowUpdater"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5

# Delta Listener 
#THING_NAME = "my thing name"
#CLIENT_ID = "DeltaListener"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5
```

### Subscibe / Publish (main.py)

```python
# user specified callback function
def customCallback(client, userdata, message):
	print("Received a new message: ")
	print(message.payload)
	print("from topic: ")
	print(message.topic)
	print("--------------\n\n")

# configure the MQTT client
pycomAwsMQTTClient = AWSIoTMQTTClient(config.CLIENT_ID)
pycomAwsMQTTClient.configureEndpoint(config.AWS_HOST, config.AWS_PORT)
pycomAwsMQTTClient.configureCredentials(config.AWS_ROOT_CA, config.AWS_PRIVATE_KEY, config.AWS_PUBLIC_KEY)

pycomAwsMQTTClient.configureOfflinePublishQueueing(config.OFFLINE_QUEUE_SIZE)
pycomAwsMQTTClient.configureDrainingFrequency(config.DRAINING_FREQ)
pycomAwsMQTTClient.configureConnectDisconnectTimeout(config.CONN_DISCONN_TIMEOUT)
pycomAwsMQTTClient.configureMQTTOperationTimeout(config.MQTT_OPER_TIMEOUT)
pycomAwsMQTTClient.configureLastWill(config.LAST_WILL_TOPIC, config.LAST_WILL_MSG, 1)

#Connect to MQTT Host
if pycomAwsMQTTClient.connect():
    print('AWS connection succeeded')

# Subscribe to topic
pycomAwsMQTTClient.subscribe(config.TOPIC, 1, customCallback)
time.sleep(2)

# Send message to host
loopCount = 0
while loopCount < 8:
	pycomAwsMQTTClient.publish(config.TOPIC, "New Message " + str(loopCount), 1)
	loopCount += 1
	time.sleep(5.0)
```

### Shadow updater (main.py)

```python
# user specified callback functions
def customShadowCallback_Update(payload, responseStatus, token):
    if responseStatus == "timeout":
        print("Update request " + token + " time out!")
    if responseStatus == "accepted":
        payloadDict = json.loads(payload)
        print("Update request with token: " + token + " accepted!")
        print("property: " + str(payloadDict["state"]["desired"]["property"]))
    if responseStatus == "rejected":
        print("Update request " + token + " rejected!")

def customShadowCallback_Delete(payload, responseStatus, token):
    if responseStatus == "timeout":
        print("Delete request " + token + " time out!")
    if responseStatus == "accepted":
        print("Delete request with token: " + token + " accepted!")
    if responseStatus == "rejected":
        print("Delete request " + token + " rejected!")

# configure the MQTT client
pycomAwsMQTTShadowClient = AWSIoTMQTTShadowClient(config.CLIENT_ID)
pycomAwsMQTTShadowClient.configureEndpoint(config.AWS_HOST, config.AWS_PORT)
pycomAwsMQTTShadowClient.configureCredentials(config.AWS_ROOT_CA, config.AWS_PRIVATE_KEY, config.AWS_PUBLIC_KEY)

pycomAwsMQTTShadowClient.configureConnectDisconnectTimeout(config.CONN_DISCONN_TIMEOUT)
pycomAwsMQTTShadowClient.configureMQTTOperationTimeout(config.MQTT_OPER_TIMEOUT)

# Connect to MQTT Host
if pycomAwsMQTTShadowClient.connect():
    print('AWS connection succeeded')

deviceShadowHandler = pycomAwsMQTTShadowClient.createShadowHandlerWithName(config.THING_NAME, True)

# Delete shadow JSON doc
deviceShadowHandler.shadowDelete(customShadowCallback_Delete, 5)

# Update shadow in a loop
loopCount = 0
while True:
    JSONPayload = '{"state":{"desired":{"property":' + str(loopCount) + '}}}'
    deviceShadowHandler.shadowUpdate(JSONPayload, customShadowCallback_Update, 5)
    loopCount += 1
    time.sleep(5)
```

### Delta Listener (main.py)

```python
# Custom Shadow callback
def customShadowCallback_Delta(payload, responseStatus, token):
	payloadDict = json.loads(payload)
	print("property: " + str(payloadDict["state"]["property"]))
	print("version: " + str(payloadDict["version"]))

    # configure the MQTT client
pycomAwsMQTTShadowClient = AWSIoTMQTTShadowClient(config.CLIENT_ID)
pycomAwsMQTTShadowClient.configureEndpoint(config.AWS_HOST, config.AWS_PORT)
pycomAwsMQTTShadowClient.configureCredentials(config.AWS_ROOT_CA, config.AWS_PRIVATE_KEY, config.AWS_PUBLIC_KEY)

pycomAwsMQTTShadowClient.configureConnectDisconnectTimeout(config.CONN_DISCONN_TIMEOUT)
pycomAwsMQTTShadowClient.configureMQTTOperationTimeout(config.MQTT_OPER_TIMEOUT)

# Connect to MQTT Host
if pycomAwsMQTTShadowClient.connect():
    print('AWS connection succeeded')

deviceShadowHandler = pycomAwsMQTTShadowClient.createShadowHandlerWithName(config.THING_NAME, True)

# Listen on deltas
deviceShadowHandler.shadowRegisterDeltaCallback(customShadowCallback_Delta)

# Loop forever
while True:
	time.sleep(1)
```
