"""
# RL Shaper Toolkit

A straightforward Python library for implementing potential-based reward shaping in reinforcement learning.

## Installation

```bash
pip install rl-shaper-toolkit
```

## Usage

```python
import numpy as np
from rl_shaper_toolkit.shaper import PotentialBasedShaper

# Assume a simple grid world environment
# where state is represented by a 2D position (x, y)
# and we want to reward reaching the goal at (5, 5).

# Define a potential function that gets closer to 0 as the agent
# gets closer to the goal. A simple Euclidean distance works well.
def potential_function(state):
    goal_state = np.array([5, 5])
    return -np.linalg.norm(state - goal_state)

# Instantiate the shaper
shaper = PotentialBasedShaper(potential_function, gamma=0.99)

# Example usage with a fake episode step
state_t = np.array([1, 2])
reward_t = -1  # Original reward
state_t_plus_1 = np.array([2, 3])

# Calculate the shaped reward
shaped_reward = shaper.get_shaped_reward(state_t, state_t_plus_1, reward_t)

print(f"Original reward: {reward_t}")
print(f"Shaped reward: {shaped_reward}")
```
"""
