# Markov Chain Model for Event Prediction

# Define event transition probabilities
transition = {
    "Sunny": {
        "Sunny": 0.7,
        "Rainy": 0.3
    },
    "Rainy": {
        "Sunny": 0.4,
        "Rainy": 0.6
    }
}

# Starting event
current_event = "Sunny"

print("MARKOV CHAIN MODEL")
print("-------------------------")

print("Current Event:", current_event)

# Predict the next event
next_event = max(
    transition[current_event],
    key=transition[current_event].get
)

print("Predicted Next Event:", next_event)

print("\nTransition Probabilities:")

for event, probability in transition[current_event].items():
    print(event, ":", probability)

# Predict a sequence of events
print("\nPredicted Event Sequence:")

sequence = [current_event]

for i in range(5):
    current_event = max(
        transition[current_event],
        key=transition[current_event].get
    )
    sequence.append(current_event)

print(" -> ".join(sequence))

print("\nMarkov Chain Prediction Completed Successfully!")
