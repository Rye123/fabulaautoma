from lib.core.character import Character
from lib.core.skill import Skill


class Skill_AbsorbMP(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Absorb MP",
            "",  #TODO
            level,
            5
        )
        #TODO: probably need to track when char suffers damage


class Skill_EntropicMagic(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Entropic Magic",
            "",  #TODO
            level,
            10
        )


class Skill_LuckySeven(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Lucky Seven",
            "",  #TODO
            level,
            1
        )
        #TODO: track current lucky number


class Skill_RitualEntropism(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Ritual Entropism",
            "",  #TODO
            level,
            1
        )

    def apply_stats(self, char: Character):
        if self.level > 0:
            char.stats.rituals.entropism = True


class Skill_StolenTime(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Stolen Time",
            "",  #TODO
            level,
            4
        )
        #TODO: another action to track.........


