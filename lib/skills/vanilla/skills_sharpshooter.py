from lib.core.skill import Skill


class Skill_Barrage(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Barrage",
            "",  #TODO
            level,
            1
        )
        #TODO: would be good to display these choices


class Skill_Crossfire(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Crossfire",
            "",  #TODO
            level,
            1
        )


class Skill_Hawkeye(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Hawkeye",
            "",  #TODO
            level,
            5
        )


class Skill_RangedWeaponMastery(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Ranged Weapon Mastery",
            "",  #TODO
            level,
            4
        )
        #TODO: some way to add this to accuracy checks


class Skill_WarningShot(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Warning Shot",
            "",  #TODO
            level,
            4
        )