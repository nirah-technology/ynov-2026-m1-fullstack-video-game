from typing import Protocol, Optional, List
from abc import abstractmethod

from ...domain.models import PlayerProfile

class WebFacade(Protocol):
    
    @abstractmethod
    def create_player_profile(self, player_profile: PlayerProfile):
        raise NotImplementedError()
    
    @abstractmethod
    def find_player_profile_by_id(self, player_id: str) -> Optional[PlayerProfile]:
        raise NotImplementedError()
    
    @abstractmethod
    def find_all_player_profiles(self) -> List[PlayerProfile]:
        raise NotImplementedError()

    @abstractmethod
    def update_player_profile(self, player_profile: PlayerProfile):
        raise NotImplementedError()
    
    @abstractmethod
    def delete_player_profile(self, player_id: str):
        raise NotImplementedError()