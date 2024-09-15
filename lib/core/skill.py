from abc import ABC, abstractmethod
from lib.core.character import Character

#TODO: to implement new actions, so probably need to scan
#TODO: through all skills -- maybe the skill would have an add_action method
#TODO: that...adds an action. but we haven't implemented actions yet
#TODO: each class probably has a class-specific attribute (e.g. esper has focus)
class Skill(ABC):
    def __init__(self, name: str, desc: str,
                 level: int = 0, max_level: int = 1):
        self.name = name
        self.desc = desc
        self.level = level
        self.max_level = max_level

    def apply_stats(self, char: Character):
        pass

    def __str__(self) -> str:
        return f"{self.name} (SL{self.level}/{self.max_level})"
