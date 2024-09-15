from lib.core.skill import Skill


class Skill_EmergencyItem(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Emergency Item",
            "",  #TODO
            level,
            1
        )


class Skill_Gadgets(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Gadgets",
            "",  #TODO
            level,
            5
        )
        #TODO: implement the gadgets


class Skill_PotionRain(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Potion Rain",
            "",  #TODO
            level,
            2
        )
        #TODO: to implement when a potion is created?


class Skill_SecretFormula(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Secret Formula",
            "",  #TODO
            level,
            5
        )
        #TODO: to implement when a potion/magisphere is created?


class Skill_Visionary(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Visionary",
            "",  #TODO
            level,
            5
        )

