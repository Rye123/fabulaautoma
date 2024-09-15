from lib.core.item import Weapon
from lib.core.constants import DamageType, WeaponType


class WeaponStaff(Weapon):
    def __init__(self):
        super().__init__(
            "Staff", "", 100,
            martial=False,
            weapon_type=WeaponType.MELEE,
            two_handed=True,
            accuracy="WLP+WLP",
            damage="HR+6",
            damage_type=DamageType.PHYSICAL
        )


class WeaponTome(Weapon):
    def __init__(self):
        super().__init__(
            "Tome", "", 100,
            martial=False,
            weapon_type=WeaponType.MELEE,
            two_handed=True,
            accuracy="INS+INS",
            damage="HR+6",
            damage_type=DamageType.PHYSICAL
        )