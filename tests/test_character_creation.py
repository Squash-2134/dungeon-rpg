import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent   # the dungeon-rpg folder
sys.path.insert(0, str(BASE_DIR))

from game.paths import RACES_PATH, CLASSES_PATH
from game.data_loader import load_races, load_classes
from ui.terminal.character_creation import create_character

races = load_races(RACES_PATH, "player_races")
classes = load_classes(CLASSES_PATH)
player = create_character(races, classes)
print(f"Welcome, {player.name}!")