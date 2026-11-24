from game.paths import RACES_PATH, CLASSES_PATH
from game.data_loader import load_races, load_classes
from game.stats import COMBAT_STATS, WORLD_STATS

VALID_GROWTH_RATES = {"Slow", "Medium", "Fast"}


def test_player_races_have_every_stat():
    races = load_races(RACES_PATH, "player_races")
    for race_id, race in races.items():
        for stat in COMBAT_STATS + WORLD_STATS:
            assert stat in race.base_stats, f"{race_id} is missing {stat}"


def test_enemy_races_have_every_combat_stat():
    races = load_races(RACES_PATH, "regular_enemy_races")
    for race_id, race in races.items():
        for stat in COMBAT_STATS:
            assert stat in race.base_stats, f"{race_id} is missing {stat}"


def test_classes_have_a_growth_rate_for_every_combat_stat():
    classes = load_classes(CLASSES_PATH)
    for class_id, player_class in classes.items():
        for stat in COMBAT_STATS:
            assert stat in player_class.growth_rate, f"{class_id} is missing {stat}"


def test_growth_rates_are_valid_names():
    classes = load_classes(CLASSES_PATH)
    for class_id, player_class in classes.items():
        for stat, rate in player_class.growth_rate.items():
            assert rate in VALID_GROWTH_RATES, f"{class_id}/{stat} has bad rate '{rate}'"