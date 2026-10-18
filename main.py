from pathlib import Path
from game.general_funcs import load_races

BASE_DIR = Path(__file__).parent          # the dungeon-rpg folder
RACES_PATH = BASE_DIR / "data" / "races.json"


def main():
    regular_enemy_races = load_races(RACES_PATH, "regular_enemy_races")
    player_races = load_races(RACES_PATH, "player_races")



if __name__ == "__main__":
    main()