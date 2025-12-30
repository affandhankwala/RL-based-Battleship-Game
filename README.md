## Introduction
This project was created in accordance with Johns Hopkins University's Reinforcement Learning (705.741) class project.

## Problem statement
I worked with Robert Franckowiack to create a Q-learning based reinforcement learning agent that would play the battleship game. This game is a two player game where players are initially given two grids. They reserve some spots on one of the grids by placing their ships there and then attempt to locate their opponent's ships by guessing individual grid locations turn by turn. 

We adapted the game by only requiring the agent to shoot the enemies ships. 

## Methodology
During the training period, ships would be place randomly within the grid and the agent would attempt to guess all ship coordinates. Each episode would terminate once the agent found all ships. 

There were three agents that were employed within this game. The Q learning agent, a SARSA agent, and a random agent that served as the benchmark. 

## Results
After training the agents, the q learning agent demonstrated the highest average reward followed by the SARSA agent. Both of these learning strategies greatly surpassed the random strategy demonstrating that these models learned the rules on how to locate ships in the game of battleship. 

Additional results and presentation can be found in the `Presentation` powerpoint. 