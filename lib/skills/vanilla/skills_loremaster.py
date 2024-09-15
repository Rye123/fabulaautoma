from lib.core.character import Character
from lib.core.skill import Skill


class Skill_FlashOfInsight(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Flash Of Insight",
            "",  #TODO
            level,
            3
        )


class Skill_Focused(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Focused",
            "",  #TODO
            level,
            5
        )

    def apply_stats(self, char: Character):
        char.stats.mp_max += 3 * self.level
        char.stats.breakdown.mp_max += [f"3 * {self.level} (Skill: {self.name})"]


class Skill_KnowledgeIsPower(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Knowledge Is Power",
            "",  #TODO
            level,
            1
        )


class Skill_QuickAssessment(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Quick Assessment",
            "",  #TODO
            level,
            6
        )
        #TODO: possible action?


class Skill_TrainedMemory(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Trained Memory",
            "",  #TODO
            level,
            1
        )

