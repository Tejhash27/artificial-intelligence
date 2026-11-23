import numpy as np

# -------------------------------------------------------------------------
# 1. NEURAL NETWORK ARCHITECTURE
# -------------------------------------------------------------------------
class NeuralNetwork:
    """
    A simple feedforward neural network with a fixed 2-4-1 architecture
    to solve the XOR problem.
    """
    def __init__(self):
        # Layer sizes: Input = 2, Hidden = 4, Output = 1
        self.input_size = 2
        self.hidden_size = 4
        self.output_size = 1
        
        # Calculate total number of parameters (weights + biases)
        # Hidden layer: (2 * 4) weights + 4 biases = 12
        # Output layer: (4 * 1) weights + 1 bias = 5
        # Total parameters = 17
        self.param_count = (self.input_size * self.hidden_size + self.hidden_size) + \
                           (self.hidden_size * self.output_size + self.output_size)
        
        self.weights1 = None
        self.biases1 = None
        self.weights2 = None
        self.biases2 = None

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

    def set_parameters(self, flat_params):
        """Unpacks a flat 1D array (chromosome) into network weights and biases."""
        idx = 0
        
        # Hidden layer weights (2x4)
        w1_end = idx + (self.input_size * self.hidden_size)
        self.weights1 = flat_params[idx:w1_end].reshape(self.input_size, self.hidden_size)
        idx = w1_end
        
        # Hidden layer biases (1x4)
        b1_end = idx + self.hidden_size
        self.biases1 = flat_params[idx:b1_end].reshape(1, self.hidden_size)
        idx = b1_end
        
        # Output layer weights (4x1)
        w2_end = idx + (self.hidden_size * self.output_size)
        self.weights2 = flat_params[idx:w2_end].reshape(self.hidden_size, self.output_size)
        idx = w2_end
        
        # Output layer bias (1x1)
        b2_end = idx + self.output_size
        self.biases2 = flat_params[idx:b2_end].reshape(1, self.output_size)

    def forward(self, X):
        """Performs forward propagation."""
        hidden_layer_input = np.dot(X, self.weights1) + self.biases1
        hidden_layer_output = self.sigmoid(hidden_layer_input)
        
        output_layer_input = np.dot(hidden_layer_output, self.weights2) + self.biases2
        output = self.sigmoid(output_layer_input)
        return output

# -------------------------------------------------------------------------
# 2. GENETIC ALGORITHM ENGINE
# -------------------------------------------------------------------------
class GeneticAlgorithm:
    def __init__(self, nn, pop_size=100, mutation_rate=0.1, crossover_rate=0.8, elite_size=2):
        self.nn = nn
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elite_size = elite_size
        self.chromosome_length = nn.param_count
        
        # Initialize population with random weights between -1.0 and 1.0
        self.population = np.random.uniform(-1.0, 1.0, (self.pop_size, self.chromosome_length))

    def calculate_fitness(self, chromosome, X, y):
        """Fitness is inversely proportional to Mean Squared Error (MSE)."""
        self.nn.set_parameters(chromosome)
        predictions = self.nn.forward(X)
        mse = np.mean((y - predictions) ** 2)
        # Add a tiny value to prevent division by zero; higher fitness is better
        fitness = 1.0 / (mse + 1e-6)
        return fitness, mse

    def select_parent(self, fitnesses):
        """Selects a parent using Tournament Selection (Size=3)."""
        tournament_idx = np.random.choice(self.pop_size, size=3, replace=False)
        best_idx = tournament_idx[np.argmax(fitnesses[tournament_idx])]
        return self.population[best_idx]

    def crossover(self, parent1, parent2):
        """Performs simulated uniform crossover between two parents."""
        if np.random.rand() < self.crossover_rate:
            mask = np.random.rand(self.chromosome_length) < 0.5
            child1 = np.where(mask, parent1, parent2)
            child2 = np.where(mask, parent2, parent1)
            return child1, child2
        return parent1.copy(), parent2.copy()

    def mutate(self, chromosome):
        """Applies Gaussian mutation to genes based on the mutation rate."""
        for i in range(self.chromosome_length):
            if np.random.rand() < self.mutation_rate:
                # Add random Gaussian noise to the weight/bias element
                chromosome[i] += np.random.normal(0, 0.2)
        return chromosome

    def evolve(self, X, y, generations=200):
        """Runs the evolutionary optimization loop."""
        for generation in range(1, generations + 1):
            # 1. Evaluate fitness and tracking MSE for all chromosomes
            evaluation = [self.calculate_fitness(chrom, X, y) for chrom in self.population]
            fitnesses = np.array([e[0] for e in evaluation])
            mses = np.array([e[1] for e in evaluation])
            
            best_idx = np.argmax(fitnesses)
            best_mse = mses[best_idx]
            
            # Print status update every 20 generations or if solved
            if generation % 20 == 0 or best_mse < 0.005:
                print(f"Generation {generation:3d} | Best Population MSE: {best_mse:.6f}")
                
            # Convergence check (Early termination if network accurately learns XOR)
            if best_mse < 0.002:
                print(f"\n[!] Problem solved early at Generation {generation}!")
                return self.population[best_idx]
            
            # 2. Elitism: Preserve the best individuals unchanged
            sorted_indices = np.argsort(fitnesses)[::-1]
            next_population = [self.population[idx].copy() for idx in sorted_indices[:self.elite_size]]
            
            # 3. Reproductive loop to fill the rest of the population
            while len(next_population) < self.pop_size:
                p1 = self.select_parent(fitnesses)
                p2 = self.select_parent(fitnesses)
                
                c1, c2 = self.crossover(p1, p2)
                
                next_population.append(self.mutate(c1))
                if len(next_population) < self.pop_size:
                    next_population.append(self.mutate(c2))
                    
            self.population = np.array(next_population)
            
        # Return the best individual found in the final generation
        final_evaluation = [self.calculate_fitness(chrom, X, y) for chrom in self.population]
        final_fitnesses = np.array([e[0] for e in final_evaluation])
        return self.population[np.argmax(final_fitnesses)]

# -------------------------------------------------------------------------
# 3. EXECUTION AND VERIFICATION
# -------------------------------------------------------------------------
if __name__ == "__main__":
    # Seed set for consistency
    np.random.seed(42)
    
    # XOR Dataset input mappings and goals
    X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_train = np.array([[0], [1], [1], [0]])
    
    print("Initializing Neuro-Evolution via Genetic Algorithm...")
    nn_instance = NeuralNetwork()
    ga = GeneticAlgorithm(nn_instance, pop_size=150, mutation_rate=0.15, crossover_rate=0.8, elite_size=4)
    
    # Run evolution
    best_chromosome = ga.evolve(X_train, y_train, generations=300)
    
    # Test the evolved network configurations
    nn_instance.set_parameters(best_chromosome)
    final_outputs = nn_instance.forward(X_train)
    
    print("\n" + "="*45)
    print("   FINAL EVALUATION OF EVOLVED NETWORK")
    print("="*45)
    for i in range(len(X_train)):
        print(f"Input: {X_train[i]} -> Expected: {y_train[i][0]} | Predicted: {final_outputs[i][0]:.4f}")
    print("="*45)
