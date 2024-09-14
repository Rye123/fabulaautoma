import unittest
from lib.character import PlayerCharacter
from lib.playerclass import *

class TestPlayerCharacter(unittest.TestCase):
    def test_lirithid(self):
        lirithid = PlayerCharacter("Lirithid", 10, 6, 10, 6, 10)
        lirithid.classes[CLASS_ENTROPIST] = 6
        lirithid.classes[CLASS_CHIMERIST] = 3
        lirithid.classes[CLASS_WEAPONMASTER] = 1

        self.assertEqual(lirithid.stats.hp_max, 45)
        self.assertEqual(lirithid.stats.mp_max, 70)
        self.assertEqual(lirithid.stats.ip_max, 6)
        self.assertEqual(lirithid.stats.initiative, 10)
        self.assertEqual(lirithid.stats.defense_physical, 6)
        self.assertEqual(lirithid.stats.defense_magical, 10)

    def test_fengtian(self):
        fengtian = PlayerCharacter("Feng Tian", 5, 10, 10, 6, 6)
        fengtian.classes[CLASS_SHARPSHOOTER] = 3
        fengtian.classes[CLASS_ROGUE] = 1
        fengtian.classes[CLASS_TINKERER] = 1

        self.assertEqual(fengtian.stats.hp_max, 40)
        self.assertEqual(fengtian.stats.mp_max, 35)
        self.assertEqual(fengtian.stats.ip_max, 10)
        self.assertEqual(fengtian.stats.initiative, 10)
        self.assertEqual(fengtian.stats.defense_physical, 10)
        self.assertEqual(fengtian.stats.defense_magical, 10)


if __name__ == '__main__':
    unittest.main()
