# Imports

# Stat Object
class Stats:
    def __init__(
        self,
        max_health = 0,
        max_mana = 0,
        attack = 0,
        defence = 0,
        magic_attack = 0,
        magic_defence = 0,
        speed = 0,
        luck = 0, # player only stat
        reputation = 0 # player only stat
    ):
        # global stats
        self.max_health = max_health
        self.current_health = max_health
        self.max_mana = max_mana
        self.current_mana = max_mana
        self.attack = attack
        self.defence = defence
        self.magic_attack = magic_attack
        self.magic_defence = magic_defence
        self.speed = speed
        # player only stats
        self.luck = luck
        self.reputation = reputation

class Race:
    def __init__(self, race_id, name, base_stats, skill_id):
        self.race_id = race_id
        self.name = name
        self.base_stats = base_stats
        self.skill_id = skill_id

    

