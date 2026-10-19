# imports
import json
from game.entities import Race, PlayerClass

def load_races(filepath, section):
    """
    function to load race data from a JSON file
    section means which category of race to load, e.g. "player_races" or "regular_enemy_races"
    """
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    races = {}
    for race_id, info in data[section].items():
        races[race_id] = Race(
            race_id = race_id,
            name = info["name"],
            base_stats = info["stats"],
            skill_id = info["skill"]
        )
    return races

def load_classes(filepath):
    """
    function to load class data from a JSON file
    returns a dict of class_id -> PlayerClass
    """
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    classes = {}
    for class_id, info in data.items():
        classes[class_id] = PlayerClass(
            class_id = class_id,
            name = info["name"],
            growth_rate = info["growth_rate"],
            skill_tree = info["skill_tree"]
        )
    return classes