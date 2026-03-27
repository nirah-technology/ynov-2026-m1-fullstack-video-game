from fastapi import FastAPI, HTTPException
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ProfileDTO:
    id: str
    pseudo: str
    email: str

class ProfileMicroService:
    def __init__(self):
        self.app = FastAPI(title="Profile Microservice")
        
        self.database = [
            ProfileDTO("01", "Nicolas", "nicolas@niratech.fr")
        ]

        self.stuff_microservices = [
            "localhost:8001",
            "localhost:8002"
        ]
        
        self._setup_routes()

    def _setup_routes(self):
        """Définit les points d'entrée de l'API en utilisant des fermetures pour accéder à self."""
        
        @self.app.get("/profiles", response_model=List[ProfileDTO])
        async def list_all_profiles():
            return self.database
        
        @self.app.get("/profiles/{profile_id}", response_model=ProfileDTO)
        async def find_profile_by_id(profile_id: str):
            profile = next((p for p in self.database if p.id == profile_id), None)
            if not profile:
                raise HTTPException(status_code=404, detail="Profile not found")
            return profile
