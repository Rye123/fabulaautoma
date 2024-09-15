from lib.core.skill import Skill


class Skill_CompressionTech(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Compression Tech",
            "",  #TODO
            level,
            1
        )


class Skill_FlexibleConfiguration(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Flexible Configuration",
            "",  #TODO
            level,
            4
        )


class Skill_HeartInTheMachine(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Heart In The Machine",
            "",  #TODO
            level,
            3
        )


class Skill_PersonalVehicle(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Personal Vehicle",
            "",  #TODO
            level,
            5
        )
        #TODO: track vehicle and modules


class Skill_StrongGrip(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Strong Grip",
            "",  #TODO
            level,
            1
        )

