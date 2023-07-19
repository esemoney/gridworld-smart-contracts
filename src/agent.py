# agent.py

import torch
import torch.nn as nn
import numpy as np

class DQN(nn.Module):

  def __init__(self, env):
    self.env = env
    self.obs_size = env.observation_space.shape[0]
    self.n_actions = env.action_space.n

    self.net = nn.Sequential(
        nn.Linear(self.obs_size, 128),
        nn.ReLU(),
        nn.Linear(128, 128),
        nn.ReLU(),
        nn.Linear(128, self.n_actions)  
    )

    self.optimizer = torch.optim.Adam(self.parameters())

  def forward(self, x):
    return self.net(x)

  def act(self, state, eps=0.1):
    if np.random.rand() < eps:
      return np.random.randint(self.n_actions)
    else:
      q_vals = self.forward(torch.tensor(state))
      return torch.argmax(q_vals).item()

  def learn(self, experiences):

    states, actions, rewards, next_states, dones = experiences

    q_values = self.forward(states)
    next_q_values = self.forward(next_states)

    q_targets = rewards + gamma * torch.max(next_q_values, axis=1)[0] * (1 - dones)

    action_q = torch.gather(q_values, 1, actions.long().unsqueeze(1)).squeeze()

    loss = nn.MSELoss()(q_targets, action_q)

    self.optimizer.zero_grad()
    loss.backward()
    self.optimizer.step()

    return loss.item()

class ReplayBuffer:
  
  def __init__(self, capacity):
    self.capacity = capacity
    self.buffer = []
    self.position = 0

  # Implementation

  def sample(batch_size):
    # Implementation

def train(env, agent, episodes):

  buffer = ReplayBuffer(10000)

  for e in episodes:

    state = env.reset()
    done = False

    while not done:

      action = agent.act(state)  
      next_state, reward, done, _ = env.step(action)

      buffer.push(state, action, reward, next_state, done)

      if len(buffer) > 128:
        batch = buffer.sample(128)
        loss = agent.learn(batch)

    print("Episode reward:", reward)

  torch.save(agent.state_dict(), 'agent.pth')