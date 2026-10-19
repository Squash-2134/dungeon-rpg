# Imports
import random
import math
from tests.test_class_race import classes

# Player Character Class
class PlayerCharacter:
    def __init__(self):
        self.name = "Template Hero"
        self.level = 10
        self.max_health = 100
        self.current_health = self.max_health
        self.attack = 10
        self.defence = 10

    def display_character_stats(self):
        print(f"Character Name: {self.name}")
        print(f"Max Health: {self.max_health}")
        print(f"Current Health: {self.current_health}")
        print(f"Attack: {self.attack}")
        print(f"Defence: {self.defence}")

    def set_player_name(self):
        self.name = input("Enter your character's name: ")

    def set_player_race(self):
        pass

    def create_new_character(self):
        pass

# Enemy Class
class Enemy:
    def __init__(self):
        enemy_names = ["Goblin", "Orc", "Troll", "Skeleton", "Zombie"]
        self.name = random.choice(enemy_names)
        self.level = 10
        self.max_health = 80
        self.current_health = self.max_health
        self.attack = 10
        self.defence = 10

    def display_enemy_stats(self):
        print(f"Enemy Name: {self.name}")
        print(f"Max Health: {self.max_health}")
        print(f"Current Health: {self.current_health}")
        print(f"Attack: {self.attack}")
        print(f"Defence: {self.defence}")

test_player = PlayerCharacter()
test_player.display_character_stats()

test_enemy = Enemy()
test_enemy.display_enemy_stats()


        