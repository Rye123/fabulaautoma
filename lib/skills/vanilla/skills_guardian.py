from lib.core.character import Character
from lib.core.skill import Skill


class Skill_Bodyguard(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Bodyguard",
            "",  #TODO
            level,
            1
        )


class Skill_DefensiveMastery(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Defensive Mastery",
            "",  #TODO
            level,
            5
        )
        #TODO: might need to compute a final damage received


class Skill_DualShieldbearer(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Dual Shieldbearer",
            "",  #TODO
            level,
            1
        )
        #TODO: not sure if need to implement


class SkillFortress(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Fortress",
            "",  #TODO
            level,
            5
        )

    def apply_stats(self, char: Character):
        char.stats.hp_max += 3 * self.level
        char.stats.breakdown.hp_max += [f"3 * {self.level} (Skill: {self.name})"]


class Skill_Protect(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Protect",
            "",  #TODO
            level,
            1
        )

