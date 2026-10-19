from pathlib import Path
from game.general_funcs import load_races, load_classes

BASE_DIR = Path(__file__).parent          # the dungeon-rpg folder
RACES_PATH = BASE_DIR / "data" / "races.json"
CLASSES_PATH = BASE_DIR / "data" / "classes.json"


def main():
    regular_enemy_races = load_races(RACES_PATH, "regular_enemy_races")
    player_races = load_races(RACES_PATH, "player_races")
    classes = load_classes(CLASSES_PATH)

    def print_race(race):
        print(f"--- {race.name} ({race.race_id}) ---")
        print(f"Skill: {race.skill_id}")
        for stat_name, value in race.base_stats.items():
            print(f"  {stat_name}: {value}")
        print()

    def print_class(player_class):
        print(f"--- {player_class.name} ({player_class.class_id}) ---")
        print(f"Skill tree: {player_class.skill_tree}")
        for stat_name, rate in player_class.growth_rate.items():
            print(f"  {stat_name}: {rate}")
        print()

    print_race(regular_enemy_races["goblin"])
    print_race(player_races["human"])

    for player_class in classes.values():
        print_class(player_class)


if __name__ == "__main__":
    main()