import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))   # project root

from game.paths import RACES_PATH, CLASSES_PATH
from game.data_loader import load_races, load_classes
from game.entities import Player, Enemy
from game.combat.battle import run_battle
from ui.terminal.combat_screen import print_battle

player_races = load_races(RACES_PATH, "player_races")
enemy_races = load_races(RACES_PATH, "regular_enemy_races")
classes = load_classes(CLASSES_PATH)

player = Player("Hero", "they", player_races["human"], classes["knight"])
enemy = Enemy(enemy_races["goblin"], 1)

events = run_battle(player, enemy)
print_battle(player, enemy, events)