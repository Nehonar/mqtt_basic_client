import paho.mqtt.client as mqtt
import json
import time
import random

from datetime import datetime

broker = "localhost"
port = 1883
topic = "nodo"

client = mqtt.Client()

client.connect(broker, port)

while True:
    nodo_message = {
        "id": "nodo1",
        "type": "nodo",
        "sensor_data": {
          "temperatura": random.randint(20, 28), 
          "humedad": random.randint(30, 60)
          },
        "timestamp": datetime.now().isoformat()
    }

    client.publish(topic, json.dumps(nodo_message))
    
    time.sleep(5)
