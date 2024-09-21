import unittest
from lib.playerclasses.vanilla import *
from lib.core.character import Stats


class CharacterMixin:
    def assertPlayerCharacter(self, char: PlayerCharacter,
                              exp_hp_max: int,
                              exp_mp_max: int,
                              exp_ip_max: int,
                              exp_initiative: int,
                              exp_initiative_modifier: int,
                              exp_defense_physical: int,
                              exp_defense_magical: int,
                              exp_martial_equip: Stats.MartialEquip,
                              exp_rituals: Stats.Rituals,
                              exp_affinities: Stats.Affinities):
        if char.stats.hp_max != exp_hp_max:
            raise AssertionError(f"hp_max Mismatch for character {char.name}: Expected {exp_hp_max}, got {char.stats.hp_max}, with breakdown: {char.stats.breakdown.hp_max}")
        if char.stats.mp_max != exp_mp_max:
            raise AssertionError(f"mp_max Mismatch for character {char.name}: Expected {exp_mp_max}, got {char.stats.mp_max}, with breakdown: {char.stats.breakdown.mp_max}")
        if char.stats.ip_max != exp_ip_max:
            raise AssertionError(f"ip_max Mismatch for character {char.name}: Expected {exp_ip_max}, got {char.stats.ip_max}, with breakdown: {char.stats.breakdown.ip_max}")
        if char.stats.initiative != exp_initiative:
            raise AssertionError(f"initiative Mismatch for character {char.name}: Expected {exp_initiative}, got {char.stats.initiative}, with breakdown: {char.stats.breakdown.initiative}")
        if char.stats.initiative_modifier != exp_initiative_modifier:
            raise AssertionError(f"mp_max Mismatch for character {char.name}: Expected {exp_initiative_modifier}, got {char.stats.initiative_modifier}, with breakdown: {char.stats.breakdown.initiative_modifier}")
        if char.stats.defense_physical != exp_defense_physical:
            raise AssertionError(f"defense_physical Mismatch for character {char.name}: Expected {exp_defense_physical}, got {char.stats.defense_physical}, with breakdown: {char.stats.breakdown.defense_physical}")
        if char.stats.defense_magical != exp_defense_magical:
            raise AssertionError(f"defense_magical Mismatch for character {char.name}: Expected {exp_defense_magical}, got {char.stats.defense_magical}, with breakdown: {char.stats.breakdown.defense_magical}")
        if char.stats.martial_equip != exp_martial_equip:
            raise AssertionError(f"martial_equip Mismatch for character {char.name}: Expected martial equip ({exp_martial_equip}), got martial equip ({char.stats.martial_equip})")
        if char.stats.rituals != exp_rituals:
            raise AssertionError(f"rituals Mismatch for character {char.name}: Expected rituals ({exp_rituals}), got rituals ({char.stats.rituals})")
        if char.stats.affinities != exp_affinities:
            raise AssertionError(f"affinities Mismatch for character {char.name}: Expected affinities ({exp_affinities}), got affinities ({char.stats.affinities}), with breakdown: {char.stats.breakdown.affinities}")


