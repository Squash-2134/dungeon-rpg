import pytest

from game.entities import Player, Enemy, Race, PlayerClass
from game.combat.actions import ATTACK, DEFEND
from game.combat.battle import resolve_attack, resolve_defend, run_round, run_battle
from game.combat.events import Attack, Defend, Defeated


def make_race(**overrides):
    stats = {"health": 100, "mana": 50, "strength": 10, "fortitude": 10,
             "arcane": 5, "wisdom": 5, "speed": 5, "luck": 5}
    stats.update(overrides)
    return Race("test", "Test", stats, "no_skill")


def make_player(**overrides):
    knight = PlayerClass("knight", "Knight", {}, "knight_skill_tree")
    return Player("Hero", "they", make_race(**overrides), knight)


def make_enemy(**overrides):
    return Enemy(make_race(**overrides), 1)


def test_attack_reduces_defender_health():
    player, enemy = make_player(), make_enemy()
    events = resolve_attack(player, enemy)
    assert isinstance(events[0], Attack)
    assert 3 <= events[0].damage <= 4       # 4.4 * variance, floored
    assert enemy.current_health == 100 - events[0].damage


def test_killing_blow_adds_defeated_event():
    player, enemy = make_player(), make_enemy(health=3)
    events = resolve_attack(player, enemy)
    assert isinstance(events[-1], Defeated)
    assert enemy.current_health == 0        # clamped, never negative


def test_battle_ends_with_exactly_one_loser():
    player, enemy = make_player(), make_enemy()
    events = run_battle(player, enemy)
    assert player.is_alive() != enemy.is_alive()
    assert isinstance(events[-1], Defeated)


def test_faster_character_attacks_first():
    events = run_battle(make_player(speed=10), make_enemy(speed=5))
    assert events[0].attacker.name == "Hero"

    events = run_battle(make_player(speed=5), make_enemy(speed=10))
    assert events[0].attacker.name == "Test"


def test_speed_tie_goes_to_player():
    events = run_battle(make_player(speed=5), make_enemy(speed=5))
    assert events[0].attacker.name == "Hero"

# ---------- Rounds, Attack and Defend ----------

def test_defending_halves_damage():
    player, enemy = make_player(), make_enemy()
    events = resolve_attack(player, enemy, defending=True)
    assert events[0].defended is True
    assert 1 <= events[0].damage <= 2       # 4.4 * 0.5 * variance, floored


def test_not_defending_by_default():
    events = resolve_attack(make_player(), make_enemy())
    assert events[0].defended is False


def test_defend_restores_ten_percent_of_max_mana():
    player = make_player()                  # max mana 50
    player.current_mana = 0
    events = resolve_defend(player)
    assert player.current_mana == 5
    assert isinstance(events[0], Defend)
    assert events[0].mana_restored == 5


def test_defend_rounds_half_up():
    player = make_player(mana=5)            # 10% of 5 = 0.5, should round UP to 1
    player.current_mana = 0
    resolve_defend(player)
    assert player.current_mana == 1


def test_defend_never_goes_over_max_mana():
    player = make_player()                  # starts at full mana
    events = resolve_defend(player)
    assert player.current_mana == 50
    assert events[0].mana_restored == 0     # reports what was actually gained


def test_defend_action_in_a_round_restores_mana():
    player, enemy = make_player(), make_enemy()
    player.current_mana = 10
    run_round(player, enemy, DEFEND, DEFEND)
    assert player.current_mana == 15


def test_defending_player_takes_reduced_damage_in_a_round():
    player, enemy = make_player(), make_enemy()
    events = run_round(player, enemy, DEFEND, ATTACK)
    attacks = [e for e in events if isinstance(e, Attack)]
    assert len(attacks) == 1
    assert attacks[0].defended is True
    assert 1 <= attacks[0].damage <= 2


def test_defend_works_even_if_the_attacker_is_faster():
    player, enemy = make_player(speed=1), make_enemy(speed=10)
    events = run_round(player, enemy, DEFEND, ATTACK)
    assert isinstance(events[0], Attack)    # the enemy really did go first
    assert events[0].defended is True


def test_both_defending_means_no_damage():
    player, enemy = make_player(), make_enemy()
    events = run_round(player, enemy, DEFEND, DEFEND)
    assert not any(isinstance(e, Attack) for e in events)
    assert player.current_health == 100
    assert enemy.current_health == 100


def test_both_attacking_hurts_both():
    player, enemy = make_player(), make_enemy()
    run_round(player, enemy, ATTACK, ATTACK)
    assert player.current_health < 100
    assert enemy.current_health < 100


def test_defeated_character_does_not_act_later_in_the_round():
    player, enemy = make_player(speed=10), make_enemy(speed=1, health=1)
    events = run_round(player, enemy, ATTACK, ATTACK)
    assert len(events) == 2                 # player's Attack, then Defeated. Enemy never swings.
    assert isinstance(events[-1], Defeated)
    assert player.current_health == 100


def test_unknown_action_is_rejected():
    with pytest.raises(ValueError):
        run_round(make_player(), make_enemy(), "dance", ATTACK)