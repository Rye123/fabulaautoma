from lib.core.skill import Skill


class Skill_Condemn(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Condemn",
            "",  #TODO
            level,
            4
        )
        #TODO: this should appear as a possible action


class Skill_Encourage(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Encourage",
            "",  #TODO
            level,
            6
        )
        #TODO: this should appear as a possible action


class Skill_MyTrustInYou(Skill):
    def __init__(self, level: int):
        super().__init__(
            "My Trust In You",
            "",  #TODO
            level,
            2
        )


class Skill_Persuasive(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Persuasive",
            "",  #TODO
            level,
            2
        )


class Skill_UnexpectedAlly(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Unexpected ally",
            "",  #TODO
            level,
            1
        )

