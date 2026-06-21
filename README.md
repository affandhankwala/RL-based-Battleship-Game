# RL-based Battleship Game

A reinforcement-learning agent that learns to play **Battleship** — locating and sinking randomly placed
ships on a grid as efficiently as possible.

## Introduction

This project was created for Johns Hopkins University's *Reinforcement Learning* course (705.741), in
collaboration with Robert Franckowiack.

## Problem Statement

Battleship is normally a two-player game in which each player hides ships on a grid and takes turns
guessing grid coordinates to locate the opponent's ships. We adapt the game to a **single-agent search
problem**: the agent's only job is to fire at grid cells and sink the (hidden, randomly placed) enemy
ships in as few shots as possible.

## Methodology

During training, ships are placed at random positions and orientations on the grid. The agent fires at
one cell per turn, observing whether each shot is a **miss**, a **hit**, or a **sink**. An episode ends
once all ships are found. Rewards shape the agent toward efficient hunting (e.g. hits and sinks are
rewarded while misses are penalized).

The environment tracks two parallel state representations: the full ship layout (held privately by the
environment) and the observable board state (given to the agent). Agents evaluated in the study:

- **Q-Learning agent** — off-policy temporal-difference learner.
- **SARSA agent** — on-policy temporal-difference learner.
- **Random agent** — benchmark baseline.

## Repository Structure

```
RL-based-Battleship-Game/
├── README.md
├── Presentation.pptx                 # Results presentation
└── RLBattleship/
    ├── environment.py                # Battleship environment (state, ship placement, rewards)
    ├── QAgent.py                     # Q-learning agent
    ├── UnitTest_environment.py       # Unit tests for the environment
    └── notes.txt                     # Design notes (state encoding, rewards, work breakdown)
```

## Running

```bash
cd RLBattleship
python QAgent.py
```

Run the environment unit tests with:

```bash
cd RLBattleship
python -m unittest UnitTest_environment.py
```

### Requirements

- Python 3

## Results

The **Q-learning agent achieved the highest average reward**, followed by the SARSA agent. Both learning
agents vastly outperformed the random benchmark, demonstrating that they successfully learned an effective
strategy for locating ships. Additional results and analysis are in [`Presentation.pptx`](Presentation.pptx).
