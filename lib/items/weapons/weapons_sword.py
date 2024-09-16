from lib.core.item import Weapon
from lib.core.constants import DamageType, WeaponType


class Weapon_BronzeSword(Weapon):
    def __init__(self):
        super().__init__(
            "Bronze Sword", "", 200,
            martial=True,
            weapon_type=WeaponType.MELEE,
            two_handed=False,
            accuracy="DEX+MIG+1",
            damage="HR+6",
            damage_type=DamageType.PHYSICAL
        )


class Weapon_Greatsword(Weapon):
    def __init__(self):
        super().__init__(
            "Greatsword", "", 200,
            martial=True,
            weapon_type=WeaponType.MELEE,
            two_handed=True,
            accuracy="DEX+MIG+1",
            damage="HR+10",
            damage_type=DamageType.PHYSICAL
        )


class Weapon_Katana(Weapon):
    def __init__(self):
        super().__init__(
            "Katana", "", 200,
            martial=True,
            weapon_type=WeaponType.MELEE,
            two_handed=True,
            accuracy="DEX+INS+1",
            damage="HR+10",
            damage_type=DamageType.PHYSICAL
        )


class Weapon_Rapier(Weapon):
    def __init__(self):
        super().__init__(
            "Rapier", "", 200,
            martial=True,
            weapon_type=WeaponType.MELEE,
            two_handed=False,
            accuracy="DEX+INS+1",
            damage="HR+6",
            damage_type=DamageType.PHYSICAL
        )


