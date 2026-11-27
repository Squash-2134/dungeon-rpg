import random

from game.combat.actions import ALL_ACTIONS


def choose_enemy_action(enemy, player, rng=random):
    """Pick the enemy's action for this round.

    For now it is a coin flip. Later this is where the scoring formula goes.
    Notice that it is given the player's STATE (health, mana, skills...) but
    NOT the action the player picked this round, because enemies can't see that.
    rng can be swapped for a fake in tests so the result is predictable.
    """
    return rng.choice(ALL_ACTIONS)