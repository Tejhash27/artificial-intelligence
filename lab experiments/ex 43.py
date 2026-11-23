# Reinforcement Learning using Q-Learning
# Simple Environment: Reach the Target

import random

# Environment settings
states = 5
actions = [0, 1]  # 0 = Left, 1 = Right

# Q-table initialization
q_table = [[0, 0] for i in range(states)]

# Learning parameters
learning_rate = 0.8
discount_factor = 0.9
episodes = 100

# Target state
target = 4

print("REINFORCEMENT LEARNING")
print("-----------------------------")

# Training the agent
for episode in range(episodes):

    state = 0

    while state != target:

        # Choose an action
        if random.random() < 0.2:
            action = random.choice(actions)
        else:
            action = q_table[state].index(max(q_table[state]))

        # Move to the next state
        if action == 1:
            next_state = min(state + 1, target)
        else:
            next_state = max(state - 1, 0)

        # Calculate reward
        if next_state == target:
            reward = 10
        else:
            reward = -1

        # Update Q-value
        old_value = q_table[state][action]

        next_max = max(q_table[next_state])

        new_value = old_value + learning_rate * (
            reward + discount_factor * next_max - old_value
        )

        q_table[state][action] = new_value

        state = next_state

# Display trained Q-table
print("Training Completed!")

print("\nLearned Q-Table:")
print("State    Left       Right")

for i in range(states):
    print(i, "    ", round(q_table[i][0], 2),
          "    ", round(q_table[i][1], 2))

# Test the trained agent
print("\nAgent Testing:")

state = 0
path = [state]

while state != target:
    action = q_table[state].index(max(q_table[state]))

    if action == 1:
        state = min(state + 1, target)
    else:
        state = max(state - 1, 0)

    path.append(state)

print("Agent Path:", path)
print("Target Reached Successfully!")
print("\nReinforcement Learning Completed!")
