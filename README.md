

 
# Gridworld Contracts

This project aims to evaluate the impact of Ethereum smart contracts on emergent coordination behaviors in multi-agent reinforcement learning systems.

## Approach

We will:

- Implement a simple gridworld environment with two agents and collectible resources
- Integrate an ERC20 smart contract deployed on Remix
- Train DQN agents with and without smart contract actions 
- Log metrics like rewards, resource sharing, gas costs
- Analyze results across conditions to quantify the effect of contracts

## Code Structure

- `environment.py`: Implements customizable Gym gridworld 
- `agent.py`: Deep Q learning agent implementation
- `contract.sol`: Solidity code for ERC20 contract
- `train.py`: Main loop for training agents and logging metrics

## Running Experiments

To train agents:

1. Ensure dependencies are installed
2. Run `train.py` to initialize env and agents
3. Vary contract integration and parameters
4. Analyze logged metrics across conditions


## Why??

In my first implementation, I was too rigid with gymnasium.

Stripping away frameworks, the goal of the project is quantitatively comparing agent cooperation across conditions (is smart contract present or not) in a controlled, reproducible environment. This is in line with the research focus on **emergent behaviors**. 

To achieve this, 

1. We strip away the rigid gridworld framework and focus on a simple customizable environment that lets us precisely control conditions.
2. The modular implementation makes it easy to define new agent actions like cooperation and exchange. We can easily add or tweak behaviors.
3. By integrating real smart contracts, we enable modeling real-world actions and incentives. Agents can actually exchange value.
4. Tracking granular metrics around cooperation, actions, transfers is built into the training loop and analysis. This is core to the experiments.
5. The results should provide insights into how smart contracts and tokenized value impact emergent coordination in multi-agent RL systems.

## Results

- TBD . We haven't run experiments and collected results.


## Next Steps

- More complex environments and emergent behaviors
- Alternate blockchain architectures and constraints
- Formal modeling of equilibrium conditions
- Learning algorithms beyond DQN (policy gradients, actor-critic, etc.)
- Social dynamics - competing vs. cooperating agents



