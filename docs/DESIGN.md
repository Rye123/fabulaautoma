# DESIGN
This system is meant to be easily extensible and modular, yet allow for automated computation of stats like HP, MP, IP and so on. 

As a result of Fabula's design, a lot of disparate systems affect those values, so it's hard to create a method of declaratively defining these systems (e.g. as JSON files).

I've come up with the following rough outline.

## Character
The `PlayerCharacter.compute()` method (in `lib.character`) computes the character's stats through the following steps:
1. Compute base values (e.g. $\verb|HP|_{\verb|max|} = \verb|level| + 5(\verb|might|)$)
2. Add bonuses/maluses based on the character's classes:
    - Each player class has a `.apply_stats(character)` method.
    - This allows for any stats bonuses or maluses to be defined within the player class definition.
    - Example player class implementation:
        ```python
        class Class_Weaponmaster(PlayerClass):
            def __init__(self, level: int):
                super().__init__("Weaponmaster",
                    level,
                    "Excel at melee combat and counter melee attacks. Allows you to equip martial melee weapons and shields"
                )
            
            def apply_stats(self, char: PlayerCharacter):
                char.stats.hp_max += 5
                char.stats.breakdown.hp_max += [f"5 ({self.name})"]
                char.stats.can_equip_martial_melee = True
                char.stats.can_equip_shield = True
        ```
        - As shown, the Weaponmaster class gives a bonus 5 Max HP, implemented in the `char.stats.hp_max + 5` line.
        - The ability to equip martial melee weapons and shields is also added in the `apply_stats()` method.
3. Add bonuses based on the character's skills.
   - Each skill's Python class also has a similar `apply_stats(character)` method.
   - Example skill class implementation:
       ```python
       class Skill_Focused(Skill):
           def __init__(self, level: int):
               super().__init__(
                   "Focused",
                   "Permanently increase your maximum Mind Points by 【SL × 3】. When you perform an Open Check using 【INS + INS】, you gain a bonus equal to 【SL】 on that Check (this only applies to Open Checks).",
                   level,
                   5
               )
           
           def apply_stats(self, char: Character):
               char.stats.mp_max += 3 * self.level
               char.stats.breakdown.mp_max += [f"3 * {self.level} (Skill: {self.name})"]
       ```
4. Add bonuses based on the character's equipment.
   - While this follows the same `apply_stats` pattern as above, custom equipment Python classes don't need to define their own `apply_stats` method.
   - Instead, this is implemented in the `Accessory`, `Weapon`, `Armor` and `Shield` classes, and specific equipment inherit from those classes
   - Example item implementation:
       ```python
       class Armor_CombatTunic(Armor):
           def __init__(self):
               super().__init__("Combat Tunic", "", 150,
                   martial=False,
                   defense_physical="DEX+1", 
                   defense_magical="INS+1", 
                   initiative_bonus=0
               )
       ```
       - Here, the defense strings are **automatically parsed** regardless of how you write it (`"1+DEX+1"`, `"2+DEX"` all are converted to `DEX+2`).
       - The parent class is carries out the `apply_stats` method based on the parsed string (e.g. setting the character's physical defense according to the string).

## Player Class
Along with the `apply_stats` method, this imperative paradigm is intended to allow us to define class-specific systems like Arcana and Symbols, hopefully without requiring us to modify external code.

This is still a work-in-progress.