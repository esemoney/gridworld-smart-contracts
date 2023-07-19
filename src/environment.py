# environment.py

"""Implements a customizable gridworld environment."""

import gymnasium as gym
import numpy as np

GRID_SIZE = 10

EMPTY_CELL = 0
AGENT_CELL = 1 
RESOURCE_CELL = 2

DEFAULT_MAP = [
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,AGENT_CELL,0,0,0,0,0,0],
  [0,0,0,0,RESOURCE_CELL,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,AGENT_CELL]  
]

"""Customizable gridworld environment.

Allows configuring size, agents, resources, etc.
"""
class GridworldEnv(gym.Env):


  def __init__(self):

    """Initialize grid map, agents, and resources.
    
    Args:
      size: Size of square grid map.
    """
    self.grid = np.array(DEFAULT_MAP)
    self.agents = [Agent(0,0), Agent(GRID_SIZE-1,GRID_SIZE-1)]
    self.resource = Resource(4,2)
   
  def reset(self):

    # Resets agent positions and clears resource pickups.

    self.grid = np.array(DEFAULT_MAP) 
    self.resource.collected = False
    return self.get_observations()

  def step(self, actions):

    """Update environment based on agent actions.

    Args:
      actions: List of actions for each agent.

    Returns:
      observations: Array of observations from each agent's perspective.
      rewards: Reward values for each agent.
      done: Boolean indicates whether episode is complete.
      info: Dict containing debug info.
    """

    # Agents take actions

    self.agents[0].move(actions[0])
    self.agents[1].move(actions[1])

    # Resolve resource pickups
    self.collect_resource()

    # Get observations and rewards 
    rewards = self.get_rewards()
    obses = self.get_observations()
    dones = self.get_dones()

    return obses, rewards, dones, {}

  def render(self):
    print(self.grid)

  def get_observations(self):
    """Get observations from each agent's perspective."""

    obs = []
    for agent in self.agents:
      obs.append(self.grid[agent.pos])
    return obs

  def get_rewards(self):
    rewards = [0, 0] 
    if self.resource.collected:
      rewards[self.resource.collector] = 1
    return rewards

  def get_dones(self):
    if self.resource.collected:
      return [True, True]
    return [False, False]

  def collect_resource(self):
    for i, agent in enumerate(self.agents):
      if agent.pos == self.resource.pos:
        self.resource.collect(i)

class Agent:

  def __init__(self, x, y):
    """Initialize agent at given grid coordinates."""

    self.pos = [x, y]

  def move(self, direction):
    """Move agent in given direction."""

    if direction == 0: # up
      self.pos[0] = max(0, self.pos[0] - 1) 
    elif direction == 1: # right
      self.pos[1] = min(GRID_SIZE - 1, self.pos[1] + 1)
    elif direction == 2: # down  
      self.pos[0] = min(GRID_SIZE - 1, self.pos[0] + 1)
    elif direction == 3: # left
      self.pos[1] = max(0, self.pos[1] - 1)

class Resource:
  
  def __init__(self, x, y):
    """Initialize resource object at given location."""

    self.pos = [x, y] 
    self.collected = False
    self.collector = None

  def collect(self, agent_id):
    """Handle resource collection by agent."""

    self.collected = True
    self.collector = agent_id