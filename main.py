from client.client_mqtt import MQTTClient

def main():
  # Broker params
  server = "localhost"
  port = 1883
  
  # MQTTClient instance
  mqtt_client = MQTTClient(server, port)
  
  # Connection
  mqtt_client.connect()
  
  # Subscribe
  mqtt_client.subscribe("#")
  
  try:
    while True:
      pass
  except KeyboardInterrupt:
    print("\nClosing MQTT client")
  
  mqtt_client.disconnect()
  
if __name__ == "__main__":
  main()