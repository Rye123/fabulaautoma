from abc import ABC, abstractmethod
from lib.core.character import Character
from lib.core.constants import ItemType, WeaponType, DamageType
from lib.core.parsers import parse_accuracy_string, parse_damage_string, parse_defense_string


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
                 martial: bool = False,
                 defense_physical: str = "",
                 defense_magical: str = "",
                 initiative_bonus: int = 0):
        super().__init__(name, desc, ItemType.ARMOR, cost)
        self.martial = martial
        self.defense_physical = parse_defense_string(defense_physical)
        self.defense_magical = parse_defense_string(defense_magical)
        self.initiative_bonus = initiative_bonus

    def __str__(self):
        report = super().__str__()
        return report

    def apply_stats(self, char: Character):
        # Parse physical defense
        phy_components = self.defense_physical.split('+')
        new_def_physical = 0
        char.stats.breakdown.defense_physical = ""
        breakdown_components = []
        for component in phy_components:
            #TODO not sure if these should be the base or effective values
            if component == "DEX":
                new_def_physical += char.attributes.dex_base
                breakdown_components.append(f"{char.attributes.dex_base} (DEX)")
            elif component == "INS":
                new_def_physical += char.attributes.ins_base
                breakdown_components.append(f"{char.attributes.ins_base} (INS)")
            elif component == "MIG":
                new_def_physical += char.attributes.mig_base
                breakdown_components.append(f"{char.attributes.mig_base} (MIG)")
            elif component == "WLP":
                new_def_physical += char.attributes.wlp_base
                breakdown_components.append(f"{char.attributes.wlp_base} (MIG)")
            else:
                try:
                    new_def_physical += int(component)
                    breakdown_components.append(component)
                except ValueError:
                    raise ValueError(f"Armor.apply_stats: Invalid component in defense string: \"{component}\".")
        char.stats.defense_physical = new_def_physical
        char.stats.breakdown.defense_physical = '(' + "+".join(breakdown_components) + ') (Armor)'

        # Parse magical defense
        mag_components = self.defense_magical.split('+')
        new_def_magical = 0
        breakdown_components = []
        for component in mag_components:
            #TODO not sure if these should be the base or effective values
            if component == "DEX":
                new_def_magical += char.attributes.dex_base
                breakdown_components.append(f"{char.attributes.dex_base} (DEX)")
            elif component == "INS":
                new_def_magical += char.attributes.ins_base
                breakdown_components.append(f"{char.attributes.ins_base} (INS)")
            elif component == "MIG":
                new_def_magical += char.attributes.mig_base
                breakdown_components.append(f"{char.attributes.mig_base} (MIG)")
            elif component == "WLP":
                new_def_magical += char.attributes.wlp_base
                breakdown_components.append(f"{char.attributes.wlp_base} (WLP")
            else:
                try:
                    new_def_magical += int(component)
                    breakdown_components.append(component)
                except ValueError:
                    raise ValueError(f"Armor.apply_stats: Invalid component in defense string: \"{component}\".")
        char.stats.defense_magical = new_def_magical
        char.stats.breakdown.defense_magical = '(' + "+".join(breakdown_components) + ') (Armor)'

        char.stats.initiative += self.initiative_bonus
        char.stats.breakdown.initiative += [f"+{self.initiative_bonus} (Armor)"]


class Shield(Item):
    def __init__(self, name: str, desc: str, cost: int,
                 martial: bool = False,
                 defense_physical_bonus: int = 0,
                 defense_magical_bonus: int = 0,
                 initiative_bonus: int = 0):
        super().__init__(name, desc, ItemType.SHIELD, cost)
        self.martial = martial
        self.defense_physical_bonus = defense_physical_bonus
        self.defense_magical_bonus = defense_magical_bonus
        self.initiative_bonus = initiative_bonus

    def __str__(self):
        report = super().__str__()
        return report

    def apply_stats(self, char: Character):
        char.stats.defense_physical += self.defense_physical_bonus
        char.stats.breakdown.defense_physical += [f"{self.defense_physical_bonus} (Shield)"]
        char.stats.defense_magical += self.defense_magical_bonus
        char.stats.breakdown.defense_magical += [f"{self.defense_magical_bonus} (Shield)"]
        char.stats.initiative += self.initiative_bonus
        char.stats.breakdown.initiative += [f"{self.initiative_bonus} (Shield)"]
