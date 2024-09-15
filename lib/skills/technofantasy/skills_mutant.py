from lib.core.skill import Skill


class Skill_Akromorphosis(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Akromorphosis",
            "",  #TODO
            level,
            3
        )


class Skill_Biophagy(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Biophagy",
            "",  #TODO
            level,
            4
        )


class Skill_Ecdysis(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Ecdysis",
            "",  #TODO
            level,
            3
        )
        #TODO: need to track damage taken


class Skill_Genoclepsis(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Genoclepsis",
            "",  #TODO
            level,
            2
        )
        #TODO: need to track when damage is done


class Skill_Theriomorphosis(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Theriomorphosis",
            "",  #TODO
            level,
            6
        )
        #TODO: track therioforms