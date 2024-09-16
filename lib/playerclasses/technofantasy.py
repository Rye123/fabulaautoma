from lib.core.playerclass import PlayerClass
from lib.character import PlayerCharacter


class Class_Esper(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Esper",
                         level,
                         "" #TODO: can't find this
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5
        char.stats.breakdown.mp_max += [f"5 ({self.name})"]


class Class_Mutant(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Mutant",
                         level,
                         "" #TODO: can't find this
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.breakdown.hp_max += [f"5 ({self.name})"]


class Class_Pilot(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Pilot",
                         level,
                         "" #TODO: can't find this
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.breakdown.hp_max += [f"5 ({self.name})"]
        char.stats.can_equip_martial_melee = True
        char.stats.can_equip_martial_ranged = True