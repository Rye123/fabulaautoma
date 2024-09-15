from abc import ABC, abstractmethod
from lib.core.character import Character
from lib.core.constants import ItemType, WeaponType, DamageType
from lib.core.parsers import parse_accuracy_string, parse_damage_string


class Item(ABC):
    def __init__(self, name: str, desc: str, item_type: ItemType, cost: int):
        self.name = name
        self.desc = desc
        self.item_type = item_type
        self.cost = cost

    @abstractmethod
    def apply_stats(self, char: 'Character'):
        raise NotImplementedError()

    def __str__(self):
        report = self.name + f" ({self.item_type.name})"
        if len(self.desc) != 0:
            report += f"\n\t{self.desc}"
        report += f"\n\tCost: {self.cost}z"
        return report


class Accessory(Item):
    def __init__(self, name: str, desc: str, cost: int):
        super().__init__(name, desc, ItemType.ACCESSORY, cost)

    def __str__(self):
        report = super().__str__()
        return report


class Weapon(Item):
    def __init__(self,
                 name: str, desc: str, cost: int,
                 martial: bool = False,
                 weapon_type: WeaponType = WeaponType.MELEE,
                 two_handed: bool = False,
                 accuracy: str = "",
                 damage: str = "",
                 damage_type: DamageType = DamageType.PHYSICAL
                 ):
        #TODO: not too sure how to represent accuracy and damage programmatically for now
        #TODO: so, I'm instead parsing them such that they give a deterministic string
        #TODO: if there's a proper way formulated later, the parser will still help to make it idiot-proof
        super().__init__(name, desc, ItemType.WEAPON, cost)
        self.martial = martial
        self.weapon_type = weapon_type
        self.two_handed = two_handed
        self.accuracy = parse_accuracy_string(accuracy)
        self.damage = parse_damage_string(damage)
        self.damage_type = damage_type

    def __str__(self):
        report = super().__str__()
        report += f"\n\tMartial: {'YES' if self.martial else 'NO'}"
        report += f"\n\tTwo-Handed: {'YES' if self.two_handed else 'NO'}"
        report += f"\n\tAccuracy: {self.accuracy}"
        report += f"\n\tDamage: {self.damage} {self.damage_type.name.lower()}"
        return report

    def apply_stats(self, char: Character):
        pass


class Armor(Item):
    def __init__(self, name: str, desc: str, cost: int,
                 martial: bool = False):
        super().__init__(name, desc, ItemType.ARMOR, cost)
        self.martial = martial

    def __str__(self):
        report = super().__str__()
        return report


class Shield(Item):
    def __init__(self, name: str, desc: str, cost: int,
                 martial: bool = False):
        super().__init__(name, desc, ItemType.SHIELD, cost)
        self.martial = martial

    def __str__(self):
        report = super().__str__()
        return report
