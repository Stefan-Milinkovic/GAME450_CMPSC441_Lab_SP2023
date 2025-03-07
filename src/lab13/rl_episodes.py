'''
Lab 13: My first AI agent.
In this lab, you will create your first AI agent.
You will use the run_episode function from lab 12 to run a number of episodes
and collect the returns for each state-action pair.
Then you will use the returns to calculate the action values for each state-action pair.
Finally, you will use the action values to calculate the optimal policy.
You will then test the optimal policy to see how well it performs.

Sidebar-
If you reward every action you may end up in a situation where the agent
will always choose the action that gives the highest reward. Ironically,
this may lead to the agent losing the game.
'''
import sys
from pathlib import Path

# line taken from turn_combat.py
sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab11.pygame_combat import PyGameComputerCombatPlayer
from lab11.turn_combat import CombatPlayer
from lab12.episode import run_episode
from ExtraCredit.ec import Crown

from collections import defaultdict
import random
import numpy as np


class PyGameRandomCombatPlayer(PyGameComputerCombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        self.weapon = random.randint(0, 2)
        return self.weapon


class PyGamePolicyCombatPlayer(CombatPlayer):
    def __init__(self, name, policy):
        super().__init__(name)
        self.policy = policy

    def weapon_selecting_strategy(self):
        self.weapon = self.policy[self.current_env_state]
        return self.weapon


def run_random_episode(player, opponent):
    player.health = random.choice(range(10, 110, 10))
    opponent.health = random.choice(range(10, 110, 10))
    return run_episode(player, opponent)


def get_history_returns(history):
    total_return = sum([reward for _, _, reward in history])
    returns = {}
    for i, (state, action, reward) in enumerate(history):
        if state not in returns:
            returns[state] = {}
        returns[state][action] = total_return - sum(
            [reward for _, _, reward in history[:i]]
        )
    return returns


def run_episodes(n_episodes):
    ''' Run 'n_episodes' random episodes and return the action values for each state-action pair.
        Action values are calculated as the average return for each state-action pair over the 'n_episodes' episodes.
        Use the get_history_returns function to get the returns for each state-action pair in each episode.
        Collect the returns for each state-action pair in a dictionary of dictionaries where the keys are states and
            the values are dictionaries of actions and their returns.
        After all episodes have been run, calculate the average return for each state-action pair.
        Return the action values as a dictionary of dictionaries where the keys are states and 
            the values are dictionaries of actions and their values.
    '''

    # creating random players
    player1 = PyGameComputerCombatPlayer("Urus")
    player2 = PyGameComputerCombatPlayer("Aventi")

    # creating a random episode with these players
    randomEpisode = run_random_episode(player1, player2)

    # storing the returns for history 
    historyReturn = get_history_returns(randomEpisode)

    # for the game we need to iterate between states and actions
    # iterate through each state in the returns dictionary
    for state in historyReturn:
        # for each state iterate through its corresponding actions
        for action in historyReturn[state]:
            # check to see if state doesn't exist in the action_values dictionary
            if state not in action_values:
                
                # create a temporary dictionary to store the current state, action and return
                stored_items = {state: {action: [historyReturn[state][action]]}}
                # update action_values with this dictionary
                action_values.update(stored_items)

            # if state does exist in the action_values dictionary, 
            else:
                # check to see if current action already exists for the state being checked
                if action not in action_values[state]:
                    # if action doesn't exist add it to correct return value
                    action_values[state][action] = [historyReturn[state][action]]
                else:
                    # if action already exists, add it to current return value in the list
                    action_values[state][action].append(historyReturn[state][action])
    
    # calculating the average return value for each state/ action pair in the dict
    # iterate through each state in the action_values dictionary
    for state in action_values:
        # iterate thorough the actions associated with each state
        for action in action_values[state]:
            # set the total to 0 and iterate through list of returns
            total_return = 0
            for ret in action_values[state][action]:
                # add the total return to the current iteration
                total_return += ret
            
            # set value associated with each state/ action as the average
            action_values[state][action] = (total_return / len(action_values[state][action]))

    
    # return updated action_values dictionary with the new average return values
    return action_values


def get_optimal_policy(action_values):
    optimal_policy = defaultdict(int)
    for state in action_values:
        optimal_policy[state] = max(action_values[state], key=action_values[state].get)
    return optimal_policy


def test_policy(policy):
    names = ["Legolas", "Saruman"]
    total_reward = 0
    for _ in range(100):
        player1 = PyGamePolicyCombatPlayer(names[0], policy)
        player2 = PyGameComputerCombatPlayer(names[1])
        players = [player1, player2]
        total_reward += sum(
            [reward for _, _, reward in run_episode(*players)]
        )
    
    Crown()
    return total_reward / 100


if __name__ == "__main__":
    action_values = run_episodes(10000)
    print(action_values)
    optimal_policy = get_optimal_policy(action_values)
    print(optimal_policy)
    print(test_policy(optimal_policy))
    
