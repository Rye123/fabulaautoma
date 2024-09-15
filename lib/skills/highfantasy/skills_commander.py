from lib.core.skill import Skill


class Skill_BishopsEdict(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Bishop's Edict",
            "",  #TODO
            level,
            5
        )
        #TODO: another action


class Skill_ChargingCavalry(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Charging Cavalry",
            "",  #TODO
            level,
            5
        )
        #TODO: another action


class Skill_CrushingChariot(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Crushing Chariot",
            "",  #TODO
            level,
            1
        )
        #TODO: another action


class Skill_KingsCastle(Skill):
    def __init__(self, level: int):
        super().__init__(
            "King's Castle",
            "",  #TODO
            level,
            4
        )
        #TODO: another action


class Skill_QueensGambit(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Queen's Gambit",
            "",  #TODO
            level,
            6
        )
        #TODO: another action