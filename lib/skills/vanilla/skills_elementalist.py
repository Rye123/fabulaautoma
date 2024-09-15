from lib.core.character import Character
from lib.core.skill import Skill


class Skill_Cataclysm(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Cataclysm",
            "",  #TODO
            level,
            3
        )


class Skill_ElementalMagic(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Elemental Magic",
            "",  #TODO
            level,
            10
        )


class Skill_MagicalArtillery(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Magical Artillery",
            "",  #TODO
            level,
            3
        )


class Skill_RitualElementalism(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Ritual Elementalism",
            "",  #TODO
            level,
            1
        )

    def apply_stats(self, char: Character):
        if self.level > 0:
            char.stats.rituals.elementalism = True


class Skill_Spellblade(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Spellblade",
            "",  #TODO
            level,
            4
        )


