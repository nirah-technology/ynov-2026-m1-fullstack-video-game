from typing import Optional, List

from ..domain.models import PlayerProfile
from ..ports.outputs.persistence import PersistenceFacade

class PlayerProfileService:

    def __init__(self, repository: PersistenceFacade):
        self.__repository: PersistenceFacade = repository
    
    def create_player_profile(self, player_profile: PlayerProfile):
        self.__repository.create_player_profile(player_profile)
    
    def find_player_profile_by_id(self, player_id: str) -> Optional[PlayerProfile]:
        return self.__repository.find_player_profile_by_id(player_id)
    
    def find_all_player_profiles(self) -> List[PlayerProfile]:
        return self.__repository.find_all_player_profiles()

    def update_player_profile(self, player_profile: PlayerProfile):
        self.__repository.update_player_profile(player_profile)
    
    def delete_player_profile(self, player_id: str):
        self.__repository.delete_player_profile(player_id)
