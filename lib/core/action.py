"""
This file contains the definition for Actions as well as SOME basic actions.

Actions that have more dependencies, like Attack, Skill and Spell, may be located in
their respective source code files instead (e.g. `Action_Attack` in `item.py`).

"""

from abc import ABC
from lib.core.character import Character


class Action(ABC):
    def __init__(self, name: str, desc: str):
        self.name = name
        self.desc = desc

    def perform_action(self, char: Character):
        """ Executes the action """
        pass

    def __str__(self) -> str:
        return f"{self.name}: {self.desc}"


class Action_Equipment(Action):
    def __init__(self):
        super().__init__("Equipment", "Equip any number of items in your backpack.")
        #TODO: not sure if we want to show one action for each item in backpack


class Action_Guard(Action):
    def __init__(self):
        super().__init__("Guard", "Until the start of the next turn, you gain Resistance to all damage types, +2 bonus to Opposed Checks and may cover another creature to prevent melee attacks against them.")


class Action_Hinder(Action):
    def __init__(self):
        super().__init__("Hinder", "You perform a Check (DL10) against an opponent, inflicting dazed, shaken, slow or weak upon them if successful.")


class Action_Inventory(Action):
    def __init__(self):
        super().__init__("Inventory", "You spend IP to produce and immediately use a consumable.")


class Action_Objective(Action):
    def __init__(self):
        super().__init__("Objective", "You perform an Attribute/Opposed Check to work towards accomplishing an objective.")


class Action_Study(Action):
    def __init__(self):
        super().__init__("Study", "You attempt to gain information about someone or something.")


class Action_Other(Action):
    def __init__(self):
        super().__init__("Other", "You perform an action not covered by any of the above.")