from lib.core.spell import Spell
from lib.core.constants import DamageType


class Spell_Acceleration(Spell):
    def __init__(self):
        super().__init__("Acceleration",
                         "todo",
                         offensive=False,
                         mp_per_target=20,
                         max_targets=1,
                         target_type="creature",
                         duration="scene")


class Spell_Anomaly(Spell):
    def __init__(self):
        super().__init__("Anomaly",
                         "todo",
                         offensive=True,
                         mp_per_target=20,
                         max_targets=1,
                         target_type="creature",
                         duration="scene")


class Spell_DarkWeapon(Spell):
    def __init__(self):
        super().__init__("Dark Weapon",
                         "todo",
                         offensive=False,
                         mp_per_target=10,
                         max_targets=1,
                         target_type="equipped weapon",
                         duration="scene")


class Spell_Dispel(Spell):
    def __init__(self):
        super().__init__("Dispel",
                         "todo",
                         offensive=False,
                         mp_per_target=10,
                         max_targets=1,
                         target_type="creature",
                         duration="instantaneous")


class Spell_Divination(Spell):
    def __init__(self):
        super().__init__("Divination",
                         "todo",
                         offensive=False,
                         mp_per_target=10,
                         max_targets=1,
                         target_type="self",
                         duration="scene")


class Spell_DrainSpirit(Spell): #TODO
    def __init__(self):
        super().__init__("Drain Spirit",
                         "todo",
                         offensive=True,
                         mp_per_target=5,
                         max_targets=1,
                         target_type="creature",
                         duration="instantaneous")


class Spell_DrainVigor(Spell):
    def __init__(self):
        super().__init__("Drain Vigor",
                         "todo",
                         offensive=True,
                         mp_per_target=10,
                         max_targets=1,
                         target_type="creature",
                         duration="instantaneous",
                         damage="HR+15",
                         damage_type=DamageType.DARK)


class Spell_Gamble(Spell): #TODO
    def __init__(self):
        super().__init__("Gamble",
                         "todo",
                         offensive=False,
                         mp_per_target=20,
                         max_targets=1,
                         target_type="special",
                         duration="instantaneous")


class Spell_Mirror(Spell):
    def __init__(self):
        super().__init__("Mirror",
                         "todo",
                         offensive=False,
                         mp_per_target=10,
                         max_targets=1,
                         target_type="creature",
                         duration="scene")


class Spell_Omega(Spell): #TODO
    def __init__(self):
        super().__init__("Omega",
                         "todo",
                         offensive=True,
                         mp_per_target=20,
                         max_targets=1,
                         target_type="creature",
                         duration="instantaneous")


class Spell_Stop(Spell):
    def __init__(self):
        super().__init__("Stop",
                         "todo",
                         offensive=True,
                         mp_per_target=10,
                         max_targets=1,
                         target_type="creature",
                         duration="instantaneous")


class Spell_Umbra(Spell):
    def __init__(self):
        super().__init__("Umbra",
                         "todo",
                         offensive=True,
                         mp_per_target=10,
                         max_targets=3,
                         target_type="creature",
                         duration="instantaneous",
                         damage="HR+15",
                         damage_type=DamageType.DARK)

