from game.combat.damage import calculate_damage
from game.combat.events import Attack, Defeated


def resolve_attack(attacker, defender):
    """One basic attack. Returns the events it caused."""
    raw = calculate_damage(
        attacker.get_stat("attack"),
        defender.get_stat("defence"),
        attacker.level,
    )
    damage = round(raw)
    defender.take_damage(damage)

    events = [Attack(attacker, defender, damage,
                     defender.current_health, defender.get_stat("health"))]
    if not defender.is_alive():
        events.append(Defeated(defender))
    return events


def run_battle(player, enemy):
    """Fight to the death (attack-only for now). Returns a list of events."""
    # Faster combatant acts first; a tie goes to the player
    if player.get_stat("speed") >= enemy.get_stat("speed"):
        order = [player, enemy]
    else:
        order = [enemy, player]

    events = []
    while player.is_alive() and enemy.is_alive():
        for attacker in order:
            defender = enemy if attacker is player else player
            events += resolve_attack(attacker, defender)
            if not defender.is_alive():
                break
    return events