class TestPlayerCharacter(unittest.TestCase, CharacterMixin):
    """ Test the computation of stats, based on attributes, classes, skills and equipment. """

    def test_base(self):
        level = 10
        dex = 8
        ins = 8
        mgt = 8
        wlp = 8
        char = PlayerCharacter("Test Character 1", level, dex, ins, mgt, wlp)
        char.compute()

        self.assertPlayerCharacter(char,
                                   level + (5 * mgt),
                                   level + (5 * wlp),
                                   6,
                                   0, 0,
                                   dex, ins, Stats.MartialEquip(), Stats.Rituals(), Stats.Affinities())

        level = 8
        dex = 6
        ins = 6
        mgt = 10
        wlp = 10
        char = PlayerCharacter("Test Character 2", level, dex, ins, mgt, wlp)
        char.compute()

        self.assertPlayerCharacter(char,
                                   level + (5 * mgt),
                                   level + (5 * wlp),
                                   6,
                                   0, 0,
                                   dex, ins, Stats.MartialEquip(), Stats.Rituals(), Stats.Affinities())

    def test_classes(self):
        level = 10
        dex = 8
        ins = 8
        mgt = 8
        wlp = 8
        char = PlayerCharacter("WeaponmasterOrator", level, dex, ins, mgt, wlp)
        char.player_classes = [Class_Weaponmaster(4), Class_Orator(6)]
        char.compute()

        self.assertPlayerCharacter(char,
                                   level + (5 * mgt) + 5,  # 5 from Weaponmaster
                                   level + (5 * wlp) + 5,  # 5 from Orator
                                   6,
                                   0, 0,
                                   dex, ins,
                                   Stats.MartialEquip(melee=True, shield=True), Stats.Rituals(), Stats.Affinities())

        level = 7
        dex = 6
        ins = 10
        mgt = 6
        wlp = 10
        char = PlayerCharacter("ArcanistChimerist", level, dex, ins, mgt, wlp)
        char.player_classes = [Class_Arcanist(3), Class_Chimerist(4)]
        char.compute()

        self.assertPlayerCharacter(char,
                                   level + (5 * mgt),
                                   level + (5 * wlp) + 10,  # 5+5 from Arcanist and Chimerist
                                   6,
                                   0, 0,
                                   dex, ins,
                                   Stats.MartialEquip(),
                                   Stats.Rituals(ritualism=True),
                                   Stats.Affinities())

        level = 4
        dex = 10
        ins = 6
        mgt = 10
        wlp = 6
        char = PlayerCharacter("SpiritistTinkererWayfarer", level, dex, ins, mgt, wlp)
        char.player_classes = [Class_Spiritist(1), Class_Tinkerer(2), Class_Wayfarer(1)]
        char.compute()

        self.assertPlayerCharacter(char,
                                   level + (5 * mgt),
                                   level + (5 * wlp) + 5,  # 5 from Spiritist
                                   6 + 4,                  # 2+2 from Tinkerer and Wayfarer
                                   0, 0,
                                   dex, ins,
                                   Stats.MartialEquip(),
                                   Stats.Rituals(ritualism=True),
                                   Stats.Affinities())
        self.assertEqual(char.stats.can_start_projects, True)

    def test_skills(self):
        import lib.skills.vanilla.skills_spiritist as skills_spiritist
        import lib.skills.vanilla.skills_loremaster as skills_loremaster
        import lib.skills.vanilla.skills_guardian as skills_guardian
        level = 1
        dex = 6
        ins = 10
        mgt = 6
        wlp = 10
        char = PlayerCharacter("Spiritist", level, dex, ins, mgt, wlp)
        char.player_classes = [Class_Spiritist(1)]
        char.skills = [skills_spiritist.Skill_RitualSpiritism(1)]
        char.compute()

        self.assertPlayerCharacter(char,
                                   level + (5 * mgt),
                                   level + (5 * wlp) + 5,  # 5 from Spiritist
                                   6,
                                   0, 0,
                                   dex, ins,
                                   Stats.MartialEquip(),
                                   Stats.Rituals(ritualism=True, spiritism=True),
                                   Stats.Affinities())

        level = 3
        dex = 6
        ins = 10
        mgt = 6
        wlp = 10
        focused_sl = 3
        char = PlayerCharacter("Loremaster", level, dex, ins, mgt, wlp)
        char.player_classes = [Class_Loremaster(3)]
        char.skills = [skills_loremaster.Skill_Focused(focused_sl)]
        char.compute()

        self.assertPlayerCharacter(char,
                                   level + (5 * mgt),
                                   level + (5 * wlp) + 5 + (focused_sl * 3),  # 5 from Loremaster & Focused
                                   6,
                                   0, 0,
                                   dex, ins,
                                   Stats.MartialEquip(),
                                   Stats.Rituals(),
                                   Stats.Affinities())

        level = 5
        dex = 8
        ins = 8
        mgt = 8
        wlp = 8
        fortress_sl = 5
        char = PlayerCharacter("Guardian", level, dex, ins, mgt, wlp)
        char.player_classes = [Class_Guardian(5)]
        char.skills = [skills_guardian.Skill_Fortress(fortress_sl)]
        char.compute()

        self.assertPlayerCharacter(char,
                                   level + (5 * mgt) + 5 + (fortress_sl * 3),
                                   level + (5 * wlp),
                                   6,
                                   0, 0,
                                   dex, ins,
                                   Stats.MartialEquip(armor=True, shield=True),
                                   Stats.Rituals(),
                                   Stats.Affinities())

    def test_armor(self):
        from lib.items.armors.basic_armors import Armor_SilkShirt, Armor_TravelGarb, Armor_SteelPlate
        level = 10
        dex = 8
        ins = 8
        mgt = 8
        wlp = 8
        char = PlayerCharacter("SilkShirt", level, dex, ins, mgt, wlp)
        char.equipment.armor = Armor_SilkShirt()
        char.compute()

        self.assertPlayerCharacter(char,
                                   level + (5 * mgt),
                                   level + (5 * wlp),
                                   6,
                                   0, -1,
                                   dex, ins+2, Stats.MartialEquip(), Stats.Rituals(), Stats.Affinities())

        char = PlayerCharacter("TravelGarb", level, dex, ins, mgt, wlp)
        char.equipment.armor = Armor_TravelGarb()
        char.compute()

        self.assertPlayerCharacter(char,
                                   level + (5 * mgt),
                                   level + (5 * wlp),
                                   6,
                                   0, -1,
                                   dex+1, ins+1, Stats.MartialEquip(), Stats.Rituals(), Stats.Affinities())

        char = PlayerCharacter("SteelPlate", level, dex, ins, mgt, wlp)
        char.equipment.armor = Armor_SteelPlate()
        char.compute()

        self.assertPlayerCharacter(char,
                                   level + (5 * mgt),
                                   level + (5 * wlp),
                                   6,
                                   0, -4,
                                   12, ins, Stats.MartialEquip(), Stats.Rituals(), Stats.Affinities())


if __name__ == '__main__':
    unittest.main()
