import numpy as np

class PotentialBasedShaper:
    """
    A class for potential-based reward shaping.
    
    Potential-based reward shaping adds an extra reward term to the environment's
    reward function to guide an agent. The new reward R' is calculated as:
    R'(s, a, s') = R(s, a, s') + gamma * F(s') - F(s)
    
    where:
    - R is the original reward from the environment.
    - gamma is the discount factor.
    - F is a potential function that maps a state to a scalar value.
    - s and s' are the current and next states, respectively.
    """
    def __init__(self, potential_function, gamma):
        """
        Initializes the shaper with a potential function and discount factor.

        Args:
            potential_function (callable): A function that takes a state as input
                                         and returns a scalar potential value.
            gamma (float): The discount factor used in the RL algorithm.
        """
        if not callable(potential_function):
            raise TypeError("potential_function must be a callable function.")
        if not isinstance(gamma, (int, float)) or not 0 <= gamma <= 1:
            raise ValueError("gamma must be a float between 0 and 1.")

        self.potential_function = potential_function
        self.gamma = gamma

    def get_shaped_reward(self, state, next_state, original_reward):
        """
        Calculates the shaped reward for a given transition.

        Args:
            state (object): The current state.
            next_state (object): The next state.
            original_reward (float): The original reward from the environment.

        Returns:
            float: The shaped reward.
        """
        try:
            potential_next_state = self.potential_function(next_state)
            potential_current_state = self.potential_function(state)
            
            shaped_reward = (original_reward +
                             self.gamma * potential_next_state -
                             potential_current_state)
            
            return shaped_reward

        except Exception as e:
            print(f"An error occurred during reward shaping: {e}")
            return original_reward
