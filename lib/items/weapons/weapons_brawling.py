from lib.core.item import Weapon
from lib.core.constants import DamageType, WeaponType


class Weapon_Unarmed(Weapon):
    def __init__(self):
        super().__init__(
            "Unarmed Strike", "Automatically equipped in each empty hand slot.", 0,
            martial=False,
            weapon_type=WeaponType.MELEE,
            two_handed=False,
            accuracy="DEX+MIG",
            damage="HR+0",
            damage_type=DamageType.PHYSICAL
        )


class Weapon_ImprovisedMelee(Weapon):
    def __init__(self):
        super().__init__(
            "Improvised (Melee)", "Breaks after the attack.", 0,
            martial=False,
            weapon_type=WeaponType.MELEE,
            two_handed=False,
            accuracy="DEX+MIG",
            damage="HR+2",
            damage_type=DamageType.PHYSICAL
        )


class Weapon_IronKnuckle(Weapon):
    def __init__(self):
        super().__init__(
            "Iron Knuckle", "", 150,
            martial=False,
            weapon_type=WeaponType.MELEE,
            two_handed=False,
            accuracy="DEX+MIG",
            damage="HR+6",
            damage_type=DamageType.PHYSICAL
        )