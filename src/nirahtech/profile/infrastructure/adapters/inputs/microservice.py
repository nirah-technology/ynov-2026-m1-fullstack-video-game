from fastapi import FastAPI
from dataclasses import dataclass
from typing import List
import uvicorn

@dataclass(frozen=True)
class ProfileDTO:
    id: str
    pseudo: str
    email: str

database = [
    ProfileDTO("01", "Nicolas", "nicolas@niratech.fr")
]

stuff_microservives = [
    "localhost:8001",
    "localhost:8002"
]

def main():

    microservice = FastAPI()
    
    @microservice.get("/profiles", response_model=List[ProfileDTO])
    def list_all_profiles():
        return database
    
    @microservice.get("/profiles/{profile_id}", response_model=ProfileDTO)
    def find_profile_by_id(profile_id: str):
        return [profile for profile in database if profile.id == profile_id][0]

    uvicorn.run(microservice, host="0.0.0.0", port=8000)