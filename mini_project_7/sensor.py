import paho.mqtt.client as mqtt
import random
import time
import json

client = mqtt.Client()
client.username_pw_set("myuser", "mypassword123")
client.connect("localhost", 1883)

print("Temperature sensor started!")

while True:
    temperature = round(random.uniform(20.0, 35.0), 2)
    payload = json.dumps({"sensor": "temperature", "value": temperature})
    client.publish("sensors/temperature", payload)
    print(f"Published: {payload}")
    time.sleep(2)