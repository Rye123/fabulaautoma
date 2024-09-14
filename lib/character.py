from abc import ABC, abstractmethod
from enum import IntEnum
from typing import List, Union, Dict
from .dice import Dice
from .item import Item, Armor, Weapon, Shield

class Trait:
    def __init__(self, name: str, desc: str):
        self.name = name
        self.desc = desc


class StatusEffect(IntEnum):
    DAZED    = 0  # Reduces Insight by 1 size
    ENRAGED  = 1  # Reduces Dex & Insight by 1 size
    POISONED = 2  # Reduces Might & Willpower by 1 size
    SHAKEN   = 3  # Reduces Willpower by 1 size
    SLOW     = 4  # Reduces Dex by 1 size
    WEAK     = 5  # Reduces Might by 1 size


class Attributes:
    def __init__(self, dex: int, ins: int, mgt: int, wlp: int):
        try:
            self.dex_base = Dice(dex)
            self.ins_base = Dice(ins)
            self.mgt_base = Dice(mgt)
            self.wlp_base = Dice(wlp)
        except ValueError as e:
            raise ValueError("Attributes.__init__: Invalid value given as dice size, expected 6, 8, 10, 12, or 20.")
        self.status_effects = []
        self.dex_bonus = self.ins_bonus = self.mgt_bonus = self.wlp_bonus = 0

    @property
    def dex_eff(self) -> Dice:
        cur_dex = self.dex_base
        for fx in self.status_effects:
            if fx in [StatusEffect.ENRAGED, StatusEffect.SLOW]:
                cur_dex = cur_dex.get_next_lower()
        return cur_dex + self.dex_bonus

    @property
    def ins_eff(self) -> Dice:
        cur_ins = self.ins_base
        for fx in self.status_effects:
            if fx in [StatusEffect.DAZED, StatusEffect.ENRAGED]:
                cur_ins = cur_ins.get_next_lower()
        return cur_ins + self.ins_bonus

    @property
    def mgt_eff(self) -> Dice:
        cur_mgt = self.mgt_base
        for fx in self.status_effects:
            if fx in [StatusEffect.POISONED, StatusEffect.WEAK]:
                cur_mgt = cur_mgt.get_next_lower()
        return cur_mgt + self.mgt_bonus

    @property
    def wlp_eff(self) -> Dice:
        cur_wlp = self.wlp_base
        for fx in self.status_effects:
            if fx in [StatusEffect.POISONED, StatusEffect.SHAKEN]:
                cur_wlp = cur_wlp.get_next_lower()
        return cur_wlp + self.wlp_bonus


