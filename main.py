from pathlib import Path
from game.general_funcs import load_races

BASE_DIR = Path(__file__).parent          # the dungeon-rpg folder
RACES_PATH = BASE_DIR / "data" / "races.json"


def main():
    enemy_races = load_races(RACES_PATH, "regular_enemy_races")
    player_races = load_races(RACES_PATH, "player_races")

    # quick test that it worked
    print(enemy_races["goblin"].name)
    print(enemy_races["goblin"].base_stats)

    print(player_races["human"].name)
    print(player_races["human"].base_stats)


if __name__ == "__main__":
    main()