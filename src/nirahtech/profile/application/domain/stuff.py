from dataclasses import dataclass
from abc import abstractmethod
from typing import List, Protocol


class Stuff:
    pass

class Helmet(Stuff):
    pass

class Chestplate(Stuff):
    pass

class Leggings(Stuff):
    pass

class Boots(Stuff):
    pass

class Gloves(Stuff):
    pass

@dataclass
class ArmorStand:
    helmet: Helmet = None
    chestplate: Chestplate = None
    leggings: Leggings = None
    boots: Boots = None
    gloves: Gloves = None


class StufferStep(Protocol):
    @abstractmethod
    def equip(self, armor: ArmorStand):
        raise NotImplementedError()


class HelmetStufferStep(StufferStep):
    def equip(self, armor: ArmorStand):
        armor.helmet = Helmet()

class ChestplateStufferStep(StufferStep):
    def equip(self, armor: ArmorStand):
        armor.chestplate = Chestplate()

class GlovesStufferStep(StufferStep):
    def equip(self, armor: ArmorStand):
        armor.gloves = Gloves()

class Stuffer:
    def __init__(self, steps: List[StufferStep]):
        self.__steps: List[StufferStep] = steps

    def equip(self, armor: ArmorStand):
        for step in self.__steps:
            step.equip(armor)