import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent   # the dungeon-rpg folder
sys.path.insert(0, str(BASE_DIR))

from game.data_loader import load_races, load_classes
from game.paths import RACES_PATH, CLASSES_PATH
from ui.terminal.display import print_class, print_race

regular_enemy_races = load_races(RACES_PATH, "regular_enemy_races")
player_races = load_races(RACES_PATH, "player_races")
classes = load_classes(CLASSES_PATH)

print_race(regular_enemy_races["goblin"])
print_race(player_races["human"])

for player_class in classes.values():
    print_class(player_class)


from game.entities import Player, Enemy
p = Player("Test", "they", player_races["human"], classes["knight"])
e = Enemy(regular_enemy_races["goblin"], 5)
print(p.name, p.get_stat("attack"), e.name, e.get_stat("attack"))