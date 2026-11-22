# Genetic Algorithm for Function Optimization

import random

# Fitness function
def fitness(x):
    return x * x

# Generate initial population
population = [random.randint(0, 31) for i in range(6)]

# Genetic Algorithm
for generation in range(10):

    # Calculate fitness
    population.sort(key=fitness, reverse=True)

    # Select best parents
    parent1 = population[0]
    parent2 = population[1]

    # Crossover
    child1 = (parent1 + parent2) // 2
    child2 = random.randint(0, 31)

    # Mutation
    if random.random() < 0.3:
        child1 = random.randint(0, 31)

    # Create new population
    population = [
        parent1, parent2, child1, child2,
        random.randint(0, 31),
        random.randint(0, 31)
    ]

# Find best solution
best = max(population, key=fitness)

# Display output
print("GENETIC ALGORITHM")
print("-------------------------")

print("Best Solution (x):", best)
print("Maximum Fitness Value:", fitness(best))

print("-------------------------")
print("Optimization Completed Successfully!")
