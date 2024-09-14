from abc import ABC, abstractmethod
from enum import IntEnum
from typing import List, Union, Dict
from .dice import Dice
from .item import Item, Armor, Weapon, Shield
from .playerclass import PlayerClass, PlayerClassBenefit

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

    @property
    def dex_eff(self) -> Dice:
        cur_dex = self.dex_base
        for fx in self.status_effects:
            if fx in [StatusEffect.ENRAGED, StatusEffect.SLOW]:
                cur_dex = cur_dex.get_next_lower()
        return cur_dex

    @property
    def ins_eff(self) -> Dice:
        cur_ins = self.ins_base
        for fx in self.status_effects:
            if fx in [StatusEffect.DAZED, StatusEffect.ENRAGED]:
                cur_ins = cur_ins.get_next_lower()
        return cur_ins

    @property
    def mgt_eff(self) -> Dice:
        cur_mgt = self.mgt_base
        for fx in self.status_effects:
            if fx in [StatusEffect.POISONED, StatusEffect.WEAK]:
                cur_mgt = cur_mgt.get_next_lower()
        return cur_mgt

    @property
    def wlp_eff(self) -> Dice:
        cur_wlp = self.wlp_base
        for fx in self.status_effects:
            if fx in [StatusEffect.POISONED, StatusEffect.SHAKEN]:
                cur_wlp = cur_wlp.get_next_lower()
        return cur_wlp


class Stats:
    def __init__(self, character: 'Character'):
        self.hp = self.mp = self.ip = 0
        self._char = character

    @property
    def hp_max(self) -> int:
        c = self._char
        mgt = c.attributes.mgt_base.value

        # PCs and NPCs have different computations.
        if isinstance(c, PlayerCharacter):
            class_bonus = 0
            for benefit in c._get_class_benefits():  #TODO: shitty design, should change PC and NPC to be composition rather than inheritance
                if benefit == PlayerClassBenefit.HP_MAX_BONUS_5:
                    class_bonus += 5
            return c.level + (5 * mgt) + class_bonus
        else:
            return (2 * c.level) + (5 * mgt)

    @property
    def mp_max(self) -> int:
        c = self._char
        wlp = c.attributes.wlp_base.value

        # PCs and NPCs have different computations.
        if isinstance(c, PlayerCharacter):
            class_bonus = 0
            for benefit in c._get_class_benefits():  #TODO: shitty design, should change PC and NPC to be composition rather than inheritance
                if benefit == PlayerClassBenefit.MP_MAX_BONUS_5:
                    class_bonus += 5
            return c.level + (5 * wlp) + class_bonus
        else:
            return (2 * c.level) + (5 * wlp)

    @property
    def ip_max(self) -> int:
        #TODO do for NPCs and other
        c = self._char

        # PCs and NPCs have different computations.
        if isinstance(c, PlayerCharacter):
            class_bonus = 0
            for benefit in c._get_class_benefits():  #TODO: shitty design, should change PC and NPC to be composition rather than inheritance
                if benefit == PlayerClassBenefit.IP_MAX_BONUS_2:
                    class_bonus += 2
            return 6 + class_bonus
        else:
            return 6

    @property
    def in_crisis(self) -> bool:
        return self.hp <= (self.hp_max // 2)

    def rest(self):
        self.hp = self.hp_max
        self.mp = self.mp_max

    @property
    def defense_physical(self) -> int:
        return self._char.attributes.dex_base.value

    @property
    def defense_magical(self) -> int:
        return self._char.attributes.ins_base.value

    @property
    def initiative(self) -> int: #TODO: different for PCs and NPCs -- this is correct for NPCs, for PCs it's 0 + other values
        return 10
        #return (self._char.attributes.dex_base.value + self._char.attributes.ins_base.value) // 2  #TODO: account for armor penalties


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
        self.stats = Stats(self)
        self.equipment = Equipment()

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

    def _get_class_benefits(self) -> List[PlayerClassBenefit]:
        raise NotImplementedError()


class PlayerCharacter(Character):
    def __init__(self,
                 name: str,
                 level: int,
                 dex: int, ins: int, mgt: int, wlp: int):
        super().__init__(name, level, dex, ins, mgt, wlp)

        self.classes: Dict[PlayerClass, int] = {}

    def _get_class_benefits(self) -> List[PlayerClassBenefit]:
        ret = []
        for pClass in self.classes.keys():
            ret += pClass.benefits

        return ret

    def __str__(self) -> str:
        report = super().__str__()
        if len(self.classes) > 0:
            report += "\nClasses:"
            for pClass, classLevel in self.classes.items():
                report += f"\n\t{pClass.name} L{classLevel}"
        return report


class NonPlayerCharacter(Character):
    def __init__(self,
                 name: str,
                 level: int,
                 dex: int, ins: int, mgt: int, wlp: int):
        super().__init__(name, level, dex, ins, mgt, wlp)
