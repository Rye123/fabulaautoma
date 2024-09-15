import unittest
from lib.core.parsers import parse_accuracy_string, parse_damage_string

class AccuracyTestCase(unittest.TestCase):
    def test_accuracy_parser(self):
        # Basic values
        self.assertEqual(
            parse_accuracy_string("[DEX]"),
            "【DEX】"
        )
        self.assertEqual(
            parse_accuracy_string("(WLP)"),
            "【WLP】"
        )
        self.assertEqual(
            parse_accuracy_string("  INS "),
            "【INS】"
        )
        self.assertEqual(
            parse_accuracy_string("(MIG)"),
            "【MIG】"
        )

        # Sums
        self.assertEqual(
            parse_accuracy_string("DEX + INS"),
            "【DEX+INS】"
        )
        self.assertEqual(
            parse_accuracy_string("[WLP+MIG]"),
            "【MIG+WLP】"    # Order is DEX, INS, MIG, WLP
        )
        self.assertEqual(
            parse_accuracy_string("【WLP  +INS】 +1"),
            "【INS+WLP】+1"  # Order is DEX, INS, MIG, WLP
        )
        self.assertEqual(
            parse_accuracy_string("MIG+MIG+2"),
            "【MIG+MIG】+2"
        )
        self.assertEqual(
            parse_accuracy_string("3+WLP+MIG+WLP+INS+DEX+MIG"),
            "【DEX+INS+MIG+MIG+WLP+WLP】+3"
        )
        self.assertEqual(
            parse_accuracy_string("3+MIG+WLP+4+7"),
            "【MIG+WLP】+14"
        )

        # Unexpected Input
        with self.assertRaises(ValueError):
            parse_accuracy_string("ASDF+FDSA")

        with self.assertRaises(ValueError):
            parse_accuracy_string(";")


class DamageTestCase(unittest.TestCase):
    def test_damage_parser(self):
        # Basic values
        self.assertEqual(
            parse_damage_string("HR"),
            "【HR】"
        )
        self.assertEqual(
            parse_damage_string("LR"),
            "【LR】"
        )

        # Sums
        self.assertEqual(
            parse_damage_string("HR + HR"),
            "【HR+HR】"
        )
        self.assertEqual(
            parse_damage_string("[   HR+ LR]"),
            "【HR+LR】"
        )
        self.assertEqual(
            parse_damage_string("【LR  +HR】 +1"),
            "【HR+LR】+1"
        )
        self.assertEqual(
            parse_damage_string("HR+2+LR"),
            "【HR+LR】+2"
        )
        self.assertEqual(
            parse_damage_string("1+LR+2+HR+3+LR+4+LR+HR"),
            "【HR+HR+LR+LR+LR】+10"
        )

        # Unexpected Input
        with self.assertRaises(ValueError):
            parse_damage_string("DEX+INS")

        with self.assertRaises(ValueError):
            parse_damage_string(";")


if __name__ == '__main__':
    unittest.main()
