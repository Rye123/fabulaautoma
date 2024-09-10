from enum import IntEnum
from random import randint


class Dice(IntEnum):
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12
    D20 = 20

    def get_next_lower(self) -> 'Dice':
        """ Returns the next lower dice size. """
        match self:
            case Dice.D6:
                return Dice.D6
            case Dice.D8:
                return Dice.D6
            case Dice.D10:
                return Dice.D8
            case Dice.D12:
                return Dice.D10
            case Dice.D20:
                return Dice.D12

    def roll(self) -> int:
        """ Rolls the dice, returning the value """
        return randint(1, self.value)

