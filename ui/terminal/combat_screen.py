from game.combat.actions import ATTACK, DEFEND
from game.combat.battle import run_round
from game.combat.enemy_ai import choose_enemy_action
from game.combat.events import Attack, Defend, Defeated
from ui.terminal.prompts import ask_choice

# Display labels live here (UI); game code only sees the action constants
ACTION_LABELS = {ATTACK: "Attack", DEFEND: "Defend"}


def print_event(event):
    if isinstance(event, Attack):
        note = f" ({event.defender.name} defended, damage halved)" if event.defended else ""
        print(f"{event.attacker.name} attacks {event.defender.name} for {event.damage} damage{note}. "
              f"{event.defender.name}: {event.defender_health}/{event.defender_max_health} HP")
    elif isinstance(event, Defend):
        print(f"{event.character.name} braces for impact and restores {event.mana_restored} mana. "
              f"{event.character.name}: {event.mana_after}/{event.max_mana} MP")
    elif isinstance(event, Defeated):
        print(f"{event.character.name} has been defeated!")


def print_status(player, enemy):
    for fighter in (player, enemy):
        print(f"  {fighter.name}: {fighter.current_health}/{fighter.get_stat('health')} HP, "
              f"{fighter.current_mana}/{fighter.get_stat('mana')} MP")


def ask_player_action():
    actions = list(ACTION_LABELS)
    index = ask_choice("Choose your action:", [ACTION_LABELS[a] for a in actions])
    return actions[index]


def play_battle(player, enemy):
    """Run a whole fight, asking the player for an action every round.
    Returns True if the player won, False if they lost."""
    print(f"\nCombat Start: {player.name} vs {enemy.name}")

    round_number = 1
    while player.is_alive() and enemy.is_alive():
        print(f"\n--- Round {round_number} ---")
        print_status(player, enemy)

        player_action = ask_player_action()
        enemy_action = choose_enemy_action(enemy, player)

        print()
        for event in run_round(player, enemy, player_action, enemy_action):
            print_event(event)
        round_number += 1

    won = player.is_alive()
    print(f"\n{'Victory!' if won else 'Game over...'}")
    return won