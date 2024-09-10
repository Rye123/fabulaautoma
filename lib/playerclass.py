from typing import List
from enum import IntEnum, auto

class PlayerClassBenefit(IntEnum):
    HP_MAX_BONUS_5 = 0
    MP_MAX_BONUS_5 = auto()
    IP_MAX_BONUS_2 = auto()
    CAN_START_PROJECTS = auto()
    EQUIP_ARMOR = auto()
    EQUIP_WEP_MELEE = auto()
    EQUIP_WEP_RANGED = auto()
    EQUIP_SHIELD = auto()
    RITUAL_ARCANISM = auto()
    RITUAL_CHIMERISM = auto()
    RITUAL_ELEMENTALISM = auto()
    RITUAL_ENTROPISM = auto()
    RITUAL_RITUALISM = auto()
    RITUAL_SPIRITISM = auto()


class PlayerClass:
    def __init__(self, name: str, desc: str, benefits: List[PlayerClassBenefit] = None):
        self.name = name
        self.desc = desc
        self.benefits: List[PlayerClassBenefit] = []
        if benefits is not None:
            for benefit in benefits:
                self.benefits.append(benefit)


CLASS_ARCANIST = PlayerClass(
    "Arcanist",
    "Summon magical avatars of ancient, godlike entities.",
    benefits=[PlayerClassBenefit.MP_MAX_BONUS_5]
)
CLASS_CHIMERIST = PlayerClass(
    "Chimerist",
    "Learn spells from creatures and speak with beasts.",
    benefits=[PlayerClassBenefit.MP_MAX_BONUS_5, PlayerClassBenefit.RITUAL_RITUALISM]
)
CLASS_DARKBLADE = PlayerClass(
    "Darkblade",
    "Unleash dark attacks and draw power from Bonds. Allows you to equip martial melee weapons and armors.",
    benefits=[PlayerClassBenefit.HP_MAX_BONUS_5, PlayerClassBenefit.EQUIP_WEP_MELEE, PlayerClassBenefit.EQUIP_ARMOR]
)
CLASS_ELEMENTALIST = PlayerClass(
    "Elementalist",
    "Wield the destructive power of the elements.",
    benefits=[PlayerClassBenefit.MP_MAX_BONUS_5, PlayerClassBenefit.RITUAL_RITUALISM]
)
CLASS_ENTROPIST = PlayerClass(
    "Entropist",
    "Channel the dark energy of the Cosmos.",
    benefits=[PlayerClassBenefit.MP_MAX_BONUS_5, PlayerClassBenefit.RITUAL_RITUALISM]
)
CLASS_FURY = PlayerClass(
    "Fury",
    "Provoke enemies and hit harder when damaged. Allows you to equip martial melee weapons and armors.",
    benefits=[PlayerClassBenefit.HP_MAX_BONUS_5, PlayerClassBenefit.EQUIP_WEP_MELEE, PlayerClassBenefit.EQUIP_ARMOR]
)
CLASS_GUARDIAN = PlayerClass(
    "Guardian",
    "Protect your allies and fight clad in heavy armor. Allows you to equip martial armor and shields.",
    benefits=[PlayerClassBenefit.HP_MAX_BONUS_5, PlayerClassBenefit.EQUIP_ARMOR, PlayerClassBenefit.EQUIP_SHIELD]
)
CLASS_LOREMASTER = PlayerClass(
    "Loremaster",
    "Be a master of knowledge and support your allies.",
    benefits=[PlayerClassBenefit.MP_MAX_BONUS_5]
)
CLASS_ORATOR = PlayerClass(
    "Orator",
    "Use your words to gain allies and influence conflicts.",
    benefits=[PlayerClassBenefit.MP_MAX_BONUS_5]
)
CLASS_ROGUE = PlayerClass(
    "Rogue",
    "Seize opportunities and steal unique items from enemies.",
    benefits=[PlayerClassBenefit.IP_MAX_BONUS_2]
)
CLASS_SHARPSHOOTER = PlayerClass(
    "Sharpshooter",
    "Excel at ranged combat and negate ranged attacks. Allows you to equip martial ranged weapons and shields",
    benefits=[PlayerClassBenefit.HP_MAX_BONUS_5, PlayerClassBenefit.EQUIP_WEP_RANGED, PlayerClassBenefit.EQUIP_SHIELD]
)
CLASS_SPIRITIST = PlayerClass(
    "Spiritist",
    "Support your allies with magic and cast light spells.",
    benefits=[PlayerClassBenefit.MP_MAX_BONUS_5, PlayerClassBenefit.RITUAL_RITUALISM]
)
CLASS_TINKERER = PlayerClass(
    "Tinkerer",
    "Craft inventions and use Inventory Points in new ways.",
    benefits=[PlayerClassBenefit.IP_MAX_BONUS_2, PlayerClassBenefit.CAN_START_PROJECTS]
)
CLASS_WAYFARER = PlayerClass(
    "Wayfarer",
    "Be a master explorer and join forces with a loyal companion.",
    benefits=[PlayerClassBenefit.IP_MAX_BONUS_2]
)
CLASS_WEAPONMASTER = PlayerClass(
    "Weaponmaster",
    "Excel at melee combat and counter melee attacks. Allows you to equip martial melee weapons and shields",
    benefits=[PlayerClassBenefit.HP_MAX_BONUS_5, PlayerClassBenefit.EQUIP_WEP_MELEE, PlayerClassBenefit.EQUIP_SHIELD]
)

