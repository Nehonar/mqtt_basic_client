def gateway_schema(gateway) -> dict:
  schema = {
    "id": gateway["id"],
    "type": gateway["type"],
    "network_status": gateway["network_status"],
    "nodo_data": gateway["nodo_data"]
  }
  
  return schema