import paho.mqtt.client as mqtt
import json

from handlers.gateway_handler import gateway_msg
from handlers.nodo_handler import nodo_msg

from models.gateway_message import GatewayMessage
from models.nodo_message import NodoMessage

from schemas.gateway_schema import gateway_schema
from schemas.nodo_schema import nodo_schema

class MQTTClient:
  def __init__(self, server, port, conn_entries=60):
    self.client = mqtt.Client()
    self.server = server
    self.port = port
    self.conn_entries = conn_entries
    self.client.on_message = self.on_message
    
  def connect(self):
    self.client.connect(self.server, self.port, self.conn_entries)
    self.client.loop_start()
    
  def subscribe(self, topic):
    self.client.subscribe(topic)
    
  def publish(self, topic, msg):
    self.client.publish(topic, msg)

  def on_message(self, client, userdate, msg):
    try:
      data = json.loads(msg.payload.decode())
      
      if data["type"] == "nodo":
        nodo_message = NodoMessage(**data)
        processed_message = nodo_schema(nodo_message.model_dump())
        nodo_msg(processed_message)
        
      elif data["type"] == "gateway":
        gateway_message = GatewayMessage(**data)
        processed_message = gateway_schema(gateway_message.model_dump())
        gateway_msg(processed_message)
        
      else:
        print(f"Unrecognized message type: {data}")
    except json.JSONDecodeError:
      print(f"Decode message error: {msg.payload.decode()}")
    
  def disconnect(self):
    self.client.loop_stop()
    self.client.disconnect()