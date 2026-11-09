STAT_NAMES = ("health", "mana", "attack", "defence", "magic_attack", "magic_defence", "speed", "luck")

class Player:
    def __init__(self, name, pronouns, race, player_class):
        self.name = name
        self.pronouns = pronouns
        self.race = race
        self.player_class = player_class
        self.level = 1

        self.stat_points = 10
        self.allocated_stat_points = {stat: 0 for stat in STAT_NAMES}

        self.unlocked_nodes = set() # Skill tree to fill out later
        self.gear = {} # Gear to fill out later

        self.current_health = self.get_stat("health")
        self.current_mana = self.get_stat("mana")

    def get_stat(self, stat_name):
        return self.race.base_stats[stat_name] + self.allocated_stat_points[stat_name]

    def get_gear_bonus(self, stat_name):
        return 0

    def spend_points(self, stat_name, amount):
        if stat_name not in self.allocated_stat_points:
            raise ValueError(f"Unknown stat: {stat_name}")
        if amount < 1 or amount > self.stat_points:
            raise ValueError("Not enough stat points")
        self.allocated_stat_points[stat_name] += amount
        self.stat_points -= amount

