from lib.core.playerclass import PlayerClass
from lib.character import PlayerCharacter


class ClassChanter(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Chanter",
                         level,
                         "" #TODO: can't find this
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5


class ClassCommander(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Commander",
                         level,
                         "" #TODO: can't find this
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.can_equip_martial_melee = True
        char.stats.can_equip_martial_ranged = True


class ClassDancer(PlayerClass):
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
        else:
            char.stats.mp_max += 5


class ClassSymbolist(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Symbolist",
                         level,
                         "" #TODO: can't find this
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.ip_max += 2

