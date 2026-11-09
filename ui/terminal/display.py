from game.entities.player import STAT_NAMES

def print_class(player_class):
        print(f"--- {player_class.name} ({player_class.class_id}) ---")
        print(f"Skill tree: {player_class.skill_tree}")
        for stat_name, rate in player_class.growth_rate.items():
            print(f"  {stat_name}: {rate}")
        print()

def print_race(race):
        print(f"--- {race.name} ({race.race_id}) ---")
        print(f"Skill: {race.skill_id}")
        for stat_name, value in race.base_stats.items():
            print(f"  {stat_name}: {value}")
        print()

def print_profile(player):
    print(f"\n=== {player.name} ({player.pronouns}) ===")
    print(f"Race: {player.race.name}   Class: {player.player_class.name}   Level: {player.level}")
    for stat in STAT_NAMES:
        print(f"  {stat}: {player.get_stat(stat)} (+{player.get_gear_bonus(stat)})")
    print(f"Race skill: {player.race.skill_id}")
    print(f"Skill tree: {player.player_class.skill_tree}")
    print("Starting loadout: (coming later)")
    print()