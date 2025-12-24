import random
import math

reward_hit = 10
reward_sink = 100
reward_miss = -1

class Environment:
    # Define the initialization function with the size of the playing field
    def __init__ (self, size: tuple = (5, 5)): 
        # Verify state space is large enough
        self.verify_size(size)
        self.size = size
        # Game state is stored such that: 

        # 0 h 0
        # 0 m 0    = "0h00m0000"
        # 0 0 0
        
        # Ship state is stored in the same manner. Howver, ship state is never sent to the agent. It is kept
        # and utilized to track whether a game has ended.
        self.reset()
        
    def verify_size(self, size: tuple): 
        # Throw error if either one of the tuple coordinates is less than 5
        if size[0] < 5 or size[1] < 5: 
            return ValueError("Size of game is too small. Minimium size: 5 x 5")
        
    # Print out the environment in a clean 2D array
    def pretty_print_state(self, state: str) -> None: 
        # Initialize state string
        state_str = ""
        for i, letter in enumerate(state): 
            # Insert new line if i % col_size = 0
            if i % self.size[0] == 0: 
                state_str += '\n'
            # Append letter with space
            state_str += f"{letter} "

        # Print state_str
        print(state_str)           
            
    # Returns a string corresponding to the starting state of the environment
    def set_starting_state(self) -> str:
        # Get size of board from size member var
        size_of_board = self.size[0] * self.size[1]
        # Initialize state to size: 'size_of_board' of all 0s
        return '0' * size_of_board

    # Select a random ship
    def select_random_ship_size(self) -> str: 
        # Options: 2-length, 3-length, 4-length, or 5-length
        return random.randint(2, 5)
    
    # Maps a ship into the state space and returns state space as string
    def place_ship(self, ship_coordinate: int, ship_size: int, orientation: str) -> str:
        # Initialize state space as a list of characters
        state_space = list(self.game_state)
        # Initialize counter
        count = 0
        # Iterate through all positions
        while count < ship_size:
            # Check orientation
            if orientation == "up": 
                # Place 'ship_size' amount of 's' going upwards from ship_coordinate
                state_space[ship_coordinate - self.size[0] * count] = 's'
            elif orientation == "right": 
                # Place 'ship_size' amount of 's' going right from ship_coordinate
                state_space[ship_coordinate + count] = 's'
            elif orientation == "down": 
                # Place 'ship_size' amount of 's' going down from ship_coordinate
                state_space[ship_coordinate + self.size[0] * count] = 's'
            else: 
                # Place 'ship_size' amount of 's' going left from ship_coordinate
                state_space[ship_coordinate - count] = 's'
            # Increment count
            count += 1
        # Return state_space as string
        return "".join(state_space)

    # Return a string corresponding to state with ship positions added
    def set_ship_positions(self, debug=False) -> str:
        # Set flag indicating whether ship has been placed
        ship_placed = False
        # Keep repeating until ship is placed
        while ship_placed is False: 
            # Select a random ship size
            ship_size = self.select_random_ship_size()
            # Select a random coordinate to place head of ship
            ship_head_coordinate = random.randint(0, self.size[0] * self.size[1] - 1)
            # Pull the x and y coordinates of ship_head_coordinate. 1-indexed
            ship_x = ship_head_coordinate % self.size[0] + 1
            ship_y = math.floor(ship_head_coordinate / self.size[1]) + 1
            # Select random orientation
            orientation = random.choice(["up", "right", "down", "left"])
            # Try to place ship
            # If 0, try to place upwards
            if orientation == "up": 
                if ship_y - ship_size >= 0: 
                    # Valid orientation, set as is
                    ship_placed = True
                # Else invalid orientation, keep trying
            # If 1, try to place to the right
            elif orientation == "right": 
                if ship_x + ship_size <= self.size[0]:
                    # Valid orientation
                    ship_placed = True
            # If 2, try to place down
            elif orientation == "down": 
                if ship_y + ship_size <= self.size[1]: 
                    # Valid orientation
                    ship_placed = True
            # If 3, try to place left
            else: 
                if ship_x - ship_size >= 0: 
                    # Valid orientation
                    ship_placed = True
        # Keep looping till ship placed
        # Place ship and retrieve state string
        ship_state = self.place_ship(ship_head_coordinate, ship_size, orientation)
        # If debug, make sure to indicate what ship was placed and where
        if debug: 
            print (f"Ship of size {ship_size} is anchored at ({ship_x - 1}, {ship_y - 1}) oriented {orientation}")
        return ship_state
    
    
    """
    Reset the environment. This function resets the environment states. It resets the game state to be
    all 0s and it resets the ship_state to have just 0's and s's indicating the ship position. Once these two 
     states are defined, we mark a random ship location and alter both state strings.
    """
    def reset(self):
        # Set the state space to all zeros
        self.game_state = self.set_starting_state()
        # Intiialize the ship_state to all zeros and s's
        self.ship_state = self.set_ship_positions(True)

        # Construct a list of all ship_positions
        ship_pos = []
        # Look for all s in ship_state
        for i, letter in enumerate(self.ship_state):
            # If letter == s, save as ship position
            if letter == 's': 
                # Determine X and Y coordinates (1-indexxed)
                x = i % self.size[1] + 1
                y = math.floor(i / self.size[0]) + 1
                # Save this coordiante
                ship_pos.append((x, y))
        # Randomly select and mark one of the ship positions
        random_pos = random.choice(ship_pos)
        # Mark it
        self.mark(random_pos[0], random_pos[1])


    # DO WE NEED THIS? 
    # I thought we agreed that the list representation was just for readability. The agent will select actions based on the state string. It doesn't know up, down, left, right but the q_table will automatically suggest these moves based on 
    # the determined value function at each action. 
    def read_state(self) -> list:
        # Takes in string representation and returns the list representation
        # (Helper function)
        print("read_state() needs to be implemented!")

    def mark(self, target_x: int, target_y: int):
        # execute_action.
        # X-direction is horizontal (+5 is furthest right)
        # Y-direction is vertical (+5 is furthest down)
        # Arguments:
        #   target_x (int): 1-indexed x-value of target mark
        #   target_y (int): 1-indexed y-value of target mark
        # returns:
        #   state (str):
        #   is_game_end (bool):
        #   reward (int): reward from the move
        terminal_flag = False
        reward = 0
        str_ind = target_x - 1 + (self.size[0] * (target_y - 1))
        if self.is_game_end():
            # If game is already over, return no reward
            return (self.game_state, reward, True)
        else:
            if self.ship_state[str_ind] == 's':    #Hit the ship
                # Replace that index with a hit
                self.ship_state = self.ship_state[:str_ind] + 'h' + self.ship_state[str_ind+1:]
                self.game_state = self.game_state[:str_ind] + 'h' + self.game_state[str_ind+1:]

                #Check if this is the hit that ends the game
                if self.is_game_end():
                    reward = reward_sink
                else:
                    reward = reward_hit
            else:
                if self.ship_state[str_ind] == 'h':     #Hit an already-hit space
                    reward = reward_miss
                else:       # Hit an empty space, miss
                    # Replace that index with a miss
                    self.game_state = self.game_state[:str_ind] + 'm' + self.game_state[str_ind+1:]
                    reward = reward_miss
        return (self.game_state, reward, self.is_game_end())
        
        
    def is_game_end(self):
        #Boolean helper function to determine if the game is over or not
        if 's' in self.ship_state:
            return False
        else:
            return True

    # do we need this? 
    def get_reward(self, ):
        print("get_reward() needs to be implemented!")  
