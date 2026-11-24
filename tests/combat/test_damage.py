import pytest
from game.combat.damage import calculate_damage

# calculate_damage(level, power, strength, fortitude, variance=None, modifier=1.0)
# variance=1.0 removes the randomness so results are predictable


def test_equal_stats_level_one():
    assert calculate_damage(1, 50, 10, 10, variance=1.0) == 4      # floor(4.4)


def test_more_attack_means_more_damage():
    assert calculate_damage(1, 50, 20, 10, variance=1.0) > calculate_damage(1, 50, 10, 10, variance=1.0)


def test_higher_level_means_more_damage():
    assert calculate_damage(10, 50, 10, 10, variance=1.0) > calculate_damage(1, 50, 10, 10, variance=1.0)


def test_zero_fortitude_is_rejected():
    with pytest.raises(ValueError):
        calculate_damage(1, 50, 10, 0)


def test_variance_stays_in_expected_range():
    for _ in range(200):
        assert 3 <= calculate_damage(1, 50, 10, 10) <= 4           # 4.4 * (0.85 to 1.00)


def test_damage_is_at_least_one():
    assert calculate_damage(1, 50, 1, 1000, variance=0.85) >= 1

def test_modifier_scales_damage():
    # 4.4 * 0.5 = 2.2, floored to 2
    assert calculate_damage(1, 50, 10, 10, variance=1.0, modifier=0.5) == 2


def test_modifier_defaults_to_no_change():
    assert calculate_damage(1, 50, 10, 10, variance=1.0) == \
           calculate_damage(1, 50, 10, 10, variance=1.0, modifier=1.0)


def test_halved_damage_is_still_at_least_one():
    assert calculate_damage(1, 50, 1, 1000, variance=0.85, modifier=0.5) == 1