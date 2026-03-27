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

class ProfileMicroService:
    def __init__(self, port: int):
        self.app = FastAPI(title="Profile Microservice")
        self.port = port
        self.database = [
            ProfileDTO("01", "Nicolas", "nicolas@niratech.fr")
        ]

        self._setup_routes()
        self.__register_eureka_client()

    def _setup_routes(self):
        """Définit les points d'entrée de l'API en utilisant des fermetures pour accéder à self."""
        
        @self.app.get("/profiles", response_model=List[ProfileDTO])
        async def list_all_profiles():
            return self.database
        

        @self.app.get("/info", response_model=Dict[str, str])
        async def info():
            return {"status": "ok"}
        
        @self.app.get("/profiles/{profile_id}", response_model=ProfileDTO)
        async def find_profile_by_id(profile_id: str):
            profile = next((p for p in self.database if p.id == profile_id), None)
            if not profile:
                raise HTTPException(status_code=404, detail="Profile not found")
            MessagePublisher.send_message("Les détails d'un utilisateur ont été demandé.", "notifications")
            return profile

    def __register_eureka_client(self):
        py_eureka_client.eureka_client.init(
            eureka_server="http://localhost:8761/eureka",
            app_name="profile-microservice",
            instance_port=self.port
        )