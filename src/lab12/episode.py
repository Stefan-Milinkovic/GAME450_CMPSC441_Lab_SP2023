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
import pygame

def run_episode(player1, player2):
    health = 100
        
    print("########################")

def run_episode(player1, player2):
    """
    Runs a single episode of combat between two players and returns a list of tuples
    representing the observations, actions, and rewards for each turn in the episode.
    """
    # Initialize the game state
    player1.reset()
    player2.reset()
    game_state = (player1.health, player2.health)
    episode_data = []

    # Play the game until one of the players wins
    while not player1.is_defeated() and not player2.is_defeated():
        # Player 1 selects a weapon and takes a turn
        p1_weapon = player1.select_weapon()
        p1_reward = player2.defend(p1_weapon)
        episode_data.append((game_state, p1_weapon, p1_reward))

        # Player 2 selects a weapon and takes a turn
        p2_weapon = player2.select_weapon()
        p2_reward = player1.defend(p2_weapon)
        episode_data.append((game_state, p2_weapon, p2_reward))

        # Update the game state
        game_state = (player1.health, player2.health)

    # Determine the winner of the game and assign rewards
    if player1.is_defeated():
        winner = player2
        loser = player1
    else:
        winner = player1
        loser = player2

    for i in range(len(episode_data)):
        # Assign reward to the winner and penalty to the loser
        if episode_data[i][1] == winner.last_weapon:
            episode_data[i] = (episode_data[i][0], episode_data[i][1], winner.win_reward)
        else:
            episode_data[i] = (episode_data[i][0], episode_data[i][1], loser.loss_penalty)

    return episode_data
