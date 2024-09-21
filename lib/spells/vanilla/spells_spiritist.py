from lib.core.spell import Spell
from lib.core.constants import DamageType


class Spell_Aura(Spell):
    def __init__(self):
        super().__init__("Aura",
                         "todo",
                         offensive=False,
                         mp_per_target=5,
                         max_targets=3,
                         target_type="creature",
                         duration="scene")


class Spell_Awaken(Spell):
    def __init__(self):
        super().__init__("Awaken",
                         "todo",
                         offensive=False,
                         mp_per_target=20,
                         max_targets=1,
                         target_type="creature",
                         duration="scene")


class Spell_Barrier(Spell):
    def __init__(self):
        super().__init__("Barrier",
                         "todo",
                         offensive=False,
                         mp_per_target=5,
                         max_targets=3,
                         target_type="creature",
                         duration="scene")


class Spell_Cleanse(Spell):
    def __init__(self):
        super().__init__("Cleanse",
                         "todo",
                         offensive=False,
                         mp_per_target=5,
                         max_targets=3,
                         target_type="creature",
                         duration="instantaneous")


class Spell_Enrage(Spell): #TODO
    def __init__(self):
        super().__init__("Enrage",
                         "todo",
                         offensive=True,
                         mp_per_target=10,
                         max_targets=1,
                         target_type="creature",
                         duration="instantaneous")


class Spell_Hallucination(Spell): #TODO
    def __init__(self):
        super().__init__("Hallucination",
                         "todo",
                         offensive=True,
                         mp_per_target=5,
                         max_targets=3,
                         target_type="creature",
                         duration="instantaneous")


class Spell_Heal(Spell):
    def __init__(self):
        super().__init__("Heal",
                         "todo",
                         offensive=False,
                         mp_per_target=10,
                         max_targets=3,
                         target_type="creature",
                         duration="instantaneous")


class Spell_Lux(Spell):
    def __init__(self):
        super().__init__("Lux",
                         "todo",
                         offensive=True,
                         mp_per_target=10,
                         max_targets=3,
                         target_type="creature",
                         duration="instantaneous",
                         damage="HR+15",
                         damage_type=DamageType.LIGHT)


class Spell_Mercy(Spell):
    def __init__(self):
        super().__init__("Mercy",
                         "todo",
                         offensive=False,
                         mp_per_target=20,
                         max_targets=1,
                         target_type="creature",
                         duration="scene")


class Spell_Reinforce(Spell):
    def __init__(self):
        super().__init__("Reinforce",
                         "todo",
                         offensive=False,
                         mp_per_target=5,
                         max_targets=3,
                         target_type="creature",
                         duration="scene")


class Spell_SoulWeapon(Spell):
    def __init__(self):
        super().__init__("Soul Weapon",
                         "todo",
                         offensive=False,
                         mp_per_target=10,
                         max_targets=1,
                         target_type="equipped weapon",
                         duration="scene")


class Spell_Torpor(Spell): #TODO
    def __init__(self):
        super().__init__("Torpor",
                         "todo",
                         offensive=True,
                         mp_per_target=5,
                         max_targets=3,
                         target_type="creature",
                         duration="instantaneous")

