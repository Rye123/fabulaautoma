from lib.core.item import Weapon
from lib.core.constants import DamageType, WeaponType


class Weapon_IronHammer(Weapon):
    def __init__(self):
        super().__init__(
            "Iron Hammer", "", 200,
            martial=False,
            weapon_type=WeaponType.MELEE,
            two_handed=False,
            accuracy="MIG+MIG",
            damage="HR+6",
            damage_type=DamageType.PHYSICAL
        )


class Weapon_Broadaxe(Weapon):
    def __init__(self):
        super().__init__(
            "Broadaxe", "", 250,
            martial=True,
            weapon_type=WeaponType.MELEE,
            two_handed=False,
            accuracy="MIG+MIG",
            damage="HR+10",
            damage_type=DamageType.PHYSICAL
        )


class Weapon_Waraxe(Weapon):
    def __init__(self):
        super().__init__(
            "Waraxe", "", 250,
            martial=True,
            weapon_type=WeaponType.MELEE,
            two_handed=True,
            accuracy="MIG+MIG",
            damage="HR+14",
            damage_type=DamageType.PHYSICAL
        )
