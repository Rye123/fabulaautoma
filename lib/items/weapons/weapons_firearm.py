from lib.core.item import Weapon
from lib.core.constants import DamageType, WeaponType


class WeaponPistol(Weapon):
    def __init__(self):
        super().__init__(
            "Pistol", "", 250,
            martial=True,
            weapon_type=WeaponType.RANGED,
            two_handed=False,
            accuracy="DEX+INS",
            damage="HR+8",
            damage_type=DamageType.PHYSICAL
        )