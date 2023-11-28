import paho.mqtt.client as mqtt
import json
import time
import random

broker = "localhost"
port = 1883
topic = "gateway"

client = mqtt.Client()

client.connect(broker, port)

while True:
    gateway_message = {
        "id": "gateway1",
        "type": "gateway",
        "network_status": "OK",
        "nodo_data": {
          "nodo1": {
            "sensor_data": {
              "temperatura": random.randint(20, 28), 
              "humedad": random.randint(30, 60)
              }
            }
          }
    }

    client.publish(topic, json.dumps(gateway_message))

    time.sleep(10)
