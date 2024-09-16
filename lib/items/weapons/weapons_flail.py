from lib.core.item import Weapon
from lib.core.constants import DamageType, WeaponType


class Weapon_Flail(Weapon):
    def __init__(self):
        super().__init__(
            "Flail", "", 150,
            martial=False,
            weapon_type=WeaponType.MELEE,
            two_handed=True,
            accuracy="DEX+DEX",
            damage="HR+8",
            damage_type=DamageType.PHYSICAL
        )