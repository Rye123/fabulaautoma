from lib.core.skill import Skill


class Skill_BeyondTheRealmsOfDeath(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Beyond The Realms Of Death",
            "",  #TODO
            level,
            5
        )
        #TODO: track grave points


class Skill_ChildrenOfTheGrave(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Children Of The Grave",
            "",  #TODO
            level,
            1
        )


class Skill_FearIsTheKey(Skill):
    def __init__(self, level: int):
        super().__init__(
            "Fear Is The Key",
            "",  #TODO
            level,
            3
        )
        #TODO: again, need to track dmg done


class Skill_ForWhomTheBellTolls(Skill):
    def __init__(self, level: int):
        super().__init__(
            "For Whom The Bell Tolls",
            "",  #TODO
            level,
            3
        )
        #TODO: again, need to track dmg done


class Skill_RondoOfNightmare(Skill):
    def __init__(self, level: int):
        super().__init__(
            "RondoOfNightmare",
            "",  #TODO
            level,
            3
        )

