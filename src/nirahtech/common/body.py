from abc import ABC

class BodyPart(ABC):
    def __init__(self, name: str):
        self.__name: str = name

    @property
    def name(self) -> str:
        return self.__name

class Head(BodyPart):
    def __init__(self):
        super().__init__("head")

class Chest(BodyPart):
    def __init__(self):
        super().__init__("chest")

class Legs(BodyPart):
    def __init__(self):
        super().__init__("legs")

class Feet(BodyPart):
    def __init__(self):
        super().__init__("feet")

class Hand(BodyPart):
    def __init__(self):
        super().__init__("hand")

class Finger(BodyPart):
    def __init__(self):
        super().__init__("ring")

class Elbow(BodyPart):
    def __init__(self):
        super().__init__("elbow")

class Shoulder(BodyPart):
    def __init__(self):
        super().__init__("shoulder")

class Waist(BodyPart):
    def __init__(self):
        super().__init__("waist")

class Back(BodyPart):
    def __init__(self):
        super().__init__("back")

class Neck(BodyPart):
    def __init__(self):
        super().__init__("neck")
    