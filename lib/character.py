"""
This holds the fundamental classes needed for Characters, including Players and NPCs.
- Attributes: The 4 base values. This class also includes tracking of the status effects.
- Stats: Values like health, MP that change more often than attributes.
- Equipment: duh

Eventually, the Character class will output a nice JSON, so that a Python server hosting this code
can return the JSON to a frontend to actually render it nicely.

"""

from abc import ABC, abstractmethod
from enum import IntEnum
from typing import List, Union
from lib.dice import Dice
from lib.item import Item, Armor, Weapon, Shield


class StatusEffect(IntEnum):
    DAZED    = 0  # Reduces Insight by 1 size
    ENRAGED  = 1  # Reduces Dex & Insight by 1 size
    POISONED = 2  # Reduces Might & Willpower by 1 size
    SHAKEN   = 3  # Reduces Willpower by 1 size
    SLOW     = 4  # Reduces Dex by 1 size
    WEAK     = 5  # Reduces Might by 1 size


class Attributes:
    """
    A character's base attributes.
    - `dex_base`, `ins_base`, `mgt_base`, `wlp_base`: The base dexterity, insight, might, and willpower values.
    - `dex_eff`, `ins_eff`, `mgt_eff`, `wlp_eff`: The effective dexterity, insight, might and willpower values, including
                                                  status effects.
    - `status_effects`: A list of existing status effects on the character.
    - `dex_bonus`, `ins_bonus`, `mgt_bonus`, `wlp_bonus`: Bonus to the respective values, which could happen due to equipment.
    """

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
    """
    A character's stats. These are likely to change every time a player levels up.
    - `hp`, `hp_max`
    - `mp`, `mp_max`
    - `ip`, `ip_max`
    - `initiative`
    - `defense_physical`, `defense_magical`
    - `can_equip_martial_armor`
    - `can_equip_martial_melee`, `can_equip_martial_ranged`
    - `can_equip_shield`
    - `can_start_projects`
    - `rituals`:
        - `arcanism`
        - `chimerism`
        - `elementalism`
        - `entropism`
        - `ritualism`
        - `spiritism`
    """

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
    """
    Equipment a character has. Since equipment can have effects on a character's stats, the `apply_stats` method
    will apply the necessary effects on the character's stats.
    - `accessory`: Can be an item, or nothing.
    - `armor`: Can be an armor, or nothing.
    - `main_hand`: Can be a weapon or a shield, or nothing.
    - `off_hand`: Can be a weapon or a shield, or nothing.
    - `backpack`: List of `Item`s in the character's backpack.
    """

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

    @abstractmethod
    def apply_stats(self, char: 'Character'):
        """ Applies the effect of this equipment on the character's stats """
        pass


class PlayerClass(ABC):
    """ Describes a class that a player can have. """

    def __init__(self, name: str, level: int, desc: str):
        self.name = name
        self.level = level
        self.desc = desc

    @abstractmethod
    def apply_stats(self, char: 'PlayerCharacter'):
        """ Applies the effects of this class on the character's stats """
        pass


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

        # Apply stats based on skills
        #TODO: not sure whether skills should be grouped under PlayerClass or under PlayerCharacter, since
        #TODO: NPC skills are class-independent (since NPCs...don't have classes)

        # Apply stats based on equipment
        #TODO: when equipment is implemented

    def __str__(self) -> str:
        report = super().__str__()
        if len(self.player_classes) > 0:
            report += "\nClasses:"
            for player_class in self.player_classes:
                report += f"\n\t{player_class.name} L{player_class.level}"

        #TODO: report player skills, equipment
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

        # Apply stats based on skills
        #TODO: when skills are implemented

        # Apply stats based on equipment
        #TODO: when equipment is implemented

    def __str__(self) -> str:
        report = super().__str__()
        #TODO: report NPC skills, equipment
        return report
