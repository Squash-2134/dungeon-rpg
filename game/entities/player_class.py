# Named PlayerClass to avoid confusion with Python's own "class" keyword
class PlayerClass:
    def __init__(self, class_id, name, growth_rate, skill_tree):
        self.class_id = class_id
        self.name = name
        self.growth_rate = growth_rate  # dict of stat name -> rate name (e.g. "fast")
        self.skill_tree = skill_tree