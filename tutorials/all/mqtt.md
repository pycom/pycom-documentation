# MQTT

MQTT is a lightweight messaging protocol that is ideal for sending small packets of data to and from IoT devices via WiFi.

The broker used in this example is the [IO Adafruit](https://io.adafruit.com) platform, which is free and allows for tinkering with MQTT.

Visit [IO Adafruit](https://io.adafruit.com) and create an account. You'll need to get hold of an API Key as well as your credentials. Visit this [guide](https://learn.adafruit.com/adafruit-io/mqtt-api) for more information about MQTT and how to use it with Adafruit's Broker.

This example will send a message to a topic on the Adafruit MQTT broker and then also subscribe to the same topic, in order to show how to use the subscribe functionality.

```python
from mqtt import MQTTClient
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

