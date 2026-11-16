from dataclasses import dataclass


@dataclass
class Attack:
    attacker: object
    defender: object
    damage: int
    defender_health: int # health left AFTER the hit
    defender_max_health: int


@dataclass
class Defeated:
    character: object

