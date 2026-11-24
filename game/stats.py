# Stats used in combat. Enemies have these too.
COMBAT_STATS = ("health", "mana", "strength", "fortitude", "arcane", "wisdom", "speed")

# Stats used outside combat. Only the player has these.
WORLD_STATS = ("luck", "reputation")

# Every stat a player has
PLAYER_STATS = COMBAT_STATS + WORLD_STATS

# Stats the player can put their starting points into.
# (Reputation is earned in the game, so it's left out.)
SPENDABLE_STATS = COMBAT_STATS + ("luck",)