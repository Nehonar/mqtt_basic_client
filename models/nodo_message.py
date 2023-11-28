from pydantic import BaseModel

class NodoMessage(BaseModel):
  id: str
  type: str
  sensor_data: dict
  timestamp: str