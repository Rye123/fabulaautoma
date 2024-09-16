from lib.core.item import Weapon
from lib.core.constants import DamageType, WeaponType


class Weapon_Crossbow(Weapon):
    def __init__(self):
        super().__init__(
            "Crossbow", "", 150,
            martial=False,
            weapon_type=WeaponType.RANGED,
            two_handed=True,
            accuracy="DEX+INS",
            damage="HR+8",
            damage_type=DamageType.PHYSICAL
        )


class Weapon_Shortbow(Weapon):
    def __init__(self):
        super().__init__(
            "Shortbow", "", 200,
            martial=False,
            weapon_type=WeaponType.MELEE,
            two_handed=True,
            accuracy="DEX+DEX",
            damage="HR+8",
            damage_type=DamageType.PHYSICAL
        )