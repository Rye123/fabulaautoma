from lib.core.character import Character
from lib.core.skill import Skill


class Skill_MagicSymbols(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Magic Symbols",
            "",  #TODO
            level,
            3
        )


class Skill_Mirage(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Mirage",
            "",  #TODO
            level,
            1
        )

    def apply_stats(self, char: Character):
        if self.level > 0:
            char.stats.rituals.ritualism = True


class Skill_PersonalTouch(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Personal Touch",
            "",  #TODO
            level,
            5
        )


class Skill_SymbolicConnection(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Symbolic Connection",
            "",  #TODO
            level,
            1
        )


class Skill_Symbolism(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Symbolism",
            "",  #TODO
            level,
            5
        )
        #TODO: will need to track the symbols

