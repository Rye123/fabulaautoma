from lib.core.skill import Skill


class Skill_Bladestorm(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Bladestorm",
            "",  #TODO
            level,
            1
        )

        #TODO: not sure how to make a general way to make this programmatically
        #TODO: available, might need to just make this a flavour thing
        #TODO: that the player must keep track of


class Skill_BoneCrusher(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Bone Crusher",
            "",  #TODO
            level,
            4
        )


class Skill_Breach(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Breach",
            "",  #TODO
            level,
            3
        )


class Skill_Counterattack(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Bone Crusher",
            "",  #TODO
            level,
            1
        )


class Skill_MeleeWeaponMastery(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Melee Weapon Mastery",
            "",  #TODO
            level,
            4
        )
        #TODO: find some way to add this bonus to all Accuracy Checks,
        #TODO: if we're implementing checks lmao

