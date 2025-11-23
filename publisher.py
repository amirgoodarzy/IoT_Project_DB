import time
import json
import random
from random import randint

import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883)

while True:
    temp_data = {
        "value": round(random.uniform(20.0,30.0)),
        "unit": "C",
        "timestamp": time.time(),
        "type": "temperature"
    }
    air_data = {
        "value": round(random.uniform(10,100),1),
        "unit": "ppm",
        "timestamp": time.time(),
        "type": "air",
    }
    Co2_data = {
        "value": round(random.uniform(1,10),1),
        "unit": "ppm",
        "timestamp": time.time(),
        "type": "Co2",
        "sensor_id": randint(1, 10)
    }

    client.publish("env/temperature", json.dumps(temp_data))
    client.publish("env/air_quality", json.dumps(air_data))
    client.publish("env/Co2", json.dumps(Co2_data))

    print("published")
    print(temp_data)
    print(air_data)
    print(Co2_data)
    time.sleep(5)