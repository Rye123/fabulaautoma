from abc import ABC, abstractmethod
from lib.core.character import Character


class PlayerClass(ABC):
    """ Describes a class that a player can have. """

    def __init__(self, name: str, level: int, desc: str):
        self.name = name
        self.level = level
        self.desc = desc

    @abstractmethod
    def apply_stats(self, char: 'Character'):
        """ Applies the effects of this class on the character's stats """
        raise NotImplementedError()
