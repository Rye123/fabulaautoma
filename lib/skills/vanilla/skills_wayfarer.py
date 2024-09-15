from lib.core.skill import Skill


class Skill_FaithfulCompanion(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Faithful Companion",
            "",  #TODO
            level,
            5
        )
        #TODO: maybe link the 'NPC'?


class Skill_Resourceful(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Resourceful",
            "",  #TODO
            level,
            4
        )
        #TODO: to implement this would require implementing
        #TODO: 'travel rolls', but i haven't reached there yet


class Skill_TavernTalk(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Tavern Talk",
            "",  #TODO
            level,
            3
        )


class Skill_TreasureHunter(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Treasure Hunter",
            "",  #TODO
            level,
            2
        )


class Skill_WellTraveled(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Well-Traveled",
            "",  #TODO
            level,
            1
        )

