"""
This involves concrete classes for both Player and Non-Player Characters.

Eventually, these classes would output a nice JSON, so that a Python backend
can return the JSON to a frontend to render it properly.
"""

from typing import List, Union
from lib.core.character import Character
from lib.core.playerclass import PlayerClass
from lib.core.item import Item
from lib.core.skill import Skill


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
        #TODO: maybe don't let this be None, keep it consistent -- either None or NoArmor/Barehands
        self.accessory: Union[None, Item] = None
        self.armor: Union[None, Item] = None
        self.main_hand: Union[None, Item] = None
        self.off_hand: Union[None, Item] = None
        self.backpack: List[Item] = []

    def apply_stats(self, char: 'Character'):
        """ Applies the effect of this set of equipment on the character's stats """
        if self.accessory is not None:
            self.accessory.apply_stats(char)
        if self.armor is not None:
            self.armor.apply_stats(char)
        if self.main_hand is not None:
            self.main_hand.apply_stats(char)
        if self.off_hand is not None:
            self.off_hand.apply_stats(char)


class PlayerCharacter(Character):
    def __init__(self,
                 name: str,
                 level: int,
                 dex: int, ins: int, mig: int, wlp: int):
        super().__init__(name, level, dex, ins, mig, wlp)

        self.player_classes: List[PlayerClass] = []
        self.equipment = Equipment()
        self.skills: List[Skill] = []

    def compute(self):
        self.stats.breakdown.reset()

        # Apply stats based on attributes
        self.stats.hp_max = self.level + (5 * self.attributes.mig_base)
        self.stats.breakdown.hp_max += [f"{self.level} (Level)", f"5 * {self.attributes.mig_base} (MIG)"]
        self.stats.mp_max = self.level + (5 * self.attributes.wlp_base)
        self.stats.breakdown.mp_max += [f"{self.level} (Level)", f"5 * {self.attributes.wlp_base} (WLP)"]
        self.stats.ip_max = 6
        self.stats.breakdown.ip_max += [f"6 (Base)"]
        self.stats.defense_physical = self.attributes.dex_base.value
        self.stats.breakdown.defense_physical = [f"{self.attributes.dex_base} (DEX)"]
        self.stats.defense_magical = self.attributes.ins_base.value
        self.stats.breakdown.defense_magical = [f"{self.attributes.ins_base} (INS)"]
        self.stats.initiative = 0
        self.stats.breakdown.initiative = []
        self.stats.initiative_modifier = 0
        self.stats.breakdown.initiative_modifier = []

        # Apply stats based on classes
        for player_class in self.player_classes:
            player_class.apply_stats(self)

        # Apply stats based on skills
        #TODO: not sure whether skills should be grouped under PlayerClass or under PlayerCharacter, since
        #TODO: NPC skills are class-independent (since NPCs...don't have classes)
        for skill in self.skills:
            skill.apply_stats(self)

        # Apply stats based on equipment
        self.equipment.apply_stats(self)

    def __str__(self) -> str:
        report = super().__str__()
        if len(self.player_classes) > 0:
            report += "\nClasses:"
            for player_class in self.player_classes:
                report += f"\n\t{player_class.name} L{player_class.level}"

        report += "\nEquipment:"
        report += f"\n\tAccessory: {self.equipment.accessory}"
        report += f"\n\tArmor: {self.equipment.armor}"
        report += f"\n\tMain Hand: {self.equipment.main_hand}"
        report += f"\n\tOff Hand: {self.equipment.off_hand}"

        if len(self.skills) > 0:
            report += "\nSkills:"
            for skill in self.skills:
                report += f"\n\t{skill}"

        #TODO: report player skills
        return report


class NonPlayerCharacter(Character):
    def __init__(self,
                 name: str,
                 level: int,
                 dex: int, ins: int, mig: int, wlp: int):
        super().__init__(name, level, dex, ins, mig, wlp)
        self.equipment = Equipment()
        self.skills: List[Skill] = []

    def compute(self):
        self.stats.breakdown.reset()

        # Apply stats based on attributes
        self.stats.hp_max = (2 * self.level) + (5 * self.attributes.mig_base)
        self.stats.breakdown.hp_max += [f"2 * {self.level} (Level)", f"5 * {self.attributes.mig_base} (MIG)"]
        self.stats.mp_max = (2 * self.level) + (5 * self.attributes.wlp_base)
        self.stats.breakdown.mp_max += [f"2 * {self.level} (Level)", f"5 * {self.attributes.wlp_base} (WLP)"]
        self.stats.ip_max = 6
        self.stats.breakdown.ip_max += [f"6 (Base)"]
        self.stats.defense_physical = self.attributes.dex_base.value
        self.stats.breakdown.defense_physical = [f"{self.attributes.dex_base} (DEX)"]
        self.stats.defense_magical = self.attributes.ins_base.value
        self.stats.breakdown.defense_magical = [f"{self.attributes.ins_base} (INS)"]
        self.stats.initiative = (self.attributes.dex_base.value + self.attributes.ins_base.value) // 2
        self.stats.breakdown.initiative = [f"({self.attributes.dex_base} (DEX) + {self.attributes.ins_base} (INS)) // 2"]
        self.stats.initiative_modifier = 0
        self.stats.breakdown.initiative_modifier = []

        # Apply stats based on skills
        for skill in self.skills:
            skill.apply_stats(self)

        # Apply stats based on equipment
        self.equipment.apply_stats(self)

    def __str__(self) -> str:
        report = super().__str__()
        #TODO: report NPC skills, equipment
        return report
