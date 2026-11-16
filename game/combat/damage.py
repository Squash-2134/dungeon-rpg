import math
import random

def calculate_damage(level, power, attack, defence):
    """
    Damage formula inspired by Pokemon:
    Damage = ((((2 * Level / 5 + 2) * Power * Attack / Defence) / 50) + 2) * Variance * Modifier
    Where:
    - Level is the level of the attacking entity
    - Power is the base power of the skill (Basic Attacks have a set power of 50)
    - Attack is the attack stat of the attacking entity (Either Strength or Arcane depending on the skill type)
    - Defence is the defence stat of the defending entity (Either Fortitude or Wisdom depending on the skill type)
    - Variance is a radomly generated number (to 2 dp) between 0.85 and 1.00
    - Modifier is a composite variable taking into account critical hits, type effectiveness, and other factors

    """
    variance = round(random.uniform(0.85, 1.00), 2)
    modifier = 1.0 # Placeholder for future implementation of critical hits, type effectiveness, etc.
    damage = ((((2 * level / 5 + 2) * power * attack / defence) / 50) + 2) * variance * modifier
    if damage < 1:
        return 1
    return math.floor(damage)


