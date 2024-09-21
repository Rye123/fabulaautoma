from lib.core.constants import DamageType
from lib.core.parsers import parse_damage_string


class Damage:
    def __init__(self, value: str, dmg_type: DamageType):
        self.value = parse_damage_string(value)
        self.type = dmg_type

    def __str__(self) -> str:
        return f"{self.value} {self.type}"

