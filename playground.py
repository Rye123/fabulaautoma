from lib.character import PlayerCharacter, NonPlayerCharacter
from lib.playerclass import *
from lib.core.item import Weapon, WeaponType, DamageType

from lib.items.weapons.weapons_sword import *
from lib.items.armors.basic_armors import *

class WeaponBreakerBladeV1(Weapon):
    def __init__(self):
        super().__init__(
            "Breaker Blade V1", "", 0,
            martial=True,
            weapon_type=WeaponType.MELEE,
            two_handed=True,
            accuracy="DEX+MIG",
            damage="HR+12",
            damage_type=DamageType.PHYSICAL
        )
        #TODO: customisations for custom weapons


if __name__ == "__main__":
    lirithid = PlayerCharacter("Lirithid", 10, 6, 10, 6, 10)
    lirithid.player_classes += [ClassEntropist(6), ClassChimerist(3), ClassWeaponmaster(1)]
    lirithid.compute()
    print(lirithid)

    print("---")
    fengtian = PlayerCharacter("Feng Tian", 5, 10, 10, 6, 6)
    fengtian.player_classes += [ClassSharpshooter(3), ClassRogue(1), ClassTinkerer(1)]
    fengtian.compute()
    print(fengtian)

    print("---")
    icaris = PlayerCharacter("Icaris", 10, 8, 8, 10, 6)
    icaris.player_classes += [ClassWeaponmaster(4), ClassEntropist(3)]  # haven't implemented pilot yet
    icaris.equipment.main_hand = WeaponBreakerBladeV1()
    icaris.equipment.armor = ArmorCombatTunic()
    icaris.compute()
    print(icaris)


