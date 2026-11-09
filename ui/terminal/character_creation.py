from game.entities import Player
from game.entities.player import STAT_NAMES
from ui.terminal.display import print_race, print_class, print_profile
from ui.terminal.prompts import (
    ask_text, ask_choice, ask_int, ask_yes_no, choose_with_confirmation
)

# Display labels live here (UI); game code only sees the stored value
PRONOUN_OPTIONS = {"He": "he", "She": "she", "Neutral": "they"}


def spend_stat_points(player):
    while player.stat_points > 0:
        print(f"\nPoints left: {player.stat_points}")
        labels = [f"{stat} ({player.get_stat(stat)})" for stat in STAT_NAMES]
        stat = STAT_NAMES[ask_choice("Add points to which stat?", labels)]
        amount = ask_int(f"How many points to {stat}?", 1, player.stat_points)
        player.spend_points(stat, amount)


def create_character(races, classes):
    while True:
        name = ask_text("Enter your character's name:")

        labels = list(PRONOUN_OPTIONS)
        pronouns = PRONOUN_OPTIONS[labels[ask_choice("Choose pronouns:", labels)]]

        race = choose_with_confirmation(races, "race", print_race)
        player_class = choose_with_confirmation(classes, "class", print_class)

        player = Player(name, pronouns, race, player_class)
        spend_stat_points(player)

        print_profile(player)
        if ask_yes_no("Happy with this character?"):
            return player