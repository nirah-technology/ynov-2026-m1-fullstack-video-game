from pathlib import Path

from .profile.application.domain.models import PlayerProfile
from .profile.infrastructure.adapters.outputs.repository import JsonPersistenceAdapter
from .profile.application.domain.models import WeaponFactory, Weapon, Skeleton, ExoSkeleton
from .profile.application.domain.stuff import *
from .profile.application.domain.mobs import Mob

from .kernel import MicroKernel


def main():
    db_file = Path("profile.json")
    db = JsonPersistenceAdapter(db_file)

    profile = PlayerProfile("test", "Test", "Human", "Warrior", 1, 0, [], [])
    db.create_player_profile(profile)

    other_player = PlayerProfile.builder()\
            .with_level(70)\
            .with_race("Blood Elf")\
            .with_classes("Paladin")\
            .build()
    
    weapon_factory = WeaponFactory()
    sword = weapon_factory.create_sword(
        id="ws-01",
        name="Glaive de Guerre d'Azzinoth",
        min_damage=10,
        max_damage=20,
        attack_speed=1.2,
        critical_chance=0.5,
        critical_rate=2
    )

    sword.generate_damage()

    # skeleton: Skeleton = Skeleton()
    proxy: ExoSkeleton = ExoSkeleton(Skeleton())
    proxy.walk()
    # proxy.__sprint()
    proxy.die()

    stuffer = Stuffer(
        [
            HelmetStufferStep(),
            ChestplateStufferStep(),
            GlovesStufferStep()
        ]
    )
    armor = ArmorStand()
    stuffer.equip(armor)


    ilidan = Mob("mob-01", "Ilidan", 80)
    lich_king = Mob("mob-02", "Roi Liche", 80)
    dumb_mob = Mob("mob-03", "Débile", 1)

    ilidan.others_linked_mobs_observers.append(lich_king)

    ilidan.enter_in_fight_mode()
    
    kernel = MicroKernel()
    kernel.load_plugins()
    kernel.run()