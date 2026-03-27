from abc import ABC

from .rarety import Rarety

class Stuff(ABC):
    def __init__(self, name: str, rarety: Rarety):
        self.__name: str = name
        self.__rarety: Rarety = rarety

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def rarety(self) -> Rarety:
        return self.__rarety


class Helmet(Stuff):
    def __init__(self):
        super().__init__("helmet")

class Chestplate(Stuff):
    def __init__(self):
        super().__init__("chestplate")

class Gloves(Stuff):
    def __init__(self):
        super().__init__("gloves")

class Boots(Stuff):
    def __init__(self):
        super().__init__("boots")

class Belt(Stuff):
    def __init__(self):
        super().__init__("belt")

class Ring(Stuff):
    def __init__(self):
        super().__init__("ring")

class Amulet(Stuff):
    def __init__(self):
        super().__init__("amulet")

class Necklace(Stuff):
    def __init__(self):
        super().__init__("necklace")

class Scroll(Stuff):
    def __init__(self):
        super().__init__("scroll")

class Orb(Stuff):
    def __init__(self):
        super().__init__("orb")

class Weapon(Stuff, ABC):
    def __init__(self, name: str):
        super().__init__(name)