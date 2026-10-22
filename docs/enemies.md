## How are Enemies defined?
- What all enemies have:
    - base stats from their race that scale with level
    - at least one skill
    - A base scoring formula that takes in all the deciding factors (Enemy HP, Player HP, etc), which can vary depending on which floor the enemy is on as well as what "rank" the enemy is, different races of enemy would value factors differently.

- Regular Enemies
    - The lowest ranking enemy in the dungeon which can be found on every floor in the dungeon, in there specified rooms
    - Regular Enemies have the lowest total base stats of the different "ranks" of enemies
    - Regular Enemies have only 1 skill
    - Regular Enemies have the simplest scoring system, only taking the base scoring system value and applying their race's valuing to the factors
    - Regular Enemies are given the knowledge of the Player's skills and loadout, factoring them into their decision from floor 70 onwards

- Mini Boss Enemies:
    - The Middle ranking enemy in the dungeon which are found every 5th floor that isn't a multiple of 10, in a mini boss room which the player must clear before being avle to reach the next floor
    - Mini Bosses act like upgraded versions of regular enemies ("Chief Orc" and "Alpha Werewolf" as examples)
    - Mini Bosses have higher base stat totals than regular enemies but not as much as Zone Bosses
    - Mini Bosses have multiple skills, 2 skills < floor 25, 3 < floor 75, 4 skills onward
    - Mini Bosses take the scoring formula of their regular enemy counter part and is more refined, added checks, and overall an upgraded version
    - Mini Bosses are given the knowledge of the Player's skills and loadout, factoring them into their decision from floor 55 onwards
    - Mini Bosses from floor 35 onwards have a consumable item (simple items at first to more useful and stronger items later into the dungeon)

- Zone Boss Enemies:
    - The 