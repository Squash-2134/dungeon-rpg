class Enemy:
    def __init__(self, race, level, rank="regular", name=None):
        self.race = race
        self.level = level
        self.rank = rank
        self.name = name or race.name
        self.skills = [race.skill_id]
        self.consumable = None

        self.current_health = self.get_stat("health")
        self.current_mana = self.get_stat("mana")

    def get_stat(self, stat_name):
        return self.race.base_stats[stat_name]