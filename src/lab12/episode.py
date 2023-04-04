import random
''' 
Lab 12: Beginnings of Reinforcement Learning
We will modularize the code in pygrame_combat.py from lab 11 together.

Then it's your turn!
Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''
# return health of players, action, reward 


def run_episode(player1, player2):
    # Initialize the players' health
    player1_health = 100
    player2_health = 100

    # Initialize the list to hold the episode history
    episode_history = []

    # Define the weapons that each player can use
    weapons = ["Sword", "Bow", "Fire"]

    # Run the episode until one player's health reaches 0
    while player1_health > 0 and player2_health > 0:
        # Determine which player is attacking and which is defending
        if random.random() < 0.5:
            attacker = player1
            defender = player2
        else:
            attacker = player2
            defender = player1

        weapon = attacker.select_weapon(weapons)
        damage = attacker.calculate_damage(weapon)
        defender_health = defender.take_damage(damage)
        reward = attacker.calculate_reward(defender_health)

        # Add the current state, action, and reward to the episode history
        state = (player1_health, player2_health)
        action = weapon
        episode_history.append((state, action, reward))

        # Update the players' health
        if attacker == player1:
            player2_health = defender_health
        else:
            player1_health = defender_health

    # Return the episode history
    return episode_history
