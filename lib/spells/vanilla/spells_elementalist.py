from lib.core.spell import Spell
from lib.core.constants import DamageType


class Spell_ElementalShroud(Spell):
    def __init__(self):
        super().__init__("Elemental Shroud",
                         "todo",
                         offensive=False,
                         mp_per_target=5,
                         max_targets=3,
                         target_type="creature",
                         duration="scene")


class Spell_ElementalWeapon(Spell):
    def __init__(self):
        super().__init__("Elemental Weapon",
                         "todo",
                         offensive=False,
                         mp_per_target=10,
                         max_targets=1,
                         target_type="weapon",
                         duration="scene")


class Spell_Flare(Spell):
    def __init__(self):
        super().__init__("Flare",
                         "todo",
                         offensive=True,
                         mp_per_target=20,
                         max_targets=1,
                         target_type="creature",
                         duration="instantaneous",
                         damage="HR+25",
                         damage_type=DamageType.FIRE)


class Spell_Fulgur(Spell):
    def __init__(self):
        super().__init__("Fulgur",
                         "todo",
                         offensive=True,
                         mp_per_target=10,
                         max_targets=3,
                         target_type="creature",
                         duration="instantaneous",
                         damage="HR+15",
                         damage_type=DamageType.BOLT)


class Spell_Glacies(Spell):
    def __init__(self):
        super().__init__("Glacies",
                         "todo",
                         offensive=True,
                         mp_per_target=10,
                         max_targets=3,
                         target_type="creature",
                         duration="instantaneous",
                         damage="HR+15",
                         damage_type=DamageType.ICE)


class Spell_Iceberg(Spell):
    def __init__(self):
        super().__init__("Iceberg",
                         "todo",
                         offensive=True,
                         mp_per_target=20,
                         max_targets=1,
                         target_type="creature",
                         duration="instantaneous",
                         damage="HR+25",
                         damage_type=DamageType.ICE)


class Spell_Ignis(Spell):
    def __init__(self):
        super().__init__("Ignis",
                         "todo",
                         offensive=True,
                         mp_per_target=10,
                         max_targets=3,
                         target_type="creature",
                         duration="instantaneous",
                         damage="HR+15",
                         damage_type=DamageType.FIRE)


class Spell_SoaringStrike(Spell):
    def __init__(self):
        super().__init__("Soaring Strike",
                         "todo",
                         offensive=False,
                         mp_per_target=10,
                         max_targets=1,
                         target_type="self",
                         duration="instantaneous")


class Spell_Terra(Spell):
    def __init__(self):
        super().__init__("Terra",
                         "todo",
                         offensive=True,
                         mp_per_target=10,
                         max_targets=3,
                         target_type="creature",
                         duration="instantaneous",
                         damage="HR+15",
                         damage_type=DamageType.EARTH)


class Spell_Thunderbolt(Spell):
    def __init__(self):
        super().__init__("Thunderbolt",
                         "todo",
                         offensive=True,
                         mp_per_target=20,
                         max_targets=1,
                         target_type="creature",
                         duration="instantaneous",
                         damage="HR+25",
                         damage_type=DamageType.BOLT)


class Spell_Ventus(Spell):
    def __init__(self):
        super().__init__("Ventus",
                         "todo",
                         offensive=True,
                         mp_per_target=10,
                         max_targets=3,
                         target_type="creature",
                         duration="instantaneous",
                         damage="HR+15",
                         damage_type=DamageType.AIR)


class Spell_Vortex(Spell):
    def __init__(self):
        super().__init__("Vortex",
                         "todo",
                         offensive=False,
                         mp_per_target=10,
                         max_targets=1,
                         target_type="self",
                         duration="")

