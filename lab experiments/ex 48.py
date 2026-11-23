# Bayesian Network using Python

# Bayesian Network:
# Rain -> Wet Grass
# Sprinkler -> Wet Grass

# Probability of Rain
P_Rain = 0.2

# Probability of Sprinkler
P_Sprinkler = 0.3

# Conditional probabilities of Wet Grass
P_Wet_given_Rain_Sprinkler = {
    (True, True): 0.99,
    (True, False): 0.90,
    (False, True): 0.80,
    (False, False): 0.01
}

print("BAYESIAN NETWORK")
print("-----------------------------")

# Calculate probability of wet grass
P_Wet = 0

for rain in [True, False]:
    for sprinkler in [True, False]:

        # Probability of Rain
        p_rain = P_Rain if rain else (1 - P_Rain)

        # Probability of Sprinkler
        p_sprinkler = (
            P_Sprinkler if sprinkler
            else (1 - P_Sprinkler)
        )

        # Conditional probability
        p_wet = P_Wet_given_Rain_Sprinkler[
            (rain, sprinkler)
        ]

        # Joint probability
        P_Wet += p_rain * p_sprinkler * p_wet

# Calculate probability of dry grass
P_Dry = 1 - P_Wet

# Display results
print("Probability of Rain:", P_Rain)
print("Probability of Sprinkler:", P_Sprinkler)

print("\nProbability of Wet Grass:")
print(round(P_Wet, 4))

print("\nProbability of Dry Grass:")
print(round(P_Dry, 4))

print("-----------------------------")
print("Bayesian Network Completed Successfully!")
