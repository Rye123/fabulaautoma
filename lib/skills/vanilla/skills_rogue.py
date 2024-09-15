from lib.core.character import Character
from lib.core.skill import Skill


class Skill_CheapShot(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Cheap Shot",
            "",  #TODO
            level,
            5
        )


class Skill_Dodge(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Dodge",
            "",  #TODO
            level,
            3
        )

    def apply_stats(self, char: Character):
        #TODO: this
        pass


class Skill_HighSpeed(Skill):
    def __init__(self, level: int):
        super().__init__(
            "High Speed",
            "",  #TODO
            level,
            3
        )


class Skill_SeeYouLater(Skill):
    def __init__(self, level: int):
        super().__init__(
            "See You Later",
            "",  #TODO
            level,
            1
        )


class Skill_SoulSteal(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Soul Steal",
            "",  #TODO
            level,
            5
        )


