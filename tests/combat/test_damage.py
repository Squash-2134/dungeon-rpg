import pytest
from game.combat.damage import calculate_damage


def test_equal_stats_level_one():
    assert calculate_damage(10, 10, 1) == pytest.approx(4.4)


def test_more_attack_means_more_damage():
    assert calculate_damage(20, 10, 1) > calculate_damage(10, 10, 1)


def test_higher_level_means_more_damage():
    assert calculate_damage(10, 10, 10) > calculate_damage(10, 10, 1)


def test_zero_defence_is_rejected():
    with pytest.raises(ValueError):
        calculate_damage(10, 0, 1)