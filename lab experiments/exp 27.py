
import random

# Objective function
def fitness(x):
    return x * x

# Generate initial population
population = [random.randint(0, 31) for _ in range(6)]

# Genetic Algorithm
for generation in range(10):

    # Evaluate fitness
    population = sorted(population, key=fitness, reverse=True)

    # Select best individuals
    parents = population[:3]

    # Create new population
    new_population = parents.copy()

    while len(new_population) < 6:

        # Crossover
        p1 = random.choice(parents)
        p2 = random.choice(parents)

        child = (p1 + p2) // 2

        # Mutation
        if random.random() < 0.2:
            child = random.randint(0, 31)

        new_population.append(child)

    population = new_population

    print("Generation:", generation + 1)
    print("Best Solution:", max(population, key=fitness))
    print("Best Fitness:", fitness(max(population, key=fitness)))
    print("----------------------")

# Final result
best = max(population, key=fitness)

print("\nOptimal Solution:", best)
print("Maximum Fitness:", fitness(best))
