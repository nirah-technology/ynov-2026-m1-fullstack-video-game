from .gloves import T6Gloves
from .helmets import T6Helmet
from .common import Helmet, Gloves

class StuffPlugin:
    def get_helmet(self) -> Helmet:
        return T6Helmet()
    
    def get_gloves(self) -> Gloves:
        return T6Gloves()