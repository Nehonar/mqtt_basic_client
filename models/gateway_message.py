from pydantic import BaseModel

class GatewayMessage(BaseModel):
    id: str
    type: str
    network_status: str
    nodo_data: dict