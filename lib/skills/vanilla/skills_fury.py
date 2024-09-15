from lib.core.skill import Skill


class Skill_Adrenaline(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Adrenaline",
            "",  #TODO
            level,
            5
        )
        #TODO: track if got crisis, and add damage accordingly


class Skill_Frenzy(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Frenzy",
            "",  #TODO
            level,
            1
        )


class Skill_IndomitableSpirit(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Indomitable Spirit",
            "",  #TODO
            level,
            4
        )
        #TODO: probably need to track fabula spending


class Skill_Provoke(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Provoke",
            "",  #TODO
            level,
            5
        )


class Skill_Withstand(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Withstand",
            "",  #TODO
            level,
            5
        )

