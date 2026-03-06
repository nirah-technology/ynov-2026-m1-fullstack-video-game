from dataclasses import dataclass, field
from typing import List

@dataclass
class Stat:
    name: str
    value: int

@dataclass
class Bag:
    id: str
    items: List[str] = field(default_factory=list)

@dataclass
class PlayerProfile:
    id: str
    pseudo: str
    breed: str
    classe: str
    level: int
    experience: int
    stats: List[Stat]
    inventory: List[Bag]
