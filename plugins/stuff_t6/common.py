from abc import ABC, abstractmethod

class StuffPart(ABC):
    def __init__(self, name: str, required_level: int, rarety: str):
        self.__name: str = name
        self.__required_level: int = required_level
        self.__rarety: str = rarety

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def required_level(self) -> int:
        return self.__required_level
    
    @property
    def rarety(self) -> str:
        return self.__rarety

class Helmet(StuffPart, ABC):
    def __init__(self, name: str, required_level: int, rarety: str):
        super().__init__(name, required_level, rarety)

class Gloves(StuffPart, ABC):
    def __init__(self, name: str, required_level: int, rarety: str):
        super().__init__(name, required_level, rarety)

class Chestplate(StuffPart, ABC):
    def __init__(self, name: str, required_level: int, rarety: str):
        super().__init__(name, required_level, rarety)