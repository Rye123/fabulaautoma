from lib.core.skill import Skill


class Skill_CognitiveFocus(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Cognitive Focus",
            "",  #TODO
            level,
            5
        )


class Skill_Hypercognition(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Hypercognition",
            "",  #TODO
            level,
            3
        )


class Skill_Navigator(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Navigator",
            "",  #TODO
            level,
            3
        )
        #TODO


class Skill_PsychicGifts(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Psychic Gifts",
            "",  #TODO
            level,
            5
        )
        #TODO: track gifts


class Skill_Psychokinesis(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Psychokinesis",
            "",  #TODO
            level,
            1
        )