import math

from game.combat.actions import ATTACK, DEFEND, ALL_ACTIONS
from game.combat.damage import calculate_damage
from game.combat.events import Attack, Defend, Defeated

BASIC_ATTACK_POWER = 50

# Balance numbers live here so they are easy to find and change later
DEFEND_DAMAGE_MULTIPLIER = 0.5   # a defending character takes half damage
DEFEND_MANA_PERCENT = 0.10       # and restores 10% of their max mana


def resolve_attack(attacker, defender, defending=False):
    """One basic attack. Returns the events it caused.
    defending=True means the defender chose Defend this round."""
    modifier = DEFEND_DAMAGE_MULTIPLIER if defending else 1.0
    damage = calculate_damage(
        attacker.level,
        BASIC_ATTACK_POWER,
        attacker.get_stat("strength"),
        defender.get_stat("fortitude"),
        modifier=modifier,
    )
    defender.take_damage(damage)

    events = [Attack(attacker, defender, damage,
                     defender.current_health, defender.get_stat("health"),
                     defended=defending)]
    if not defender.is_alive():
        events.append(Defeated(defender))
    return events


def resolve_defend(character):
    """Defend: restore a percentage of max mana. (The damage reduction is
    applied by resolve_attack, since it only matters when someone attacks.)"""
    max_mana = character.get_stat("mana")
    # floor(x + 0.5) rounds .5 UP. Python's round() would turn 0.5 into 0,
    # which would give a 5-mana Orc nothing back.
    amount = math.floor(max_mana * DEFEND_MANA_PERCENT + 0.5)

    mana_before = character.current_mana
    character.restore_mana(amount)
    gained = character.current_mana - mana_before

    return [Defend(character, gained, character.current_mana, max_mana)]


def run_round(player, enemy, player_action, enemy_action):
    """Play ONE round. Both sides have already chosen an action.
    Returns the list of events from this round."""
    for action in (player_action, enemy_action):
        if action not in ALL_ACTIONS:
            raise ValueError(f"Unknown action: {action}")

    # Each turn is (who acts, who they're facing, their action, the other's action)
    player_turn = (player, enemy, player_action, enemy_action)
    enemy_turn = (enemy, player, enemy_action, player_action)

    # Faster combatant acts first; a tie goes to the player
    if player.get_stat("speed") >= enemy.get_stat("speed"):
        turns = [player_turn, enemy_turn]
    else:
        turns = [enemy_turn, player_turn]

    events = []
    for actor, target, actor_action, target_action in turns:
        if not actor.is_alive():
            continue    # knocked out earlier this round, so they don't get to act

        if actor_action == ATTACK:
            # Defend counts for the WHOLE round, even if the attacker is faster
            events += resolve_attack(actor, target,
                                     defending=(target_action == DEFEND))
        else:
            events += resolve_defend(actor)
    return events


def run_battle(player, enemy):
    """Auto-battle where both sides only attack. Returns a list of events.
    Kept for now so the old demo still works; it will be replaced by a
    player-driven loop on the screen side in session 2."""
    events = []
    while player.is_alive() and enemy.is_alive():
        events += run_round(player, enemy, ATTACK, ATTACK)
    return events