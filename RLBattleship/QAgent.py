"""
This class serves as the model of an agent capable of navigating the battleship environment via Q Learning
"""

from environment import Environment
import random 
import math

class QAgent:
    def __init__(self, env: Environment, alpha: float, discount_rate: float):
        # Assign environment
        self.env = env
        # Assign learning rate
        self.learning_rate = alpha
        # Assign discount rate
        self.discount_rate = discount_rate
        # Initialize Q table
        self.q_table = {}

"""
best_q_and_a function analyzes the current state of the agent and returns the best posible action the agent can make 
Returns: Best action in form of coordinates
"""
def best_q_and_a(self, state: str) -> tuple: 
    # Get the best action if stored
    if state in self.q_table:
        best_q, best_a = -9999, None
        # Determine which action has the highest q value
        for action, q_val in self.q_table[state].items():
            if q_val > best_q: 
                best_q = q_val
                best_a = action
        # Return best values
        return best_q, best_a
    # If state is unexplored, return random action
    return 0, self.select_random_action()

"""
select_random_action() function analyzes the current state of the environment and randomly selects a random coordinate to mark
Returns: Coordinates to mark
"""
def select_random_action(self) -> tuple: 
    # Store the current environment state
    state = self.env.game_state
    # Initialize a boolean indicating if random location has been chosen
    chosen = False
    while not chosen:
        # Select a random index
        chosen_index = random.choices(list(range(len(state))), k=1)
        # Select index only if never marked
        if state[chosen_index] == '0':
            chosen = True
    # Convert index into x and y 
    size_x, size_y = self.env.size
    x = chosen_index % size_x + 1
    y = math.floor(chosen_index / size_y) + 1
    # Return coordinates as tuple
    return (x, y)

"""
train() function trains the q table by traversing the agent through the environment over a set number of episodes.
Parameters: 
episodes: Number of training episodes (each episode is from agent initialization to game finish)
"""
def train(self, episodes: int): 
    # Initialize exponential decay e values
    e_max, e_min = 1, -0.02
    # Initialzie Episode rewards list
    episode_rewards = []
    # Play through a set number of episodes
    for ep in range(episodes): 
        # Update E
        r = max((episodes - ep) / episodes, 0)
        e = max((e_max - e_min) * r + e_min, 0.01)
        # Reset the environment
        self.env.reset()
        state = self.env.game_state
        # Initialize a state, actions, and rewards list
        states, actions, rewards = [state], [], []
        # Initialize boolean indicating whether game is finished
        game_end = False
        # Play game until termination
        while not game_end:
            # Determine if agent explores of exploits
            decision = random.choices(['exploit', 'explore'], weights = [1 - e, e])
            # Select an action 
            if decision[0] == 'exploit': 
                res = self.best_q_and_a(state)
                # Only retain action val
                action = res[1]
            else: 
                # Exploring so select random action
                action = self.select_random_action()
            # Act on that action
            state, reward, game_end = self.env.mark(action[0], action[1])
            # Store states, actions
            states.append(state)
            actions.append(action)
            rewards.append(reward)
        # Once agent reaches goal, update q table
        for i in range(len(states) - 1): 
            # Pull current state, next state, action, and rewards
            s = states[i]
            next_s = states[i + 1]
            a = actions[i]
            r = rewards[i]
            
            # Retrieve old Q value if exists
            q = 0
            # Determine if current state has been explored
            if s in self.q_table:
                # Determine if current action has been explored
                if a in self.q_table[s]:
                    # Pull q value from this state, action pair
                    q = self.q_table[s][a]
            # Determine maximum next state q value
            max_q = 0
            if next_s in self.q_table: 
                max_q = self.best_q_and_a(next_s)[0]
            # Calculate updatd q value
            q = q + self.learning_rate * (r + self.discount_rate * max_q - q)

            # Update q table
            # Determine if state exists in q_table
            if s not in self.q_table:
                # Create state dictionary within q table 
                self.q_table[s] = {}
            # Assign q value to state action pair
            self.q_table[s][a] = q
        # Sum all episode rewards
        episode_rewards.append(sum(rewards))
    # Return episode rewards
    return episode_rewards


        

