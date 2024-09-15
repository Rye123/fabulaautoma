from lib.core.playerclass import PlayerClass
from lib.character import PlayerCharacter


class ClassNecromancer(PlayerClass):
    """
    Since the Necromancer's free benefit increases max HP OR max MP, this is
    indicated upon class instantiation with `increase_hp`.
    """

    def __init__(self, level: int, increase_hp: bool = True):
        super().__init__("Necromancer",
                         level,
                         "" #TODO: can't find this
                         )
        self._increase_hp = increase_hp

    def apply_stats(self, char: PlayerCharacter):
        if self._increase_hp:
            char.stats.hp_max += 5
        else:
            char.stats.mp_max += 5
