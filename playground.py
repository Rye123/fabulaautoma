from lib.playerclasses.vanilla import *
from lib.playerclasses.technofantasy import *

from lib.items.weapons.weapons_sword import *
from lib.items.weapons.weapons_dagger import *
from lib.items.weapons.weapons_thrown import *
from lib.items.armors.basic_armors import *

from lib.skills.vanilla.skills_tinkerer import *
from lib.skills.vanilla.skills_loremaster import *
from lib.skills.vanilla.skills_darkblade import *
from lib.skills.vanilla.skills_spiritist import *
from lib.skills.vanilla.skills_guardian import *

class Weapon_BreakerBladeV1(Weapon):
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
    # lirithid = PlayerCharacter("Lirithid", 10, 6, 10, 6, 10)
    # lirithid.player_classes += [Class_Entropist(6), Class_Chimerist(3), Class_Weaponmaster(1)]
    # lirithid.compute()
    # print(lirithid)

    # print("---")
    # fengtian = PlayerCharacter("Feng Tian", 5, 10, 10, 6, 6)
    # fengtian.player_classes += [Class_Sharpshooter(3), Class_Rogue(1), Class_Tinkerer(1)]
    # fengtian.compute()
    # print(fengtian)

    print("---")
    icaris = PlayerCharacter("Icaris", 10, 8, 8, 10, 6)
    icaris.player_classes += [Class_Weaponmaster(4), Class_Entropist(3), Class_Pilot(3)]
    icaris.equipment.main_hand = Weapon_BreakerBladeV1()
    icaris.equipment.armor = Armor_CombatTunic()
    icaris.compute()
    print(icaris)

    # print("---")
    # chroma = PlayerCharacter("Chroma Aber", 10, 6, 10, 6, 10)
    # chroma.player_classes += [Class_Tinkerer(6), Class_Loremaster(4)]
    # chroma.equipment.main_hand = Weapon_SteelDagger()
    # chroma.equipment.off_hand = Weapon_Shuriken()
    # chroma.skills += [
    #     Skill_Gadgets(4), Skill_SecretFormula(1),
    #     Skill_KnowledgeIsPower(1), Skill_TrainedMemory(1),
    #     Skill_QuickAssessment(1), Skill_Focused(1)
    # ]
    # chroma.compute()
    # print(chroma)

    # print("---")
    # nova = PlayerCharacter("NoVA", 10, 6, 10, 10, 6)
    # nova.player_classes += [Class_Darkblade(6), Class_Guardian(1), Class_Spiritist(3)]
    # nova.skills += [
    #     Skill_Agony(2), Skill_DarkBlood(1), Skill_HeartOfDarkness(1), Skill_PainfulLesson(1), Skill_ShadowStrike(1),
    #     Skill_Protect(1), Skill_SpiritualMagic(2), Skill_Vismagus(1)
    # ]
    # nova.compute()
    # print(nova)
