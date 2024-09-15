"""
This involves concrete classes for both Player and Non-Player Characters.

Eventually, these classes would output a nice JSON, so that a Python backend
can return the JSON to a frontend to render it properly.
"""

from typing import List, Union
from lib.core.character import Character
from lib.core.playerclass import PlayerClass
from lib.core.item import Item


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

    def compute(self):
        # Apply stats based on attributes
        self.stats.hp_max = self.level + (5 * self.attributes.mig_base)
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
        self.equipment.apply_stats(self)

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
                 dex: int, ins: int, mig: int, wlp: int):
        super().__init__(name, level, dex, ins, mig, wlp)
        self.equipment = Equipment()

    def compute(self):
        # Apply stats based on attributes
        self.stats.hp_max = (2 * self.level) + (5 * self.attributes.mig_base)
        self.stats.mp_max = (2 * self.level) + (5 * self.attributes.wlp_base)
        self.stats.ip_max = 6
        self.stats.defense_physical = self.attributes.dex_base.value
        self.stats.defense_magical = self.attributes.ins_base.value
        self.stats.initiative = (self.attributes.dex_base.value + self.attributes.ins_base.value) // 2

        # Apply stats based on skills
        #TODO: when skills are implemented

        # Apply stats based on equipment
        self.equipment.apply_stats(self)

    def __str__(self) -> str:
        report = super().__str__()
        #TODO: report NPC skills, equipment
        return report
