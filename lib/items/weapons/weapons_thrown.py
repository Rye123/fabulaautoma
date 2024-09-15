from lib.core.item import Weapon
from lib.core.constants import DamageType, WeaponType


class WeaponImprovisedRanged(Weapon):
    def __init__(self):
        super().__init__(
            "Improvised (Ranged)", "Breaks after the attack.", 0,
            martial=False,
            weapon_type=WeaponType.RANGED,
            two_handed=False,
            accuracy="DEX+MIG",
            damage="HR+2",
            damage_type=DamageType.PHYSICAL
        )


class WeaponShuriken(Weapon):
    def __init__(self):
        super().__init__(
            "Shuriken", "", 150,
            martial=False,
            weapon_type=WeaponType.RANGED,
            two_handed=False,
            accuracy="DEX+INS",
            damage="HR+4",
            damage_type=DamageType.PHYSICAL
        )

