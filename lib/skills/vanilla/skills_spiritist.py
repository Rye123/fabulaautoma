from lib.core.character import Character
from lib.core.skill import Skill


class Skill_HealingPower(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Healing Power",
            "",  #TODO
            level,
            2
        )
        #TODO: not sure how to implement, but would be nice
        #TODO: for these to be automatically computed


class Skill_RitualSpiritism(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Ritual Spiritism",
            "",  #TODO
            level,
            1
        )

    def apply_stats(self, char: Character):
        if self.level > 0:
            char.stats.rituals.spiritism = True


class Skill_SpiritualMagic(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Spiritual Magic",
            "",  #TODO
            level,
            10
        )
        #TODO: spells would probably be under the character, but
        #TODO: there needs to be some way to link the number of spells
        #TODO: used to this


class Skill_SupportMagic(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Support Magic",
            "",  #TODO
            level,
            1
        )


class Skill_Vismagus(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Vismagus",
            "",  #TODO
            level,
            1
        )

