def nodo_schema(nodo) -> dict:
  schema = {
    "id": nodo["id"],
    "type": nodo["type"],
    "sensor_data": nodo["sensor_data"],
    "timestamp": nodo["timestamp"]
  }
  
  return schema