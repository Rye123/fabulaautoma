from lib.core.character import Character
from lib.core.skill import Skill


class Skill_ArcaneCircle(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Arcane Circle",
            "",  #TODO
            level,
            4
        )


class Skill_ArcaneRegeneration(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Arcane Regeneration",
            "",  #TODO
            level,
            2
        )
        #TODO: track when summoning arcanum


class Skill_BindAndSummon(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Bind And Summon",
            "",  #TODO
            level,
            1
        )
        #TODO: lmao whats an arcanist


class Skill_EmergencyArcanum(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Emergency Arcanum",
            "",  #TODO
            level,
            6
        )


class Skill_RitualArcanism(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Ritual Arcanism",
            "",  #TODO
            level,
            1
        )

    def apply_stats(self, char: Character):
        if self.level > 0:
            char.stats.rituals.arcanism = True


