import json
import paho.mqtt.client as mqtt
from sqlidb import save_to_sqlite
from mongodb import save_to_mongodb
from neo4jdb import save_to_neo4j

def on_message(client, userdata, message):
        payload = json.loads(message.payload.decode("utf-8"))
        sensor_type = payload.get("type")
        print(f"Received payload: {payload}")

        if sensor_type == 'temperature':
            save_to_sqlite(json.dumps(payload))
            print("temp added")

        elif sensor_type == 'air':
            save_to_mongodb(payload)
            print("air added")

        elif sensor_type == "Co2":
            save_to_neo4j(payload)
            print("Co2 added")

        else:
            print(f"Unknown sensor type: {sensor_type}")


client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("env/#")
client.on_message = on_message

print(on_message)

print("Listening...")
client.loop_forever()