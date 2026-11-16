from game.entities import Player, Enemy, Race, PlayerClass
from game.combat.battle import resolve_attack, run_battle
from game.combat.events import Attack, Defeated


def make_race(**overrides):
    stats = {"health": 100, "mana": 50, "attack": 10, "defence": 10,
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
    assert events[0].damage == 4            # round(4.4)
    assert enemy.current_health == 96


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