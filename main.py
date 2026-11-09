from game.paths import RACES_PATH, CLASSES_PATH
from game.data_loader import load_races, load_classes
from ui.terminal.character_creation import create_character


def main():
    races = load_races(RACES_PATH, "player_races")
    classes = load_classes(CLASSES_PATH)
    player = create_character(races, classes)
    print(f"Welcome, {player.name}!")


if __name__ == "__main__":
    main()