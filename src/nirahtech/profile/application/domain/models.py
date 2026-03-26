from dataclasses import dataclass, field
from typing import List, Set
from abc import ABC

@dataclass
class Stat:
    name: str
    value: int

@dataclass
class Bag:
    id: str
    items: List[str] = field(default_factory=list)


class PlayerProfileBuilder:
    def __init__(self):
        self.__id: str = None
        self.__pseudo: str = "Player"
        self.__race: str = "Human"
        self.__classes: str = "Warrior"
        self.__level: int = 1
        self.__experience: int = 0
        self.__stats: Set[Stat] = set() # {}
        self.__inventory: List[Bag] = list() # []

    def with_id(self, id: str) -> PlayerProfileBuilder:
        self.__id = id
        return self

    def with_pseudo(self, pseudo: str) -> PlayerProfileBuilder:
        self.__pseudo = pseudo
        return self
    
    def with_race(self, race: str) -> PlayerProfileBuilder:
        self.__race = race
        return self
    
    def with_classes(self, classes: str) -> PlayerProfileBuilder:
        self.__classes = classes
        return self
    
    def with_level(self, level: int) -> PlayerProfileBuilder:
        self.__level = level
        return self
    
    def with_experience(self, experience: int) -> PlayerProfileBuilder:
        self.__experience = experience
        return self
    
    def with_stats(self, stats: Set[Stat]) -> PlayerProfileBuilder:
        self.__stats = stats
        return self
    
    def with_specific_stat(self, stat: Stat) -> PlayerProfileBuilder:
        self.__stats.add(stat)
        return self
    
    def with_inventory(self, inventory: List[Bag]) -> PlayerProfileBuilder:
        self.__inventory = inventory
        return self
    
    def build(self) -> PlayerProfile:
        return PlayerProfile(
            id=self.__id,
            pseudo=self.__pseudo,
            race=self.__race,
            classes=self.__classes,
            level=self.__level,
            experience=self.__experience,
            stats=self.__stats,
            inventory=self.__inventory
        )

@dataclass(frozen=True)
class PlayerProfile:
    id: str
    pseudo: str
    breed: str
    classe: str
    level: int
    experience: int
    stats: List[Stat]
    inventory: List[Bag]

    @staticmethod
    def builder() -> PlayerProfileBuilder:
        return PlayerProfileBuilder()


class Weapon(ABC):
    def __init__(self, id: str, name: str, min_damage: int, max_damage: int, critical_chance: float, critical_rate: float, attack_speed: float):
        self.__id: str = id
        self.__name: str = name
        self.__min_damage: int = min_damage
        self.__max_damage: int = max_damage
        self.__critical_chance: float = critical_chance
        self.__critical_rate: float = critical_rate
        self.__attack_speed: float = attack_speed
    
    def generate_damage(self) -> float:
        pass # A implémenter

class Sword(Weapon):
    def __init__(self, id: str, name: str, min_damage: int, max_damage: int, critical_chance: float, critical_rate: float, attack_speed: float):
        super().__init__(
            id=id,
            name=name,
            min_damage=min_damage,
            max_damage=max_damage,
            critical_chance=critical_chance,
            critical_rate=critical_rate,
            attack_speed=attack_speed
        )

class Bow(Weapon):
    def __init__(self, id: str, name: str, min_damage: int, max_damage: int, critical_chance: float, critical_rate: float, attack_speed: float):
        super().__init__(
            id=id,
            name=name,
            min_damage=min_damage,
            max_damage=max_damage,
            critical_chance=critical_chance,
            critical_rate=critical_rate,
            attack_speed=attack_speed
        )

class WeaponFactory:
    def create_sword(self, id: str, name: str, min_damage: int, max_damage: int, critical_chance: float, critical_rate: float, attack_speed: float) -> Sword:
        return Sword(
            id=id,
            name=name,
            min_damage=min_damage,
            max_damage=max_damage,
            critical_chance=critical_chance,
            critical_rate=critical_rate,
            attack_speed=attack_speed
        )

    def create_bow(self, id: str, name: str, min_damage: int, max_damage: int, critical_chance: float, critical_rate: float, attack_speed: float) -> Bow:
        return Bow(
            id=id,
            name=name,
            min_damage=min_damage,
            max_damage=max_damage,
            critical_chance=critical_chance,
            critical_rate=critical_rate,
            attack_speed=attack_speed
        )