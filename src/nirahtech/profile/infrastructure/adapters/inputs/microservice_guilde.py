import py_eureka_client.eureka_client

from fastapi import FastAPI, HTTPException
from dataclasses import dataclass
from typing import List, Dict
import py_eureka_client
from ..outputs.message_broker import MessageConsumer, MessagePublisher

@dataclass(frozen=True)
class ProfileDTO:
    id: str
    pseudo: str
    email: str

@dataclass(frozen=True)
class GuildeDTO:
    id: str
    name: str
    members: List[str|ProfileDTO]

class GuildeMicroService:
    def __init__(self, port: int):
        self.app = FastAPI(title="Guilde Microservice")
        self.port = port
        self.database = [
            GuildeDTO("01", "Ynov-M1-Fullstack", ["01"])
        ]

        self._setup_routes()
        self.__register_eureka_client()
        MessageConsumer.subscribe("notifications", self.__notification)
    
    def __notification(self, message, x, y, z):
        print(x)
        print(y)
        print(z)
        print(message)

    def _setup_routes(self):
        """Définit les points d'entrée de l'API en utilisant des fermetures pour accéder à self."""
        
        @self.app.get("/guildes", response_model=List[GuildeDTO])
        async def list_all_guildes():
            return self.database
        

        @self.app.get("/info", response_model=Dict[str, str])
        async def info():
            return {"status": "ok"}
        
        @self.app.get("/guildes/{guilde_id}", response_model=GuildeDTO)
        async def find_guilde_by_id(guilde_id: str):
            guilde = next((g for g in self.database if g.id == guilde_id), None)
            if not guilde:
                raise HTTPException(status_code=404, detail="Gilde not found")
            response = await py_eureka_client.eureka_client.do_service_async("PROFILE-MICROSERVICE", f"/profiles/{guilde.members[0]}", return_type="json")
            guilde.members[0] = ProfileDTO(**response)
            return guilde

    def __register_eureka_client(self):
        py_eureka_client.eureka_client.init(
            eureka_server="http://localhost:8761/eureka",
            app_name="guilde-microservice",
            instance_port=self.port
        )