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

    def take_damage(self, amount):
        self.current_health = max(0, self.current_health - amount)

    def restore_mana(self, amount):
        self.current_mana = min(self.get_stat("mana"), self.current_mana + amount)

    def is_alive(self):
        return self.current_health > 0