from dataclasses import dataclass, field
from typing import List

@dataclass
class Mob:
    id: str
    name: str
    level: int
    is_in_fight_mode: bool = False

    others_linked_mobs_observers: List[Mob] = field(default_factory=list)

    def enter_in_fight_mode(self):
        if not self.is_in_fight_mode:
            self.is_in_fight_mode = True
            print(f"{self.name} passe en mode combat.")
            for observer in self.others_linked_mobs_observers:
                print(f"{self.name} envoie une notification à {observer.name} pour qu'il passe en mode combat.")
                observer.enter_in_fight_mode()

    
