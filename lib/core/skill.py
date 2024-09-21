from abc import ABC
from lib.core.character import Character
from lib.core.action import Action


class Skill(ABC):
    def __init__(self, name: str, desc: str,
                 level: int = 0, max_level: int = 1):
        self.name = name
        self.desc = desc
        self.level = level
        self.max_level = max_level

    def apply_stats(self, char: Character):
        """ Apply this skill's modifiers to the character's stats. """
        pass

    def add_actions(self, char: Character):
        """ Add any potential new actions this skill gives to the character. """
        pass

    def __str__(self) -> str:
        return f"{self.name} (SL{self.level}/{self.max_level})"


class Action_Skill(Action):
    def __init__(self, skill: Skill):
        super().__init__(f"Use Skill: {skill.name}", skill.desc)
        #TODO: not sure what else to add, depends on what skills are available
