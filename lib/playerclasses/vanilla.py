"""
This file contains all possible player classes.

For IDE ease, each class follows the following syntax:
class Class_{CLASS_NAME}(PlayerClass):
    def __init__(self, level: int):
        super().__init__("{CLASS_NAME}",
                         level,
                         "{CLASS_DESCRIPTION}"
                        )
    def apply_stats(self, char: PlayerCharacter):
        # Here, we apply the necessary stats on the player character.
        # This includes iterating through any skills the character has. (Not implemented)

In the future, since in Fabula some classes have entire systems, the respective class will
contain the necessary logic. The way this is currently coded is to (hopefully) enable easy extension for
the various player classes, instead of forcing all that logic on the PlayerCharacter class.

For instance, the `Class_Entropist` class doesn't need to track arcana, but the `ClassArcanist` class probably does.
The logic for all that will hence be encapsulated entirely within the `ClassArcanist` class.
"""

from lib.core.playerclass import PlayerClass
from lib.character import PlayerCharacter


class Class_Arcanist(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Arcanist",
                         level,
                         "Summon magical avatars of ancient, godlike entities."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5
        char.stats.breakdown.mp_max += [f"5 ({self.name})"]


class Class_Chimerist(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Chimerist",
                         level,
                         "Learn spells from creatures and speak with beasts."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5
        char.stats.breakdown.mp_max += [f"5 ({self.name})"]
        char.stats.rituals.ritualism = True


class Class_Darkblade(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Darkblade",
                         level,
                         "Unleash dark attacks and draw power from Bonds. Allows you to equip martial melee weapons and armors."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.breakdown.hp_max += [f"5 ({self.name})"]
        char.stats.martial_equip.melee = True
        char.stats.martial_equip.armor = True


class Class_Elementalist(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Elementalist",
                         level,
                         "Wield the destructive power of the elements."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5
        char.stats.breakdown.mp_max += [f"5 ({self.name})"]
        char.stats.rituals.ritualism = True


class Class_Entropist(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Entropist",
                         level,
                         "Channel the dark energy of the Cosmos."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5
        char.stats.breakdown.mp_max += [f"5 ({self.name})"]
        char.stats.rituals.ritualism = True


class Class_Fury(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Fury",
                         level,
                         "Provoke enemies and hit harder when damaged. Allows you to equip martial melee weapons and armors."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.breakdown.hp_max += [f"5 ({self.name})"]
        char.stats.martial_equip.melee = True
        char.stats.martial_equip.armor = True


class Class_Guardian(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Guardian",
                         level,
                         "Protect your allies and fight clad in heavy armor. Allows you to equip martial armor and shields."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.breakdown.hp_max += [f"5 ({self.name})"]
        char.stats.martial_equip.armor = True
        char.stats.martial_equip.shield = True


class Class_Loremaster(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Loremaster",
                         level,
                         "Be a master of knowledge and support your allies."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5
        char.stats.breakdown.mp_max += [f"5 ({self.name})"]


class Class_Orator(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Orator",
                         level,
                         "Use your words to gain allies and influence conflicts."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5
        char.stats.breakdown.mp_max += [f"5 ({self.name})"]


class Class_Rogue(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Rogue",
                         level,
                         "Seize opportunities and steal unique items from enemies."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.ip_max += 2
        char.stats.breakdown.ip_max += [f"2 ({self.name})"]


class Class_Sharpshooter(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Sharpshooter",
                         level,
                         "Excel at ranged combat and negate ranged attacks. Allows you to equip martial ranged weapons and shields."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.breakdown.hp_max += [f"5 ({self.name})"]
        char.stats.martial_equip.martial_ranged = True
        char.stats.martial_equip.shield = True


class Class_Spiritist(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Spiritist",
                         level,
                         "Support your allies with magic and cast light spells."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5
        char.stats.breakdown.mp_max += [f"5 ({self.name})"]
        char.stats.rituals.ritualism = True


class Class_Tinkerer(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Tinkerer",
                         level,
                         "Craft inventions and use Inventory Points in new ways."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.ip_max += 2
        char.stats.breakdown.ip_max += [f"2 ({self.name})"]
        char.stats.can_start_projects = True


class Class_Wayfarer(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Wayfarer",
                         level,
                         "Be a master explorer and join forces with a loyal companion."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.ip_max += 2
        char.stats.breakdown.ip_max += [f"2 ({self.name})"]


class Class_Weaponmaster(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Weaponmaster",
                         level,
                         "Excel at melee combat and counter melee attacks. Allows you to equip martial melee weapons and shields"
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.breakdown.hp_max += [f"5 ({self.name})"]
        char.stats.martial_equip.melee = True
        char.stats.martial_equip.shield = True




