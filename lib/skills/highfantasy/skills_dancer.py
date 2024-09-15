from lib.core.skill import Skill


class Skill_Dance(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Dance",
            "",  #TODO
            level,
            10
        )
        #TODO: track dances


class Skill_FollowMyLead(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Follow My Lead",
            "",  #TODO
            level,
            1
        )
        #TODO: check when doing a dance


class Skill_FreneticFootwork(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Frenetic Footwork",
            "",  #TODO
            level,
            2
        )
        #TODO: check when doing a dance


class Skill_QuickChange(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Quick-Change",
            "",  #TODO
            level,
            1
        )
        #TODO: check when doing a dance


class Skill_Wardancer(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Wardancer",
            "",  #TODO
            level,
            5
        )
        #TODO: check when doing a dance

