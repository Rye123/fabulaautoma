import unittest
from lib.playerclasses.vanilla import *


class TestPlayerCharacter(unittest.TestCase):
    """ Test the computation of stats, based on attributes and classes. """

    def test_lirithid(self):
        lirithid = PlayerCharacter("Lirithid", 10, 6, 10, 6, 10)
        lirithid.player_classes += [Class_Entropist(6), Class_Chimerist(3), Class_Weaponmaster(1)]
        lirithid.compute()

        self.assertEqual(lirithid.stats.hp_max, 45)
        self.assertEqual(lirithid.stats.mp_max, 70)
        self.assertEqual(lirithid.stats.ip_max, 6)
        self.assertEqual(lirithid.stats.initiative, 10)
        self.assertEqual(lirithid.stats.defense_physical, 6)
        self.assertEqual(lirithid.stats.defense_magical, 10)

    def test_fengtian(self):
        fengtian = PlayerCharacter("Feng Tian", 5, 10, 10, 6, 6)
        fengtian.player_classes += [Class_Sharpshooter(3), Class_Rogue(1), Class_Tinkerer(1)]
        fengtian.compute()

        self.assertEqual(fengtian.stats.hp_max, 40)
        self.assertEqual(fengtian.stats.mp_max, 35)
        self.assertEqual(fengtian.stats.ip_max, 10)
        self.assertEqual(fengtian.stats.initiative, 10)
        self.assertEqual(fengtian.stats.defense_physical, 10)
        self.assertEqual(fengtian.stats.defense_magical, 10)


if __name__ == '__main__':
    unittest.main()
