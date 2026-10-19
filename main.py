from game.paths import RACES_PATH, CLASSES_PATH
from game.data_loader import load_races, load_classes
from ui.terminal.display import print_class, print_race



def main():
    regular_enemy_races = load_races(RACES_PATH, "regular_enemy_races")
    player_races = load_races(RACES_PATH, "player_races")
    classes = load_classes(CLASSES_PATH)

    print_race(regular_enemy_races["goblin"])
    print_race(player_races["human"])

    for player_class in classes.values():
        print_class(player_class)


if __name__ == "__main__":
    main()