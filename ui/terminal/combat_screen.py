from game.combat.events import Attack, Defeated


def print_event(event):
    if isinstance(event, Attack):
        print(f"{event.attacker.name} attacks {event.defender.name} for {event.damage} damage. "
              f"{event.defender.name}: {event.defender_health}/{event.defender_max_health} HP")
    elif isinstance(event, Defeated):
        print(f"{event.character.name} has been defeated!")


def print_battle(player, enemy, events):
    print(f"Combat Start: {player.name} vs {enemy.name}")
    for event in events:
        print_event(event)