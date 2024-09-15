from lib.core.skill import Skill


class Skill_Agony(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Agony",
            "",  #TODO
            level,
            5
        )
        #TODO: track bonds


class Skill_DarkBlood(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Dark Blood",
            "",  #TODO
            level,
            1
        )
        #TODO: need to track affinities too lmao


class Skill_HeartOfDarkness(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Heart Of Darkness",
            "",  #TODO
            level,
            1
        )


class Skill_PainfulLesson(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Painful Lesson",
            "",  #TODO
            level,
            3
        )


class Skill_ShadowStrike(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Shadow Strike",
            "",  #TODO
            level,
            5
        )


