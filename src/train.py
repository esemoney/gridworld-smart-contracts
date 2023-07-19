# train.py

import environment
import agent
import contract

import csv
import argparse

# Initialize environment and agent
env = Environment()
agent = DQN(env)

# Compile and deploy contract
compiled_contract = compile_contract('contract.sol') 
deployed_contract = deploy_contract(compiled_contract)

# Training hyperparameters
hyper_params = {
  'max_episodes': 5000,
  'max_steps': 200,
  'batch_size': 128,
  'gamma': 0.95, 
  'eps_start': 1.0,
  'eps_end': 0.05,
  'eps_decay': 0.998
}

# Metrics file
metrics_file = open('metrics.csv', 'w')
metrics_writer = csv.DictWriter(metrics_file, fieldnames=['episode', 'reward', 'steps', 'loss', 'transfers']) 
metrics_writer.writeheader()

def train(hyper_params, use_contract):

  for episode in range(hyper_params['max_episodes']):

    state = env.reset()
    done = False
    episode_reward = 0

    for step in range(hyper_params['max_steps']):
      
      # Agent selects action  
      action = agent.act(state, eps)

      if use_contract:
        # Unlock ability to call contract
        action_space += 1  

        if action == transfer_tokens:
          # Contract action
          deployed_contract.transfer(...)

      # Take env step   
      next_state, reward, done, _ = env.step(action)
      
      # Store in replay buffer
      replay_buffer.push(state, action, reward, next_state, done)

      # Train agent
      if len(buffer) > hyper_params['batch_size']:
        batch = replay_buffer.sample(hyper_params['batch_size'])
        loss = agent.learn(batch) 

      # Update state
      state = next_state
      episode_reward += reward

      if done:
        break

    # Log metrics for episode
    log_metrics(episode, episode_reward, step, loss, transfers)

  metrics_file.close()

def log_metrics(episode, reward, steps, loss, transfers):

  metrics_writer.writerow({
    'episode': episode,
    'reward': reward,
    'steps': steps, 
    'loss': loss,
    'transfers': transfers
  })

# Parse command line args  
parser = argparse.ArgumentParser()
parser.add_argument('--contract', action='store_true')
args = parser.parse_args()

# Call training loop
train(hyper_params, args.contract)