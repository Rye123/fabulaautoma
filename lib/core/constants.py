from enum import IntEnum, StrEnum


class StatusEffect(IntEnum):
    DAZED    = 0  # Reduces Insight by 1 size
    ENRAGED  = 1  # Reduces Dex & Insight by 1 size
    POISONED = 2  # Reduces Might & Willpower by 1 size
    SHAKEN   = 3  # Reduces Willpower by 1 size
    SLOW     = 4  # Reduces Dex by 1 size
    WEAK     = 5  # Reduces Might by 1 size


class DamageType(StrEnum):
    PHYSICAL = "PHYSICAL"
    AIR = "AIR"
    BOLT = "BOLT"
    DARK = "DARK"
    EARTH = "EARTH"
    FIRE = "FIRE"
    ICE = "ICE"
    LIGHT = "LIGHT"
    POISON = "POISON"


class DamageAffinity(IntEnum):
    VULNERABILITY = 0
    NORMAL = 1
    RESISTANCE = 2
    IMMUNITY = 3
    ABSORPTION = 4


class ItemType(IntEnum):
    ACCESSORY = 0
    ARMOR = 1
    SHIELD = 2
    WEAPON = 3


class WeaponType(IntEnum):
    MELEE = 0
    RANGED = 1
