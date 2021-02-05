---
title: "MQTT"
aliases:
    - tutorials/all/mqtt.html
    - tutorials/all/mqtt.md
    - chapter/tutorials/all/mqtt
---

MQTT is a lightweight messaging protocol that is ideal for sending small packets of data to and from IoT devices via WiFi. You will need to get the mqtt library file from our [Pycom libraries](https://github.com/pycom/pycom-libraries/tree/master/lib) repository on GitHub and place it in the `lib` folder of your project. 

The broker used in this example is the [IO Adafruit](https://io.adafruit.com) platform, which is free and allows for tinkering with MQTT.

Visit [IO Adafruit](https://io.adafruit.com) and create an account. You'll need to get hold of an API Key as well as your credentials. Visit this [guide](https://learn.adafruit.com/adafruit-io/mqtt-api) for more information about MQTT and how to use it with Adafruit's Broker.

This example will send a message to a topic on the Adafruit MQTT broker and then also subscribe to the same topic, in order to show how to use the subscribe functionality.

In the Pybytes library, we use mqtt as well. If you want to use a separate mqtt connection in conjunction with Pybytes, you will need to rename the `class MQTTCLient:` in the `mqtt.py` file to (for example) `class MQTTClient_lib:`, and import using the commented statement to avoid a naming conflict.

```python
from mqtt import MQTTClient
# from mqtt import MQTTClient_lib as MQTTClient
from network import WLAN
import machine
import time

def sub_cb(topic, msg):
   print(msg)

wlan = WLAN(mode=WLAN.STA)
wlan.connect("yourwifinetwork", auth=(WLAN.WPA2, "wifipassword"), timeout=5000)

while not wlan.isconnected():  
    machine.idle()
print("Connected to WiFi\n")

client = MQTTClient("device_id", "io.adafruit.com",user="your_username", password="your_api_key", port=1883)

client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="youraccount/feeds/lights")

while True:
    print("Sending ON")
    client.publish(topic="youraccount/feeds/lights", msg="ON")
    time.sleep(1)
    print("Sending OFF")
    client.publish(topic="youraccount/feeds/lights", msg="OFF")
    client.check_msg()

    time.sleep(1)
```

