import math
import random

def calculate_damage(level, power, strength, fortitude, variance=None):
    """
    Damage formula inspired by Pokemon:
    Damage = ((((2 * Level / 5 + 2) * Power * Strength / Fortitude) / 50) + 2) * Variance * Modifier
    Where:
    - Level is the level of the attacking entity
    - Power is the base power of the skill (Basic Attacks have a set power of 50)
    - Strength is the strength stat of the attacking entity (Either Strength or Arcane depending on the skill type)
    - Fortitude is the fortitude stat of the defending entity (Either Fortitude or Wisdom depending on the skill type)
    - Variance is a radomly generated number (to 2 dp) between 0.85 and 1.00
    - Modifier is a composite variable taking into account critical hits, type effectiveness, and other factors
        - Crit is a 1.5x multiplier to damage if the attack is a critical hit
        - Type is a multiplier (2x, 1x, 0.5x, 0x) based on the skill's damage type and the target's resistances
        - AoE skills have a 0.8x multiplier if there are multiple targets hit by the skill

    """
    if fortitude <= 0:
        raise ValueError("Fortitude must be positive")
    if variance is None:  # tests pass a fixed value so results are predictable
        variance = round(random.uniform(0.85, 1.00), 2)
    modifier = 1.0 # Placeholder for future implementation of critical hits, type effectiveness, etc.
    damage = ((((2 * level / 5 + 2) * power * strength / fortitude) / 50) + 2) * variance * modifier
    if damage < 1:
        return 1
    return math.floor(damage)


