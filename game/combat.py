# imports
from entities import test_player, test_enemy

def damage_formula(offesive_stat, defensive_stat, attacker_level):
    dmg = (2 *attacker_level / 5 + 2) * 50 * (offesive_stat / defensive_stat) / 50 + 2
    return dmg

def combat(player, enemy):
    print(f"Combat Start: {player.name} vs {enemy.name}")
    while player.current_health > 0 and enemy.current_health > 0:
        # Player attacks enemy
        damage_to_enemy = damage_formula(player.attack, enemy.defence, player.level)
        enemy.current_health -= damage_to_enemy
        print(f"{player.name} attacks {enemy.name} for {damage_to_enemy} damage. {enemy.name}'s health is now {enemy.current_health}/{enemy.max_health}")

        if enemy.current_health <= 0:
            print(f"{enemy.name} has been defeated!")
            break

        # Enemy attacks player
        damage_to_player = damage_formula(enemy.attack, player.defence, enemy.level)
        player.current_health -= damage_to_player
        print(f"{enemy.name} attacks {player.name} for {damage_to_player} damage. {player.name}'s health is now {player.current_health}/{player.max_health}")

        if player.current_health <= 0:
            print(f"{player.name} has been defeated!")
            break

combat(test_player, test_enemy)