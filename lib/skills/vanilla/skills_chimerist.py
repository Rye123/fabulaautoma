from lib.core.character import Character
from lib.core.skill import Skill


class Skill_Consume(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Consume",
            "",  #TODO
            level,
            5
        )
        #TODO: track when char deals damage


class Skill_FeralSpeech(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Feral Speech",
            "",  #TODO
            level,
            1
        )


class Skill_Pathogenesis(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Pathogenesis",
            "",  #TODO
            level,
            1
        )


class Skill_RitualChimerism(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Ritual Chimerism",
            "",  #TODO
            level,
            1
        )

    def apply_stats(self, char: Character):
        if self.level > 0:
            char.stats.rituals.chimerism = True


class Skill_SpellMimic(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Spell Mimic",
            "",  #TODO
            level,
            10
        )
        #TODO: need to track both chimerist spells and the magic check choice


