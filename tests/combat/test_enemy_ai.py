from game.combat.actions import ALL_ACTIONS, ATTACK, DEFEND
from game.combat.enemy_ai import choose_enemy_action


class FakeRandom:
    """Stands in for the random module and always picks the LAST option."""
    def choice(self, options):
        return options[-1]


def test_enemy_always_picks_a_valid_action():
    for _ in range(100):
        assert choose_enemy_action(None, None) in ALL_ACTIONS


def test_enemy_uses_the_random_source_it_is_given():
    assert choose_enemy_action(None, None, rng=FakeRandom()) == DEFEND


def test_enemy_picks_both_actions_over_many_tries():
    picked = {choose_enemy_action(None, None) for _ in range(200)}
    assert picked == {ATTACK, DEFEND}