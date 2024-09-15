from lib.core.playerclass import PlayerClass
from lib.character import PlayerCharacter


class ClassEsper(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Esper",
                         level,
                         "" #TODO: can't find this
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5


class ClassMutant(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Mutant",
                         level,
                         "" #TODO: can't find this
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5


class ClassPilot(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Pilot",
                         level,
                         "" #TODO: can't find this
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.can_equip_martial_melee = True
        char.stats.can_equip_martial_ranged = True