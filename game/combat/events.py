from dataclasses import dataclass

@dataclass
class Attack:
    attacker: object
    defender: object
    damage: int
    defender_health: int # health left AFTER the hit
    defender_max_health: int
    defended: bool = False  # True if the defender was defending (damage halved)

@dataclass
class Defend:
    character: object
    mana_restored: int  # how much mana was ACTUALLY gained (0 if already full)
    mana_after: int
    max_mana: int

@dataclass
class Defeated:
    character: object