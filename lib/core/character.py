from abc import ABC, abstractmethod
from lib.core.dice import Dice
from lib.core.constants import StatusEffect


class Attributes:
    """
    A character's base attributes.
    - `dex_base`, `ins_base`, `mig_base`, `wlp_base`: The base dexterity, insight, might, and willpower values.
    - `dex_eff`, `ins_eff`, `mig_eff`, `wlp_eff`: The effective dexterity, insight, might and willpower values, including
                                                  status effects.
    - `status_effects`: A list of existing status effects on the character.
    - `dex_bonus`, `ins_bonus`, `mig_bonus`, `wlp_bonus`: Bonus to the respective values, which could happen due to equipment.
    """

    def __init__(self, dex: int, ins: int, mig: int, wlp: int):
        try:
            self.dex_base = Dice(dex)
            self.ins_base = Dice(ins)
            self.mig_base = Dice(mig)
            self.wlp_base = Dice(wlp)
        except ValueError as e:
            raise ValueError("Attributes.__init__: Invalid value given as dice size, expected 6, 8, 10, 12, or 20.")
        self.status_effects = []
        self.dex_bonus = self.ins_bonus = self.mig_bonus = self.wlp_bonus = 0

    @property
    def dex_eff(self) -> Dice:
        cur_dex = self.dex_base
        for fx in self.status_effects:
            if fx in [StatusEffect.ENRAGED, StatusEffect.SLOW]:
                cur_dex = cur_dex.get_next_lower()
        return cur_dex

    @property
    def ins_eff(self) -> Dice:
        cur_ins = self.ins_base
        for fx in self.status_effects:
            if fx in [StatusEffect.DAZED, StatusEffect.ENRAGED]:
                cur_ins = cur_ins.get_next_lower()
        return cur_ins

    @property
    def mig_eff(self) -> Dice:
        cur_mig = self.mig_base
        for fx in self.status_effects:
            if fx in [StatusEffect.POISONED, StatusEffect.WEAK]:
                cur_mig = cur_mig.get_next_lower()
        return cur_mig

    @property
    def wlp_eff(self) -> Dice:
        cur_wlp = self.wlp_base
        for fx in self.status_effects:
            if fx in [StatusEffect.POISONED, StatusEffect.SHAKEN]:
                cur_wlp = cur_wlp.get_next_lower()
        return cur_wlp


class Stats:
    """
    A character's stats. These are likely to change every time a player levels up.
    - `hp`, `hp_max`
    - `mp`, `mp_max`
    - `ip`, `ip_max`
    - `initiative`
    - `defense_physical`, `defense_magical`
    - `can_equip_martial_armor`
    - `can_equip_martial_melee`, `can_equip_martial_ranged`
    - `can_equip_shield`
    - `can_start_projects`
    - `rituals`:
        - `arcanism`
        - `chimerism`
        - `elementalism`
        - `entropism`
        - `ritualism`
        - `spiritism`
    """

    class Rituals:
        def __init__(self):
            self.arcanism = self.chimerism = self.elementalism = False
            self.entropism = self.ritualism = self.spiritism = False

    def __init__(self):
        self.hp = self.mp = self.ip = 0
        self.hp_max = self.mp_max = self.ip_max = 0
        self.initiative = 0
        self.defense_physical = self.defense_magical = 0
        self.can_equip_martial_armor = self.can_equip_martial_melee = False
        self.can_equip_martial_ranged = self.can_equip_shield = False
        self.can_start_projects = False
        self.rituals = Stats.Rituals()

    @property
    def in_crisis(self) -> bool:
        return self.hp <= (self.hp_max // 2)

    def rest(self):
        self.hp = self.hp_max
        self.mp = self.mp_max


class Character(ABC):
    def __init__(self,
                 name: str,
                 level: int,
                 dex: int, ins: int, mig: int, wlp: int):
        self.name = name
        self.level = level
        self.attributes = Attributes(dex, ins, mig, wlp)
        self.stats = Stats()

    @abstractmethod
    def compute(self):
        """ Computes the stats of this character, based on their attributes, stats and equipment. """
        raise NotImplementedError()

    def __str__(self) -> str:
        report = f"{self.name} (Level {self.level})\n"
        report += "Attributes:" + \
            f"\n\tDEX: {self.attributes.dex_eff} (base {self.attributes.dex_base})" + \
            f"\n\tINS: {self.attributes.ins_eff} (base {self.attributes.ins_base})" + \
            f"\n\tMIG: {self.attributes.mig_eff} (base {self.attributes.mig_base})" + \
            f"\n\tWLP: {self.attributes.wlp_eff} (base {self.attributes.wlp_base})\n"
        report += "Stats:" + \
            f"\n\tHP: {self.stats.hp}/{self.stats.hp_max}  (CRISIS: {self.stats.in_crisis})" + \
            f"\n\tMP: {self.stats.mp}/{self.stats.mp_max}" + \
            f"\n\tIP: {self.stats.ip}/{self.stats.ip_max}" + \
            f"\n\tInitiative: {self.stats.initiative}" + \
            f"\n\tDefense: {self.stats.defense_physical}" + \
            f"\n\tMagical Defense: {self.stats.defense_magical}"
        return report
