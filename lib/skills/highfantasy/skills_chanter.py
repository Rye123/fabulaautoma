from lib.core.character import Character
from lib.core.skill import Skill


class Skill_Magichant(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Magichant",
            "",  #TODO
            level,
            10
        )


class Skill_Resonance(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Resonance",
            "",  #TODO
            level,
            3
        )


class Skill_SirensSong(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Siren's Song",
            "",  #TODO
            level,
            1
        )

    def apply_stats(self, char: Character):
        if self.level > 0:
            char.stats.rituals.ritualism = True


class Skill_SoundBarrier(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Sound Barrier",
            "",  #TODO
            level,
            5
        )


class Skill_Vibrato(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Vibrato",
            "",  #TODO
            level,
            1
        )

