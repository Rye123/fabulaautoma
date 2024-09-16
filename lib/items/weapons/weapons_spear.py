from lib.core.item import Weapon
from lib.core.constants import DamageType, WeaponType


class Weapon_LightSpear(Weapon):
    def __init__(self):
        super().__init__(
            "Light Spear", "", 200,
            martial=True,
            weapon_type=WeaponType.MELEE,
            two_handed=False,
            accuracy="DEX+MIG",
            damage="HR+8",
            damage_type=DamageType.PHYSICAL
        )


class Weapon_HeavySpear(Weapon):
    def __init__(self):
        super().__init__(
            "Heavy Spear", "", 200,
            martial=True,
            weapon_type=WeaponType.MELEE,
            two_handed=True,
            accuracy="DEX+MIG",
            damage="HR+12",
            damage_type=DamageType.PHYSICAL
        )
