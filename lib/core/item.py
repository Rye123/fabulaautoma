from abc import ABC, abstractmethod
from lib.core.character import Character
from lib.core.constants import ItemType


class Item(ABC):
    def __init__(self, name: str, desc: str, item_type: ItemType):
        self.name = name
        self.desc = desc
        self.item_type = item_type

    @abstractmethod
    def apply_stats(self, char: 'Character'):
        raise NotImplementedError()


class Accessory(Item):
    def __init__(self, name: str, desc: str):
        super().__init__(name, desc, ItemType.ACCESSORY)


class Weapon(Item):
    def __init__(self, name: str, desc: str, martial: bool = False):
        super().__init__(name, desc, ItemType.WEAPON)
        self.martial = martial


class Armor(Item):
    def __init__(self, name: str, desc: str, martial: bool = False):
        super().__init__(name, desc, ItemType.ARMOR)
        self.martial = martial


class Shield(Item):
    def __init__(self, name: str, desc: str, martial: bool = False):
        super().__init__(name, desc, ItemType.SHIELD)
        self.martial = martial
