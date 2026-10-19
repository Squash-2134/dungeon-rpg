import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent   # the dungeon-rpg folder
sys.path.insert(0, str(BASE_DIR))

from game.general_funcs import load_races, load_classes

RACES_PATH = BASE_DIR / "data" / "races.json"
CLASSES_PATH = BASE_DIR / "data" / "classes.json"

regular_enemy_races = load_races(RACES_PATH, "regular_enemy_races")
player_races = load_races(RACES_PATH, "player_races")
classes = load_classes(CLASSES_PATH)


def print_race(race):
    print(f"--- {race.name} ({race.race_id}) ---")
    print(f"Skill: {race.skill_id}")
    for stat_name, value in race.base_stats.items():
        print(f"  {stat_name}: {value}")
    print()


print_race(regular_enemy_races["goblin"])
print_race(player_races["human"])

for class_id, info in classes.items():
    print(f"--- {info['name']} ({class_id}) ---")
    print(f"Skill tree: {info['skill_tree']}")
    for stat_name, rate in info["growth_rate"].items():
        print(f"  {stat_name}: {rate}")
    print()