class Stats:
    class Rituals:
        def __init__(self):
            self.arcanism = self.chimerism = self.elementalism = False
            self.entropism = self.ritualism = self.spiritism = False

    def __init__(self):
        self.hp = self.mp = self.ip = 0
        self.hp_max = self.mp_max = self.ip_max = 0
        self.initiative = 0
        self.defense_physical = self.defense_magical = 0
        self.can_equip_martial_armor = self.can_equip_martial_melee = False
        self.can_equip_martial_ranged = self.can_equip_shield = False
        self.can_start_projects = False
        self.rituals = Stats.Rituals()

    @property
    def in_crisis(self) -> bool:
        return self.hp <= (self.hp_max // 2)

    def rest(self):
        self.hp = self.hp_max
        self.mp = self.mp_max


class Equipment:
    def __init__(self):
        self.accessory: Union[None, Item] = None
        self.armor: Union[None, Armor] = None
        self.main_hand: Union[None, Weapon, Shield] = None
        self.off_hand: Union[None, Weapon, Shield] = None
        self.backpack: List[Item] = []

    def equip(self, item: Item, equip_on_main_hand=None):
        if isinstance(item, Armor):
            self.armor = item
        elif isinstance(item, Weapon):
            if equip_on_main_hand is None or not isinstance(equip_on_main_hand, bool):
                raise ValueError("Equipment.equip: Expected boolean for equip_on_main_hand.")
            if equip_on_main_hand:
                self.main_hand = item
            else:
                self.off_hand = item
        elif isinstance(item, Shield):
            if equip_on_main_hand is None or not isinstance(equip_on_main_hand, bool):
                raise ValueError("Equipment.equip: Expected boolean for equip_on_main_hand.")
            if equip_on_main_hand:
                self.main_hand = item
            else:
                self.off_hand = item
        else:
            self.accessory = item


class Character(ABC):
    def __init__(self,
                 name: str,
                 level: int,
                 dex: int, ins: int, mgt: int, wlp: int):
        self.name = name
        self.level = level
        self.attributes = Attributes(dex, ins, mgt, wlp)
        self.stats = Stats()
        self.equipment = Equipment()

    @abstractmethod
    def compute(self):
        """ Computes the stats of this character, based on their attributes, stats and equipment. """
        raise NotImplementedError()

    def __str__(self) -> str:
        report = f"{self.name} (Level {self.level})\n"
        report += "Attributes:" + \
            f"\n\tDEX: {self.attributes.dex_eff} (base {self.attributes.dex_base})" + \
            f"\n\tINS: {self.attributes.ins_eff} (base {self.attributes.ins_base})" + \
            f"\n\tMGT: {self.attributes.mgt_eff} (base {self.attributes.mgt_base})" + \
            f"\n\tWLP: {self.attributes.wlp_eff} (base {self.attributes.wlp_base})\n"
        report += "Stats:" + \
            f"\n\tHP: {self.stats.hp}/{self.stats.hp_max}  (CRISIS: {self.stats.in_crisis})" + \
            f"\n\tMP: {self.stats.mp}/{self.stats.mp_max}" + \
            f"\n\tIP: {self.stats.ip}/{self.stats.ip_max}" + \
            f"\n\tInitiative: {self.stats.initiative}" + \
            f"\n\tDefense: {self.stats.defense_physical}" + \
            f"\n\tMagical Defense: {self.stats.defense_magical}"
        return report


class PlayerClass(ABC):
    def __init__(self, name: str, level: int, desc: str):
        self.name = name
        self.level = level
        self.desc = desc

    @abstractmethod
    def apply_stats(self, char: 'PlayerCharacter'):
        """ Applies the effects of this class on the character's stats """
        pass


class PlayerCharacter(Character):
    def __init__(self,
                 name: str,
                 level: int,
                 dex: int, ins: int, mgt: int, wlp: int):
        super().__init__(name, level, dex, ins, mgt, wlp)

        self.player_classes: List[PlayerClass] = []

    def compute(self):
        # Apply stats based on attributes
        self.stats.hp_max = self.level + (5 * self.attributes.mgt_base)
        self.stats.mp_max = self.level + (5 * self.attributes.wlp_base)
        self.stats.ip_max = 6
        self.stats.defense_physical = self.attributes.dex_base.value
        self.stats.defense_magical = self.attributes.ins_base.value
        self.stats.initiative = 10

        # Apply stats based on classes
        for player_class in self.player_classes:
            player_class.apply_stats(self)

        # Apply stats based on equipment


    def __str__(self) -> str:
        report = super().__str__()
        if len(self.player_classes) > 0:
            report += "\nClasses:"
            for player_class in self.player_classes:
                report += f"\n\t{player_class.name} L{player_class.level}"
        return report


class NonPlayerCharacter(Character):
    def __init__(self,
                 name: str,
                 level: int,
                 dex: int, ins: int, mgt: int, wlp: int):
        super().__init__(name, level, dex, ins, mgt, wlp)

    def compute(self):
        # Apply stats based on attributes
        self.stats.hp_max = (2 * self.level) + (5 * self.attributes.mgt_base)
        self.stats.mp_max = (2 * self.level) + (5 * self.attributes.wlp_base)
        self.stats.ip_max = 6
        self.stats.defense_physical = self.attributes.dex_base.value
        self.stats.defense_magical = self.attributes.ins_base.value
        self.stats.initiative = (self.attributes.dex_base.value + self.attributes.ins_base.value) // 2

        # Apply stats based on classes

        # Apply stats based on equipment