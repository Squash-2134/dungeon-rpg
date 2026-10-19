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