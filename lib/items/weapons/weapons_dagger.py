from lib.core.item import Weapon
from lib.core.constants import DamageType, WeaponType


class Weapon_SteelDagger(Weapon):
    def __init__(self):
        super().__init__(
            "Steel Dagger", "", 150,
            martial=False,
            weapon_type=WeaponType.MELEE,
            two_handed=False,
            accuracy="DEX+INS+1",
            damage="HR+4",
            damage_type=DamageType.PHYSICAL
        )