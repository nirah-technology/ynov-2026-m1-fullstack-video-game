from typing import List
from pathlib import Path
from json import load, dump
from dataclasses import asdict

from ....application.domain.models import PlayerProfile, Bag, Stat
from ....application.ports.outputs.persistence import PersistenceFacade

class JsonPersistenceAdapter(PersistenceFacade):
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(JsonPersistenceAdapter, cls).__new__(cls)
        return cls.__instance

    def __init__(self, database_json_file: Path):
        self.__database_json_file: Path = database_json_file

    def create_player_profile(self, player_profile):
        data = self.find_all_player_profiles()
        data.append(player_profile)
        with open(self.__database_json_file, 'w') as file:
            dump([asdict(profie) for profie in data], file, indent=4)

    def find_player_profile_by_id(self, player_id):
        data = self.find_all_player_profiles()
        for profile in data:
            if profile.id == player_id:
                return profile
        return None

    def find_all_player_profiles(self):
        if not self.__database_json_file.exists():
            return []
        with open(self.__database_json_file, 'r') as file:
            try:
                data = load(file)
            except Exception:
                return []
        
        profiles = []
        for profile in data:
            profile['stats'] = [Stat(**stat) for stat in profile.get('stats', [])]
            profile['inventory'] = [Bag(**bag) for bag in profile.get('inventory', [])]
            profiles.append(PlayerProfile(**profile))
        return profiles

    def update_player_profile(self, player_profile):
        data = self.find_all_player_profiles()
        for index, profile in enumerate(data):
            if profile.id == player_profile.id:
                data[index] = player_profile
                with open(self.__database_json_file, 'w') as file:
                    dump([asdict(profie) for profie in data], file, indent=4)
                break
    
    def delete_player_profile(self, player_id):
        data = self.find_all_player_profiles()
        for index, profile in enumerate(data):
            if profile.id == player_id:
                del data[index]
                with open(self.__database_json_file, 'w') as file:
                    dump([asdict(profie) for profie in data], file, indent=4)
                break
    
