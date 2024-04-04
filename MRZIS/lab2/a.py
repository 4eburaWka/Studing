import numpy as np

class Autoencoder:
    def __init__(self, input_dim, hidden_dim, learning_rate):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.learning_rate = learning_rate

        # Initialize weights randomly
        self.weights = np.random.rand(input_dim, hidden_dim)

    def activate(self, x):
        # Sigmoid activation function
        return 1 / (1 + np.exp(-x))

    def derivative(self, x):
        # Derivative of sigmoid activation function
        return x * (1 - x)

    def oja_update(self, input_vector, hidden_vector, output_vector):
        # Oja's rule for updating weights
        self.weights += self.learning_rate * (input_vector - output_vector) * hidden_vector[:, np.newaxis] * self.derivative(hidden_vector)[:, np.newaxis]

    def train(self, input_vector):
        # Forward pass
        hidden_vector = self.activate(np.dot(input_vector, self.weights))
        output_vector = self.activate(np.dot(hidden_vector, self.weights.T))

        # Backward pass
        self.oja_update(input_vector, hidden_vector, output_vector)

        return output_vector

# Example usage
autoencoder = Autoencoder(input_dim=10, hidden_dim=5, learning_rate=0.1)

# Train the autoencoder on some input data
input_data = np.random.rand(100, 10)
for i in range(1000):
    for input_vector in input_data:
        autoencoder.train(input_vector)

# Test the autoencoder on some new input data
test_data = np.random.rand(10, 10)
for input_vector in test_data:
    output_vector = autoencoder.train(input_vector)
    print(output_vector)