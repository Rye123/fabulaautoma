from abc import ABC
from lib.core.constants import DamageType
from lib.core.damage import Damage
from lib.core.action import Action
from lib.core.character import Character


class Action_Spell(Action):
    def __init__(self, spell: 'Spell'):
        super().__init__(f"Use Spell: {spell.name}", spell.desc)


class Spell(ABC):
    def __init__(self, name: str, desc: str, offensive: bool,
                 mp_per_target: int, max_targets: int, target_type: str, duration: str,
                 damage: str = "", damage_type: DamageType = DamageType.PHYSICAL):
        self.name = name
        self.desc = desc
        self.offensive = offensive
        self.mp_per_target = mp_per_target
        self.max_targets = max_targets
        self.target_type = target_type
        self.duration = duration
        self.damage = Damage(damage, damage_type)

    def apply_stats(self, char: Character):
        pass

    def add_actions(self, char: 'Character'):
        #TODO: don't show spells that can't be cast (e.g. with MP check)?
        char.actions.append(Action_Spell(self))

    def __str__(self):
        report = self.name
        report += f"\n\tOffensive: {'YES' if self.offensive else 'NO'}"
        report += f"\n\tMP/target: {self.mp_per_target}"
        report += f"\n\tTarget: {self.max_targets} {self.target_type}"  #TODO: address plural and 'self' cases
        if self.offensive:
            report += f"\n\tDamage: {self.damage}"
        return report
