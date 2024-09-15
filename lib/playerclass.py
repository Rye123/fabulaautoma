"""
This file contains all possible player classes.

For IDE ease, each class follows the following syntax:
class Class{CLASS_NAME}(PlayerClass):
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

For instance, the `ClassEntropist` class doesn't need to track arcana, but the `ClassArcanist` class probably does.
The logic for all that will hence be encapsulated entirely within the `ClassArcanist` class.
"""

from lib.core.playerclass import PlayerClass
from lib.character import PlayerCharacter


class ClassArcanist(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Arcanist",
                         level,
                         "Summon magical avatars of ancient, godlike entities."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5


class ClassChimerist(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Chimerist",
                         level,
                         "Learn spells from creatures and speak with beasts."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5
        char.stats.rituals.ritualism = True


class ClassDarkblade(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Darkblade",
                         level,
                         "Unleash dark attacks and draw power from Bonds. Allows you to equip martial melee weapons and armors."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.can_equip_martial_melee = True
        char.stats.can_equip_martial_armor = True


class ClassElementalist(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Elementalist",
                         level,
                         "Wield the destructive power of the elements."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5
        char.stats.rituals.ritualism = True


class ClassEntropist(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Entropist",
                         level,
                         "Channel the dark energy of the Cosmos."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5
        char.stats.rituals.ritualism = True


class ClassFury(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Fury",
                         level,
                         "Provoke enemies and hit harder when damaged. Allows you to equip martial melee weapons and armors."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.can_equip_martial_melee = True
        char.stats.can_equip_martial_armor = True


class ClassGuardian(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Guardian",
                         level,
                         "Protect your allies and fight clad in heavy armor. Allows you to equip martial armor and shields."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.can_equip_martial_armor = True
        char.stats.can_equip_shield = True


class ClassLoremaster(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Loremaster",
                         level,
                         "Be a master of knowledge and support your allies."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5


class ClassOrator(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Orator",
                         level,
                         "Use your words to gain allies and influence conflicts."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5


class ClassRogue(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Rogue",
                         level,
                         "Seize opportunities and steal unique items from enemies."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.ip_max += 2


class ClassSharpshooter(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Sharpshooter",
                         level,
                         "Excel at ranged combat and negate ranged attacks. Allows you to equip martial ranged weapons and shields."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.can_equip_martial_ranged = True
        char.stats.can_equip_shield = True


class ClassSpiritist(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Spiritist",
                         level,
                         "Support your allies with magic and cast light spells."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.mp_max += 5
        char.stats.rituals.ritualism = True


class ClassTinkerer(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Tinkerer",
                         level,
                         "Craft inventions and use Inventory Points in new ways."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.ip_max += 2
        char.stats.can_start_projects = True


class ClassWayfarer(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Wayfarer",
                         level,
                         "Be a master explorer and join forces with a loyal companion."
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.ip_max += 2


class ClassWeaponmaster(PlayerClass):
    def __init__(self, level: int):
        super().__init__("Weaponmaster",
                         level,
                         "Excel at melee combat and counter melee attacks. Allows you to equip martial melee weapons and shields"
                         )

    def apply_stats(self, char: PlayerCharacter):
        char.stats.hp_max += 5
        char.stats.can_equip_martial_melee = True
        char.stats.can_equip_shield = True




