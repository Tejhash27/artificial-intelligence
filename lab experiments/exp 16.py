import math
import random

# Seed the random number generator for reproducibility across runtime cycles
random.seed(42)

class FeedforwardNeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate=0.5):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.lr = learning_rate

        # Initialize Weights randomly using a uniform distribution between -1.0 and 1.0
        self.weights_ih = [[random.uniform(-1, 1) for _ in range(self.input_nodes)] for _ in range(self.hidden_nodes)]
        self.weights_ho = [[random.uniform(-1, 1) for _ in range(self.hidden_nodes)] for _ in range(self.output_nodes)]

        # Initialize Biases to zero or small random values
        self.bias_h = [random.uniform(-1, 1) for _ in range(self.hidden_nodes)]
        self.bias_o = [random.uniform(-1, 1) for _ in range(self.output_nodes)]

    def _sigmoid(self, x):
        """Standard Sigmoid activation function."""
        try:
            return 1.0 / (1.0 + math.exp(-x))
        except OverflowError:
            return 0.0 if x < 0 else 1.0

    def _sigmoid_derivative(self, sigmoid_output):
        """Derivative of the sigmoid function given its calculated output value."""
        return sigmoid_output * (1.0 - sigmoid_output)

    def forward(self, input_vector):
        """Performs forward propagation to calculate node states and output layers."""
        self.inputs = input_vector

        # 1. Calculate Hidden Layer Node Outputs
        self.hidden_inputs = []
        for i in range(self.hidden_nodes):
            # Dot product of inputs and hidden layer weights + bias
            sum_nodes = sum(self.inputs[j] * self.weights_ih[i][j] for j in range(self.input_nodes))
            self.hidden_inputs.append(sum_nodes + self.bias_h[i])
        
        self.hidden_outputs = [self._sigmoid(x) for x in self.hidden_inputs]

        # 2. Calculate Final Output Layer States
        self.output_inputs = []
        for i in range(self.output_nodes):
            # Dot product of hidden outputs and output layer weights + bias
            sum_nodes = sum(self.hidden_outputs[j] * self.weights_ho[i][j] for j in range(self.hidden_nodes))
            self.output_inputs.append(sum_nodes + self.bias_o[i])

        self.final_outputs = [self._sigmoid(x) for x in self.output_inputs]
        return self.final_outputs

    def backward(self, target_vector):
        """Performs backpropagation to calculate error gradients and update parameters."""
        # 1. Calculate Error Gradient at the Output Layer
        output_errors = [target_vector[i] - self.final_outputs[i] for i in range(self.output_nodes)]
        output_gradients = [output_errors[i] * self._sigmoid_derivative(self.final_outputs[i]) for i in range(self.output_nodes)]

        # 2. Calculate Error Gradient at the Hidden Layer
        hidden_errors = []
        for i in range(self.hidden_nodes):
            error = sum(output_gradients[j] * self.weights_ho[j][i] for j in range(self.output_nodes))
            hidden_errors.append(error)
        
        hidden_gradients = [hidden_errors[i] * self._sigmoid_derivative(self.hidden_outputs[i]) for i in range(self.hidden_nodes)]

        # 3. Update Weights and Biases for the Output Layer
        for i in range(self.output_nodes):
            for j in range(self.hidden_nodes):
                self.weights_ho[i][j] += self.lr * output_gradients[i] * self.hidden_outputs[j]
            self.bias_o[i] += self.lr * output_gradients[i]

        # 4. Update Weights and Biases for the Hidden Layer
        for i in range(self.hidden_nodes):
            for j in range(self.input_nodes):
                self.weights_ih[i][j] += self.lr * hidden_gradients[i] * self.inputs[j]
            self.bias_h[i] += self.lr * hidden_gradients[i]


# --- Execution Flow ---
if __name__ == "__main__":
    print("=" * 60)
    print("      FEEDFORWARD NEURAL NETWORK FROM SCRATCH (XOR GATE)")
    print("=" * 60)

    # XOR Dataset Inputs and Expected Targets
    xor_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    xor_targets = [[0], [1], [1], [0]]

    # Initialize Network: 2 Input Nodes, 4 Hidden Nodes, 1 Output Node
    nn = FeedforwardNeuralNetwork(input_nodes=2, hidden_nodes=4, output_nodes=1, learning_rate=0.5)

    # Train the network over multiple epochs
    epochs = 20000
    print(f"Training network over {epochs} epochs. Processing...")
    
    for epoch in range(epochs):
        # Pick a random sample configuration from the dataset to train on
        sample_idx = random.randint(0, 3)
        X = xor_inputs[sample_idx]
        y = xor_targets[sample_idx]

        nn.forward(X)
        nn.backward(y)

    print("\nTraining completed successfully! Testing predictions:\n")
    print("-" * 60)
    print(" Input Matrix   |   Target Value   |   Network Prediction Output")
    print("-" * 60)
    
    for i in range(4):
        pred = nn.forward(xor_inputs[i])
        print(f"   {xor_inputs[i]}        |       {xor_targets[i][0]}       |   {pred[0]:.4f}")
    
    print("=" * 60)
