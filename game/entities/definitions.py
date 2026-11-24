from dataclasses import dataclass

@dataclass
class Race:
    race_id: str
    name: str
    base_stats: dict
    skill_id: str

# Named PlayerClass to avoid confusion with Python's own "class" keyword
@dataclass
class PlayerClass:
    class_id: str
    name: str
    growth_rate: dict  # stat name -> rate name (e.g. "Fast")
    skill_tree: str