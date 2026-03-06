from pathlib import Path

from .profile.application.domain.models import PlayerProfile
from .profile.infrastructure.adapters.outputs.repository import JsonPersistenceAdapter


def main():
    db_file = Path("profile.json")
    db = JsonPersistenceAdapter(db_file)

    profile = PlayerProfile("test", "Test", "Human", "Warrior", 1, 0, [], [])
    db.create_player_profile(profile)
