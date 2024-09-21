from lib.core.playerclass import PlayerClass
from lib.character import PlayerCharacter


class Class_Chanter(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Chanter",
                         level,
                         "" #TODO: can't find this
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5
        char.stats.breakdown.mp_max += [f"5 ({self.name})"]


class Class_Commander(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Commander",
                         level,
                         "" #TODO: can't find this
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.breakdown.hp_max += [f"5 ({self.name})"]
        char.stats.martial_equip.melee = True
        char.stats.martial_equip.ranged = True


class Class_Dancer(PlayerClass):
    """
    Since the Dancer's free benefit increases max HP OR max MP, this is
    indicated upon class instantiation with `increase_hp`.
    """

    def __init__(self, level: int, increase_hp: bool = True):
        super().__init__("Dancer",
                         level,
                         "" #TODO: can't find this
                         )
        self._increase_hp = increase_hp

    def apply_stats(self, char: PlayerCharacter):
        if self._increase_hp:
            char.stats.hp_max += 5
            char.stats.breakdown.hp_max += [f"5 ({self.name})"]
        else:
            char.stats.mp_max += 5
            char.stats.breakdown.mp_max += [f"5 ({self.name})"]


class Class_Symbolist(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Symbolist",
                         level,
                         "" #TODO: can't find this
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.ip_max += 2
        char.stats.breakdown.ip_max += [f"2 ({self.name})"]

